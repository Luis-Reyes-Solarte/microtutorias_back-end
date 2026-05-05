from rest_framework import serializers

from .models import TutoringAd


class TutoringAdSerializer(serializers.ModelSerializer):
    tutor = serializers.StringRelatedField()

    class Meta:
        model = TutoringAd
        fields = "__all__"
