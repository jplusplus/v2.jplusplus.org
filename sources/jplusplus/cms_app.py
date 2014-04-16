#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 16-Apr-2014
# Last mod : 16-Apr-2014
# -----------------------------------------------------------------------------
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class JppHook(CMSApp):
    name = _("J++ App")
    urls = ["jplusplus.urls"]

apphook_pool.register(JppHook)

# EOF
