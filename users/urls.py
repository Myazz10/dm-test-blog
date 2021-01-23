from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_changed/', views.password_changed, name='password-changed'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='user-profile-page'),
    path('<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create-profile-page/', CreateProfilePageView.as_view(), name='create-profile-page'),
]
