from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializador para la reserva de una tutoría.

    Parameters
    ----------
    serializers : Class
        Super clase de rest_framework.serializers.ModelSerializer que proporciona
        funcionalidades para serializar modelos de datos.

    Returns
    -------
    Object
        Serializador para la reserva de una tutoría.

    Raises
    ------
    serializers.ValidationError
        Si ya existe una reserva con estado "ACCEPTED" para la tutoría.
    """

    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        """
        Valida la reserva de una tutoría.
        Verifica si ya existe una reserva con
        estado "ACCEPTED" para la tutoría.

        Parameters
        ----------
        data : Object
            Datos de la reserva.

        Returns
        -------
        Object
            Serializador para la reserva de una tutoría.

        Raises
        ------
        serializers.ValidationError
            Si ya existe una reserva con estado "ACCEPTED" para la tutoría.
        """
        tutoring = data["tutoring"]

        if Booking.objects.filter(tutoring=tutoring, status="ACCEPTED").exists():
            raise serializers.ValidationError("Esta tutoría ya está ocupada")

        return data
