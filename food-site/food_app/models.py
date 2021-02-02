from django.db import models

class Dinner_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  difficulty = models.CharField(max_length=100,default='')
  instructions_1 = models.TextField(max_length=500,default='')
  instructions_2 = models.TextField(max_length=500,default='')
  instructions_3 = models.TextField(max_length=500,default='')
  instructions_4 = models.TextField(max_length=500,default='')
  ingredients_1 = models.TextField(max_length=500,default='')
  ingredients_2 = models.TextField(max_length=500,default='')
  ingredients_3 = models.TextField(max_length=500,default='')
  ingredients_4 = models.TextField(max_length=500,default='')
  cook_time_lower = models.IntegerField(default=1)
  cook_time_upper = models.IntegerField(default=1)
  prep_time_lower = models.IntegerField(default=1)
  prep_time_upper = models.IntegerField(default=1)

  def __str__(self):
    return self.title

class Snack_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  difficulty = models.CharField(max_length=100,default='')
  instructions_1 = models.TextField(max_length=500,default='')
  instructions_2 = models.TextField(max_length=500,default='')
  instructions_3 = models.TextField(max_length=500,default='')
  instructions_4 = models.TextField(max_length=500,default='')
  ingredients_1 = models.TextField(max_length=500,default='')
  ingredients_2 = models.TextField(max_length=500,default='')
  ingredients_3 = models.TextField(max_length=500,default='')
  ingredients_4 = models.TextField(max_length=500,default='')
  cook_time_lower = models.IntegerField(default=1)
  cook_time_upper = models.IntegerField(default=1)
  prep_time_lower = models.IntegerField(default=1)
  prep_time_upper = models.IntegerField(default=1)

  def __str__(self):
    return self.title

class Dessert_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  difficulty = models.CharField(max_length=500,default='')
  instructions = models.TextField(max_length=500,default='')
  cook_time_lower = models.IntegerField(default=1)
  cook_time_upper = models.IntegerField(default=1)
  prep_time_lower = models.IntegerField(default=1)
  prep_time_upper = models.IntegerField(default=1)

  def __str__(self):
    return self.title
