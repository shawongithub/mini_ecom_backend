from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def user_signup(request):
    if request.method == 'GET':
        return Response(data={'result':'ok'})