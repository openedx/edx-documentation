.. _Preventing XSS in Django Templates:

Preventing XSS in Django Templates
==================================

Django Templates are safe-by-default, which means that expressions are HTML-escaped by default.  However, there are cases where expressions are not properly escaped by default:

1. If your template includes JavaScript, then any expression inside the
   JavaScript should be JavaScript-escaped and not HTML-escaped.  Where
   possible you should avoid inline JS in your HTML Templates and instead
   reference bundled JS files.

2. We would like to HTML-escape translations, but Django Templates assumes translations are safe and thus they are not HTML-escaped.  See below for details on how to properly escape translations in Django Templates.

.. note:: Do not use the `"striptags" filter <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#striptags>`__, which only makes an attempt at stripping HTML.  Instead, use the bleach library.

HTML-escaping Translations in Django Templates
----------------------------------------------

In Django templates, strings wrapped in ``trans`` and ``blocktrans`` are not automatically escaped, which leads to a vulnerability where translators could include malicious script tags in their translations.

For most cases simply wrapping the ``trans`` or ``blocktrans`` in a ``force_escape`` filter is sufficient.

.. code-block::
   :name: Basic example

    {% trans "somestring" as tmsg %}{{ tmsg | force_escape }}

.. code-block::
   :name: Block Translation Example

    {% filter force_escape %}
        {# Translators: Some note here. #}
        {% blocktrans trimmed with organization_name=program_details.organizations.0.display_name platform_name=site.siteconfiguration.platform_name %}
        a program offered by {{ organization_name }}, in collaboration with {{ platform_name }}
        {% endblocktrans %}
    {% endfilter %}

.. note:: Translator notes must be in the line immediately preceding the translated string, so the force_escape filter should be declared around the translator's note as well.
