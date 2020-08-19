import os
import warnings

from django.conf import settings

from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_icon.cms_plugins import IconPlugin


class IconPluginsTestCase(CMSTestCase):

    def setUp(self):
        self.language = "en"
        self.home = create_page(
            title="home",
            template="page.html",
            language=self.language,
        )
        self.home.publish(self.language)
        self.page = create_page(
            title="content",
            template="page.html",
            language=self.language,
        )
        self.page.publish(self.language)
        self.placeholder = self.page.placeholders.get(slot="content")
        self.superuser = self.get_superuser()

    def tearDown(self):
        self.page.delete()
        self.home.delete()
        self.superuser.delete()

    def test_icon_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=IconPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()  # should not raise an error
        self.assertEqual(plugin.plugin_type, "IconPlugin")

    def test_plugin_structure(self):
        request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=IconPlugin.__name__,
            language=self.language,
            icon="fa-icon",
        )
        self.page.publish(self.language)
        self.assertEqual(plugin.get_plugin_class_instance().name, "Icon")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertContains(response, '<i class="fa-icon" aria-hidden="true"></i>')

    def test_full_plugin_render(self):
        request_url = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type=IconPlugin.__name__,
            language=self.language,
        )
        data = {
            "icon": "fas fa-address-book",
            "template": "default"
        }

        with self.login_user_context(self.superuser), warnings.catch_warnings():
            # hide the "DontUsePageAttributeWarning" warning when using
            # `get_add_plugin_uri` to get cleaner test results
            warnings.simplefilter("ignore")
            response = self.client.get(request_url)
            submission = self.client.post(request_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<div class="djangocms-icon"')
        # plugin succeeded and the change page view is shown
        self.assertEquals(submission.status_code, 200)
        self.assertContains(submission, "Change a page")
        self.assertNotIn(b"Please correct the errors below.", submission.content)

    def test_custom_plugin_render(self):
        request_url = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type=IconPlugin.__name__,
            language=self.language,
        )

        settings.DJANGOCMS_ICON_SETS = [
            ('fontawesome4', 'fa', 'Font Awesome 4'),
        ]
        data = {
            "icon": "fa fa-address-book",
            "template": "default"
        }

        with self.login_user_context(self.superuser), warnings.catch_warnings():
            # hide the "DontUsePageAttributeWarning" warning when using
            # `get_add_plugin_uri` to get cleaner test results
            warnings.simplefilter("ignore")
            response = self.client.get(request_url)
            submission = self.client.post(request_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<div class="djangocms-icon"')
        # plugin succeeded and the change page view is shown
        self.assertEquals(submission.status_code, 200)
        self.assertContains(submission, "Change a page")
        self.assertNotIn(b"Please correct the errors below.", submission.content)

    def test_json_plugin_render(self):
        request_url = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type=IconPlugin.__name__,
            language=self.language,
        )
        iconset = os.path.join(
            os.path.dirname(__file__),
            'sample_web.json',
        )

        with open(iconset) as fh:
            ICONSET = fh.read()

        settings.DJANGOCMS_ICON_SETS = [
            ('fontawesome4', 'fa', 'Font Awesome 4'),
            (ICONSET, 'custom_icon', 'Custom web font'),
        ]
        data = {
            "icon": "custom_icon icon-icon1",
            "template": "default"
        }

        with self.login_user_context(self.superuser), warnings.catch_warnings():
            # hide the "DontUsePageAttributeWarning" warning when using
            # `get_add_plugin_uri` to get cleaner test results
            warnings.simplefilter("ignore")
            response = self.client.get(request_url)
            submission = self.client.post(request_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Font Awesome 4')
        self.assertContains(response, 'Custom web font')
        self.assertContains(response, '<div class="djangocms-icon"')
        # plugin succeeded and the change page view is shown
        self.assertEquals(submission.status_code, 200)
        self.assertContains(submission, "Change a page")
        self.assertNotIn(b"Please correct the errors below.", submission.content)

    def test_svg_plugin_render(self):
        request_url = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type=IconPlugin.__name__,
            language=self.language,
        )
        iconset = os.path.join(
            os.path.dirname(__file__),
            'sample_svg.json',
        )

        with open(iconset) as fh:
            ICONSET = fh.read()

        settings.DJANGOCMS_ICON_SETS = [
            ('fontawesome4', 'fa', 'Font Awesome 4'),
            (ICONSET, 'svg_icon', 'Custom svg font'),
        ]
        data = {
            "icon": "svg_icon icon-icon2",
            "template": "default"
        }

        with self.login_user_context(self.superuser), warnings.catch_warnings():
            # hide the "DontUsePageAttributeWarning" warning when using
            # `get_add_plugin_uri` to get cleaner test results
            warnings.simplefilter("ignore")
            response = self.client.get(request_url)
            submission = self.client.post(request_url, data)

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Font Awesome 4')
        self.assertContains(response, 'Custom svg font')
        self.assertContains(response, '<div class="djangocms-icon"')
        # plugin succeeded and the change page view is shown
        self.assertEquals(submission.status_code, 200)
        self.assertContains(submission, "Change a page")
        self.assertNotIn(b"Please correct the errors below.", submission.content)
