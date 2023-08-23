from django.urls import path,include
from petstagram.pets.views import pet_add_page, pet_details_page, pet_edit_page, pet_delete_page

urlpatterns = [
    path('add/', pet_add_page, name='pet_add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', pet_details_page, name='pet_details'),
        path('edit/', pet_edit_page, name='pet_edit'),
        path('delete/', pet_delete_page, name='pet_delete')
    ]))
]
