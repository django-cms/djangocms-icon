# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO

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


class MigrationTestCase(TestCase):

    def test_makemigrations(self):
        """Fail if there are schema changes with no migrations."""
        app_name = 'djangocms_file'
        out = StringIO()
        call_command('makemigrations', dry_run=True, no_input=True, stdout=out)
        output = out.getvalue()
        self.assertNotIn(app_name, output, (
            '`makemigrations` thinks there are schema changes without'
            ' migrations.'
        ))
