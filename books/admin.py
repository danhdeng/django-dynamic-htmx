from django.contrib import admin
from .models import Book, Author

# Register your models here.

class BookInLineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]


admin.site.register(Author, AuthorAdmin)
