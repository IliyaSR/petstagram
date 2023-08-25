from django.urls import path, include
from petstagram.accounts.views import UserLoginView, profile_details_page, UserEditView, \
    profile_delete_page, UserRegisterView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', profile_details_page, name='profile_details'),
        path('edit/', UserEditView.as_view(), name='profile_edit'),
        path('delete/', profile_delete_page, name='profile_delete')
    ]))
]
