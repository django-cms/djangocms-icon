# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.forms import fields, widgets
from django.template.loader import render_to_string
from django.utils.translation import ugettext


def get_iconsets():
    iconsets = getattr(settings, 'DJANGOCMS_ICON_SETS', (
        ('fontawesome5regular', 'far', 'Font Awesome 5 Regular', 'lastest'),
        ('fontawesome5solid', 'fas', 'Font Awesome 5 Solid', 'lastest'),
        ('fontawesome5brands', 'fab', 'Font Awesome 5 Brands', 'lastest'),
    ))

    current_iconsets = []
    for iconset in iconsets:
        if len(iconset) == 3:
            iconset = iconset + ('lastest',)
        current_iconsets.append(iconset)

    return tuple(current_iconsets)


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
        if value is None:
            value = ''

        iconsets = get_iconsets()
        active_iconset = iconsets[0]

        if value:
            segments = value.split(None, 1)
            value = segments[1]
            selected_iconset = None

            for iconset in iconsets:
                if iconset[1] == segments[0]:
                    selected_iconset = iconset
                    break

            active_iconset = active_iconset if selected_iconset is None else selected_iconset

        rendered = render_to_string(
            'admin/djangocms_icon/widgets/icon.html',
            {
                'value': value,
                'name': name,
                'iconset': active_iconset[0],
                'version': active_iconset[3],
                'prefix': active_iconset[1],
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
