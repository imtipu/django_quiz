from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeIndex(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeIndex, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Home'
        return ctx
