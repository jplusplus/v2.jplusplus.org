#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 15-Apr-2014
# Last mod : 15-Apr-2014
# -----------------------------------------------------------------------------
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library
import json
import datetime

register = Library()

class JsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.date):
            # return int(mktime(obj.timetuple()))
            return (obj.year, obj.month, obj.day)
        return json.JSONEncoder.default(self, obj)

def jsonify(object):
    if isinstance(object, QuerySet):
        if len(object) > 0 and hasattr(object[0], "_translated_field_names"):
            results = []
            for obj in object:
                fields = [field for field in obj._translated_field_names if not field in ["language_code", "id", "master"]]
                obj_dict = obj.__dict__
                for field in fields:
                    obj_dict[field] = obj.safe_translation_getter(field)
                obj_dict.pop("_translated_field_names_cache", None)
                obj_dict.pop("_state", None)
                obj_dict.pop("translations_cache", None)
                results.append(obj_dict)
            return json.dumps(results, cls = JsonEncoder)
        return serialize('json', object)
    return simplejson.dumps(object)

register.filter('jsonify', jsonify)

# EOF
