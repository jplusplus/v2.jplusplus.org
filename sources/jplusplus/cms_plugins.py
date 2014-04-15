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
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import WhatWeDo

class WhatWeDoPlugin(CMSPluginBase):
    name            = _("What we do")
    render_template = "whatwedo.html"

    def render(self, context, instance, placeholder):
        items = WhatWeDo.objects.all()
        context.update({
            'instance' : instance,
            'items'    : items,
        })
        return context 
 
plugin_pool.register_plugin(WhatWeDoPlugin)

# EOF
