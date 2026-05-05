from collections import OrderedDict

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_tutor", "is_student", "date_joined"]
        extra_kwargs = {"password": {"write_only": True}}

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return OrderedDict(
            [
                (key, value)
                for key, value in ret.items()
                if value not in [None, "", [], {}]
            ]
        )
