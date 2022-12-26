from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'location', 'photo']

    #Check a given credintial is unique
    def validate(self, attrs):
        username_exists = User.objects.filter(username = attrs['username']).exists()
        if username_exists:
            raise ValidationError(f'This username is already used by another user')

        email_exists = User.objects.filter(email = attrs['email']).exists()
        if email_exists:
            raise ValidationError(f'This email is already used by another user')

        phone_exists = User.objects.filter(phone_number = attrs['phone_number']).exists()
        if phone_exists:
            raise ValidationError(f'This phone number is already used by another user')

        return super().validate(attrs)

    #Create The user and assign its password hashed
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user