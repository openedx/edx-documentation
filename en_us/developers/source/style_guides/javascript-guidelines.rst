..  _edx_javascript_guidelines:

###############################
Open edX JavaScript Style Guide
###############################

This section describes the requirements and conventions used to contribute
JavaScript programming to the Open edX platform.

.. contents::
 :local:
 :depth: 2

******************
JavaScript Version
******************

Open edX JavaScript should be written consistent with the latest ECMA-262
specification in order to ensure future support, the largest community and the
availability of modern features. To support this syntax in older browsers, use
`Babel`_. Babel may also be configured to add syntax extensions widely adopted
by the community of our recommended framework (e.g., `JSX`_).

Note: Much of the existing Open edX front end code is written conformant to the version
of ECMA-262 released in 2009 (ES5). Files written in ES5 should be gradually
converted to the newer standard as new development in those feature areas
requires.

**********
Code Style
**********

In order to standardize and enforce Open edX's JavaScript coding style across
multiple codebases, Open edX has published an `ESLint`_ configuration that provides
an enforceable specification. Open edX JavaScript style generally follows the
`Airbnb JavaScript Style Guide`_, with a few custom rules. The
`edX ESLint Config`_ is made available as an npm package that can be installed
into any Open edX package.

Note: The `edX ESLint Config for ES5`_ may be used where ES5 is in use. Both
configs may be used in the same codebase through the use of
`ESLint glob configurations`_.

*******
Testing
*******

All JavaScript code should be tested using `Jasmine`_. In addition, there are a
number of Jasmine-based helper classes provided by the `edX UI Toolkit`_.

JavaScript tests are run with `Karma`_, along with `karma-coverage`_ to
provide code coverage reporting.

For more information about testing JavaScript, see the
`description of testing for the edx-platform repository`_.

*************
Documentation
*************

All JavaScript code should be documented using JSDoc. For detailed information
about using JSDoc, see the `JSDOC site`_.

As a tool, JSDoc takes JavaScript code with special ``/** */`` comments and
produces HTML documentation for it. An example follows.

.. code-block:: javascript

    /** @namespace */
    var util = {
        /**
         * Repeat <tt>str</tt> several times.
         *
         * @param {string} str The string to repeat.
         * @param {number} [times=1] How many times to repeat the string.
         * @returns {string}
         */
        repeat: function(str, times) {
            if (times === undefined || times < 1) {
                times = 1;
            }
            return new Array(times+1).join(str);
        }
    };

.. Link targets

.. _Airbnb JavaScript Style Guide: https://github.com/airbnb/javascript
.. _Babel: https://babeljs.io/
.. _description of testing for the edx-platform repository: https://github.com/openedx/edx-platform/blob/master/docs/en_us/internal/testing.rst
.. _edX ESLint Config: https://github.com/edx-unsupported/eslint-config-edx/tree/master/packages/eslint-config-edx
.. _edX ESLint Config for ES5: https://github.com/edx-unsupported/eslint-config-edx/tree/master/packages/eslint-config-edx-es5
.. _edX UI Toolkit: http://ui-toolkit.edx.org/
.. _ES5: https://www.ecma-international.org/ecma-262/5.1/
.. _ES2015: http://www.ecma-international.org/ecma-262/6.0/
.. _ESLint: https://eslint.org/
.. _ESLint glob configurations: https://eslint.org/docs/user-guide/configuring#configuration-based-on-glob-patterns
.. _Jasmine: http://jasmine.github.io/
.. _jasmine-jquery: https://github.com/velesin/jasmine-jquery
.. _JSDOC site: http://usejsdoc.org/
.. _JSX: https://facebook.github.io/react/docs/introducing-jsx.html
.. _Karma: https://karma-runner.github.io/
.. _karma-coverage: https://www.npmjs.com/package/karma-coverage
