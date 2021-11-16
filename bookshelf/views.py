from django.shortcuts import redirect, render
from .models import Book
from datetime import datetime, timedelta


def books_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookshelf/home.html', { 'books': books })


def add_book(request):
    book_title = request.POST.get('book_title')
    book_author = request.POST.get('book_author')

    book_info = Book(title=book_title, author=book_author)
    if book_title and book_author:
        book_info.save()
    return redirect('home')


def borrow_book(request, book_id):
    Book.objects.filter(pk=book_id).update(borrow=datetime.now()+timedelta(minutes=1))
    return redirect('home')


def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('home')
