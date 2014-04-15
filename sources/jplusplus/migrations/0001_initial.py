# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WhatWeDoTranslation'
        db.create_table(u'jplusplus_whatwedo_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['jplusplus.WhatWeDo'])),
        ))
        db.send_create_signal(u'jplusplus', ['WhatWeDoTranslation'])

        # Adding unique constraint on 'WhatWeDoTranslation', fields ['language_code', 'master']
        db.create_unique(u'jplusplus_whatwedo_translation', ['language_code', 'master_id'])

        # Adding model 'WhatWeDo'
        db.create_table(u'jplusplus_whatwedo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'jplusplus', ['WhatWeDo'])


    def backwards(self, orm):
        # Removing unique constraint on 'WhatWeDoTranslation', fields ['language_code', 'master']
        db.delete_unique(u'jplusplus_whatwedo_translation', ['language_code', 'master_id'])

        # Deleting model 'WhatWeDoTranslation'
        db.delete_table(u'jplusplus_whatwedo_translation')

        # Deleting model 'WhatWeDo'
        db.delete_table(u'jplusplus_whatwedo')


    models = {
        u'jplusplus.whatwedo': {
            'Meta': {'object_name': 'WhatWeDo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'jplusplus.whatwedotranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'WhatWeDoTranslation', 'db_table': "u'jplusplus_whatwedo_translation'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['jplusplus.WhatWeDo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['jplusplus']