from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models


class HomePageView(TemplateView):
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ProjectPageView(ListView):
    template_name = 'project-page.html'
    queryset = models.Project.objects.all()
    context_object_name = 'projects'
    paginate_by = 3

