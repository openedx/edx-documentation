.. This is a placeholder for redirects to the new release notes site.
   See https://docs.openedx.org/en/latest/community/release_notes/index.html
.. _Enable Bulk Email:

################################
Enabling the Bulk Email Feature
################################

This section describes a change to the process for enabling or disabling the
bulk email feature. This change was released to the edx-platform repository on
24 May 2016. On that date, the bulk email feature was disabled on all Open edX
installations. To re-enable the bulk email feature, you must follow the new
procedure described in this section.

.. contents::
   :local:
   :depth: 1

**********************
About This Change
**********************

Prior to this change, you enabled or disabled the bulk email feature by making
manual updates to several files, including the ``lms/envs/common.py`` Python
file. The two relevant settings in the FEATURES section of this file were
``ENABLE_INSTRUCTOR_EMAIL`` and ``REQUIRE_COURSE_EMAIL_AUTH``.

.. important:: As of 21 May 2016, ``ENABLE_INSTRUCTOR_EMAIL: False`` is set for
  all Open edX sites that follow the edx-platform repository closely.

To simplify the process of changing the bulk email settings, a **Bulk_Email**
option is now available in the Django administration console.

*******************************
Changing the Bulk Email Setting
*******************************

To enable or disable the bulk email feature for an Open edX site, follow these
steps.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. In the **Bulk_Email** section, next to **Bulk email flags**, select **Add**.

#. To enable the bulk email feature, select the **Enabled** check box.

   To disable the bulk email feature, clear the **Enabled** check box.

#. If you previously set ``REQUIRE_COURSE_EMAIL_AUTH: True``, select the
   **Require course email auth** check box.

#. At the bottom of the page, select **Save**.

