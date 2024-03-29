# Generated by Django 2.2.17 on 2022-09-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumkiapp', '0018_auto_20210721_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_collection',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='sumkiapp.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(related_name='products', to='sumkiapp.ProductImage'),
        ),
    ]
