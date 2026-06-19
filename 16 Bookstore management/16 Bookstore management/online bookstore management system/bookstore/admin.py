from django.contrib import admin
from . models import Book,cart

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display=['id','title','author_name','price']
@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display=['id','user']
