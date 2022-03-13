
from django.conf import settings
from django.http import Http404
from django.shortcuts import render

import logging 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Order #, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST'])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
     def get(self, request, id, format=None):
        logging.debug('SOLICITUD', request.headers['User-Agent'])
        orders = Order.objects.get(id=id)  
        serializer = MyOrderSerializer(orders)
        # dataset = self.request.user.username
        return Response(serializer.data)
    # def get(self, request, id=None):
    #     print(request)
    #     if id:
    #         try:
    #             queryset = Order.objects.get(id=id)
    #         except:
    #             return Response({'errors': 'La orden no existe'}, status=400)

    #         read_serializer = OrderSerializer(queryset)
    #     else:
    #         queryset = Order.objects.all()
    #         read_serializer = OrderSerializer(queryset, many=True)

    #     return Response(read_serializer.data)