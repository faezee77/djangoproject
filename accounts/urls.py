# from .views import RegisterAPI, LoginAPI
from django.urls import path
import rest_auth.urls
import rest_auth.registration.urls
from django.urls import path, include
from .views import CustomAuthToken, Profile

urlpatterns = [
    #     path('api/register/', RegisterAPI.as_view(), name='register'),
    #     path('api/login/', LoginAPI.as_view(), name='login'),
    #     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    #     path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('logininfo/', CustomAuthToken.as_view()),
    path('profile/', Profile.as_view()),

]
