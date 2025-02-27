from django.contrib import admin
from .models import *

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ('name',)
    search_fields = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ('name',)
    search_fields = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('Recipe', 'Ingredient', 'Quantity')
    search_fields = ('Recipe',)
    list_filter = ('Ingredient',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
