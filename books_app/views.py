from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Book

# This allows ANY name to register
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Force login as a normal guest
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# This allows ANY registered name to login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.borrower:
        book.borrower = request.user
        book.save()
    return redirect('home')

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.borrower == request.user:
        book.borrower = None
        book.save()
    return redirect('home')