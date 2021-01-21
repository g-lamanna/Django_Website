# Generated by Django 3.1.4 on 2020-12-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0002_auto_20201228_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert_post',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='dessert_post',
            name='steps',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='dinner_post',
            name='steps',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='snack_post',
            name='steps',
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_1',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_10',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_2',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_3',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_4',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_5',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_6',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_7',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_8',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredient_9',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_1',
            field=models.CharField(default='step 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_10',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_2',
            field=models.CharField(default='step 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_3',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_4',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_5',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_6',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_7',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_8',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='step_9',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_1',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_10',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_2',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_3',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_4',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_5',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_6',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_7',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_8',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredient_9',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_1',
            field=models.CharField(default='step 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_10',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_2',
            field=models.CharField(default='step 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_3',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_4',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_5',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_6',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_7',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_8',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='step_9',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_1',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_10',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_2',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_3',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_4',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_5',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_6',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_7',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_8',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredient_9',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_1',
            field=models.CharField(default='step 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_10',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_2',
            field=models.CharField(default='step 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_3',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_4',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_5',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_6',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_7',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_8',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='step_9',
            field=models.CharField(default='ingredient 1', max_length=100),
        ),
    ]
