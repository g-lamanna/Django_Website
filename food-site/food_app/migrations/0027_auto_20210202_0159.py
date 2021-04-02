# Generated by Django 3.1.4 on 2021-02-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0026_auto_20210202_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dinner_post',
            old_name='ingredients',
            new_name='ingredients_1',
        ),
        migrations.RenameField(
            model_name='dinner_post',
            old_name='instructions',
            new_name='ingredients_2',
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_3',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='ingredients_4',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_1',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_2',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_3',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='instructions_4',
            field=models.TextField(default='', max_length=500),
        ),
    ]
