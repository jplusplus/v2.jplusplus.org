# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemTranslation'
        db.create_table(u'whatwedo_item_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['whatwedo.Item'])),
        ))
        db.send_create_signal(u'whatwedo', ['ItemTranslation'])

        # Adding unique constraint on 'ItemTranslation', fields ['language_code', 'master']
        db.create_unique(u'whatwedo_item_translation', ['language_code', 'master_id'])

        # Adding model 'Item'
        db.create_table(u'whatwedo_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'whatwedo', ['Item'])


    def backwards(self, orm):
        # Removing unique constraint on 'ItemTranslation', fields ['language_code', 'master']
        db.delete_unique(u'whatwedo_item_translation', ['language_code', 'master_id'])

        # Deleting model 'ItemTranslation'
        db.delete_table(u'whatwedo_item_translation')

        # Deleting model 'Item'
        db.delete_table(u'whatwedo_item')


    models = {
        u'whatwedo.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'whatwedo.itemtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ItemTranslation', 'db_table': "u'whatwedo_item_translation'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['whatwedo.Item']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['whatwedo']