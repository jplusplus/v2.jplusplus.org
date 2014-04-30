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
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ProjectPluginModel, TitlePluginModel, Office, WhatWeDo

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
        context.update({
            'title'    : instance.title,
            'instance' : instance,
        })
        return context

class MapPlugin(CMSPluginBase):
    name            = _("J++ Map")
    render_template = "jplusplus/partials/map.html"
    # model           = TitlePluginModel
    def render(self, context, instance, placeholder):
        offices = Office.objects.all().exclude(map_top=0, map_left=0)
        context.update({
            'instance' : instance,
            'offices'  : offices
        })
        return context

class WhatWeDoPlugin(CMSPluginBase):
    name            = _("J++ WhatWeDo")
    render_template = "jplusplus/partials/what_we_do.html"
    def render(self, context, instance, placeholder):
        what_we_do = WhatWeDo.objects.all()
        context.update({
            'instance'   : instance,
            'what_we_do' : what_we_do
        })
        return context

plugin_pool.register_plugin(ContactPlugin)
plugin_pool.register_plugin(ProjectsPlugin)
plugin_pool.register_plugin(TitlePlugin)
plugin_pool.register_plugin(MapPlugin)
plugin_pool.register_plugin(WhatWeDoPlugin)

# EOF
