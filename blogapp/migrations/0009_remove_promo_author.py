# Generated by Django 4.0.4 on 2022-04-30 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_promo_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promo',
            name='author',
        ),
    ]