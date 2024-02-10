import os
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
    bio = models.TextField()

    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_trustee = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_nominated = models.BooleanField(default=False)  # New field for nomination
    is_executive = models.BooleanField(default=False)  # New field for marking elected members

    def save(self, *args, **kwargs):
        # Replace spaces with underscores in the name before creating the slug
        self.slug = slugify(self.full_name.replace(" ", "_"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
    


class Nomination(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    is_nominated = models.BooleanField(default=False)
    n_reason = models.TextField()

    def __str__(self):
        return self.member.full_name  # Assuming 'name' is a field in the Members model



class Todos(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

    



def generate_file_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f"{instance.title}_vol{instance.version}{file_extension}"



class Journalfiles(models.Model):
    Journal = models.FileField(upload_to=generate_file_path)
    title = models.CharField(max_length=100)
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
    


class VolunteerApplication(models.Model):
    POSITION_CHOICES = [
        ('editor_in_chief', 'Editor-in-Chief'),
        ('managing_editor', 'Managing Editor'),
        ('section_editor', 'Section Editor'),
        ('copy_editor', 'Copy Editor'),
        ('peer_review_coordinator', 'Peer Review Coordinator'),
        ('design_layout_editor', 'Design and Layout Editor'),
        ('technical_editor', 'Technical Editor'),
        ('publications_manager', 'Publications Manager'),
        ('marketing_coordinator', 'Marketing Coordinator'),
        ('advisory_board_member', 'Advisory Board Member'),
    ]
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # You can adjust the max length based on your needs
    email = models.EmailField()
    skills = models.TextField()
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    why_volunteer = models.TextField()
    fit_for_position = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.first_name} {self.surname}"
