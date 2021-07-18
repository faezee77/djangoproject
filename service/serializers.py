from rest_framework import serializers
from .models import Service, Comment, Cart
from accounts.serializers import CustomUserDetailsSerializer


# post
class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    # user = CustomUserDetailsSerializer()

    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'price', 'group', 'groupPersian', 'Rating', 'user')
        # depth = 1


# get
class ServiceRetrieveSerializer(serializers.ModelSerializer):
    user = CustomUserDetailsSerializer()  # or you could use your UserSerializer, see the last part of the answer

    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'price', 'group', 'groupPersian', 'Rating', 'user')
        read_only = ('id', 'title', 'description', 'user',)
        depth = 1


# post
class CommentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'
        # depth = 1


# get
class CommentRetrieveSerializer(serializers.ModelSerializer):
    writerComment = CustomUserDetailsSerializer()
    service = ServiceSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'rate_AI', 'writerComment', 'service')
        depth = 1


class CartSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'
        # depth = 1


# get
class CartRetrieveSerializer(serializers.ModelSerializer):

    user = CustomUserDetailsSerializer()
    Services = ServiceSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'Services', 'user')
        depth = 1
