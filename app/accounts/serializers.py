from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token




class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

# class UserRegisterSerializer(serializers.ModelSerializer):
#     id = serializers.PrimaryKeyRelatedField(read_only=True)
#     username = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ["id", "username", "first_name",
#                   "last_name", "email", "password", "password2"]
#         extra_kwargs = {
#             'password': {"write_only": True}
#         }
#
#     def validate_username(self, username):
#         if User.objects.filter(username=username).exists():
#             detail = {
#                 "detail": "User Already exist!"
#             }
#             raise ValidationError(detail=detail)
#         return username
#
#     def validate(self, instance):
#         if instance['password'] != instance['password2']:
#             raise ValidationError({"message": "Both password must match"})
#
#         if User.objects.filter(email=instance['email']).exists():
#             raise ValidationError({"message": "Email already taken!"})
#
#         return instance
#
#     def create(self, validated_data):
#         passowrd = validated_data.pop('password')
#         passowrd2 = validated_data.pop('password2')
#         user = User.objects.create(**validated_data)
#         user.set_password(passowrd)
#         user.save()
#         Token.objects.create(user=user)
#         return user
