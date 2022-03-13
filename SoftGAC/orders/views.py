
from django.conf import settings
from django.http import Http404
from django.shortcuts import render

import logging 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Order #, OrderItem
from .serializers import OrderSerializer

class OrderListView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin
):

    def get(self, request, id=None):
        print(request)
        if id:
            try:
                queryset = Order.objects.get(id=id)
            except:
                return Response({'errors': 'La orden no existe'}, status=400)

            read_serializer = OrderSerializer(queryset)
            logging.debug(queryset)
        else:
            queryset = Order.objects.all()
            read_serializer = OrderSerializer(queryset, many=True)

        return Response(read_serializer.data)