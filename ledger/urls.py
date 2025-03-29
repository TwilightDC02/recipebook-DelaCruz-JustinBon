from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import recipe_list, detailed_recipe

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:recipe_num>', detailed_recipe, name="recipe")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "ledger"
