from django.db import models
from datetime import datetime

from django.db import models

class Item(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField()

    def __str__(self):
        return f'Отзыв: {self.review[:30]}...'