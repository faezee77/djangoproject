from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from subprocess import Popen, PIPE
from .serializers import ServiceSerializer, ServiceRetrieveSerializer, CommentSerializer, CommentRetrieveSerializer\
    , CartRetrieveSerializer, CartSerializer
from .models import Service, Comment, Cart
from django.core.files import File

from accounts.models import Account
# Service API
class ServiceAPI(generics.GenericAPIView):
    # serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            retrive_serializer = ServiceRetrieveSerializer(instance)
            return Response(retrive_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Service.objects.all()
        serializer = ServiceRetrieveSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data)


class ServiceDetails(generics.GenericAPIView):
    serializer_class = ServiceRetrieveSerializer

    def get(self, request, *args, **kwargs):
        service = Service.objects.filter(pk=self.kwargs['pk'])
        serializer = ServiceRetrieveSerializer(service, context={'request': request}, many=True)
        return Response(serializer.data)


class ServiceGroup(generics.GenericAPIView):
    serializer_class = ServiceRetrieveSerializer

    def post(self, request, *args, **kwargs):
        group = request.data["group"]
        service = Service.objects.filter(group=group)
        serializer = ServiceRetrieveSerializer(service, context={'request': request}, many=True)
        return Response(serializer.data)


class MyService(generics.GenericAPIView):
    serializer_class = ServiceRetrieveSerializer

    def post(self, request, *args, **kwargs):
        user = request.data["user"]
        service = Service.objects.filter(user=user)
        serializer = ServiceRetrieveSerializer(service, context={'request': request}, many=True)
        return Response(serializer.data)


class CommentAPI(generics.GenericAPIView):
    # serializer_class = CommentSerializer
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            retrive_serializer = CommentRetrieveSerializer(instance)
            print(request.data['content'])
            f = open('C:/Users/faeze/Desktop/comments.txt', 'a', encoding='utf-8')
            testfile = File(f)
            testfile.write("%s,%s \n" % ( retrive_serializer.data['id'],request.data['content']))
            testfile.close
            f.close
            with open("C:/Users/faeze/Desktop/comments.txt", "r", encoding='utf-8') as a_file:
                for line in a_file:
                    stripped_line = line.split(',')
                    print(stripped_line[1])

            return Response(retrive_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        with open("C:/Users/faeze/Desktop/resultcomments.txt", "r", encoding='utf-8') as a_file:
            for line in a_file:
                stripped_line = line.split(',')
                print(round(float(stripped_line[0])))
                print(stripped_line[1])
                product = Comment.objects.filter(id=stripped_line[1]).first()
                request ={'data':{
                    'rate_AI': round(float(stripped_line[0]))
                }}
                serializer = CommentSerializer(product, data=request['data'])
                if serializer.is_valid():
                    serializer.save()
            products = Comment.objects.all()
            serializer = CommentRetrieveSerializer(products, context={'request': request}, many=True)
            return Response(serializer.data)



class CommentDetails (generics.GenericAPIView):
    serializer_class = CommentRetrieveSerializer

    def post(self, request, *args, **kwargs):
        with open("C:/Users/faeze/Desktop/resultcomments.txt", "r", encoding='utf-8') as a_file:
            for line in a_file:
                stripped_line = line.split(',')
                print(round(float(stripped_line[0])))
                print(stripped_line[1])
                product = Comment.objects.filter(id=stripped_line[1]).first()
                myrequest ={'data':{
                    'rate_AI': round(float(stripped_line[0]))
                }}
                serializer = CommentSerializer(product, data=myrequest['data'])
                if serializer.is_valid():
                    serializer.save()
            service_id = request.data["service_id"]
            comment = Comment.objects.filter(service=service_id)
            serializer = CommentRetrieveSerializer(comment, context={'request': request}, many=True)
            return Response(serializer.data)

    class ServiceAPI(generics.GenericAPIView):
        # serializer_class = ServiceSerializer

        def post(self, request, *args, **kwargs):
            serializer = ServiceSerializer(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                retrive_serializer = ServiceRetrieveSerializer(instance)
                return Response(retrive_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def get(self, request):
            products = Service.objects.all()
            serializer = ServiceRetrieveSerializer(products, context={'request': request}, many=True)
            return Response(serializer.data)

class CartAPI(generics.GenericAPIView):
    # serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            retrive_serializer = CartRetrieveSerializer(instance)
            return Response(retrive_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Cart.objects.all()
        serializer = CartRetrieveSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user_id = request.data['user']
        cart = Cart.objects.get(user=user_id)
        print(cart)
        cart.Services.add(request.data['Services'][0])
        # user.first_name = request.data['first_name']
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AiAPI(generics.GenericAPIView):
    def get(self, request):
        p = Popen(["python", "C:/Users/faeze/Desktop/AIprojet/main.py"], cwd='C:/Users/faeze/Desktop/AIprojet', stdout=PIPE, stderr=PIPE)
        print('pp')
        out, err = p.communicate()
        print(out,err)

        return Response(out, status=status.HTTP_200_OK)
