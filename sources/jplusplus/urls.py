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
from django.conf.urls import url

urlpatterns = [
    url(r'^projects/$'                                   , 'jplusplus.views.projects'       , name='jplusplus_projects'),
    url(r'^project/(?P<slug>[\w-]+)/$'                   , 'jplusplus.views.project_details', name='jplusplus_project_details'),
    url(r'^(?P<office>[\w-]+)/projects/$'                , 'jplusplus.views.projects'       , name='jplusplus_projects'),
    url(r'^(?P<office>[\w-]+)/project/(?P<slug>[\w-]+)/$', 'jplusplus.views.project_details', name='jplusplus_project_details'),
]
# EOF
