from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductModelSerializer
from .models import ProductModel

@api_view(['GET'])
def product_model_list(request):
    cars = ProductModel.objects.all()
    serializer = ProductModelSerializer(cars, many=True)
    return Response(serializer.data)