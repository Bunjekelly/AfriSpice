from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='user-signup'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password-change'),
]