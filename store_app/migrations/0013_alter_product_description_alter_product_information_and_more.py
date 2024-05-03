# Generated by Django 4.2.7 on 2023-12-10 07:20

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0012_alter_product_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_id',
            field=models.CharField(blank=True, default=uuid.UUID('4dbab182-c1d8-47f2-a856-6af8938dcad6'), max_length=100, null=True, unique=True),
        ),
    ]