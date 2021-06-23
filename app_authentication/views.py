from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import SignUpSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        data = request.data
        serializer = SignUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
        return Response(data={'result':'ok'})

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print(user)
        else:
            print('not found')

        return Response(data='ok')