# Generated by Django 3.1.4 on 2021-02-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0029_auto_20210203_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.JPG', upload_to='image_posts')),
                ('difficulty', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
