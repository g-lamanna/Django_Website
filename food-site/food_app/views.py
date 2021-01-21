from django.shortcuts import render
from .models import Dinner_Post, Dessert_Post, Snack_Post

def home(request):
  return render(request,'food_app/home.html')

def dinner(request):

  posty = Dinner_Post.objects.all()
  for post in posty:
    ran = post.stars
  context = {
    'posts': Dinner_Post.objects.all(),
    'range':range(ran)
  }
  return render(request,'food_app/dinner.html', context)

def snack(request):
  posty = Snack_Post.objects.all()
  for post in posty:
    ran = post.stars
  context = {
    'posts': Snack_Post.objects.all(),
    'range':range(ran)
  }
  return render(request,'food_app/snack.html', context)

def dessert(request):
  posty = Dessert_Post.objects.all()
  for post in posty:
    ran = post.stars
  context = {
    'posts': Dessert_Post.objects.all(),
    'range':range(ran)
  }
  return render(request,'food_app/dessert.html', context)