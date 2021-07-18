from .views import ServiceAPI, ServiceDetails, ServiceGroup, CommentAPI, CommentDetails, CartAPI,AiAPI,MyService
from django.urls import path

urlpatterns = [
    path('api/services/', ServiceAPI.as_view(), name='service'),
    path('api/service/<int:pk>/', ServiceDetails.as_view(), name='service-detail'),
    path('api/service/group/', ServiceGroup.as_view(), name='service-detail'),
    path('api/service/myservices/', MyService.as_view(), name='my-service'),
    path('api/service/comments/', CommentAPI.as_view(), name='comment'),
    path('api/service/comment/post/', CommentDetails.as_view(), name='service-comments'),
    path('api/service/cart/', CartAPI.as_view(), name='cart'),
    path('api/service/ai/', AiAPI.as_view(), name='AI'),

]