# Generated by Django 4.0.4 on 2022-05-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_remove_promo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='test', max_length=60),
            preserve_default=False,
        ),
    ]