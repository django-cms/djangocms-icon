from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangocmsIconConfig(AppConfig):
    name = 'djangocms_icon'
    verbose_name = _("django CMS Icon")
    default_auto_field = 'django.db.models.AutoField'
