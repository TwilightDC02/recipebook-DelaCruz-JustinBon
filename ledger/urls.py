from django.urls import path
from .views import recipe_list, detailed_recipe

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:recipe_num>', detailed_recipe, name="recipe")
]

app_name = "ledger"
