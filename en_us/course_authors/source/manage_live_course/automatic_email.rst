.. _Automatic Email:

#################################
Automatic Email Messages from edX
#################################

.. Note: Any update to the **discussion notification** information should also
.. be made to the manage_live_course/automatic_email.rst file in the Open edX
.. course authors guide.

To help learners become and remain engaged in a course, edX sends several types
of automatic email messages.

.. list-table::
 :widths: 20 10 20 50
 :header-rows: 1

 * - Email Type
   - Course Pacing
   - Day Sent
   - Description
 * - :ref:`Day 3 Nudge Message`
   - Self-paced
   - 3 days after enrollment
   - Single message that welcomes and encourages the learner to return to the
     course. Includes an upsell message if the learner has not enrolled in the
     verified track.
 * - :ref:`Day 10 Nudge Message`
   - Self-paced
   - 10 days after enrollment
   - Single message that encourages the learner to return to the course.
     Includes an upsell message if the learner has not enrolled in the verified
     track. Is not sent if the learner receives a :ref:`weekly course
     highlight message <Weekly Course Highlight Message>` on day 7.
 * - :ref:`Day 19 Upgrade Reminder`
   - Self-paced
   - 19 days after enrollment or 2 days before upgrade
     deadline
   - Reminder to upgrade if the learner hasn't enrolled in the verified track.
     Is not sent if the learner receives :ref:`weekly course highlight messages
     <Weekly Course Highlight Message>`.
 * - :ref:`Weekly Course Highlight Message<Weekly Course Highlight Message>`
   - Self-paced
   - Every 7 days after enrollment
   - Weekly message that lists 3-5 highlights for the
     next course "week", or section. Is not sent if the course team has not
     added highlights for the section in Studio. For more information, see
     :ref:`Set Section Highlights for Weekly Course Highlight Messages`.
 * - :ref:`Discussion Notification`
   - Instructor-paced and self-paced
   - Unspecified
   - Notifications that a user has responded to a post on a :ref:`course
     discussion<Managing Discussions Index>`.

*****************************
Automatic Email Message Text
*****************************

The following example messages show the text of the email messages that edX
sends to learners automatically.

.. contents::
 :local:
 :depth: 1

.. _Day 3 Nudge Message:

===================
Day 3 Nudge Message
===================

EdX sends the following message three days after a learner enrolls in a course.
::

  Subject: Keep learning in Creating a Course with edX Studio!

  Remember when you enrolled in Creating a Course with edX Studio on edX.org?
  We do, and we’re glad to have you! Come see what everyone is learning.

EdX sends the following message three days after a learner enrolls in more than
one course.

::

  Subject: Keep learning on edX!

  Remember when you enrolled in Creating a Course with edX Studio and other
  courses on edX.org? We do, and we’re glad to have you! Come see what everyone
  is learning.

.. _Day 10 Nudge Message:

====================
Day 10 Nudge Message
====================

.. note::
 If learners receive a weekly course highlight message on day 7, they do not
 receive this day 10 nudge message.

EdX sends the following message 10 days after a learner enrolls in a course.

::

  Subject: Keep up the momentum!

  Many edX learners in Creating a Course with edX Studio are completing more
  problems every week, and participating in the discussion forums. What do you
  want to do to keep learning?

EdX sends the following message 10 days after a learner enrolls in more than
one course.

::

  Subject: Keep up the momentum!

  Many edX learners are completing more problems every week, and participating
  in the discussion forums. What do you want to do to keep learning?

.. _Day 19 Upgrade Reminder:

========================
Day 19 Upgrade Reminder
========================

.. note::
 If learners receive :ref:`weekly course highlight messages<Weekly Course
 Highlight Message>`, they do not receive this upgrade reminder.

EdX sends the following message 19 days after a learner enrolls in a course or
two days before the upgrade deadline for the course.

::

  Subject: Upgrade to earn a verified certificate in Creating a Course with edX
  Studio

  We hope you’re enjoying learning with us so far in Creating a Course with edX
  Studio! A verified certificate will allow to you highlight your new knowledge
  and skills. An edX certificate is official and easily shareable.

  Upgrade by November 25, 2017.

EdX sends the following message 19 days after a learner enrolls in more than
one course or two days before the upgrade deadline for one of the learner's
courses.

::

  Subject: Upgrade to earn a verified certificate on edX

  We hope you’re enjoying learning with us so far on edX! A verified
  certificate allows to you highlight your new knowledge and skills. An edX
  certificate is official and easily shareable.

  Upgrade by November 25, 2017.

.. _Weekly Course Highlight Message:

================================
Weekly Highlight Email
================================

EdX sends the following message every seven days after a learner enrolls in a
course. For more information, see :ref:`Set Section Highlights for Weekly
Course Highlight Messages`.

.. include:: ../../../shared/developing_course/course_highlight_message_text.rst

.. _Discussion Notification:

================================
Discussion Notification
================================

.. Note: Any update to the **discussion notification** information should also
.. be made to the manage_live_course/automatic_email.rst file in the Open edX
.. course authors guide.

After a learner or course team member creates a post in the course discussions,
edX sends the following email message the first time a learner or course team
member replies to the original post.

::

  Subject: Response to <title of post>

  <edX username> replied to <title of post>:

    <text of comment>

The message also contains a **View discussion** option that takes the learner
to the discussion post.

EdX does not send individual messages for any additional replies on the post.
However, the learner automatically receives a daily digest email message that
summarizes additional activity on the post. For more information, see
:ref:`learners:Receiving Discussion Notifications` and
:ref:`learners:Receiving Daily Digests`.
