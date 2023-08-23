from django.shortcuts import render, redirect

from petstagram.pets.forms import PetBaseForm, PetEditForm, PetCreateForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def pet_add_page(request):
    if request.method == "GET":
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_details', pk=1)

    context = {
        'form': form
    }

    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    photos_count = all_photos.count()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'photos_count': photos_count,
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_edit_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'GET':
        form = PetEditForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_details', username, pet_slug)

    context = {
        'form': form
    }

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def pet_delete_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile_details', pk=1)

    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form
    }

    return render(request, template_name='pets/pet-delete-page.html', context=context)
