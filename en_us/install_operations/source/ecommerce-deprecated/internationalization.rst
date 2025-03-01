Internationalization
====================

.. warning::
   This service is deprecated and was last tagged for the Redwood release. We are not fixing bugs or developing new features for it. For updates, `follow along on the DEPR ticket <https://github.com/openedx/public-engineering/issues/22>`_


Follow the `internationalization coding guidelines`_ in the edX Developer's Guide when developing new features.

Languages are enabled in the settings file, for example in ``ecommerce/settings/base.py``

.. code-block:: python

  LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('es-419', _('Spanish (Latin American)')),
  )

More details can be found in the `Django documentation for Languages`_.

.. _E-Commerce Language Negotiation:

E-Commerce Language Negotiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Language negotiation for E-Commerce is handled by `Django's Locale Middleware`_. Django's Language Negotiation rules, in
priority order, are as follows.

#. Language prefix is not enabled by default for the E-Commerce application.
#. LANGUAGE_SESSION_KEY is not used.
#. LANGUAGE_COOKIE_NAME is used to negotiate language. A user's language is set in their account settings in edx-platform which sets the language cookie. The language cookie name that is set for the E-Commerce language should be the same as the language cookie name set in the edx-platform repo. This can be configured in ``ecommerce/settings/base.py``.

    ..  code-block:: python

      LANGUAGE_COOKIE_NAME = 'openedx-language-preference'

#. The Accept-Language HTTP header is used.
#. LANGUAGE_CODE is used as the last resort. This can be set in ``ecommerce/settings/base.py``

.. _PayPal Language Negotiation:

PayPal Language Negotiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
To enable localization for PayPal, follow these steps.

#. Sign in to the LMS Django administration console for your base URL. For
   example, ``http://{your_URL}/admin``.

#. On the **Site Administration** page, locate **Waffle**.

#. In the **Waffle** section, next to **Switches**, select **Add**.

#. On the **Add switch** page, locate the **Name** field, and then add ``create_and_set_webprofile``.

#. On the **Add switch** page, select the **Active** checkbox.

#. Select **Save**.

A language code for E-Commerce will be taken from a cookie as described in `E-Commerce Language Negotiation`_. When the
language code is fetched from the cookie, only the base language is used. For example, ``es-419`` resolves to ``es``.
PayPal requires a country code. To get the country code, we use the language code to map it to a country. For example,
the language code ``es`` will map to the country code ``MX`` when it is sent to PayPal. To add your language for PayPal,
look up `PayPal's country to language mapping`_ and add it to PAYPAL_LOCALES in ``ecommerce/extensions/payment/constants.py``.

.. code-block:: python

    PAYPAL_LOCALES = {
        'zh': 'CN',
        'fr': 'FR',
        'en': 'US',
        'es': 'MX',
    }


If a language fetched from the cookie cannot be found in PAYPAL_LOCALES, the LANGUAGE_CODE is used. If the LANGUAGE_CODE does not exist in PAYPAL_LOCALES, PayPal will use its own language negotiation.

.. _internationalization coding guidelines: http://edx.readthedocs.io/projects/edx-developer-guide/en/latest/conventions/internationalization/i18n.html
.. _Django's Locale Middleware: https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#how-django-discovers-language-preference
.. _PayPal's country to language mapping: https://developer.paypal.com/docs/classic/api/locale_codes/
.. _Django documentation for Languages: https://docs.djangoproject.com/en/2.0/ref/settings/#languages


