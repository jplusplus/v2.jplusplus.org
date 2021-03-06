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
# Last mod : 07-May-2014
# -----------------------------------------------------------------------------

from rest_framework import viewsets, serializers
from jplusplus.models import Project, Office
from cms.models import CMSPlugin
from rest_framework.exceptions import ParseError
from django.utils.translation import get_language

# -----------------------------------------------------------------------------
#
#    SERIALIZERS
#
# -----------------------------------------------------------------------------
class TagListSerializer(serializers.WritableField):
     
    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")     
        return data
     
    def to_native(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj

class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    description = serializers.CharField(source='description', read_only=True)
    title       = serializers.CharField(source='title', read_only=True)
    image       = serializers.ImageField(source='image', read_only=True)
    tags        = TagListSerializer(blank=True)
    url         = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model  = Project
        fields = ("slug", "tags", "url", "offices", "date", "image", "order", "highlighted", "link", "title", "description")

    def transform_image(self, obj, value):
        if obj.image:
            return obj.image.url_small
        else:
            return None

class OfficeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Office
        fields = ("slug", "title")

# -----------------------------------------------------------------------------
#
#    VIEWS
#
# -----------------------------------------------------------------------------
class OfficeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    ordering = ("order", "-date",)
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Project.objects.language(get_language()).all().order_by(*self.ordering)
        plugin_instance = self.request.QUERY_PARAMS.get('plugin_instance', None)
        if plugin_instance is not None:
            plugin_instance  = CMSPlugin.objects.get(pk=plugin_instance)
            plugin_instance  = plugin_instance.get_plugin_instance()[0]
            selected_offices = plugin_instance.offices.all()
            if selected_offices:
                queryset = queryset.filter(offices__in=selected_offices)
            if plugin_instance.highlighted:
                queryset = queryset.filter(highlighted=True)
        return queryset

# EOF
