from django.urls import path, include

from petstagram.photos.views import photo_add_page, photo_details_page, photo_edit_page, photo_delete_page

urlpatterns = [
    path('add/', photo_add_page, name='photo_add'),
    path('<int:pk>/', include([
        path('', photo_details_page, name='photo_details'),
        path('edit/', photo_edit_page, name='photo_edit'),
        path('delete/', photo_delete_page, name='delete_page')
    ]))
]

