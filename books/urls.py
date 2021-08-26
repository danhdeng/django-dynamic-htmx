from django.urls import path
from .views import create_book, create_book_form

app_name="book"

urlpatterns = [
    path('<int:pk>/', create_book, name='create-book'),
    # path('htmx/book-form', create_book_form, name='book-form')

]
