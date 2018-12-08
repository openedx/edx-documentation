    ..  _edx_javascript_guidelines:

##########################
EdX JavaScript Style Guide
##########################

This section describes the requirements and conventions used to contribute
JavaScript programming to the edX platform.

.. contents::
 :local:
 :depth: 2

****************
Google Standards
****************

In general, edX JavaScript style follows the `Google JavaScript Style Guide`_.
In particular, the section `JavaScript Language Rules`_ includes useful advice.

EdX JavaScript style is defined by the linters for JavaScript code in each
repository. Following Google JavaScript style will bring your code close to the
standards set by edX linters.

**********
Code Style
**********

Use four spaces for indenting. An example follows.

.. code-block:: javascript

    function renderElements(state) {
        var youTubeId;

        if (state.videoType === 'html5') {
            state.videoPlayer.player = new HTML5Video.Player(state.el, {
                playerVars: state.videoPlayer.playerVars,
                videoSources: state.html5Sources,
                events: {
                    onReady: state.videoPlayer.onReady,
                    onStateChange: state.videoPlayer.onStateChange
                }
            });
        }
    }

****************
Linting
****************

EdX repositories include linters such as ESLint, JSHint, and JSCS that enforce
coding style according to the requirements of the repository and the history of
the code. The development team at edX is working to make the
JavaScript linters consistent across edX repositories, you must adhere to the
requirements of the linters for the repository that you are working in.

********************
RequireJS
********************

EdX uses RequireJS to help manage JavaScript dependencies and integrate our
pattern library more efficiently into our main platform, since it too uses
RequireJS. You should have some familiarity with using RequireJS so that your
scripts are not only included, but efficient.

For more information, see the `RequireJS site`_.

****************
Testing
****************

For information about testing JavaScript UI code, see the `description of
testing for the edx-platform repository`_.

****************
Documentation
****************

All JavaScript code should be documented using JSDoc. For detailed information
about using JSDoc, see the `JSDOC site`_.

As a tool, JSDoc takes JavaScript code with special ``/** */`` comments and
produces HTML documentation for it. An example follows.

.. code-block:: javascript

    /** @namespace */
    var util = {
        /**
         * Repeat <tt>str</tt> several times.
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

.. _JSDOC site: http://usejsdoc.org/

.. _description of testing for the edx-platform repository: https://github.com/edx/edx-platform/blob/master/docs/en_us/internal/testing.rst

.. _RequireJS site: http://requirejs.org/

.. _JavaScript Language Rules: https://google.github.io/styleguide/jsguide.html#language-features

.. _Google JavaScript Style Guide: https://google.github.io/styleguide/jsguide.html
