from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    # We use related_name to specify the name of the reverse relationship.
    # This will allow us to access related objects easily from a user object by using the user.blog_posts notation
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.CharField(max_length=255)
    publish = models.DateTimeField(default=timezone.now)  # returns date in timezone aware format
    created = models.DateTimeField(auto_now_add=True)  # adds the current date in the database once does not change it
    # after
    updated = models.DateTimeField(auto_now=True)  # updates the current date in the database
    category = models.ManyToManyField(Category)  # Need to create category model
    tag = models.ManyToManyField(Tag)  # Need to create tag model
    body = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:  # Defines metadata for the model
        ordering = ['-publish']  # ordering attribute to sort the data while fetching
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
