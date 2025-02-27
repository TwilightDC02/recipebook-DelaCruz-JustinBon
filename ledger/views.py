from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import *

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe(request, recipe_num):
    recipe1 = {
        "name": "Recipe 1",
        "number": "1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "ledger/recipe/1"
    }
    recipe2 = {
        "name": "Recipe 2",
        "number": "2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "ledger/recipe/2"
    }
    if (recipe_num == 1):
        recipe = recipe1
    elif (recipe_num == 2):
        recipe = recipe2
    else:
        recipe = ""
    return render(request, 'recipe.html', recipe)
