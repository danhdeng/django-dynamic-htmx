from django.shortcuts import redirect, render
from .models import Book, Author
from .forms import BookForm, BookFormSet

# Create your views here.


def create_book(request, pk):
    author = Author.objects.get(id=pk)
    formset = BookFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect('book:create-book', pk=author.id)

    context = {"formset": formset, 'author': author}

    return render(request, "books\create_book.html", context)

def create_book_form(request):
    bookForm =BookForm(request.POST or None)
    context = {"form": bookForm}
    return render(request, "books\create_book_form.html", context)

