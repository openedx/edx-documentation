.. _Enabling the Weekly Learning Goals Feature:

##########################################
Enabling the Weekly Learning Goals Feature
##########################################

.. contents::
   :local:
   :depth: 1

***************
Overview
***************

The feature adds a new Weekly Learning Goal widget to the course home page. Goal setting and planning supports learner success.  It also supports learners’ time management efforts and accountability. By prompting learners to set their goals when beginning a course and subscribe to helpful reminder emails, we expect to increase engagement and completion rates.

To use it, learners use the Weekly Learning Goal widget from the course home page to select a weekly learning goal and are automatically subscribed to goal reminder emails. The weekly reminders continue until the learner completes their course and/or their audit access ends. Learners can modify/cancel their goal and reminder settings at any time from the widget or via links in the email.

The Weekly Learning Goals feature was discussed in this `Nutmeg blog post <https://openedx.org/blog/nutmeg-feature-round-up/>`_.

.. note:: This feature is only available on the new learning micro frontend. If that is not already enabled for you, you can view `instructions here <https://openedx.atlassian.net/wiki/spaces/COMM/pages/2023915819/Lilac>`_.


**********************
Enable the feature
**********************

The following waffle flag needs to be enabled:

   ``course_experience.enable_course_goals``

To send goal reminder emails, you need to regularly run the following `management command <https://github.com/openedx/edx-platform/blob/master/lms/djangoapps/course_goals/management/commands/goal_reminder_email.py#L101>`_.

edx.org runs this command at the following cron schedule H \*/3 \* \* \*

.. note:: For the emails to work you will need to have at least one email channel configured within https://github.com/openedx/edx-ace
