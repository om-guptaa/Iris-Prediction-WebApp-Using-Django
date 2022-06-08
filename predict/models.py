from django.db import models

# Create your models here.

# Create Database model for storing Test Results


class PredResults(models.Model):

    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=50)

    def __str__(self):
        return self.classification
