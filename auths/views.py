from django.contrib.auth import authenticate, login as auth_login
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignupSerializer


@api_view(['GET'])
def auth_status(request):
    is_authenticated = request.user.is_authenticated

    return Response({"is_authenticated": is_authenticated}, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    error_message = "잘못된 유저 정보 입니다."
    email = request.data.get("email")
    password = request.data.get("password")

    if email is None or password is None:
        return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, email=email, password=str(password))
    if user is None:
        return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

    auth_login(request, user)
    return Response(status=status.HTTP_204_NO_CONTENT)


class Signup(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            email = request.data.get("email")
            password = request.data.get("password")
            user = authenticate(request, email=email, password=password)
            auth_login(request, user)

        return response
