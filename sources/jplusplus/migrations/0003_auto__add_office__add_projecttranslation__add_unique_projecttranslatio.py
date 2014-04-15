# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Office'
        db.create_table(u'jplusplus_office', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'jplusplus', ['Office'])

        # Adding model 'ProjectTranslation'
        db.create_table(u'jplusplus_project_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['jplusplus.Project'])),
        ))
        db.send_create_signal(u'jplusplus', ['ProjectTranslation'])

        # Adding unique constraint on 'ProjectTranslation', fields ['language_code', 'master']
        db.create_unique(u'jplusplus_project_translation', ['language_code', 'master_id'])

        # Adding model 'Project'
        db.create_table(u'jplusplus_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'jplusplus', ['Project'])

        # Adding M2M table for field offices on 'Project'
        m2m_table_name = db.shorten_name(u'jplusplus_project_offices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'jplusplus.project'], null=False)),
            ('office', models.ForeignKey(orm[u'jplusplus.office'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'office_id'])


        # Changing field 'WhatWeDoTranslation.description'
        db.alter_column(u'jplusplus_whatwedo_translation', 'description', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Removing unique constraint on 'ProjectTranslation', fields ['language_code', 'master']
        db.delete_unique(u'jplusplus_project_translation', ['language_code', 'master_id'])

        # Deleting model 'Office'
        db.delete_table(u'jplusplus_office')

        # Deleting model 'ProjectTranslation'
        db.delete_table(u'jplusplus_project_translation')

        # Deleting model 'Project'
        db.delete_table(u'jplusplus_project')

        # Removing M2M table for field offices on 'Project'
        db.delete_table(db.shorten_name(u'jplusplus_project_offices'))


        # Changing field 'WhatWeDoTranslation.description'
        db.alter_column(u'jplusplus_whatwedo_translation', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'jplusplus.office': {
            'Meta': {'object_name': 'Office'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jplusplus.project': {
            'Meta': {'object_name': 'Project'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'offices': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['jplusplus.Office']", 'symmetrical': 'False'})
        },
        u'jplusplus.projecttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ProjectTranslation', 'db_table': "u'jplusplus_project_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['jplusplus.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'jplusplus.whatwedo': {
            'Meta': {'ordering': "('order',)", 'object_name': 'WhatWeDo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'jplusplus.whatwedotranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'WhatWeDoTranslation', 'db_table': "u'jplusplus_whatwedo_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['jplusplus.WhatWeDo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['jplusplus']