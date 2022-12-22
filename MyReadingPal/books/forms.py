from django.forms import ModelForm

from MyReadingPal.books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['creator_id']

