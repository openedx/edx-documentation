.. _Preventing XSS in Django Templates:

Preventing XSS in Django Templates
==================================

Django Templates are safe-by-default, which means that expressions are HTML-escaped by default.  However, there are cases where expressions are not properly escaped by default:

1. If your template includes JavaScript, then any expression inside the JavaScript should be JavaScript-escaped and not HTML-escaped. See :ref:`JavaScript Context in Mako` for some help on this topic, although it was written for Mako Templates.

2. We would like to HTML-escape translations, but Django Templates assumes translations are safe and thus they are not HTML-escaped. See below for details on how to properly escape translations in Django Templates.

XSS is a security concern.  To learn more about XSS in general, what it is, and why we want to prevent it, see \ `Best Practices for Preventing XSS <preventing_xss_overview.rst>`__.

.. note:: Do not use the `"striptags" filter <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#striptags>`__, which only makes an attempt at stripping HTML.  Instead, use the bleach library.

HTML-escaping Translations in Django Templates
----------------------------------------------

In Django templates, strings wrapped in ``trans`` and ``blocktrans`` are not automatically escaped, which leads to a vulnerability where translators could include malicious script tags in their translations.

HTML-escaping Simple Translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For most cases simply wrapping the ``trans`` or ``blocktrans`` in a ``force_escape`` filter is sufficient.

Trans Example: 
^^^^^^^^^^^^^^^

Approach 1:

.. code::

    {% trans "somestring" as tmsg %}{{ tmsg | force_escape }}

Blocktrans Example:
^^^^^^^^^^^^^^^^^^^

.. code::

    {% filter force_escape %}
        {# Translators: Some note here. #}
        {% blocktrans trimmed with organization_name=program_details.organizations.0.display_name platform_name=site.siteconfiguration.platform_name %}
        a program offered by {{ organization_name }}, in collaboration with {{ platform_name }}
        {% endblocktrans %}
    {% endfilter %}

Note: translator notes must be in the line immediately preceding the translated string, so the force_escape filter should be declared around the translator's note as well.

There also exists a **deprecated** custom filter named htmlescape in credentials that does the same thing as force_escape, only with hacky exceptions for some HTML.  Instead, please follow the examples documented in this page.

HTML Interpolation and HTML-escaping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases developers mix HTML into strings directly, typically for styling purposes. In these cases simply force escaping the entire translated string is not an option, since it will escape the HTML that is 'safe' and developer written. 

To solve this in credentials and credentials-themes, a custom tag was created which allows for interpolating safe-HTML into a string. Below is the custom tag and an example of its usage.

Custom Interpolation Tag Example:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    {% blocktrans trimmed asvar msg %}
    some text {start_anchor} anchor text for to display {end_anchor}.
    {% endblocktrans %}
    {% interpolate_html msg start_anchor='<ahref="'|add:site.siteconfiguration.certificate_help_url|add:'">'|safe end_anchor='</a>'|safe %}

See an `example of this custom tag <https://github.com/openedx/credentials/blob/57d02cb5d5bde7fce4f4862fd03cd42879e6f123/credentials/templates/credentials/programs/base.html#L116-L120>`__ used in the credentials codebase.

The `interpolate_html tag <https://github.com/openedx/xss-utils/blob/f2333be958e1f2e0970cf92c9da5a707999f6aad/xss_utils/templatetags/django_markup.py#L11>`__ is now available in a shared library for use in all IDAs.
