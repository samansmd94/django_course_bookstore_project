from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])
