# Generated by Django 3.1.4 on 2021-01-31 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0008_auto_20201230_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert_post',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='stars',
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='steps',
            field=models.TextField(default='TEST'),
        ),
    ]
