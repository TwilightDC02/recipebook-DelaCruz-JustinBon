from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class RecipeIngredient(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['Quantity', 'Ingredient']