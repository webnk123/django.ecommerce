# Generated by Django 2.2.17 on 2021-01-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumkiapp', '0013_auto_20210118_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, default='Москва', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]