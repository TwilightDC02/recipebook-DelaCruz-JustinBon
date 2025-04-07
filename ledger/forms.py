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

class RequiredFormset(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormset, self).__init__(*args,**kwargs)
        for form in self.forms:
            form.empty_permitted = False

RecipeIngredientFormset = inlineformset_factory(Recipe, RecipeIngredient, RecipeIngredientForm, formset=RequiredFormset, can_delete=True, extra=5)

RecipeImageFormset = inlineformset_factory(Recipe, RecipeImage, RecipeImageForm,formset=RequiredFormset, can_delete=False, extra=1)
