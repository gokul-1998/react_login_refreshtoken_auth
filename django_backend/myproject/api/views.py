# api/views.py
from rest_framework import generics
from .models import Employee, User
from .serializers import EmployeeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
def handle_login(request):
    username = request.data.get('user')
    password = request.data.get('pwd')
    print("inside login", username)
    if not username or not password:
        return Response({'message': 'Username and password are required.'}, status=400)

    try:
        user = User.objects.get(username=username)
        print(user)
        hashed_password = make_password(password)
        print(user.password== hashed_password)
        if user.password == hashed_password:  # You should hash and compare passwords in a real app
            access_token = jwt.encode({'username': user.username}, settings.ACCESS_TOKEN_SECRET, algorithm='HS256')
            refresh_token = jwt.encode({'username': user.username}, settings.REFRESH_TOKEN_SECRET, algorithm='HS256')
            return Response({'access_token': access_token, 'refresh_token': refresh_token})
        return Response({'message': 'Unauthorized'}, status=401)
    except User.DoesNotExist:
        return Response({'message': 'Unauthorized'}, status=401)

@api_view(['POST'])
def handle_logout(request):
    # Handle logout logic, typically you'd revoke the refresh token
    return Response(status=204)


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

@api_view(['POST'])
def register_user(request):
    # Get the username and password from the request data
    username = request.data.get('user')
    password = request.data.get('pwd')
    print(username, password)
    # Check if both username and password are provided
    if not username or not password:
        return Response({'message': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the username already exists in the database
    if User.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists.'}, status=status.HTTP_409_CONFLICT)

    # Create a new user and hash the password
    user = User(username=username, password=make_password(password))
    user.save()

    # Return a success response
    return Response({'message': f'User {username} registered successfully!'}, status=status.HTTP_201_CREATED)
