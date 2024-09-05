from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.TextField(max_length=28)
    ingredients = models.TextField()
    tags = models.ManyToManyField(Tag)
    prep_time = models.FloatField()
    servings = models.IntegerField()
    description = models.TextField()
    directions = models.TextField()

    def __str__(self):
        return self.name
