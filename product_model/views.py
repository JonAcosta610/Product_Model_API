from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductModelSerializer
from .models import ProductModel
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def product_model_list(request):
    if request.method == 'GET':
        products = ProductModel.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)

@api_view(['GET', 'PUT'])
def product_model_detail(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    if request.method == 'GET':
        serializer = ProductModelSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductModelSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
