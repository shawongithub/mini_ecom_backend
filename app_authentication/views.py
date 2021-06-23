from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        data = request.data

        return Response(data={'result':'ok'})