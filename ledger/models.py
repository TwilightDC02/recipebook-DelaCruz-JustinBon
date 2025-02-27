from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'This is the recipe for: {}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.name)])

class RecipeIngredient(models.Model):
    Quantity = models.IntegerField()
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient')
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe')
