from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=60)
#     email = models.EmailField()
#     age = models.IntegerField()


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    data_of_birth = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.firstname}, {self.lastname}"

    def __str__(self):
        return self.full_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(null=False, db_index=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save()

    def __str__(self):
        return self.title
