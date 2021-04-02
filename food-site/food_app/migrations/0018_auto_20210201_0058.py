# Generated by Django 3.1.4 on 2021-02-01 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0017_auto_20210201_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dessert_post',
            old_name='stars',
            new_name='cook_time',
        ),
        migrations.RenameField(
            model_name='dessert_post',
            old_name='time',
            new_name='prep_time',
        ),
        migrations.RenameField(
            model_name='dinner_post',
            old_name='stars',
            new_name='cook_time',
        ),
        migrations.RenameField(
            model_name='dinner_post',
            old_name='drink',
            new_name='difficulty',
        ),
        migrations.RenameField(
            model_name='dinner_post',
            old_name='time',
            new_name='prep_time',
        ),
        migrations.RenameField(
            model_name='snack_post',
            old_name='stars',
            new_name='cook_time',
        ),
        migrations.RenameField(
            model_name='snack_post',
            old_name='drink',
            new_name='difficulty',
        ),
        migrations.RenameField(
            model_name='snack_post',
            old_name='time',
            new_name='prep_time',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_1',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_1',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_1',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_1',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_1',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_1',
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='difficulty',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients',
            field=models.TextField(default='Placeholder', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions',
            field=models.TextField(default='', max_length=100),
        ),
    ]
