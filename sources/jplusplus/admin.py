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
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import Office, Project, Title, WhatWeDo, Trombinoscope
from adminsortable.admin import SortableAdminMixin

class OfficeAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        # for prepopulate fields
        # See : https://github.com/KristianOellegaard/django-hvad/issues/10#issuecomment-5572524
        super(OfficeAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}

    list_display = ("title", "slug")

class TitleAdmin(TranslatableAdmin):
    list_display = ("get_title", "anchor")

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')

class WhatWeDoAdmin(SortableAdminMixin, TranslatableAdmin):
    list_display = ("get_title",)

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')

class TombinoscopeAdmin(SortableAdminMixin, TranslatableAdmin):
    pass

class ProjectAdmin(SortableAdminMixin, TranslatableAdmin):
    def __init__(self, *args, **kwargs):
        # for prepopulate fields
        # See : https://github.com/KristianOellegaard/django-hvad/issues/10#issuecomment-5572524
        super(ProjectAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}

    list_display = ("get_title", "highlighted", "link", "order")
    list_filter  = ('offices__title', 'highlighted')

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')

admin.site.register(Office, OfficeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(WhatWeDo, WhatWeDoAdmin)
admin.site.register(Trombinoscope, TombinoscopeAdmin)

# EOF
