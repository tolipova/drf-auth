from django.urls import path
from .views import *
urlpatterns = [
    path('book/list', BookListView.as_view() ),
    path('book/create', BookCreateView.as_view()),
    path('<int:pk>', BookDetailView.as_view()),
    path('update/<int:pk>', BookUpdateView.as_view()),
    path('delete/<int:pk>', BookDeleteView.as_view()),
]



