from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import *

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def detailed_recipe(request, recipe_num):
    recipe = Recipe.objects.get(id=recipe_num)
    return render(request, 'recipe.html', {'recipe': recipe})
