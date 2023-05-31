from django.shortcuts import render

from django.views.generic import TemplateView
# from django.contrib.auth.models import User

# from bakery.views import BuildableTemplateView, BuildableListView

class HomeView(TemplateView):
    template_name = "home.html"

# class IndexBuildView(BuildableListView):
#     build_path = "build/index.html"
#     queryset = User.objects.all()
#     template_name = "home.html"
