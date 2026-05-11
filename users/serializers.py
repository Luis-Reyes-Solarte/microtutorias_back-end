from collections import OrderedDict

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"write_only": True},
            "is_staff": {"write_only": True},
            "is_active": {"write_only": True},
            "date_joined": {"write_only": True},
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data.pop("password"))
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return OrderedDict(
            [
                (key, value)
                for key, value in ret.items()
                if value not in [None, "", [], {}]
            ]
        )
