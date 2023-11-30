from django.db import models
from django.utils.text import slugify
import datetime



class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    message =  models.TextField()

    def __str__(self):
        return self.full_name




class Journal(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='journal_images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Replace spaces with underscores in the name before creating the slug
        self.slug = slugify(self.name.replace(" ", "_"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Members(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=50)
    image_url = models.URLField(null=True)
    fb = models.URLField(null=True, blank=True)
    lk = models.URLField(null=True, blank=True)
    x = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True)
    bio = models.TextField()

    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_trustee = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
   

    def save(self, *args, **kwargs):
        # Replace spaces with underscores in the name before creating the slug
        self.slug = slugify(self.full_name.replace(" ", "_"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name



class Todos(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title