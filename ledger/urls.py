from django.urls import path
from .views import recipe_list, detailed_recipe, add_recipe, add_image

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:recipe_num>', detailed_recipe, name="recipe")
    path('recipe/add/', add_recipe, name="new_recipe")
    path('recipe/<int:recipe_num>', add_image, name="add_image")
]

app_name = "ledger"
