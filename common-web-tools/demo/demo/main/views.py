import linecache
from random import randint
from time import time

from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

# decorator for caching view
# arg is for time of invalidating
# @cache_page(15)
from django.views.generic import TemplateView, ListView
from demo.main.models import Profile


# pagination in class based view
class ProfilesListView(ListView):
    model = Profile
    template_name = 'profilies-list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET('pages_count', 1)


def index(request):
    Profile.objects.create(
        name='Doncho Minkov',
        email='doncho@abv.bg'
    )
    profiles = Profile.objects.all()
    if not cache.get('value2'):
        value2 = randint(1024, 2028)
        cache.set('value2', value2, 30)
    count = request.session.get('count') or 0
    request.session['count'] = count + 1
    # setup how much pages u want
    paginator = Paginator(profiles, per_page=5)
    # gets queryparam from url ?page=xxx or 1
    current_page = request.GET.get('page', 1)

    context = {
        'value': randint(1, 1024),
        # we can keep track of cached values using redis insight tool(trough docker)
        'value2': cache.get('value2'),
        # number of times we accessed site in this session
        # every user has his own session so count will be different for different clients
        'count': count,
        'profile_page': paginator.get_page(current_page),
    }
    return render(request, 'index.html', context)


# cookies are text files sent by server which contain key-value pairs
# u can keep last state in session
def show_book_details(request, pk):
    # session key rules (keys cannnot start with _, must be strings and can't be overridden)
    request.session['last_viewed_book'] = pk
    return HttpResponse()


# to add this abstract functionality we must inherit this in all views
# with middleware we avoid that
class MeasureTimeMixin(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        start = time()
        result = super().dispatch(*args, **kwargs)
        end = time()
        print(end - start)
        return result


def last_view_books_middleware(get_response):
    def middleware(request):
        request.books = request.session.get('last_viewed_books', [])
        return get_response(request)

    return middleware

# def active_user_middleware(get_response):
#     def middleware(request,*args,**kwargs):
#         if request.user.is_authenticated:
#             friends =  request.user.friends
#             alert_user_online(friends,user)
#     return middleware

# signals allow us to keep track of occurred events within the db

#
