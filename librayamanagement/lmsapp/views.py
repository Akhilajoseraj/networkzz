from django.shortcuts import render

from .models import Book,Author
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})
