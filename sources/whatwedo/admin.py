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

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import Item

class ItemAdmin(TranslatableAdmin):
    pass

admin.site.register(Item, ItemAdmin)

# EOF
