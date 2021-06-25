from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
def add_to_cart(request):
    data = request.data
    print(data)
    return Response("ok")
