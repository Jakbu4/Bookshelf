from django.urls import path
from . import views

# url configuration

urlpatterns = [
    path('', views.books_list, name='home'),
    path('add_book/', views.add_book, name='add-book'),
    path('borrow_book/<book_id>', views.borrow_book, name='borrow-book'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),

]