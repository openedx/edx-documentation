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
     track. Is not sent if the learner receives a :ref:`course
     highlight message <Course Highlight Message>` on day 7.
 * - :ref:`Day 19 Upgrade Reminder`
   - Self-paced
   - 19 days after enrollment or 2 days before upgrade
     deadline
   - Reminder to upgrade if the learner hasn't enrolled in the verified track.
     Is not sent if the learner receives :ref:`course highlight messages
     <Course Highlight Message>`.
 * - :ref:`Course Highlight Message`
   - Instructor-paced and Self-paced
   - See :ref:`Course Highlight Message` for message send dates.
   - Message that lists 3-5 highlights for the next course "week", or section.
     Is not sent if the course team has not added highlights for the section
     in Studio. For more information, see :ref:`Set Section Highlights for
     Course Highlight Messages`.


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
 If learners receive a :ref:`course highlight message <Course Highlight
 Message>` on day 7, they do not receive this day 10 nudge message.

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
 If learners receive :ref:`course highlight messages <Course
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

.. _Course Highlight Message:

================================
Course Highlight Email
================================

EdX sends Course Highlight messages for both Instructor-paced and Self-paced
courses. The logic for when the message is sent depends on the Course pacing.

* Instructor-paced:

  * Highlights are sent every seven days after a learner enrolls in a course.

* Self-paced:

  * Highlights are sent based on the due dates calculated from the learner's enrollment date, the number of sections in the course, and the expected duration of the course (known as a Personalized Learner Schedule). Once the calculated due date for a section has passed, the highlights for the next section are sent out.
  * Example: Section 2 ends on December 3, 2020 for a specific learner based on their Schedule. Section 3 highlights will be sent out on December 4, 2020 for that learner.
  * **Note**: This could result in highlights being sent out every few days (3/4 days) in shorter expected duration courses with many sections or longer than a week (10+ days) in longer expected duration courses with few sections.

For more information, see :ref:`Set Section Highlights for Course Highlight
Messages`.

.. include:: ../../../shared/developing_course/course_highlight_message_text.rst


.. _Discussion Notification:

================================
Discussion Notification
================================

After a learner or course team member creates a post in the course discussions, edX sends the following email message the first time a learner or course team member replies to the original post.

::

  Subject: Response to <title of post>

  <edX username> replied to <title of post>:

  <text of comment>

The message also contains a View discussion option that takes the learner to the discussion post. EdX does not send individual messages for any additional replies on the post.
