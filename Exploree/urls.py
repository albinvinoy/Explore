from django.urls import path, include
from . import views


app_name='exploree'
urlpatterns =[
    path('', views.index, name='index'),
]


