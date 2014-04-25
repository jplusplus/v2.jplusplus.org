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
# Last mod : 25-Apr-2014
# -----------------------------------------------------------------------------
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields
from cms.models.pluginmodel import CMSPlugin
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from cms.models import Page
from redactor.fields import RedactorField

class Office(models.Model):
    """
    Office Model
    """
    title     = models.CharField(_('title'), max_length=255)
    slug      = models.SlugField(_('slug'), help_text=_("should be the same that the office page"), unique=True)
    page_link = models.ForeignKey(Page, verbose_name=_("page"), blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.page_link.get_absolute_url()

class Project(TranslatableModel):
    """
    Project Model
    """
    translations = TranslatedFields(
        title       = models.CharField(_('title'), max_length=255),
        description = RedactorField(_('description'), blank=True, null=True),
        client      = models.CharField(_('client'), max_length=255, blank=True, null=True)
    )
    slug         = models.SlugField(unique=True)
    offices      = models.ManyToManyField(Office)
    date         = models.DateField(blank=True, null=True)
    image        = models.ImageField(_("image"), upload_to="projects", blank=True, null=True)
    order        = models.PositiveIntegerField(default=0, blank=False, null=False)
    highlighted  = models.BooleanField(_("highlighted"))
    link         = models.CharField(_('link'), max_length=255, blank=True, null=True)
    tags         = TaggableManager(blank=True)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jplusplus.views.project_details', args=[str(self.slug)])

class ProjectPluginModel(CMSPlugin):
    offices     = models.ManyToManyField(Office, verbose_name=_("filter by office"), blank=True, null=True)
    highlighted = models.BooleanField(_("show only highlighted projects"))

    def copy_relations(self, oldinstance):
        self.offices = oldinstance.offices.all()

class Title(TranslatableModel):
    """
    Title Model
    """
    translations = TranslatedFields(
        title = models.CharField(_('title'), help_text=_("to be translated"), max_length=255),
    )
    anchor = models.CharField(_('anchor'), help_text=_("don't translate"), max_length=255, unique=True)

    def __unicode__(self):
        return self.title

class TitlePluginModel(CMSPlugin):
    title     = models.ForeignKey(Title, verbose_name=_("title"))
    def __unicode__(self):
        try:
            return self.title.title
        except:
            return "TitlePluginModel"
# EOF
