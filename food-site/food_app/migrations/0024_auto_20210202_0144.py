# Generated by Django 3.1.4 on 2021-02-02 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0023_auto_20210202_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dinner_post',
            old_name='ingredients_1',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='dinner_post',
            old_name='ingredients_2',
            new_name='instructions',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredients_3',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredients_4',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='instructions_1',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='instructions_2',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='instructions_3',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='instructions_4',
        ),
    ]