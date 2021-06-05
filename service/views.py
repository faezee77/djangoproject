from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ServiceSerializer
from .models import Service


# Service API
class ServiceAPI(generics.GenericAPIView):
    serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Service.objects.all()
        serializer = ServiceSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data)


class ServiceDetails(generics.GenericAPIView):
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        service = Service.objects.filter(pk=self.kwargs['pk'])
        serializer = ServiceSerializer(service, context={'request': request}, many=True)
        return Response(serializer.data)


class ServiceGroup(generics.GenericAPIView):
    serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
        group = request.data["group"]
        service = Service.objects.filter(group=group)
        serializer = ServiceSerializer(service, context={'request': request}, many=True)
        return Response(serializer.data)
