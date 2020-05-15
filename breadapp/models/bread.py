from django.db import models
from django.urls import reverse


class Bread(models.Model):

    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    ingredients = models.ManyToManyField("Ingredient", through='BreadIngredient')

    class Meta:
        verbose_name = ("Bread")
        verbose_name_plural = ("Breads")

    def __str__(self):
        return f"{self.name} ({self.region})"

    def get_absolute_url(self):
        return reverse("Bread_detail", kwargs={"pk": self.pk})
