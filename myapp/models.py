from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    data_of_birth = models.DateTimeField(default=timezone.now())

    @property
    def full_name(self):
        return f"{self.firstname, self.lastname}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField()
    views = models.IntegerField(default=0)
