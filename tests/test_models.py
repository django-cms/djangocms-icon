from django.conf import settings
from django.test import TestCase

from djangocms_icon.models import Icon, get_templates


class IconModelTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_settings(self):
        self.assertEqual(get_templates(), [("default", "Default")])
        settings.DJANGOCMS_ICON_TEMPLATES = [("feature", "Feature")]
        self.assertEqual(get_templates(), [("default", "Default"), ("feature", "Feature")])

    def test_icon_instance(self):
        Icon.objects.create(
            icon="fa-heart",
            template="default",
            label="some label",
            attributes="{'data-type', 'icon'}",
        )
        instance = Icon.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = Icon.objects.first()
        self.assertEqual(instance.icon, "fa-heart")
        self.assertEqual(instance.template, "default")
        self.assertEqual(instance.label, "some label")
        self.assertEqual(instance.attributes, "{'data-type', 'icon'}")
        # test strings
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "some label")
        instance.label = None
        self.assertEqual(instance.get_short_description(), "")
