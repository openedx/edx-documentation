.. _Conditional Module:

####################
Conditional Module
####################

.. note:: EdX offers provisional support for this problem type.

A conditional module controls the content that learners see after a response
that they make meets a certain condition. For example, learners who answer
"Yes" to a poll question see a different block of text from the learners who
answered "No" to the same question.

********************
Format description
********************

The main tag of conditional module input is ``conditional``.

.. code-block:: xml

    <conditional> ... </conditional>

``conditional`` can include any number of any Xmodule tags (``html``,
``video``, ``poll``, etc.) or ``show`` tags.

====================
``conditional`` Tag
====================

The main container for a single instance of a conditional module. The
following attributes can be specified for this tag.

.. code-block:: xml

    sources - location id of required modules, separated by ';'
    [message | ""] - message for case, where one or more are not passed. Here you can use variable {link}, which generate link to required module.

    [submitted] - map to `is_submitted` module method.
    (pressing RESET button makes this function to return False.)

    [correct] - map to `is_correct` module method
    [attempted] - map to `is_attempted` module method
    [poll_answer] - map to `poll_answer` module attribute
    [voted] - map to `voted` module attribute

============
``show`` Tag
============

Symlink to some set of Xmodules. The following attribute can be specified for
this tag.

.. code-block:: xml

    sources - location id of modules, separated by ';'

*********
Examples
*********

========================================
Example: conditional depends on poll
========================================

.. code-block:: xml

    <conditional sources="i4x://MITx/0.000x/poll_question/first_real_poll_seq_with_reset" poll_answer="man"
    message="{link} must be answered for this to become visible.">
        <html>
            <h3>You see this because your vote value for "First question" was "man"</h3>
        </html>
    </conditional>

========================================================
Example: conditional depends on poll (use <show> tag)
========================================================

.. code-block:: xml

    <conditional sources="i4x://MITx/0.000x/poll_question/first_real_poll_seq_with_reset" poll_answer="man"
    message="{link} must be answered for this to become visible.">
        <html>
            <show sources="i4x://MITx/0.000x/problem/test_1; i4x://MITx/0.000x/Video/Avi_resources; i4x://MITx/0.000x/problem/test_1"/>
        </html>
    </conditional>

================================================
Examples of conditional depends on problem
================================================

.. code-block:: xml

    <conditional sources="i4x://MITx/0.000x/problem/Conditional:lec27_Q1" attempted="True">
        <html display_name="HTML for attempted problem">You see this because "lec27_Q1" was attempted.</html>
    </conditional>
    <conditional sources="i4x://MITx/0.000x/problem/Conditional:lec27_Q1" attempted="False">
        <html display_name="HTML for not attempted problem">You see this because "lec27_Q1" was not attempted.</html>
    </conditional>
