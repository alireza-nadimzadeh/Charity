from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


class LogoutAPIView(APIView):
    pass


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )    
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User added successfully!'})

        return Response({'message': user_serializer.errors})