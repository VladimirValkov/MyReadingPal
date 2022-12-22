from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from MyReadingPal.books.models import Book
from MyReadingPal.home.forms import CreateUserForm
from MyReadingPal.home.models import UserLikes


def home(request):
    return render(request, 'home.html')



def book_lists_page(request):
    users = User.objects.all()
    booklists = []
    for user in users:
        book_count = len(Book.objects.filter(creator_id=user.id).filter(is_public=True))
        if book_count > 0:
            booklists.append({
                'id': user.id,
                'username': user.username,
                'likes': len(UserLikes.objects.filter(liked_user=user.id)),
                'books_count': book_count
            })

    context = {
        'lists': booklists,
    }
    return render(request, 'book-lists.html', context)

def book_lists_details(request, pk):
    books = Book.objects.filter(creator_id=pk)
    user = User.objects.get(id=pk)
    userlikes = UserLikes.objects.filter(liker_user=request.user.id).filter(liked_user=pk)
    is_liked = len(userlikes) > 0
    if request.method == 'POST':
        if request.POST.get('dislike'):
            userlikes.delete()
            is_liked = False
        else:
            userlikes = UserLikes()
            userlikes.liked_user = pk
            userlikes.liker_user = request.user.id
            userlikes.save()
            is_liked = True


    context = {
        'books': books,
        'user_data': user,
        'is_liked': is_liked,
    }
    return render(request, 'book-list-details.html', context)

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
