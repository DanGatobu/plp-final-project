# Generated by Django 4.1.7 on 2023-04-15 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestockapp', '0007_remove_tempcart_category_suppliments_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliments',
            name='vendor',
            field=models.CharField(default='Farmy', max_length=400),
        ),
    ]
