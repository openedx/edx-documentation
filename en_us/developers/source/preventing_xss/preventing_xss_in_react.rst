.. _Preventing XSS in React:

Preventing XSS in React
=======================

React is safe-by-default, so there are fewer places where you need to be careful regarding XSS.  In general, JSX knows what is HTML and what is not, and properly HTML-escapes whatever is not meant to be markup.

The two places where you need to be more careful, include:

1. Using the aptly named \ `dangerouslySetInnerHTML <https://reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml>`__ function.

2. Handling i18n and translations.

i18n and Translations
---------------------

If you use the library react-intl, it provides several components for handling messages; some are safe and some are not.

Use FormattedMessage
~~~~~~~~~~~~~~~~~~~~

Use FormattedMessage for safe translations.  The messages and translated messages will all be properly HTML-escaped.  It will also properly handle HTML-escaping with interpolated variables.  The code gets a little messy with interpolated variables, and if the interpolations have their own translated message, it may be difficult on translators, but it is workable.

.. code::

    <FormattedMessage
      id="test.hello"
      defaultMessage="Hello {name}, please go visit {link}"
      values={{
        name: <strong>Ben</strong>,
        link:(
          <Hyperlink destination="/visit-me"
            content={
              <FormattedMessage
                id="test.hello.link"
                defaultMessage="this link"
              />
            }
          />
        ),
      }}
    />

Don't Use FormattedHTMLMessage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FormattedHTMLMessage uses dangerouslySetInnerHTML behind the scenes.  It is meant to work with legacy strings that are safe and contain HTML, but it is never safe.  Even if the default message is safe, we can't ensure that a translator doesn't input some unsafe text in the translation.

.. code::

    // do NOT use this!
    <FormattedHTMLMessage
      id="test.evil"
      defaultMessage={ `<img src='x' onError="alert('Bad bad!')" />` }
    />

Alternative Message Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you run into a use case that cannot be resolved via FormattedMessage, you can explore some of the following:

-  https://www.npmjs.com/package/react-intl-formatted-xml-message

-  Related Threads: 

   -  https://github.com/yahoo/react-intl/issues/68#issuecomment-276702602

   -  https://github.com/yahoo/react-intl/issues/513

   -  Note: These were mentioned in the react-intl-formatted-xml-message README.

-  Markdown (react-remarkable)

   -  See \ https://github.com/yahoo/react-intl/issues/513#issuecomment-252083860
