from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import SignUpSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from utils.auth import TokenProvider

@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        data = request.data
        serializer = SignUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'result':'user saved successfully'})

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user_pk = user.id
            token_provider = TokenProvider()
            sts, token = token_provider.provide(user_pk)
            if sts:
                return Response(data={'token':token})
        else:
            return Response(data={'result':'no user found'})
