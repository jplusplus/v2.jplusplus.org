# -*- coding: utf-8 -*-
from __future__ import with_statement

from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template
from django.core.urlresolvers import NoReverseMatch
from menus.utils import DefaultLanguageChanger

register = template.Library()

class PageLanguageUrl(InclusionTag):
    """
    Displays the url of the current page in the defined language.
    You can set a language_changer function with the set_language_changer function in the utils.py if there is no page.
    This is needed if you have slugs in more than one language.
    """
    name = 'page_language_url'
    template = 'cms/content.html'

    options = Options(
        Argument('lang'),
    )

    def get_context(self, context, lang):
        try:
            # If there's an exception (500), default context_processors may not be called.
            request = context['request']
        except KeyError:
            return {'template': 'cms/content.html'}
        if hasattr(request, "_language_changer"):
            try:
                url = request._language_changer(lang)
            except NoReverseMatch:
                url = DefaultLanguageChanger(request)(lang)
        else:
            # use the default language changer
            try:
                url = DefaultLanguageChanger(request)(lang)
            except:
                url = None
        return {'content': url}

register.tag(PageLanguageUrl)
