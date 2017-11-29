# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.template.loader import select_template

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class IconPlugin(CMSPluginBase):
    model = models.Icon
    name = _('Icon')
    allow_children = True
    text_enabled = True

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_icon/{}/icon.html'.format(instance.template)


plugin_pool.register_plugin(IconPlugin)
