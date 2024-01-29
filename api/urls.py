from django.urls import path
from .views import *
urlpatterns = [
    path('news/', NewsListCreateViewApi.as_view() ),
    path('news/<int:pk>/', NewsUpdateOrDeleteViewApi.as_view()),
    path('news/detail/<int:pk>/', NewsDetailApi.as_view()),
    path('news/create/', NewsCreateView.as_view()),
    path('news/update/<int:pk>/', NewsUpdateApi.as_view()),
    path('news/delete/<int:pk>/', NewsDeleteApi.as_view()),
]
