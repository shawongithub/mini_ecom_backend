from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from . models import Product, Cart
from . serializers import ProductSerializer
from utils.auth import authenticate_appuser

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
def add_to_cart(request):
    sts, user_pk = authenticate_appuser(request)
    if sts:
        data = request.data
        products = data.get('products')
        try:
            user = User.objects.get(pk=user_pk)
            for product in products:
                item = Product.objects.get(pk=product.get('id'))
                cart, created = Cart.objects.get_or_create(user=user,item=item)
                cart.quantity +=1
                cart.save()
            return Response("ok",status=status.HTTP_201_CREATED)
        except:
            return Response(data="invalid request",status=status.HTTP_400_BAD_REQUEST)
    return Response(data="invalid user",status=status.HTTP_400_BAD_REQUEST)
