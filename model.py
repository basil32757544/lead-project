from django.db import models

# Create your models here.


class Lead(models.Model):
    # Choices for status and source
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Converted', 'Converted'),
        ('Rejected', 'Rejected'),
    ]

    SOURCE_CHOICES = [
        ('Online', 'Online'),
        ('Referral', 'Referral'),
        ('Event', 'Event'),
        ('Advertisement', 'Advertisement'),
    ]

    # Fields for the Lead model
    name = models.CharField(max_length=255)  # Name of the lead
    email = models.EmailField(unique=True)  # Email (must be unique)
    phone_number = models.CharField(max_length=15)  # Phone number
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')  # Status
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='Online')  # Source

    def __str__(self):
        return self.name
