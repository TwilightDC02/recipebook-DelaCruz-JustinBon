from django.urls import path
from .views import recipe_list

urlpatterns = [
    path('/recipes/list', recipe_list, name="recipe_list"),
]

app_name = "ledger"