from django.shortcuts import render, redirect

from MyReadingPal.books.forms import BookForm
from MyReadingPal.books.models import Book


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
        'can_edit': can_edit
    }

    return render(request, 'book-details.html', context)


def edit_book(request, pk):
    pass


def delete_book(request, pk):
    pass
