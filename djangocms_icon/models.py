# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_attributes_field.fields import AttributesField

from .fields import Icon


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_ICON_TEMPLATES',
        [],
    )
    return choices


@python_2_unicode_compatible
class AbstractIcon(CMSPlugin):
    icon = Icon()

    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return self.label or ''


class Icon(AbstractIcon):
    class Meta:
        abstract = False
