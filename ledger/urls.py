from django.urls import path
from .views import home

urlpatterns = [
    path('/recipes/list', recipe_list, name="recipelist"),
    path('/recipe/<int:num>', recipe_num, name="recipe_num")
]

app_name = "ledger"