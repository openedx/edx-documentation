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

The script does a number of checks before sending emails. There are five main conditions that must be met in order for an email to be sent, otherwise an email will not be sent:

1. The script will check the number of days left for a learner to successfully hit their goal compared to the learning goal selected by the learner (i.e. if the learner has chosen to learn once per week, three times per week, or five times per week)
2. If you're not actively enrolled in the course or your enrollment was this week
3. If an audit user's access expires this week, exclude them from the email since they may not be able to hit their goal anyway
4. If a user has a downloadable certificate, we will consider them as having completed the course and opt them out of receiving emails
5. We want to email users during the morning of their timezone

.. note:: For the emails to work you will need to have at least one email channel configured within https://github.com/openedx/edx-ace
