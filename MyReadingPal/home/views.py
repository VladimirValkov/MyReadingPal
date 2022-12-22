from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from MyReadingPal.books.models import Book
from MyReadingPal.home.forms import CreateUserForm


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def book_lists_page(request):
    return render(request, 'book-lists.html')


@login_required(login_url='login')
def my_book_list(request):
    books = Book.objects.filter(creator_id=request.user.id)
    context = {
        'books': books
    }
    return render(request, 'my-book-list.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Registration successful.")
                return redirect('login')
            messages.error(request, "Unsuccessful registration. Invalid information.")

        context = {
            'form': form
        }

        return render(request, 'register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("home")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")

        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, "login.html", context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')
