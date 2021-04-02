# Generated by Django 3.1.4 on 2021-02-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0010_auto_20210201_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert_post',
            name='cook_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dessert_post',
            name='prep_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='cook_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='prep_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='cook_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='prep_time',
            field=models.IntegerField(default=1),
        ),
    ]