from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from initial_app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import RegistrationSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]




class DummyClass(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):

        print(request)
        return Response({'hello': 'Rahul'})


class Registration(APIView):

    def post(self, request, *args, **kwargs):

        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                created, profile_id, message = serializer.create(
                    validated_data=validated_data)
                if created:
                    return Response(
                        {
                            'created': True,
                            'user_id': profile_id
                        },
                        status=status.HTTP_200_OK)
                else:
                    return Response(
                        {
                            'message': message
                        },
                        status=status.HTTP_400_BAD_REQUEST) 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response(
                {'message': 'Issue'},
                status=status.HTTP_409_CONFLICT)
