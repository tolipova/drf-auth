from django.urls import path
from .views import *
urlpatterns = [
    path('', NewsListCreateViewApi.as_view() ),
    path('<int:pk>/', NewsUpdateOrDeleteViewApi.as_view()),
    
]
