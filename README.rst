===============
django CMS Icon
===============


|pypi| |build| |coverage|

**django CMS Icon** is a plugin for `django CMS <http://django-cms.org>`_
that allows you to insert an icon (font or svg) into your project.

This addon is compatible with `Divio Cloud <http://divio.com>`_ and is also available on the
`django CMS Marketplace <https://marketplace.django-cms.org/en/addons/browse/djangocms-icon/>`_
for easy installation.

# .. image:: preview.gif


Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

One of the easiest contributions you can make is helping to translate this addon on
`Transifex <https://www.transifex.com/projects/p/djangocms-icon/>`_.


Documentation
=============

See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-icon/blob/master/setup.py>`_
file for additional dependencies:

* Python 2.7, 3.3 or higher
* Django 1.8 or higher


Installation
------------

For a manual install:

* run ``pip install djangocms-icon``
* add ``djangocms_icon`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_icon``


Configuration
-------------

Note that the provided templates are very minimal by design. You are encouraged
to adapt and override them to your project's requirements.


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python setup.py test


.. |pypi| image:: https://badge.fury.io/py/djangocms-icon.svg
    :target: http://badge.fury.io/py/djangocms-icon
.. |build| image:: https://travis-ci.org/divio/djangocms-icon.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-icon
.. |coverage| image:: https://codecov.io/gh/divio/djangocms-icon/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divio/djangocms-icon
