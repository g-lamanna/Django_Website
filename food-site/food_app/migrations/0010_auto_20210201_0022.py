# Generated by Django 3.1.4 on 2021-02-01 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0009_auto_20210131_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dessert_post',
            old_name='time',
            new_name='cook_time',
        ),
        migrations.RenameField(
            model_name='dessert_post',
            old_name='ingredient_10',
            new_name='difficulty',
        ),
        migrations.RenameField(
            model_name='dinner_post',
            old_name='time',
            new_name='cook_time',
        ),
        migrations.RenameField(
            model_name='dinner_post',
            old_name='steps',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='snack_post',
            old_name='time',
            new_name='cook_time',
        ),
        migrations.RenameField(
            model_name='snack_post',
            old_name='ingredient_1',
            new_name='difficulty',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_1',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_2',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_3',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_4',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_5',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_6',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_7',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_8',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredient_9',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_1',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_10',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_2',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_3',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_4',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_5',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_6',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_7',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_8',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='step_9',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_1',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_10',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_2',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_3',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_4',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_5',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_6',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_7',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_8',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredient_9',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_1',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_10',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_2',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_3',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_4',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_5',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_6',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_7',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_8',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='step_9',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_10',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_2',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_3',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_4',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_5',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_6',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_7',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_8',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredient_9',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_1',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_10',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_2',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_3',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_4',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_5',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_6',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_7',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_8',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='step_9',
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients',
            field=models.TextField(default='TEST'),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions',
            field=models.TextField(default='TEST'),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='prep_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='difficulty',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions',
            field=models.TextField(default='TEST'),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='prep_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients',
            field=models.TextField(default='TEST'),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions',
            field=models.TextField(default='TEST'),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='prep_time',
            field=models.IntegerField(default=1),
        ),
    ]