from rest_framework import viewsets
from . import models
from . import serializers


class LaptopViewset(viewsets.ModelViewSet):
	queryset = models.Laptop.objects.all()
	serializer_class = serializers.LaptopSerializer
