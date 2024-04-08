from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='user-signup'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/delete/', views.UserDeleteView.as_view(), name='user_delete'),
]