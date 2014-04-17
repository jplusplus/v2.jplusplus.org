#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 17-Apr-2014
# Last mod : 17-Apr-2014
# -----------------------------------------------------------------------------

from rest_framework import viewsets, serializers
from jplusplus.models import Project, Office


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    description = serializers.CharField(source='description', read_only=True)
    title = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Project
        fields = ("slug", "offices", "date", "image", "order", "highlighted", "link", "title", "description")
    def transform_title(self, obj, value):
        return value
    def transform_description(self, obj, value):
        return value

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class OfficeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Office
        fields = ("slug", "title")

class OfficeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
# EOF
