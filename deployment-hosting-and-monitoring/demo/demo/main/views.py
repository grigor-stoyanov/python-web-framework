from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from demo.main.models import Item


class IndexView(ListView):
    template_name = 'index.html'
    model=Item