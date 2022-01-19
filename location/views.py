from operator import ge
from rest_framework.viewsets import generics
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim

from location.serializers import HotelSerializer
from location.models import Hotel

geolocator = Nominatim(user_agent="location")

class ListCreateHotelView(generics.ListCreateAPIView):
    queryset=Hotel.objects.all()
    serializer_class = HotelSerializer
    
    def perform_create(self,serializer):
        address = serializer.initial_data=['address']
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lat,lng)
        print(pnt)
        serializer.save(location=pnt)
        
class RetrieveUpdateHotelView(generics.RetrieveUpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    def perform_create(self,serializer):
        address = serializer.initial_data=['address']
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lat,lng)
        print(pnt)
        serializer.save(location=pnt)