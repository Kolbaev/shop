# Generated by Django 3.2 on 2021-05-09 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_ru',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='name_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='name_ru',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
