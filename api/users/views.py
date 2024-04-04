from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer, UserSerializer
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class UserSignupView(APIView):
    """
    Allows users to sign up and obtain an authentication token.

    **POST** method:
    - Requires:
      - `username`: The username for the new user.
      - `password`: The password for the new user.
    - Returns:
      - `token`: Authentication token for the newly created user.
    """

    permission_classes = [AllowAny]

    def post(self, request):
      serializer = CustomUserSerializer(data=request.data)
      if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user) 

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    """
    Allows users to log in and obtain an authentication token.

    **POST** method:
    - Requires:
      - `username`: The username of the user.
      - `password`: The password of the user.
    - Returns:
      - `token`: Authentication token for the logged-in user.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token_queryset = Token.objects.filter(user=user)
            if token_queryset.exists():
                token = token_queryset.first()
            else:
                token = Token.objects.create(user=user)

            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            raise AuthenticationFailed('Invalid credentials')



class UserLogoutView(APIView):
    """
    Allows authenticated users to log out by deleting their authentication token.

    **POST** method:
    - Logs out the user by deleting the authentication token.
    - Returns:
      - `detail`: Confirmation message indicating successful logout.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'detail': 'Logged out successfully'}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    """
    Allows authenticated users to view and update their profile.

    **GET** method:
    - Retrieves the profile of the authenticated user.

    **PUT** method:
    - Updates the profile of the authenticated user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    """
    Allows authenticated users to view the list of all users.

    **GET** method:
    - Retrieves the list of all users.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a specific user by their ID.

    **GET** method:
    - Requires:
      - `id`: The ID of the user to retrieve.
    - Returns:
      - The data of the specified user.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'