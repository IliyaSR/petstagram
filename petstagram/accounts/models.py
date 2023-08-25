from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.accounts.validators import name_only_alphabetical


class PetstagramUser(AbstractUser):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show')
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(validators=(MinLengthValidator(2), name_only_alphabetical), max_length=30)
    last_name = models.CharField(validators=(MinLengthValidator(2), name_only_alphabetical), max_length=30)
    profile_picture = models.URLField()
    gender = models.CharField(choices=GENDER)
