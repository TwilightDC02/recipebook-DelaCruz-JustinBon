from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Recipe, RecipeImage
from .forms import RecipeForm, RecipeIngredientFormset, IngredientForm, RecipeImageFormset

@login_required
def recipe_list(request):
    '''
    This view generates the webpage that displays the list of all available recipes that links to its respective page.

    '''
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def detailed_recipe(request, recipe_num):
    '''
    This view generates the webpage that displays the necessary ingredients and quantities needed for the chosen recipe.

    '''
    recipe = Recipe.objects.get(id=recipe_num)
    return render(request, 'recipe.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        ingredients_formset = RecipeIngredientFormset(request.POST)
        image_formset = RecipeImageFormset(request.POST)

        if 'add_ingredients' in request.POST:
            ingredient_form.save()
            return redirect('ledger:add_recipe')

        elif 'add_recipe' in request.POST and recipe_form.is_valid() and ingredients_formset.is_valid() and image_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.profile
            recipe_form.save()
            ingredients_formset.instance = recipe
            image_formset.instance = recipe
            ingredients_formset.save()
            image_formset.save()

            return redirect('ledger:add_recipe')
        
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    ingredients_formset = RecipeIngredientFormset()
    image_formset = RecipeImageFormset()

    return render(request, 'add_recipe.html', {'add_recipe_form': recipe_form, 'new_ingredient_form': ingredient_form, 'ingredients_formset': ingredients_formset, 'image_formset': image_formset})

@login_required
def add_image(request, recipe_num):
    recipe = Recipe.objects.get(id=recipe_num)
    if request.method == "POST":
        image_formset = RecipeImageFormset(request.POST, request.FILES)

        if image_formset.is_valid():
            image_formset.instance = recipe 
            image_formset.save()

            return redirect('ledger:recipe', recipe_num)
    
    image_formset = RecipeImageFormset()

    return render(request, 'add_image.html', {'image_formset': image_formset, 'recipe': recipe})