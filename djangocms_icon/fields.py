# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import fields, widgets
from django.utils.translation import ugettext, ugettext_lazy as _

from .constants import DJANGOCMS_ICON_SETS


class IconFieldWidget(widgets.TextInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super(IconFieldWidget, self).render(name, value, attrs=attrs, **kwargs)
        if value is None:
            value = ''
        iconset = value.split('-')[0] if value and '-' in value else ''
        iconset_prefexes = [s[1] for s in DJANGOCMS_ICON_SETS]
        if len(DJANGOCMS_ICON_SETS) and iconset not in iconset_prefexes:
            # invalid iconset! maybe because the iconset was removed from
            # the project. set it to the first in the list.
            iconset = DJANGOCMS_ICON_SETS[0][1]
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'djangocms_bootstrap4/widgets/icon.html',
            {
                'input_html': input_html,
                'value': value,
                'name': name,
                'iconset': iconset,
                'is_required': self.is_required,
                'iconsets': DJANGOCMS_ICON_SETS,
            },
        )
        return rendered


class IconField(fields.CharField):
    widget = IconFieldWidget
    DEFAULT = ''

    def __init__(self, *args, **kwargs):
        if 'initial' not in kwargs:
            kwargs['initial'] = self.DEFAULT
        kwargs.pop('coerce', None)
        kwargs.pop('max_length', None)
        kwargs.pop('widget', None)
        kwargs['widget'] = self.widget
        super(IconField, self).__init__(*args, **kwargs)


class Icon(models.CharField):
    default_field_class = IconField
    south_field_class = 'models.fields.CharField'

    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = ugettext('Icon')
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        if 'default' not in kwargs:
            kwargs['default'] = self.default_field_class.DEFAULT
        super(Icon, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_field_class,
        }
        defaults.update(kwargs)
        return super(Icon, self).formfield(**defaults)
