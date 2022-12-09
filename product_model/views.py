from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductModelSerializer
from .models import ProductModel
from rest_framework import status

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