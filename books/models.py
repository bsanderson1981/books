
import uuid # new for uuid in urls
from django.contrib.auth import get_user_model #new
from django.db import models
from django.urls import reverse #new


# Create your models here.
class Book(models.Model):
    #id for uuid field
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, #needed for encrytion
        editable=False)


    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    cover =  models.ImageField(upload_to='covers/', blank=True) # 4 user upload media

    class Meta: #add permissions access to class
        permissions = [
            ('special_status', 'Can read all books'),


        ]
    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name ='reviews',

    )

    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.review

