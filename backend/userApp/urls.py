from django.urls import path
from .views import (
    index, signup, login, list_users, get_user, update_user, delete_user, search_user, reset_password
)
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('users/', list_users, name='list_users'),
    path('users/<int:user_id>/', get_user, name='get_user'),
    path('users/<int:user_id>/update/', update_user, name='update_user'),
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),
    path('users/search/', search_user, name='search_user'),
    path('reset_password/', reset_password, name='reset_password'),
]
