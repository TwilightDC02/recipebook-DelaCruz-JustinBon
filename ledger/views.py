from django.shortcuts import render, HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def recipe_list(request):
    '''
    This view generates the webpage that displays the list of all available recipes that links to its respective page.

    '''
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def detailed_recipe(request, recipe_num):
    '''
    This view generates the webpage that displays the necessary ingredients and quantities needed for the chosen recipe.

    '''
    recipe = Recipe.objects.get(id=recipe_num)
    return render(request, 'recipe.html', {'recipe': recipe})
