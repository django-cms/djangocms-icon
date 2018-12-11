===============
django CMS Icon
===============


|pypi| |build| |coverage|

**django CMS Icon** is a plugin for `django CMS <http://django-cms.org>`_
that allows you to insert an icon (font or svg) into your project.

This addon is compatible with `Divio Cloud <http://divio.com>`_ and is also available on the
`django CMS Marketplace <https://marketplace.django-cms.org/en/addons/browse/djangocms-icon/>`_
for easy installation.

.. image:: preview.gif


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

* Python 2.7, 3.4 or higher
* Django 1.11 or higher


Installation
------------

For a manual install:

* run ``pip install djangocms-icon``
* add ``djangocms_icon`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_icon``


Configuration
-------------

Web Font Icons
##############

The django CMS Icon plugin ships with **Font Awesome 4 as default**. This can
be changed by overriding the following setting::

    DJANGOCMS_ICON_SETS = [
        ('fontawesome', 'fa', 'Font Awesome'),
    ]

To use Font Awesome 5 in the above example; change the first parameter to
``fontawesome5``, the second and third stay unchanged. The second defines the
prefix of the icon class and the third the display name.

In addition **you need to load** the resources for your fonts in
``/admin/djangocms_icon/includes/assets.html``. Add this file to your project
in order for the icon picker to pick up your custom icons in the admin.

The icon picker supports `numerous font libraries <http://victor-valencia.github.io/bootstrap-iconpicker/>`_
out of the box. You can also add multiple font sets like this::

    DJANGOCMS_ICON_SETS = [
        ('fontawesome5', 'fa', 'Font Awesome'),
        ('materialdesign', 'zmdi', 'Material Design'),
    ]

Just don't forget to include both libraries in the ``assets.html`` file.
This is only necessary for the plugin rendering while selecting the icon.
You still need to implement the font libraries into your frontend stack.

Custom Web Font Icons
#####################

You can also add your own custom web fonts, for this you need to tell the
icon picker where to find the necessary files::

    DJANGOCMS_ICON_SETS = [
        (ICONSET, 'icon', 'Custom web font'),
    ]

In this example, we add our own font icon set on top of it. Please mind
that the second parameter needs to be the icon prefix. ``ICONSET`` is an
external reference to a JSON file at the root of your project setting up
your custom font icons, add this before::

    with open('iconset.json') as fh:
        ICONSET = fh.read()

Here an example of its content::

    {
        "iconClass": "icon",
        "icons": [
            "icon-icon1",
            "icon-icon2",
            "..."
        ]
    }

The ``iconClass`` refers to the second parameter in the settings file for the
icon prefix. Make sure both of them are the same. Instead of using an external
file you can also write the settings directly to the ``DJANGOCMS_ICON_SETS``
setting.

`djangocms-boilerplate-webpack <https://github.com/divio/djangocms-boilerplate-webpack/blob/master/tools/tasks/icons/json.js>`_
can generate the ``iconset.json`` automatically for you through ``gulp icons``.

Make sure the icons names contain the iconset prefix as shown in the example,
the widget will determine the iconset based on that. They can be omitted if only
one iconset is used.

Don't forget to also add your custom fonts to
``/admin/djangocms_icon/includes/assets.html`` into your project.

SVG Icons
#########

django CMS Icon also supports SVG icons. Follow the instructions from
`Custom Web Font Icons`_ and then adapt the JSON file a bit::

    {
        "svg": true,
        "spritePath": "sprites/icons.svg",
        "iconClass": "icon",
        "iconClassFix": "icon-",
        "icons": [
            "icon-icon1",
            "icon-icon2",
            "..."
        ]
    }

``svg`` and ``spritePath`` are the only required additional properties. You
may need to define ``iconClassFix`` depending on your SVG setup.


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
