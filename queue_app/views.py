from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer, ReviewSerializer
from rest_framework import status # 404, 403, 405 / 200, 201
from rest_framework.decorators import api_view # get, post, put, delete
from rest_framework.response import Response

@api_view(['GET'])
def api_root_view(request):
    routes = {
        "get_full_queue": "http://127.0.0.1:8000/api/v1/queue/ - GET",
        "post_queue": "http://127.0.0.1:8000/api/v1/post/ - POST",
        "get_queue_view": "http://127.0.0.1:8000/api/v1/queue/detail/pk - GET",
        "delete_queue_self": "http://127.0.0.1:8000/api/v1/queue/delete/pk - DELETE",
        "post_review": "http://127.0.0.1:8000/api/v1/reviews/post - POST"
    }
    return Response(routes)

@api_view(['GET'])
def get_full_queue(request):
    items = Item.objects.all() #table data 
    serializer = ItemSerializer(items, many=True) # json
    return Response(serializer.data)

@api_view(['POST'])
def post_queue(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_queue_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    serializer  = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_queue_self(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def post_review(request):
    serializer = ReviewSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
