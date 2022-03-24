from django.urls import reverse_lazy
from django.views.generic.base import View, TemplateView, RedirectView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

# django view is a function
# pure python func with django request object
# return django response
from django101.web.models import Todo


def index(request):
    ctx = {
        'title': 'Function-based view'
    }
    return render(request, 'demo.html', ctx)


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
