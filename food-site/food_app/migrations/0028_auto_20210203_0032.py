# Generated by Django 3.1.4 on 2021-02-03 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0027_auto_20210202_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert_post',
            name='instructions',
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_1',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_10',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_2',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_3',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_4',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_5',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_6',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_7',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_8',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='ingredients_9',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_1',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_10',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_2',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_3',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_4',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_5',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_6',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_7',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_8',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dessert_post',
            name='instructions_9',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_10',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_5',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_6',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_7',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_8',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_9',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_10',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_5',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_6',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_7',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_8',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_9',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients_10',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients_5',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients_6',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients_7',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients_8',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='ingredients_9',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions_10',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions_5',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions_6',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions_7',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions_8',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='instructions_9',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='ingredients_1',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='ingredients_2',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='ingredients_3',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='ingredients_4',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='instructions_1',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='instructions_2',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='instructions_3',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='dinner_post',
            name='instructions_4',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='ingredients_1',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='ingredients_2',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='ingredients_3',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='ingredients_4',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='instructions_1',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='instructions_2',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='instructions_3',
            field=models.TextField(default='.', max_length=500),
        ),
        migrations.AlterField(
            model_name='snack_post',
            name='instructions_4',
            field=models.TextField(default='.', max_length=500),
        ),
    ]