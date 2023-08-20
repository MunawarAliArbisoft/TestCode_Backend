from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = Candidate
        fields = ["id", "first_name", "last_name", "is_staff", "email", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        candidate = Candidate(**validated_data)
        candidate.set_password(password)  # Hash the password
        candidate.save()
        return candidate

    def update(self, instance, validated_data):
        if password := validated_data.pop("password", None):
            instance.set_password(password)  # Hash the password
        return super().update(instance, validated_data)
