from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Recipe, RecipeImage
from .forms import RecipeForm, RecipeIngredientFormset, IngredientForm

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
        form = RecipeForm(request.POST)
        form_2 = IngredientForm(request.POST)
        formset = RecipeIngredientFormset(request.POST)

        if 'add_ingredients' in request.POST:
            form_2.save()
            return redirect('ledger:add_recipe')

        elif form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user.profile
            form.save()
            formset.instance = recipe
            formset.save()

            return redirect('ledger:add_recipe')
        
    form = RecipeForm()
    form_2 = IngredientForm()
    formset = RecipeIngredientFormset()

    return render(request, 'add_recipe.html', {'add_recipe_form': form, 'new_ingredient_form': form_2, 'ingredients_formset': formset})