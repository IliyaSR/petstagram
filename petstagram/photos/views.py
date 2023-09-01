from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


def photo_add_page(request):
    if request.method == "GET":
        form = PhotoAddForm()
    else:
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)


def photo_details_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.count()
    comments = photo.comment_set.all()
    photo_is_liked_by_user = likes.filter(user=request.user)

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'photo_is_liked_by_user': photo_is_liked_by_user
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit_page(request, pk):
    photo = Photo.objects.get(pk=pk)

    if request.method == 'GET':
        form = PhotoEditForm(initial=photo.__dict__, instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_details', pk)

    context = {
        'form': form
    }
    return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')
