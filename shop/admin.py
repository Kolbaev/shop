from django.contrib import admin

# Register your models here.
from .models import Category, Product, Comment
from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class CommentAdmin(TranslationAdmin):
    list_display = ['name', 'content']
admin.site.register(Comment, CommentAdmin)