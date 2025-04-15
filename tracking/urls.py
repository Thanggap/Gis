from django.urls import path
from .views import (
    home_view, login_view, register_view, logout_view, map_view, profile_view, update_profile_view, change_password_view,
    RegisterView, LoginView, LogoutView,
    LocationUpdateView, LocationFetchView, AllUserLocationsView
)

urlpatterns = [
    # ----------- Giao diện người dùng (HTML) -----------
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('map/', map_view, name='map'),
    path('profile/', profile_view, name='profile'),
    path('update-profile/', update_profile_view, name='update_profile'),
    path('change-password/', change_password_view, name='change_password'),

    # ----------- API (Django REST Framework) -----------
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    path('api/update_location/', LocationUpdateView.as_view(), name='api-update-location'),
    path('api/get_user_location/<str:username>/', LocationFetchView.as_view(), name='api-user-location'),
    path('api/get_all_locations/', AllUserLocationsView.as_view(), name='api-all-locations'),
]

