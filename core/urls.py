from django.urls import path
from .views import homepage, add, compare



urlpatterns = [
    path('', homepage, name='homepage'),
    path('add/', add, name='add'),
    path('compare/', compare, name='compare'),
]
