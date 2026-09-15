from django.contrib import admin

from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_bestselling", "rating", "author")
    list_display = ("title", "author", "rating", "is_bestselling")

admin.site.register(Book, BookAdmin)
