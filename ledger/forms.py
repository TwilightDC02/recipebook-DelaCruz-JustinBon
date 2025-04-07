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
        widgets = {
            'Quantity': forms.TextInput(attrs={'required': True}),
            'Ingredient': forms.Select(attrs={'required': True})
        }

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': True}),
            'description': forms.Textarea(attrs={'required': False})
        }

RecipeIngredientFormset = inlineformset_factory(Recipe, RecipeIngredient, RecipeIngredientForm, can_delete=True, extra=3)

RecipeImageFormset = inlineformset_factory(Recipe, RecipeImage, RecipeImageForm, can_delete=False, extra=1)
