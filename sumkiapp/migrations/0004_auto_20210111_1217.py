# Generated by Django 2.2.17 on 2021-01-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumkiapp', '0003_quickorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_collection',
            field=models.CharField(max_length=20),
        ),
    ]
