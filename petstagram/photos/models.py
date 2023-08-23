from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.photos.validators import image_max_size


class Photo(models.Model):
    pet_image = models.ImageField(
        validators=(image_max_size,),
        upload_to="photos/"
    )
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)])
    location = models.CharField(max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
