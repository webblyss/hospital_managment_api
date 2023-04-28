from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import authentication, permissions

class LoginView(APIView): 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Wrong username or password'}, status=status.HTTP_401_UNAUTHORIZED)



class UserInfoView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'username': user.username, 'email': user.email})










