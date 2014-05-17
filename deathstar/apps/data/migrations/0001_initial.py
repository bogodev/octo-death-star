# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SensorData'
        db.create_table(u'data_sensordata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stamp', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('data_line', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'data', ['SensorData'])


    def backwards(self, orm):
        # Deleting model 'SensorData'
        db.delete_table(u'data_sensordata')


    models = {
        u'data.sensordata': {
            'Meta': {'object_name': 'SensorData'},
            'data_line': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stamp': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['data']