from django.db import models
from users.models import CustomUser

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_seller': True})

    def __str__(self):
        return self.title