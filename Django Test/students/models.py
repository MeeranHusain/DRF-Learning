from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])

    # Academic Information
    standard = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    section = models.CharField(max_length=10)
    roll_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    # Contact Information
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    # Status
    is_active = models.BooleanField(default=True)
    