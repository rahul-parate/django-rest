

from .models import Profile
from rest_framework import serializers
from .services.registration_service import RegistrationService


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile


class RegistrationSerializer(serializers.Serializer):

	name = serializers.CharField(max_length=200)
	phone = serializers.CharField(max_length=100)
	address = serializers.CharField(max_length=300)
	username = serializers.CharField(max_length=100)
	email = serializers.CharField(max_length=100)

	def create(self, validated_data):

		email = validated_data['email']
		phone=validated_data['phone']

		profile_id = None
		registration_service = RegistrationService(phone=phone, email=email)
		can_create, message = registration_service.validate_user()
		if can_create:
			profile_id = registration_service.create_user(
				registration_data=validated_data)
			return can_create, profile_id, message
		return can_create, profile_id, message


	def update(self, validated_data):
		print("Updating data")