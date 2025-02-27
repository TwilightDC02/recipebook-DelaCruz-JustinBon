from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import *

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def detailed_recipe(request, recipe_num):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', recipes)
