from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ProjectPageView(TemplateView):
    template_name = 'project-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

