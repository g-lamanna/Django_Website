# Generated by Django 3.1.4 on 2021-02-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0031_auto_20210207_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine_post',
            old_name='region',
            new_name='article_id',
        ),
        migrations.RemoveField(
            model_name='wine_post',
            name='scents',
        ),
        migrations.RemoveField(
            model_name='wine_post',
            name='tannins',
        ),
        migrations.AddField(
            model_name='wine_post',
            name='description',
            field=models.TextField(default='.', max_length=500),
        ),
    ]