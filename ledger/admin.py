from django.contrib import admin
from .models import *

class RecipeIngredientReadOnlyInline(admin.TabularInline):
    model = RecipeIngredient

    # Prevents unintentional edits to the recipe and/or quantity.
    readonly_fields = ['Recipe', 'Quantity']

class RecipeIngredientEditableInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ('name',)
    search_fields = ('name',)
    
    # Allows for admin to view which recipes require the chosen ingredient and how much is needed.
    inlines = [RecipeIngredientReadOnlyInline, ]

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ('name',)
    search_fields = ('name',)

    # Allows for admin to modify the recipes by adding/deleting ingredients.
    inlines = [RecipeIngredientEditableInline, RecipeImageInLine]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('Recipe', 'Ingredient', 'Quantity',)
    list_filter = ('Recipe', 'Ingredient', )

class ProfileAdmin(admin.ModelAdmin):
    model = Profile

    list_display = ('user', 'name', 'bio',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Profile, ProfileAdmin)
