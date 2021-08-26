from django import forms
from django.forms.models import (
    inlineformset_factory,
    modelform_factory,
    modelformset_factory,
)
from .models import Author, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {"title", "number_of_pages"}


BookFormSet = inlineformset_factory(
    Author, Book, fields=('title','number_of_pages', ), can_delete=False, min_num=2, extra=0
)
