from rest_framework import serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Group


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField()
    name_group = serializers.CharField()
    url = serializers.CharField()
    def create(self, validated_data):
        g = Group.objects.create(**validated_data)
        return g

    def update(self, instance, validated_data):
        return
