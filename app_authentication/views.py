from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import SignUpSerializer


@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        data = request.data
        serializer = SignUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
        return Response(data={'result':'ok'})