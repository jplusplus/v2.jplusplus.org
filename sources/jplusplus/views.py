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
# Last mod : 04-May-2014
# -----------------------------------------------------------------------------
from django.template.context import RequestContext
from django.template import loader, Template, TemplateDoesNotExist
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from .models import Project
from django.http import HttpResponse
from django.core.mail import mail_admins
import json
from django.views.decorators.csrf import requires_csrf_token
from django import http
from django.core.validators import validate_email

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def projects(request, office=None):
	projects = Project.objects.all()
	if office:
		projects = projects.filter(offices__slug=office)
	context = {'projects':projects, 'office':office}
	return render_to_response("jplusplus/projects.html", context, RequestContext(request))

def project_details(request, slug, office=None):
	project = get_object_or_404(Project, slug=slug)
	# TODO: raise 404 if office isn't related to the project. This is the law.
	context = {'project':project}
	return render_to_response("jplusplus/project_details.html", context, RequestContext(request))

def contact(request):
	if request.method == 'POST':
		try:
			validate_email(request.POST["email"])
		except Exception:
			return HttpResponse(json.dumps({"status":"error", "message":unicode(_("Your email is required"))}), status=400)
		body = ""
		for key, value in request.POST.items():
			if key == "csrfmiddlewaretoken": continue
			body += "%s: %s\n" % (key.replace("-", " "), value)
		body += "ip: %s\n" % (get_client_ip(request))
		mail_admins('Contact Form', body, fail_silently=False)
		return HttpResponse(json.dumps({"status":"success"}))
	return HttpResponse(json.dumps({"status":"error", "message":unicode(_("post required"))}), status=400)

@requires_csrf_token
def server_error(request, template_name='500.html'):
	try:
		template = loader.get_template(template_name)
	except TemplateDoesNotExist:
		template = Template('<h1>Server Error (500)</h1>')
	return http.HttpResponseNotFound(template.render(RequestContext(request, {'request_path': request.path})))

# EOF
