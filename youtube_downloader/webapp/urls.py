from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('search/', views.searchbar, name='searchbar'),
    path('download/', views.download, name='download')


]
