# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_icon.models import Icon


class IconTestCase(TestCase):

    def setUp(self):
        Icon.objects.create(
            label='icon',
        )

    def test_icon_instance(self):
        """Icon instance has been created"""
        icon = Icon.objects.get(label='icon')
        self.assertEqual(icon.label, 'icon')
