from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.id)])

class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=255)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
