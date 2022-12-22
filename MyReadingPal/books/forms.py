from django.forms import ModelForm

from MyReadingPal.books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['creator_id']


class DeletedBookForm(BookForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

