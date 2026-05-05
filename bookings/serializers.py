from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        tutoring = data["tutoring"]

        if Booking.objects.filter(tutoring=tutoring, status="ACCEPTED").exists():
            raise serializers.ValidationError("Esta tutoría ya está ocupada")

        return data
