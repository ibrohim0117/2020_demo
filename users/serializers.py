from typing import Any
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework import  serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from .models import User


class UserCreateSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'password')

    def validate_password(self, value):
        value = make_password(value)
        return value



class UserLoginSerializer(TokenObtainSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs['password']
        user = User.objects.filter(email__iexact=email).first()
        if user is None:
            raise ValidationError('Bazada bunday email topilmadi!')


        auth_user = authenticate(email=email, password=password)
        if auth_user is None:
            raise ValidationError('Parol yoki email xato aka!')

        data = {
           'access_token': auth_user.token().get('access_token'),
           'refresh_token': auth_user.token().get('refresh_token'),
        }

        return data


class UserUpdateSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    new_password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'phone', 'new_password', 'old_password')

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        old_password = attrs.get('old_password')
        email = attrs.get('email')
        return attrs

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance










