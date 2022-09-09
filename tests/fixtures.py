from cms.api import create_page

try:
    import djangocms_versioning  # noqa

    DJANGO_CMS4 = True
except ImportError:
    DJANGO_CMS4 = False


class TestFixture:
    if DJANGO_CMS4:  # CMS V4

        def _get_version(self, grouper, version_state, language=None):
            language = language or self.language

            from djangocms_versioning.models import Version

            versions = Version.objects.filter_by_grouper(grouper).filter(
                state=version_state
            )
            for version in versions:
                if (
                    hasattr(version.content, "language")
                    and version.content.language == language
                ):
                    return version

        def publish(self, grouper, language=None):
            from djangocms_versioning.constants import DRAFT

            version = self._get_version(grouper, DRAFT, language)
            if version is not None:
                version.publish(self.superuser)

        def unpublish(self, grouper, language=None):
            from djangocms_versioning.constants import PUBLISHED

            version = self._get_version(grouper, PUBLISHED, language)
            if version is not None:
                version.unpublish(self.superuser)

        def create_page(self, title, **kwargs):
            kwargs.setdefault("language", self.language)
            kwargs.setdefault("created_by", self.superuser)
            kwargs.setdefault("in_navigation", True)
            kwargs.setdefault("limit_visibility_in_menu", None)
            kwargs.setdefault("menu_title", title)
            return create_page(
                title=title,
                **kwargs
            )

        def get_placeholders(self, page):
            return page.get_placeholders(self.language)

    else:  # CMS V3

        def publish(self, page, language=None):
            page.publish(language)

        def unpublish(self, page, language=None):
            page.unpublish(language)

        def create_page(self, title, **kwargs):
            kwargs.setdefault("language", self.language)
            kwargs.setdefault("menu_title", title)
            return create_page(
                title=title,
                **kwargs
            )

        def get_placeholders(self, page):
            return page.get_placeholders()
