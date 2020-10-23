.. _Automatic Email:

###################################################
Automatic Email Messages from the Open edX Platform
###################################################

.. Currently (5 January 2018), edx.org sends several different automatic
.. messages to learners. Those messages are listed in the partner version of
.. this topic. Open edX only sends discussion notifications. This topic was
.. created to mirror the partner topic and to provide a place to add any
.. additional messages that become available on Open edX.

.. Any update to this information should also be made to the
.. manage_live_course/automatic_email.rst file in the partner course authors
.. guide.


To help learners become and remain engaged in a course, the Open edX platform
can send automatic email messages that notify learners of responses to
discussion posts.

.. note::
  Before the system can send automatic email messages for any courses, a system
  administrator must enable automatic messages on the instance of the Open edX
  platform. For more information, see :ref:`installation:Enable Discussion
  Notifications`.

*****************************
Automatic Email Message Text
*****************************

After a learner or course team member creates a post in the course discussions,
the platform sends the following email message the first time a learner or
course team member replies to the original post.

::

  Subject: Response to <title of post>

  <username> replied to <title of post>:

    <text of comment>

The message also contains a **View discussion** option that takes the learner
to the discussion post.

The platform does not send individual messages for any additional replies on
the post.  For more information,
see :ref:`openlearners:Receiving Discussion Notifications`.
