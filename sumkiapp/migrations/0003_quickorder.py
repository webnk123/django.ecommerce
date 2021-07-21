# Generated by Django 2.2.17 on 2021-01-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumkiapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quickorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]