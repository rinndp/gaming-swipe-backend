from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views.auth import LoginView, RegisterView
from users.views.get_user import GetUserView
from users.views.update_user import UpdateUserView

urlpatterns = [
    path('users/login', LoginView.as_view(), name='login'),
    path('users/create', RegisterView.as_view(), name='register'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/<str:slug>', GetUserView.as_view(), name='get-user'),
    path('users/update/<str:slug>', UpdateUserView.as_view(), name='update-user'),
]

