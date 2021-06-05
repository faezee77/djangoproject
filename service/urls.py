from .views import ServiceAPI, ServiceDetails, ServiceGroup
from django.urls import path

urlpatterns = [
    path('api/services/', ServiceAPI.as_view(), name='service'),
    path('api/service/<int:pk>/', ServiceDetails.as_view(), name='service-detail'),
    path('api/service/group/', ServiceGroup.as_view(), name='service-detail'),

]