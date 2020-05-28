from django.urls import path
from .views import homepage, add, compare, compare_projects, project_detail



urlpatterns = [
    path('', homepage, name='homepage'),
    path('add/', add, name='add'),
    path('compare/', compare, name='compare'),
    path('compare/data=<project_1>vs<project_2>', compare_projects, name='compare_projects'),
    path('projects/<int:project_id>', project_detail, name='project_detail'),
]

