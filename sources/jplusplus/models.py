#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 14-Apr-2014
# Last mod : 14-Apr-2014
# -----------------------------------------------------------------------------
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields
from cms.models.pluginmodel import CMSPlugin

class WhatWeDo(TranslatableModel):
    """
    What we Do Model
    """
    class Meta:
        verbose_name_plural = "What we do"
        ordering = ('order',)

    image = models.ImageField(_("image"), upload_to="whatwedo", blank=True, null=True)
    url   = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("If present image will be clickable."))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    translations = TranslatedFields(
        title       = models.CharField(_('title'), max_length=255),
        description = models.TextField(_('description')),
    )

    search_fields = ('description', 'title')

    def __unicode__(self):
        return self.title

class Office(models.Model):
    """
    Office Model
    """
    title = models.CharField(_('title'), max_length=255)

    def __unicode__(self):
        return self.title

class Project(TranslatableModel):
    """
    Project Model
    """
    class Meta:
        ordering = ('order',)

    offices      = models.ManyToManyField(Office)
    date         = models.DateField(blank=True, null=True)
    image        = models.ImageField(_("image"), upload_to="projects", blank=True, null=True)
    order        = models.PositiveIntegerField(default=0, blank=False, null=False)
    highlighted  = models.BooleanField(_("highlighted"))
    translations = TranslatedFields(
        title       = models.CharField(_('title'), max_length=255),
        description = models.TextField(_('description'), blank=True, null=True),
    )

    def __unicode__(self):
        return self.title

class ProjectPluginModel(CMSPlugin):
    offices = models.ManyToManyField(Office, verbose_name=_("filter by office"), blank=True, null=True)

# EOF
