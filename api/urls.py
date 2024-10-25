from django.urls import path
from .views import UserLoginView, UserRegisterView, ImageUploadView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
]