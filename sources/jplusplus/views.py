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
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from .models import Project

def projects(request, office=None):
	projects = Project.objects.all()
	if office:
		projects = projects.filter(offices__slug=office)
	context = {'projects':projects, 'office':office}
	return render_to_response("jplusplus/projects.html", context, RequestContext(request))

def project_details(request, slug, office=None):
	project = Project.objects.get(slug=slug)
	# TODO: raise 404 if office isn't related to the project. This is the law.
	context = {'project':project}
	return render_to_response("jplusplus/project_details.html", context, RequestContext(request))

# EOF
