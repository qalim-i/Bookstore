from django.urls import path
from . import views

urlpatterns = [
    path('add-book',views.add_book, name='add_book'),
    path('add-author',views.add_author, name='add_author'),
    path('book-list',views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
]