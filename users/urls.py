from django.urls import path

from users.views import RegistrView, LoginView, LogoutView, EditProfileView

urlpatterns = [
    path('register/', RegistrView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('editprofile/', EditProfileView.as_view(), name='editprofile')
]
