# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Icon
from .forms import IconForm


class IconPlugin(CMSPluginBase):
    model = Icon
    form = IconForm
    name = _('Icon')
    allow_children = True
    text_enabled = True
    change_form_template = 'admin/djangocms_icon/change_form.html'

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_icon/{}/icon.html'.format(instance.template)


plugin_pool.register_plugin(IconPlugin)
