from django.shortcuts import render
from .models import Menuitem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MenuItemSerializer
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuItemSerializer


# @api_view(['GET','POST'])
# def menu_items(request):

#     if request.method == 'GET':
#         items = Menuitem.objects.select_related('category').all()
#         serialized_item = MenuItemSerializer(items, many=True)
#         return Response(serialized_item.data)
    
#     elif request.method == "POST":
#         serialized_item = MenuItemSerializer(data=request.data)
#         serialized_item.is_valid(raise_exception=True)
#         serialized_item.save()
#         return Response(serialized_item.validated_data, status.HTTP_201_CREATED)
    

# @api_view()
# def single_item(request, id):
#     item = get_object_or_404(Menuitem, pk=id)
#     serialized_item = MenuItemSerializer(item)
#     return Response(serialized_item.data)