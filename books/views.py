from django.shortcuts import render, redirect
from .forms import BookForm, AuthorForm
from .models import Book, Author
from django.contrib.auth.decorators import login_required

@login_required
def add_book(request):
    if request.user.is_seller:
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                book = form.save(commit=False)
                book.seller = request.user
                book.save()
                return redirect('book_list')  # Redirect to a list of books after saving
        else:
            form = BookForm()
        return render(request, 'books/add_book.html', {'form': form})
    else:
        return redirect('home')

@login_required
def add_author(request):
    if request.user.is_seller:
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('author_list')  # Redirect to a list of authors after saving
        else:
            form = AuthorForm()
        return render(request, 'books/add_author.html', {'form': form})
    else:
        return redirect('home')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()  # Get all authors from the database
    return render(request, 'books/author_list.html', {'authors': authors})
