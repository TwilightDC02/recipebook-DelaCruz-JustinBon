from django.urls import path
from .views import recipe_list, recipe

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipes/list/<int:num>', recipe, name="recipe")
]

app_name = "ledger"
