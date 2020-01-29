=========
Changelog
=========


1.5.0 (unreleased)
==================

* Added support for Django 3.0


1.4.2 (2019-11-05)
==================

* Added further tests to raise coverage
* Fixed smaller issues found during testing
* Fixes an issue with older installations
* Fixes double save issue, where icon is lost


1.4.1 (2019-07-31)
==================

* Fixes an issue where the icon widget throws a Javascript error


1.4.0 (2019-05-22)
==================

* Added support for Django 2.2 and django CMS 3.7
* Removed support for Django 2.0
* Extended test matrix
* Fixes an issue when using multiple icons on different models #20


1.3.0 (2019-03-13)
==================

* Added support for Font Awesome 5
* Added support for custom data iconset
* Added isort and adapted imports
* Fixed an issue where Font Awesome is not rendered on a clean install
* Extended test matrix
* Adapted code base to align with other supported addons


1.2.0 (2018-12-12)
==================

* Added documentation on how to configure web fonts, custom web fonts and
  custom SVG icons
* Updated icon picker library to latest version and include more icon sets
* Fixed test matrix
* Exclude ``tests`` folder from release build


1.1.0 (2018-11-20)
==================

* Added support for Django 1.11, 2.0 and 2.1
* Removed support for Django 1.8, 1.9, 1.10
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.5 and 3.6


1.0.0 (2018-02-13)
==================

* Proper release on Divio Marketplace
* Updated translations
* Removed newline from ``*icon.html``
* Fixed bugs in the icon widget


0.2.0 (2017-12-27)
==================

* Added separate icon include
* Removed change_form template in favour of include


0.1.0 (2017-12-22)
==================

* Initial release
