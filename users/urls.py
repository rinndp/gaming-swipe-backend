from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views.auth import LoginView, RegisterView

urlpatterns = [
    path('users/login', LoginView.as_view(), name='login'),
    path('users/create', RegisterView.as_view(), name='login'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]