from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(ModelViewSet):
    """
    ViewSet para la reserva de una tutoría.

    Parameters
    ----------
    ModelViewSet : Class
        Super clase de rest_framework.viewsets.ModelViewSet que proporciona
        funcionalidades para manejar vistas basadas en modelos.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        asigna automáticamente el estudiante logueado a la reserva.

        Parameters
        ----------
        serializer : Object
            Serializador para la reserva de una tutoría.
        """
        serializer.save(student=self.request.user)
