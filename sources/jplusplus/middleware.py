#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 04-May-2014
# Last mod : 04-May-2014
# -----------------------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.contrib.sites.models import get_current_site
from cms.models import Page
from django.conf import settings

class DomainNamesMiddleware(object):

    def __init__(self):
        self.from_sites = settings.SITES.keys()

    def process_request(self, request):
        host = request.META.get('HTTP_HOST')
        if host in self.from_sites:
            site = get_current_site(request)
            page = Page.objects.filter(reverse_id=settings.SITES[host])[0]
            return HttpResponseRedirect("http://%s/%s" % (site.domain, page.get_path()))
        return None

# EOF
