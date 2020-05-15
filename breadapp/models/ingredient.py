from django.db import models
from django.urls import reverse


class Ingredient(models.Model):

    name = models.CharField(max_length=100)
    local_source = models.CharField(max_length=100)
    breads = models.ManyToManyField("Bread", through='BreadIngredient')

    class Meta:
        verbose_name = ("Ingredient")
        verbose_name_plural = ("Ingredients")

    def __str__(self):
        return f"{self.name} ({self.local_source})"

    def get_absolute_url(self):
        return reverse("Ingredient_detail", kwargs={"pk": self.pk})
