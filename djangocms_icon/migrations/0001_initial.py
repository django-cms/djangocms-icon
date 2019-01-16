# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import djangocms_attributes_field.fields

import djangocms_icon.fields
from djangocms_icon.models import get_templates


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.CMSPlugin', related_name='djangocms_icon_icon', primary_key=True, serialize=False, parent_link=True, auto_created=True)),
                ('icon', djangocms_icon.fields.Icon(max_length=255, default='', verbose_name='Icon', blank=True)),
                ('template', models.CharField(max_length=255, default=get_templates()[0][0], verbose_name='Template', choices=get_templates())),
                ('label', models.CharField(max_length=255, verbose_name='Label', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
