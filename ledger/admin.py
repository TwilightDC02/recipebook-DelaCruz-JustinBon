from django.contrib import admin
from .models import *

class RecipeIngredientReadOnlyInline(admin.TabularInline):
    model = RecipeIngredient

    readonly_fields = ['Recipe', 'Quantity']

class RecipeIngredientEditableInline(admin.TabularInline):
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ('name',)
    search_fields = ('name',)
    inlines = [RecipeIngredientReadOnlyInline, ]

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ('name',)
    search_fields = ('name',)
    inlines = [RecipeIngredientEditableInline, ]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('Recipe', 'Ingredient', 'Quantity')
    list_filter = ('Recipe', 'Ingredient', )

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
