from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='site-home'),
    path('dinner/', views.dinner, name='site-dinner'),
    path('snack/', views.snack, name='site-snack'),
    path('dessert/', views.dessert, name='site-dessert'),
    path('about/', views.about, name='site-about'),
    path('wine/', views.wine, name='site-wine'),
    path('tips/', views.tips, name='site-tips'),
    path('wine-guide/', views.wine_guide, name='site-wine_guide'),
    path('wine-generator/', views.wine_generator, name='site-wine_generator'),
    path('wine-make/', views.wine_make, name='site-wine_make'),
]