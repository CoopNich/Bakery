from django.db import models


class BreadIngredient(models.Model):

    bread = models.ForeignKey("Bread", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    amount = models.CharField(max_length=25)
