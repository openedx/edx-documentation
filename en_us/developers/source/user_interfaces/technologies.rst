..  _ui_technologies:

######################
Front End Technologies
######################

The rapid pace of development in front end tooling has created opportunities
to greatly improve the quality of the Open edX user and developer experience.
After an assessment of industry best practices, the edX Front End Working Group
(FedX) has recommended the following technologies.

You can read more about the rationale behind these decisions in
`OEP-11: Front End Technology Standards`_. The Open edX wiki also has a
full list of `Open edX front end technologies`_.

.. _ui_django_templates:

************************************************************
Server-side content should be rendered with Django Templates
************************************************************

There are many template languages available for Django, but the simplest option
is to use the built-in `Django Templates`_. The Open edX codebase has a mixture
of Django and `Mako`_ templates, but the former are easier to reason about
because they don't support arbitrary code evaluation.

Note: Mako templates can continue to be used within edx-platform for consistency
with the existing code base. This is because the base templates and theming
support are all provided via Mako, so it is too much to expect a new feature to
be implemented with a different framework. There is much desire to replace Mako
within edx-platform so this exception may eventually be removed.

************************************************
JavaScript libraries should be installed via npm
************************************************

It is important that JavaScript libraries are kept up-to-date, and one key
component is to make it as simple as possible to perform upgrades. Projects that
use npm maintain all of their library requirements in a single `package.json`
file, which can be easily changed as the versions change.

**************************************************************
Use React and Redux when building new client-side applications
**************************************************************

`React`_ should be used for building new UIs, as it is widely adopted by the
community and strikes a balance between flexibility and feature richness. For
state management of complex client-side interactions, `Redux`_ should be used.
This library was chosen because it sees strong use in the React community, but
is also flexible enough to be used in situations where a hybrid React/Backbone
architecture exists.

Note: When building new applications within edx-platform, it is currently
acceptable to use `Backbone`_. Backbone is a somewhat old technology in the
JavaScript world and has seen a rapid drop off in usage within the community.
The plan is to incrementally adopt React within edx-platform as it can
interoperate cleanly with Backbone.

******************************************
JavaScript should be bundled using Webpack
******************************************

`Webpack`_ is the tool of choice for code optimization and bundling, as it is
widely used throughout the industry, and because it seamlessly handles modern
code bases as well as all of the older technologies used by edX, such as
`AMD Modules`_. Webpack should be implemented to handle as much of the asset
pipeline as possible, rather than passing this responsibility on to Django.

*************************************************************
JavaScript dependencies should be managed with ES2015 Modules
*************************************************************

JavaScript module systems allow front end code to specify its dependencies and
be grouped into bundles that minimize the assets needed to provide page
functionality. The most prevalent module syntax is currently `ES2015 Modules`_,
which should be adopted everywhere edX code is written to the ES2015 spec or
later.

Note: Much of edX's existing (ES5) JavaScript uses the older `AMD Modules`_
syntax for modules. AMD Modules are interoperable with ES2015 Modules if Webpack
is used for bundling, so AMD is an acceptable module definition if the code must
remain ES5.

**********************************
CSS should be generated using Sass
**********************************

Sass's SCSS syntax is an extension of CSS that adds power and elegance to the
basic language. It makes the maintenance of large CSS files more manageable
though the ability to use variables, mixins, imports and more. In particular, it
makes theming possible with the ability to override variables that define
colors, fonts etc.

You can find out more about Sass in the official `Sass documentation`_. For more
information about writing Sass for edX UIs, see :ref:`edx_sass_guidelines`.

*******************
Legacy Technologies
*******************

--------
Backbone
--------

`Backbone`_ was an early JavaScript framework that provided a formal
model/view/controller paradigm. It is used pervasively in the Open edX code
base, but in 2017 `React`_ was chosen as the recommended framework.

------------
CoffeeScript
------------

The Open edX codebase made heavy use of `CoffeeScript`_ for several years, but
its use at edX has now been officially deprecated. Most of the language benefits
of CoffeeScript were made available in JavaScript as of the ES2015 spec, and
CoffeeScript’s community has largely moved on.

For more information about writing JavaScript for edX applications, see
:ref:`edx_javascript_guidelines`.

-------------------
edX Pattern Library
-------------------

The `edX Pattern Library`_ is an initiative that was started in 2015 to
modernize the way that edX applications were built. At the time, Bootstrap was
considered to not be suitable for edX because applications always looked like
they were built with Bootstrap. In addition, Bootstrap’s rules were defined
using Less and so were not compatible with edX’s Sass-based styles. Finally, all
sizing was done using pixels which was not compatible with responsive
typography.

The pattern library project was somewhat successful, and a number of edX pages
were built using it. However, it became clear that there were not enough
resources available to build a comprehensive solution, and the non-standard
nature of the project meant that the community chose not to adopt it. It was at
this point that the decision was made to adopt `Bootstrap`_ instead.

For more on Bootstrap, see the chapter :ref:`ui_bootstrap`.

------
jQuery
------

`JQuery`_ is used pervasively in the Open edX code base, but in 2017 `React`_
was chosen as the recommended technology.

----
Mako
----

Mako Templates are used throughout edx-platform, but the recommendation is to
use Django Templates now. See :ref:`ui_django_templates` for more details.

----------
Underscore
----------

`Underscore`_ is a utility library that provides a large number of helper
functions that were not provided by early versions of JavaScript. The majority
of this functionality has been added to JavaScript in the `ES2015`_ standard,
so Underscore is no longer recommended.

.. Link destinations

.. _AMD Modules: https://github.com/amdjs/amdjs-api/wiki/AMD
.. _Backbone: http://backbonejs.org/
.. _Bootstrap: https://getbootstrap.com/
.. _CoffeeScript: http://coffeescript.org/
.. _Django Templates: https://docs.djangoproject.com/en/1.8/topics/templates/
.. _edX Front End Development: https://openedx.atlassian.net/wiki/display/FEDX/Front+End+Development
.. _edX UI Toolkit: http://ui-toolkit.edx.org/
.. _edX Website Accessibility Policy: https://www.edx.org/accessibility
.. _ES2015: http://www.ecma-international.org/ecma-262/6.0/
.. _ES2015 Modules: http://www.ecma-international.org/ecma-262/6.0/#sec-imports
.. _JQuery: https://jquery.com/
.. _LMS build file: https://github.com/edx/edx-platform/blob/master/lms/static/lms/js/build.js
.. _lms/envs/common.py: https://github.com/edx/edx-platform/blob/master/lms/envs/common.py#L1373
.. _lms/static/lms/js/require-config.js: https://github.com/edx/edx-platform/blob/master/lms/static/lms/js/require-config.js#L51>
.. _Mako: http://www.makotemplates.org/
.. _npmjs.com: https://www.npmjs.com/
.. _OEP-11\: Front End Technology Standards: https://open-edx-proposals.readthedocs.io/en/latest/oep-0011.html
.. _Open edX front end technologies: https://openedx.atlassian.net/wiki/spaces/FEDX/pages/159330534/Front+End+Technologies
.. _React: https://facebook.github.io/react/
.. _Redux: https://github.com/reactjs/redux
.. _Sass documentation: http://sass-lang.com/
.. _Underscore: http://underscorejs.org/
.. _Webpack: https://webpack.js.org/
