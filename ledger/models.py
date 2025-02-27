from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    name = models.CharField(max_length=255)

class RecipeIngredient(models.Model):
    Quantity = models.IntegerField()
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient')
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe')
