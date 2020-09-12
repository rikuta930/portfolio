from django.urls import path

from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('jobs', views.jobs, name='jobs'),
    path('hobby', views.hobby, name='hobby'),
]
