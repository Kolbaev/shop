from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, Comment


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category', 'name', 'description')

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('name', 'content')
