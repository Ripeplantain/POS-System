from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']
    USERNAME_FIELD = 'email'  # Use a string here, not a list
