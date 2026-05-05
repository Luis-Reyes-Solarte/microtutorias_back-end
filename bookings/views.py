# Create your views here.
from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer


class BookingUpdateView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
