# your_app/api/views.py
from datetime import date
from rest_framework import generics, status
from .serializers import LibrarySerializer
from ..models import Library
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class BookListAPIView(generics.ListAPIView):
    serializer_class = LibrarySerializer

    def get_queryset(self):
        limit = self.request.query_params.get('limit', None)
        queryset = Library.objects.all()
        if limit:
            queryset = queryset[:int(limit)]
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class CheckoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        book_id = request.data['pk']
        book = Library.objects.get(pk=book_id)

        if book.is_in_stock:
            book.is_in_stock = False
            book.date_checked_out = date.today()
            book.save()

            serializer = LibrarySerializer(book)
            return Response({'success': True, 'data': serializer.data})
        else:
            serializer = LibrarySerializer(book)
            return Response({'success': False, 'data': serializer.data})