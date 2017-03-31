    ..  _edx_javascript_guidelines:

##########################
EdX JavaScript Style Guide
##########################

This section describes the requirements and conventions used to contribute
JavaScript programming to the edX platform. The majority of edX JavaScript code
is written as `ES5`_, but is starting to move to `ES2015`_.

.. contents::
 :local:
 :depth: 2

**********
Code Style
**********

EdX JavaScript style generally follows the `Airbnb JavaScript Style Guide`_,
with a few custom rules that can be seen in the `eslint-config-edx repository`_.
EdX recommends using ESLint for JavaScript linting, and provides configurations
for both ES2015 and ES5.

*******
Testing
*******

All JavaScript code should be tested using `Jasmine`_. In addition, there are a
number of Jasmine-based helper classes provided by the `edX UI Toolkit`_.

JavaScript tests are run with `Karma`_, along with `karma-coverage`_ to
provide code coverage reporting.

For more information about testing JavaScript, see the `description of
testing for the edx-platform repository`_.

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
.. _description of testing for the edx-platform repository: https://github.com/edx/edx-platform/blob/master/docs/en_us/internal/testing.rst
.. _edX UI Toolkit: http://ui-toolkit.edx.org/
.. _ES5: https://www.ecma-international.org/ecma-262/5.1/
.. _ES2015: http://www.ecma-international.org/ecma-262/6.0/
.. _eslint-config-edx repository: https://github.com/edx/eslint-config-edx
.. _Jasmine: http://jasmine.github.io/
.. _jasmine-jquery: https://github.com/velesin/jasmine-jquery
.. _JSDOC site: http://usejsdoc.org/
.. _Karma: https://karma-runner.github.io/
.. _karma-coverage: https://www.npmjs.com/package/karma-coverage
