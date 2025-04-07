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
        image_formset = RecipeImageFormset(request.POST, request.FILES)

        if 'add_ingredients' in request.POST:
            ingredient_form.save()
            return redirect('ledger:add_recipe')

        elif 'add_recipe' in request.POST:
            recipe = recipe_form.save(commit=False)
            ingredients_formset.instance = recipe
            image_formset.instance = recipe
            if  recipe_form.is_valid() and ingredients_formset.is_valid() and image_formset.is_valid():
                print("validated")
                recipe.author = request.user.profile
                recipe.save()
                ingredients_formset.save()
                image_formset.save()

                return redirect('ledger:add_recipe')
            else:
                print("Recipe form errors:", recipe_form.errors)
                print("Ingredients formset errors:", ingredients_formset.errors)
                print("Image formset errors:", image_formset.errors)
                print(image_formset.is_valid())
                print(recipe_form.is_valid())
                print(ingredients_formset.is_valid())
                for form in ingredients_formset:
                    print(form.errors)
    
    empty_recipe = Recipe()
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    ingredients_formset = RecipeIngredientFormset(instance=empty_recipe)
    image_formset = RecipeImageFormset(instance=empty_recipe)

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