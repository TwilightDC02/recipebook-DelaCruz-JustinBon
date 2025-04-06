from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['Quantity', 'Ingredient']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'

RecipeIngredientFormset = inlineformset_factory(Recipe, RecipeIngredient, RecipeIngredientForm, can_delete=False)
RecipeImageFormset = inlineformset_factory(Recipe, RecipeImage, RecipeImageForm, can_delete=False, extra=2)
