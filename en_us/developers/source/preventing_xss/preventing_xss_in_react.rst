.. _Preventing XSS in React:

Preventing XSS in React
=======================

React is safe-by-default, so there are fewer places where you need to be careful regarding XSS. In general, JSX knows what is HTML and what is not, and properly HTML-escapes whatever is not meant to be markup.

The one place where you need to be careful is when using the aptly named `dangerouslySetInnerHTML`_.

.. Link targets

.. _dangerouslySetInnerHTML: https://react.dev/reference/react-dom/components/common#dangerously-setting-the-inner-html