from django.conf import settings
from django.test import TestCase

from djangocms_icon.fields import get_iconsets


class IconFieldTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_iconsets(self):
        self.assertEqual(
            get_iconsets(),
            (
                ('fontawesome5regular', 'far', 'Font Awesome 5 Regular', 'lastest'),
                ('fontawesome5solid', 'fas', 'Font Awesome 5 Solid', 'lastest'),
                ('fontawesome5brands', 'fab', 'Font Awesome 5 Brands', 'lastest'),
            ),
        )
        settings.DJANGOCMS_ICON_SETS = []
        self.assertEqual(get_iconsets(), ())
        settings.DJANGOCMS_ICON_SETS = [('glyphicon', 'glyphicon', 'Glyphicons')]
        self.assertEqual(get_iconsets(), (('glyphicon', 'glyphicon', 'Glyphicons', 'lastest'),))
        # will append "lastest" for compatibility reasons
        settings.DJANGOCMS_ICON_SETS = [
            ('fontawesome5regular', 'far', 'Font Awesome 5 Regular'),
            ('fontawesome5solid', 'fas', 'Font Awesome 5 Solid'),
            ('fontawesome5brands', 'fab', 'Font Awesome 5 Brands'),
        ]
        self.assertEqual(
            get_iconsets(),
            (
                ('fontawesome5regular', 'far', 'Font Awesome 5 Regular', 'lastest'),
                ('fontawesome5solid', 'fas', 'Font Awesome 5 Solid', 'lastest'),
                ('fontawesome5brands', 'fab', 'Font Awesome 5 Brands', 'lastest'),
            ),
        )
