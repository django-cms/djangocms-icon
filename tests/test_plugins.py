# -*- coding: utf-8 -*-
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

        # from html5print import HTMLBeautifier
        # print(HTMLBeautifier.beautify(response.content, 2))

        self.assertContains(response, '<i class="fa-icon" aria-hidden="true"></i>')
