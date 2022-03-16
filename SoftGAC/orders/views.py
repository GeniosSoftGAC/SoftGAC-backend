
from django.conf import settings
from django.http import Http404
from django.shortcuts import render

import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Order  # , OrderItem
from .serializers import OrderSerializer


class OrderListView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin
):

    def get(self, request, id=None):
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

    def post(self, request):
        create_serializer = OrderSerializer(data=request.data)

        if create_serializer.is_valid():
            order_item_object = create_serializer.save()
            read_serializer = OrderSerializer(order_item_object)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)

    def put(self, request, id=None):
        try:
            order_item = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'errors': 'La orden no existe'}, status=400)

        update_serializer = OrderSerializer(order_item, data=request.data)

        if update_serializer.is_valid():
            order_item_object = update_serializer.save()
            read_serializer = OrderSerializer(order_item_object)
            return Response(read_serializer.data, status=200)

        return Response(update_serializer.errors, status=400)

    def delete(self, request, id=None):
        try:
            order_item = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'errors': 'La orden no existe'}, status=400)

        order_item.delete()
        return Response(status=204)
