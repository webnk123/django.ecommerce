# Generated by Django 2.2.17 on 2021-07-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumkiapp', '0016_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]