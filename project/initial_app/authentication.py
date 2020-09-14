from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from datetime import datetime
from datetime import timedelta
import pytz


class ExpiringTokenAuthentication(TokenAuthentication):
	def authenticate_credentials(self, key):
		self.model = Token
		print(key, self.model)
		try:
			token = self.model.objects.get(key=key)
		except self.model.DoesNotExist:
			raise AuthenticationFailed('Invalid token')

		if not token.user.is_active:
			raise AuthenticationFailed('User inactive or deleted')

		# This is required for the time comparison
		utc_now = datetime.utcnow()
		utc_now = utc_now.replace(tzinfo=pytz.utc)

		if token.created < utc_now - timedelta(minutes=2):
			raise AuthenticationFailed('Token has expired')

		return token.user, token