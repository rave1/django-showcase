from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.generics import ListCreateAPIView

from cars.serializers import CarSerializer

from cars.models import Car
# Create your views here.

class CarView(ListView):
    model = Car


class CarsListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer