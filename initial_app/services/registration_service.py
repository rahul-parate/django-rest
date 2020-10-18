from initial_app.models import Profile

class RegistrationService:

	def __init__(self, email, phone):

		self.email=email
		self.phone=phone

	def validate_user(self):

		profile_email_object = Profile.objects.filter(email=self.email)

		profile_phone_object = Profile.objects.filter(phone=self.phone)

		if profile_phone_object or profile_email_object:

			return False, 'Phone or email already exists'
		return True, None

	def create_user(self, registration_data):

		profile_object = Profile.objects.create(
			name=registration_data['name'],
			phone=registration_data['phone'],
			address=registration_data['address'],
			username=registration_data['username'],
			email=registration_data['email'])
		return profile_object.id