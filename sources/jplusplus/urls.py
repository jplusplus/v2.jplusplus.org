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
# Last mod : 23-Apr-2014
# -----------------------------------------------------------------------------
from django.conf.urls import url, include
from rest_framework import routers
import api

router = routers.DefaultRouter()
router.register(r'projects', api.ProjectViewSet)
router.register(r'offices', api.OfficeViewSet)

urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
    # url(r'^projects/$'                                   , 'jplusplus.views.projects'       , name='jplusplus_projects'),
    url(r'^project/(?P<slug>[\w-]+)/$'                   , 'jplusplus.views.project_details', name='jplusplus_project_details'),
    # url(r'^(?P<office>[\w-]+)/projects/$'                , 'jplusplus.views.projects'       , name='jplusplus_projects'),
    # url(r'^(?P<office>[\w-]+)/project/(?P<slug>[\w-]+)/$', 'jplusplus.views.project_details', name='jplusplus_project_details'),
    url(r'^redactor/', include('redactor.urls'))
]
# EOF
