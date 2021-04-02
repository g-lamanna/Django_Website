# Generated by Django 3.1.4 on 2021-02-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0015_auto_20210201_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert_post',
            name='stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dessert_post',
            name='time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='time',
            field=models.IntegerField(default=1),
        ),
    ]
