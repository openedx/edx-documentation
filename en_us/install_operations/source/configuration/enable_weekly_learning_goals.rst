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

The feature adds a new Weekly Learning Goal widget to the course home page.

To use it, learners select a weekly learning goal and are automatically subscribed to goal reminder emails. The weekly reminders continue until the learner completes their course and/or their audit access ends. Learners can modify/cancel their goal and reminder settings at any time from the widget or via links in the email.

For more details on this feature or screenshots see this `blog post <https://openedx.atlassian.net/wiki/spaces/PROD/blog/2021/12/07/3266805795/Course+Goal+Setting>`_.


.. note:: This feature is only available on the new learning micro frontend. If that is not already enabled for you, you can view `instructions here <https://openedx.atlassian.net/wiki/spaces/COMM/pages/2023915819/Lilac>`_.


**********************
Enable the feature
**********************

The following waffle flags need to be enabled:

#. course_goals.number_of_days_goals

#. course_experience.enable_course_goals

To send goal reminder emails, you need to regularly run the following `management command <https://github.com/edx/edx-platform/blob/master/lms/djangoapps/course_goals/management/commands/goal_reminder_email.py#L101>`_.  

edx.org runs this command at the following cron schedule H \*/3 \* \* \*

.. note:: For the emails to work you will need to have at least one email channel configured within https://github.com/edx/edx-ace