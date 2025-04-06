from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    ingredient = forms.CharField(max_length=255, required=True)
    class Meta:
        model = RecipeIngredient
        fields = ['Quantity']

RecipeIngredientFormset = inlineformset_factory(Recipe, RecipeIngredient, RecipeIngredientForm, can_delete=False)