from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from MyReadingPal.books.forms import BookForm, DeletedBookForm
from MyReadingPal.books.models import Book


@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator_id = request.user.id
            form.save()
            return redirect('my book list')
    else:
        form = BookForm()

    context = {
        'form': form
    }

    return render(request, 'create-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    can_edit = False
    if request.user.id == book.creator_id:
        can_edit = True
    context = {
        'title': book.title,
        'type': book.type,
        'author': book.author,
        'opinion': book.opinion,
        'image': book.image.url ,
        'can_edit': can_edit,
        'id': pk,
    }

    return render(request, 'book-details.html', context)


@login_required(login_url='login')
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('my book list')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form
    }

    return render(request, 'edit-book.html', context)


@login_required(login_url='login')
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('my book list')
    else:
        form = DeletedBookForm(instance=book)

    context = {
        'form': form
    }

    return render(request, 'delete-book.html', context)