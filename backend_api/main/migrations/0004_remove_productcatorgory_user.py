# Generated by Django 5.0.1 on 2024-01-28 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_category_product_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcatorgory',
            name='user',
        ),
    ]
