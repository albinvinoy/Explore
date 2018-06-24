from django.urls import path, include
from . import views


app_name="exploree"
urlpatterns =[
    path('', views.index, name='index'),
    # path('food/', views.food, name='food'),
    # path('activities/', views.activitites, name='activities'),
    path('<str:whatTodo>/', views.whatTodo, name='whatTodo' )
]


