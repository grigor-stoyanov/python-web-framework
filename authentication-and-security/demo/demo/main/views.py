from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic.base import View, TemplateView, RedirectView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

# django view is a function
# pure python func with django request object
# return django response
from demo.main.models import Todo, Category


def allowed_groups(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exist():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this content!')

        return wrapper

    return decorator


def permissions_required(required_permissons):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return HttpResponse('No permission')
            if not user.has_perms(required_permissons):
                return HttpResponse('No permission')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


# decorator checks weather user logged in
# other option is add LOGIN_URL = '/login'
# @login_required(login_url='login')
@permissions_required(required_permissons=[
    'main.change_category'
])
def index(request):
    # Same as
    # if not request.user.is_authenticated:
    #     redirect('login')

    ctx = {
        'title': 'Function-based view',
        'user': request.user
    }
    # UserModel = get_user_model()
    # UserModel.objects.create_user(
    #     username='doncho1',
    #     password='12345qwe'
    # )
    # authenticate returns the user based on username or password
    user = authenticate(request, username='doncho1', password='12345qwe')
    print(authenticate(request, username='doncho1', password='12345qwe'))
    print(authenticate(request, username='doncho2', password='12345qwe'))
    print(authenticate(request, username='doncho1', password='12445qwe'))
    # before login check if the user is authenticated
    if user:
        login(request, user)
    # logout deletes login from the request

    # we also have permissions/roles for each user
    # default permissions crud permissions
    # users can be added to groups to have/not have rights for certain things
    # we need to explicitly give them
    if user.has_perm('main.change_category'):
        cat = Category.objects.get(pk=4)
        cat.name = 'New name 2'
        cat.save()
    # better to check permission than group because it makes code depend on administration

    return render(request, 'demo.html', ctx)
    # validating permissions is done trough custom decorators


# classes can be used as functions by overriding call function
# allows us to write clean code with class based views
# and allow us to use mixin pattern for related class functionality
class IndexView(View):
    # if we want to use/add methods within the view
    http_method_names = ['get', 'post']

    def get(self, request):
        context = {
            'title': 'class-based view'
        }
        return render(request, 'demo.html', context)

    def post(self, request):
        pass

    # rewriting dispatch allows us to restrict the user to editing only his content
    def dispatch(self, request, *args, **kwargs):
        # custom logic
        return super().dispatch(request, *args, **kwargs)


# visualises something
class IndexTemplateView(TemplateView):
    template_name = 'demo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-Based Template View'
        return context


# we can directly put in url also
class RedirectToIndexView(RedirectView):
    url = reverse_lazy('index class-based')

    # if we want to customize it
    # def get_redirect_url(self, *args, **kwargs):
    #     if True:
    #         return 'place 1'
    #     else:
    #         return 'place 2'


# special purpouse views
class MyListView(ListView):
    model = Todo
    template_name = 'todo-list.html'
    ordering = ('-category__name',)
    # renames default object_list in context
    context_object_name = 'todos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = 'something'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset.prefetch_related('category')
        # when there is a querystring in the url
        title_filter = self.request.GET.get('filter', None)
        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)
        return queryset


class TodoDetails(DetailView):
    # basic minimum
    model = Todo
    template_name = 'todo-details.html'
    # extensibility
    context_object_name = 'todo'

    # allows to dynamically select which template to be shown
    def get_template_name(self):
        pass


class TodoCreate(CreateView):
    model = Todo
    template_name = 'todo-create.html'
    # when the same for each create
    success_url = reverse_lazy('index class-based 3')
    fields = ('title', 'category', 'description')

    # form_class = CreateTodoForm
    # makes forms dynamic
    def get_form_class(self):
        pass
    # when different based on the create
    # def get_success_url(self):
    #     pass
    # or we can overwrite get_absolute_url() method in the model
