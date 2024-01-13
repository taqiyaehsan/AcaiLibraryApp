# your_app/api/serializers.py
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from .. import models

class LibrarySerializer(ModelSerializer):
    class Meta:
        model = models.Library
        fields = '__all__'