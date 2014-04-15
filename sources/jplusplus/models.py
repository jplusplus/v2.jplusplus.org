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

class WhatWeDo(TranslatableModel):
    class Meta:
        verbose_name_plural = "What we do"

    translations = TranslatedFields(
        title       = models.CharField('title', max_length=255),
        description = models.CharField('description', max_length=255),
    )
    image       = models.ImageField(_("image"), upload_to="whatwedo", blank=True, null=True)
    url         = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("If present image will be clickable."))

    search_fields = ('description', 'title')

    def __unicode__(self):
        return self.title

# EOF
