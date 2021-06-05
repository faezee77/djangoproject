# from rest_framework import serializers
# # from django.contrib.auth.models import User
# from .models import Account
#
#
# # User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ('id', 'name', 'email', 'password', 'phone', 'last_name')
#
#
# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     last_name = serializers.CharField(max_length=150)
#     phone = serializers.CharField(max_length=150)
#
#     class Meta:
#         model = Account
#         fields = ('id', 'name', 'email', 'password', 'phone', 'last_name')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = Account.objects.create_user(validated_data['name'], validated_data['email'], validated_data['password'])
#         return user


from abc import ABC

from . import models
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer, get_adapter, setup_user_email


class CustomRegisterSerializer(RegisterSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True, source="user.id")
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    mobile_number = serializers.CharField(max_length=50, default='09028080656')
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150, default='ahmadi')

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        clean_data = {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get("first_name", ''),
            'last_name': self.validated_data.get("last_name", ''),
            'mobile_number': self.validated_data.get("mobile_number", '')

        }
        return clean_data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('id', 'username', 'email','mobile_number', 'first_name', 'last_name')
        # fields = ('username', 'email', 'first_name', 'last_name')


class USerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'
