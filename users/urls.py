from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import CheckIfEmailIsAlreadyRegistered, CheckIfUsernameIsAlreadyRegistered
from users.views.auth import LoginView, RegisterView
from users.views.get_user import GetUserView, SearchUserView
from users.views.update_user import UpdateUserView, UpdatePasswordView

urlpatterns = [
    path('users/login', LoginView.as_view(), name='login'),
    path('users/create', RegisterView.as_view(), name='register'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/<str:slug>', GetUserView.as_view(), name='get-user'),
    path('users/update/<str:slug>', UpdateUserView.as_view(), name='update-user'),
    path('users/update-password/<str:slug>', UpdatePasswordView.as_view(), name='update-password'),
    path('users/search/', SearchUserView.as_view(), name='search-user'),
    path('users/check-if-registered/', CheckIfEmailIsAlreadyRegistered.as_view(), name='check-if-registered'),
    path('users/check-if-username-registered/', CheckIfUsernameIsAlreadyRegistered.as_view(), name='check-if-username-registered'),
]

