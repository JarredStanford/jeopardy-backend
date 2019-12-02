from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show', views.fetch_answers_by_show),
    path('numbers', views.get_show_numbers),
    path('episodes', views.get_episodes)
]