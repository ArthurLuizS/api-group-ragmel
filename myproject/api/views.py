from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import GroupSerializer
from .models import Group
class GroupView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [AllowAny]

