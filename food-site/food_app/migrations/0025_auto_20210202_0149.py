# Generated by Django 3.1.4 on 2021-02-02 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0024_auto_20210202_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert_post',
            name='cook_time_lower',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='cook_time_upper',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='instructions',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='prep_time_lower',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='prep_time_upper',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='cook_time_lower',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='cook_time_upper',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='instructions',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='prep_time_lower',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='prep_time_upper',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='cook_time_lower',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='cook_time_upper',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredients_1',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredients_2',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredients_3',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredients_4',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='instructions_1',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='instructions_2',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='instructions_3',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='instructions_4',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='prep_time_lower',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='prep_time_upper',
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='drink',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_1',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_10',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_2',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_6',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_7',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_8',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_9',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_10',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_6',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_7',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_8',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_9',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='time',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='drink',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_1',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_10',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_2',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_3',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_4',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_5',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_6',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_7',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_8',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_9',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_1',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_10',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_2',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_3',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_4',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_5',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_6',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_7',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_8',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_9',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='time',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='drink',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_10',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_6',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_7',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_8',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_9',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_10',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_6',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_7',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_8',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_9',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='time',
            field=models.IntegerField(default=1),
        ),
    ]
