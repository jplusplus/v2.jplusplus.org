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
# Last mod : 23-Apr-2014
# -----------------------------------------------------------------------------
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ProjectPluginModel, TitlePluginModel

class ProjectsPlugin(CMSPluginBase):
    model           = ProjectPluginModel
    name            = _("J++ Projects Mosaic")
    render_template = "jplusplus/partials/projects.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance' : instance,
        })
        return context

class ContactPlugin(CMSPluginBase):
    name            = _("J++ Contact")
    render_template = "jplusplus/partials/contact_form.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance' : instance,
        })
        return context

class TitlePlugin(CMSPluginBase):
    name            = _("J++ Titles")
    render_template = "jplusplus/partials/title.html"
    model           = TitlePluginModel

    def render(self, context, instance, placeholder):
        print instance.__dict__
        context.update({
            'title'    : instance.title,
            'instance' : instance,
        })
        return context

plugin_pool.register_plugin(ContactPlugin)
plugin_pool.register_plugin(ProjectsPlugin)
plugin_pool.register_plugin(TitlePlugin)

# EOF
