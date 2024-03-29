from django.shortcuts import render
from django.template.defaulttags import register
from .models import Dinner_Post, Dessert_Post, Snack_Post, Wine_Post, Tips_Post, Wine_Generator, Wine_Guide


def home(request):
  context = {
  'posts': Wine_Post.objects.all(),
  }
  return render(request,'food_app/home.html', context)

def dinner(request):
  context = {
    'posts': Dinner_Post.objects.all(),
  }
  return render(request,'food_app/dinner.html', context)

def snack(request):
  context = {
    'posts': Snack_Post.objects.all(),
  }
  return render(request,'food_app/snack.html', context)

def dessert(request):
  context = {
    'posts': Dessert_Post.objects.all(),
  }
  return render(request,'food_app/dessert.html', context)
  
def about(request):
  return render(request,'food_app/about.html')

def wine(request):
  context = {
    'posts': Wine_Post.objects.all(),
  }
  return render(request,'food_app/wine.html', context)

def tips(request):
  context = {
    'posts': Tips_Post.objects.all(),
  }
  return render(request,'food_app/tips.html',context)

#articles

def wine_guide(request):
  context = {
    'posts': Wine_Guide.objects.all(),
  }
  return render(request, 'food_app/wine_guide.html', context)

def wine_generator(request):
  return render(request, 'food_app/wine_generator.html')

def wine_make(request):
  return render(request, 'food_app/wine_make.html')

def wine_guide_base(request):
  context = {
  'posts': Wine_Guide.objects.all(),
  }
  return render(context)
