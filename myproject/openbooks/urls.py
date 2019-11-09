from django.urls import path

from . import views


app_name = 'openbooks'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/create', views.create, name='create'),

    path('post', views.post, name='post'),
]