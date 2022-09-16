..  _edx_sass_guidelines:

####################
EdX Sass Style Guide
####################

This section describes the requirements and conventions used to contribute
Sass stylesheets to the edX platform.

.. contents::
 :local:
 :depth: 2

.. highlight:: none

**********
Code Style
**********

In order to standardize and enforce Open edX's Sass coding style across
multiple codebases, edX uses `Stylelint`_ which is a widely adopted CSS linter
written in JavaScript. In particular, edX provides the `edX Stylelint Config`_
which is an npm package that defines the rule set to be used to validate Sass.

EdX generally adopts the standard Stylelint rule set:

* `CSS Rules`_
* `SCSS-Specific Rules`_

If you are interested in the exceptions, see the `edX Stylelint Config README`_.

*************
Use Variables
*************

It is strongly recommended to avoid hard-coding values such as colors and fonts.
Using hard-coded values makes it difficult to change the value in the future as
it may have been used in many stylesheets. Using variables also allows themes
to simply override the value in one place.

Before defining a new variable, see if you can reuse an existing one. If you
need to create a new one, be sure to use the ``!default`` flag. This allows
themes to provide a different value for this variable if they choose. See the
Sass documentation for `default flag`_ for more details.

For example, here is an example of a hard-coded style::

    .my-element {
      color: #0000ff;
    }

This should instead be written as::

    $my-custom-color: #0000ff !default;

    .my-element {
      color: $my-custom-color;
    }

.. _CSS Rules: https://github.com/stylelint/stylelint/blob/master/docs/user-guide/rules.md#possible-errors
.. _default flag: http://sass-lang.com/documentation/file.SASS_REFERENCE.html#Variable_Defaults___default
.. _edX Stylelint Config: https://github.com/edx-unsupported/stylelint-config-edx
.. _edX Stylelint Config README: https://github.com/edx-unsupported/stylelint-config-edx#sass-style-guide
.. _SCSS-Specific Rules: https://www.npmjs.com/package/stylelint-scss#list-of-rules
.. _Stylelint: https://stylelint.io/
