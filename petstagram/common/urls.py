from django.urls import path, include
from petstagram.common.views import home_page, like_functionality, copy_link_to_clipboard, add_comment

urlpatterns = [
    path('', home_page, name='home'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>', add_comment, name='add_comment')
]
