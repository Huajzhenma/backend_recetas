from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cocina.models import Cocina
from cocina.serializers import CocinaSerializer

@api_view(['GET', 'POST','DELETE'])
def cocina_list(request, id = None):
    """
    List all code Books, or create a new Book.
    """
    if request.method == 'GET':
        cocina = Cocina.objects.all()
        serializer = CocinaSerializer(cocina, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CocinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        cocina = Cocina.objects.filter(id = id)
        serializer = CocinaSerializer(cocina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cocina = Cocina.objects.filter(id = id)
        cocina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
      
    
