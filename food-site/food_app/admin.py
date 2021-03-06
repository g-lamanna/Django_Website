from django.contrib import admin
from .models import Dinner_Post, Snack_Post, Dessert_Post, Wine_Post, Tips_Post, Wine_Generator

admin.site.register(Dinner_Post)
admin.site.register(Snack_Post)
admin.site.register(Dessert_Post)
admin.site.register(Wine_Post)
admin.site.register(Tips_Post)
admin.site.register(Wine_Generator)