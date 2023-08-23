from django.urls import path, include
from petstagram.accounts.views import registration_page, login_page, profile_details_page, profile_edit_page, \
    profile_delete_page

urlpatterns = [
    path('register/', registration_page, name='register'),
    path('login/', login_page, name='login'),
    path('profile/<int:pk>/', include([
        path('', profile_details_page, name='profile_details'),
        path('edit/', profile_edit_page, name='profile_edit'),
        path('delete/', profile_delete_page, name='profile_delete')
    ]))
]
