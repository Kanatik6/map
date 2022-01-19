from typing import List
from django.urls import path

from location.views import ListCreateHotelView,RetrieveUpdateHotelView


urlpatterns = [
    path('hotels/',ListCreateHotelView.as_view(),name='hotels'),
    path('hotels/<int:pk>/',RetrieveUpdateHotelView.as_view(),name='hotel')
]