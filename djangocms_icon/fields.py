# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.forms import fields, widgets
from django.utils.translation import ugettext


def get_iconsets():
    return getattr(settings, 'DJANGOCMS_ICON_SETS', (
        ('fontawesome', 'fa', 'Font Awesome'),
    ))


class IconFieldWidget(widgets.TextInput):
    class Media:
        css = {
            'all': (
                'djangocms_icon/css/djangocms-icon.css',
            )
        }
        js = (
            'djangocms_icon/js/dist/bundle.icon.min.js',
        )

    def render(self, name, value, attrs=None, **kwargs):
        input_html = super(IconFieldWidget, self).render(name, value, attrs=attrs, **kwargs)
        if value is None:
            value = ''
        iconset = value.split('-')[0] if value and '-' in value else ''
        iconsets = get_iconsets()
        iconset_prefixes = [s[1] for s in iconsets]
        if len(iconsets) and iconset not in iconset_prefixes:
            # invalid iconset! maybe because the iconset was removed from
            # the project. set it to the first in the list.
            iconset = iconsets[0][1]
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'admin/djangocms_icon/widgets/icon.html',
            {
                'input_html': input_html,
                'value': value,
                'name': name,
                'iconset': iconset,
                'is_required': self.is_required,
                'iconsets': iconsets,
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
