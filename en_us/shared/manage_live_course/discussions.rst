.. _Discussions:

##################################
Managing Course Discussions
##################################

Course discussions foster interaction among learners and between learners and
the course team. You can set up different topics to guide these interactions
when you create your course, and then run and moderate discussions throughout
the course to encourage participation and develop course community.
Discussions are also excellent sources of feedback and ideas for the future.

.. only:: Partners

 For information about participating in discussions, see the
 :ref:`learners:Course Discussions Index` section in the *EdX Learner's Guide*.
 Consider referring learners in your courses to that section, which describes
 the structure and features of edX course discussions, and provides useful
 information to help learners make the most of their participation in course
 discussions.

.. only:: Open_edX

 For information about participating in discussions, see the
 :ref:`openlearners:Course Discussions Index` section in the *Open edX
 Learner's Guide*. Consider referring learners in your courses to that section,
 which describes the structure and features of course discussions, and provides
 useful information to help learners make the most of their participation in
 course discussions.

For information about running and moderating discussions, see the following
sections.

.. contents::
 :local:
 :depth: 1

.. note:: Some features of discussions, especially moderation features, are
   not available when discussions are accessed in the edX mobile app. For
   information about the differences between discussions on the edx.org site
   and in the mobile app, see :ref:`Discussions on Mobile Apps`.

For information about how using cohorts in your course affects how your course
team might moderate course discussions, see :ref:`Moderating Discussions for
Cohorts`.

.. _Overview_discussions:

************
Overview
************

Learners and the course team use course discussions to share ideas, exchange
views, consider different viewpoints, and ask questions. In course discussions
there are three hierarchical levels of interaction.

* A post is the first level of interaction. A post opens a new subject. Posts
  can be made as questions, to solicit a concrete answer, or as discussions,
  to start a conversation. When participants add a post, they must choose an
  existing topic to associate it with, and decide whether to add it as a
  **Question** or as a **Discussion**.

* A response is the second level of interaction. A response is a reply made
  directly to a post to provide a solution or continue the conversation.

* A comment is the third level of interaction. A comment is often a
  clarification or side note made to a specific response, rather than to the
  post as a whole.

The dialog created by a post, its responses, and the comments on those
responses is sometimes called a thread. Discussion threads are saved as part
of the course history.

All course team members and enrolled learners can add posts, responses, and
comments, and they can also view posts, responses, and comments made by other
course participants. For information about cohorts and how members of cohorts
interact in course discussions, see :ref:`Coursewide Discussion Topics and
Cohorts` and see :ref:`Content Specific Discussion Topics and Cohorts`.

Members of the course community, learners as well as the course team, can be
given permission to moderate or administer course discussions through a set of
discussion administration roles.

.. note:: The course team members that you set up in Studio or in the LMS are
   not automatically granted discussion administration roles. Only people who
   have a discussion administration role can view all of the discussion
   contributions, for example in courses using cohorts.

   Discussion administration roles must be explicitly granted to members of
   the course team for them to moderate or administer course discussions. The
   course author, and any team members with the Admin role, can grant
   discussion administration roles. For information about assigning discussion
   privileges, see :ref:`Assigning_discussion_roles`.

.. note:: Not all options for moderating discussions are available when
   discussions are accessed using the edX mobile apps. For information about
   the differences between discussions on the edx.org site and in the mobile
   apps, see :ref:`Discussions on Mobile Apps`.

.. _Organizing_discussions:

*************************************************
Creating Discussion Topics for Your Course
*************************************************

Discussions in an edX course include both broad topics on course-wide areas of
interest such as "Feedback", "Troubleshooting", or "Technical Help", and the
content-specific topics that you add to course units as discussion components.
You create both types of discussion topics in Studio.

For more information about creating discussion topics, see :ref:`Create
CourseWide Discussion Topics` and :ref:`Create ContentSpecific Discussion
Topics`. For information about configuring discussion topics in courses that
use cohorts, see :ref:`Set up Discussions in Cohorted Courses`.

.. _Create CourseWide Discussion Topics:

=====================================
Create Course-Wide Discussion Topics
=====================================

All courses include a page named **Discussion**. When you create a course, a
course-wide discussion topic named "General" is already included by default.

You can add additional course-wide discussion topics to guide how learners
share and find information during your course. Such course-wide topics might
include Introduction and Announcements, Feedback, or Troubleshooting.
Discussions in these topics can begin as soon as your course is available.

.. note:: Make sure each discussion topic in your course has a unique name,
   whether it is a course-wide topic or a content-specific discussion topic
   that you add as a discussion component. If different discussion topics
   share the same name, learners might be confused as to which discussion
   topic they are participating in. For example, do not add a content-specific
   discussion topic named "General", because a course-wide discussion topic
   named "General" already exists in every course.

To create a course-wide discussion topic, follow these steps.

#. Open your course in Studio.

#. Select **Settings**, then **Advanced Settings**.

#. Scroll down to the **Discussion Topic Mapping** policy key. By default, its
   value looks like this.

   ::

     {
         "General": {
             "id": "course"
         }
     }

4. Copy the three lines provided for the General topic and paste
   them above the closing brace character (``}``).


   ::

     {
         "General": {
             "id": "course"
         }
         "General": {
             "id": "course"
         }
     }


5. Replace the second "General" with the quoted name of your new topic. For
   example, name the new topic "Questions about the Course".

   ::

     {
        "General": {
            "id": "course"
        }
        "Questions about the Course": {
             "id": "course"
        }
     }

6. Change the value for the second "id" to a unique identifier. For example,
   append a reference to the name of the topic.

   ::

     {
        "General": {
            "id": "course"
        }
        "Questions about the Course": {
             "id": "course_q"
        }
     }

   .. note:: In discussion topic IDs, you can use only alphanumeric characters
     and these special characters: underscore, hyphen, and period.

7. Add a comma after the first closing brace (``},``).

   ::

     {
        "General": {
            "id": "course"
        },
        "Questions about the Course": {
             "id": "course_q"
        }
     }

#. Select **Save Changes**.

   Studio checks the syntax of your entry and reformats your entry to add line
   feeds and indentation.

#. Scroll back to the **Discussion Topic Mapping** field to verify that your
   entry was saved as you expect. Entries that do not contain all of the
   required punctuation characters revert to the previous value when you save,
   and no warning is presented.

When learners select the **Discussion** page for your course, the drop-down
Discussion list now includes the topic you added.

 .. image:: ../../../shared/images/NewCategory_Discussion.png
  :width: 300
  :alt: A new topic named Course Q&A in the list of discussion topics.

.. note:: In courses that use cohorts, the course-wide discussion topics that
   you add are unified. All posts can be read and responded to by every
   learner, regardless of the cohort that they belong to. You can optionally
   configure these topics to be divided by cohort. For more information, see
   :ref:`Coursewide Discussion Topics and Cohorts`.

.. _Create ContentSpecific Discussion Topics:

============================================
Create Content-Specific Discussion Topics
============================================

To create a content-specific discussion topic, you add a discussion component
to a unit. Typically, you do this while you are designing and creating your
course in Studio. Follow the instructions in :ref:`Working with Discussion
Components`. The result is a discussion topic associated with a unit and its
content.

.. warning:: Follow the recommended steps to add discussion components. Do not
   create discussion topics by using the **Duplicate** button in Studio, and do
   not reference the same discussion ID in more than one place in your course.
   Duplicated discussion components result in discussion topics that contain the
   same conversations, even if learners post in different discussion topics.

For information about the visibility of content-specific discussion
topics, see :ref:`Visibility of Discussion Topics`.

.. note:: In courses with cohorts enabled, all content-specific discussion
   topics are divided by cohort when you first add them. Posts by learners to
   divided discussion topics can only be read and responded to by members of
   the same cohort and course team members who have a discussion administration
   role. You can change the configuration of content-specific discussion topics
   to make them unified and available to all learners in the course. For more
   information, see :ref:`Content Specific Discussion Topics and Cohorts`.


.. _Assigning_discussion_roles:

*************************************************
Assign Discussion Administration Roles
*************************************************

You can designate a team of people to help you run course discussions. Team
members who have a discussion administration role have additional options for
working with posts, responses, and comments.


.. important:: The course team members that you set up in Studio or in the LMS
   are not automatically granted discussion administration roles.

   Discussion administration roles must be explicitly granted to members of
   the course team for them to be able to moderate or administer course
   discussions. The course author and any team members who have the Admin role
   can grant discussion administration roles.

Different options for working with discussions are available through
the following roles.

.. note:: The options for moderating discussions described below are only
   available when members of the discussion administration team work in a web
   browser. The edX mobile apps do not currently offer moderation options.

   For more information about differences between discussions on the edx.org
   site and on the mobile apps, see :ref:`Discussions on Mobile Apps`.

* Discussion moderators can edit and delete messages at any level, review
  messages flagged for misuse, close and reopen posts, pin posts, and mark
  responses as correct answers.

  Posts, responses, and comments made by moderators are marked with a
  **Staff** identifier. The moderator role is often given to course team
  members who already have the Staff role.

.. removed this clause from 1st sentence per JAAkana and MHoeber: , and, if the
.. course is cohorted, see posts from all cohorts

* Discussion community teaching assistants (TAs) have the same options for
  working with discussions as moderators do.

  Posts, responses, and comments made by community TAs are marked with a
  **Community TA** identifier. The community TA role is often given to
  learners.

* Discussion admins have the same options for working with discussions as
  moderators, and their posts, responses, and comments have the same **Staff**
  identifiers.

  This role can be reserved for assignment to course team members
  who have the Admin role only: the discussion admins can then both
  moderate discussions and give other users discussion management roles
  whenever necessary.

Before you can assign roles to your discussion team, you need their email
addresses or usernames.

* To get this information for a course team member, in the LMS select
  **Instructor** to access the instructor dashboard. Select **Membership**, and
  then select either **Staff** or **Admin**.

* To get this information for an enrolled learner, in the LMS select
  **Instructor** to access the instructor dashboard. Select **Data Download**,
  and then **Download profile information as a CSV**.

====================================
Assign Roles
====================================

You can assign a course team role to any user who is already enrolled in your
course. To assign a discussion administration role, you must be the course
author or an Admin.

#. View the live version of the course.

#. Select **Instructor**, and then select **Membership**.

#. In the **Course Team Management** section, select **Discussion Admins**,
   **Discussion Moderators**, or **Discussion Community TAs**.

#. Under the list of users who currently have that role, enter an email address
   or username, and then select **Add** for the role type.


==============
Remove Roles
==============

To remove a role from a user, you must be the course author or an Admin.

#. View the live version of the course.

#. Select **Instructor**, and then select **Membership**.

#. In the **Course Team Management** section, select **Discussion Admins**,
   **Discussion Moderators**, or **Discussion Community TAs**.

#. From the list of users who currently have that role, select the user you
   want to remove, and then select **Revoke access**.


.. _Visibility of Discussion Topics:

**********************************
Visibility of Discussion Topics
**********************************

The names that you specify as the category and subcategory names for discussion
components are not visible on the **Discussion** page in the LMS until after
the course has started and the unit is released.

However, "seed" posts that you create in content-specific discussion topics
before a course starts, or before the unit is released, are immediately visible
on the **Discussion** page, even though the containing category or subcategory
names are not visible. EdX recommends that you do not create posts in
content-specific discussion topics before a unit is released. For more
information about release dates and the visibility of components, see
:ref:`Controlling Content Visibility`.

In contrast, :ref:`course-wide discussion topics<Create CourseWide Discussion
Topics>` that you create on the **Advanced Settings** page in Studio,
including the default "General" discussion topic, are immediately visible,
regardless of whether the course has started. They are not associated with any
particular section or subsection of the course, and are not subject to
release dates.


.. _Anonymous_posts:

************************************
Enabling Anonymous Discussion Posts
************************************

By default, when learners participate in a discussion, their usernames are
visible in the discussion. You can enable learners to make their discussion
posts anonymous, so that their usernames are not visible to other learners.
Their usernames will still be visible to course staff.

To enable anonymous discussion posts in your course, follow these steps.

#. In Studio, select **Settings**, then select **Advanced Settings**.

#. Locate the **Allow Anonymous Discussion Posts to Peers** field. The default
   value is ``false``.

#. Change the value of the setting to ``true``.

#. Select **Save Changes**.

Learners can now create discussion posts in your course that are anonymous
to other learners.

The **Advanced Settings** page in Studio also includes a field named **Allow
Anonymous Discussion Posts**. Setting the value of that field to ``true``
enables learners to create discussion posts that are anonymous to course
staff, as well as to other learners. As a best practice, edX recommends
that you do not set this field to ``true``.


.. _Running_discussions:

*********************
Run a Discussion
*********************

On an ongoing basis, the members of your discussion team run the course
discussion by making contributions, marking answers as correct, and guiding
learner messages into pertinent threads. Techniques that you can use
throughout your course to make discussions successful follow.

==========================================
Use Conventions in Discussion Subjects
==========================================

To identify certain types of messages and make them easier to find, you can
define a set of standard tags to include in the subject of a post or in the
body of a response or comment. Examples follow.

* Use "[OFFICIAL]" at the start of announcements about changes to the course.

* Provide information about corrected errors with a subject that begins
  "[CORRECTIONS]" or "[ERRORS]".

* Ask learners to use "[STAFF]" in the subject of each post that needs the
  attention of a course team member.

Both the discussion team and your learners can use tags like these to search
the discussions more effectively.

When a post is created its type must be selected: either "question" or
"discussion". Members of the discussion team should be thoughtful when
selecting the type for their posts, and encourage learners to do the same. For
more information, see :ref:`Find Question Posts and Discussion Posts`.

.. future: changing the type of a post, maybe resequence or separate  conventions from post types

========================
Seed Discussion Topics
========================

To help learners learn how to get the most out of course discussions, and find
the best discussion topic to use for their questions and conversations, you can
seed discussion topics in course-wide discussion topics before the course
starts.

Some examples follow.

* In the General topic (which is included in every course by default), add an
  [INTRO] post to initiate a thread for learner and course team introductions.

* For each course-wide discussion topic that you create, add an initial post
  to describe the way you intend that discussion to be used. In addition to
  providing guidance, these initial messages can act as models for learners to
  follow when they create their own posts.

EdX strongly recommends that you do not create seed posts in content-specific
discussion topics before the course starts or before the containing unit is
released. The category and subcategory names for content-specific discussion
topics are subject to the release visibility of their containing unit, and are
not visible until the unit is released. For more details, see :ref:`Visibility
of Discussion Topics`.


======================================
Minimize Thread Proliferation
======================================

To encourage longer, threaded discussions rather than many similar, separate
posts, the discussion team can use the following techniques. However, be aware
that long threads (with more than 200 responses and comments) can be difficult
to read, and can therefore result in an unsatisfactory experience in the
discussion.

.. note:: You can only pin or close posts and mark questions as answered when
   you work in a web browser. You cannot complete these activities when you
   work in the edX mobile app.

* Pin a post. Pinning a post makes it appear at the top of the list of posts in
  the discussion navigation pane on the **Discussion** page. As a result, it is
  more likely that learners will see and respond to pinned posts. You can write
  your own post and then pin it, or pin a post by any author. Select the "More"
  icon and then **Pin**.

  .. image:: ../../../shared/images/Discussion_Pin.png
   :alt: The pin icon for discussion posts.

* Mark a response as answered or endorsed. Depending on whether a post is a
  question or a discussion, you use the same option to mark a response either
  as the answer to the posted question, or to endorse a response. Marking a
  question as answered makes it easier for learners to find answers to already
  asked questions, rather than ask the same question again. Endorsing a
  response confirms that it adds value to a discussion.

  To mark a response as answered or endorsed, select the "check mark" icon.
  You cannot mark your own responses as answers or as endorsed.

  .. image:: ../../../shared/images/Discussion_MarkAsAnswer.png
   :alt: The "check mark" icon for marking a response as the correct answer
         to a question.

* Vote for posts or responses. Learners can sort discussions by posts with the
  most votes, so posts and responses with many votes are more likely to be
  read and responded to. Select the "plus" icon for the response. You cannot
  vote for your own posts.

  .. image:: ../../../shared/images/Discussion_vote.png
   :alt: The "plus" icon for voting for discussion posts.

* Close a post. You can respond to a redundant post by (optionally) pasting in
  a link to the post that you prefer learners to contribute to, and prevent
  further interaction by closing the post. Select the "More" icon and then
  **Close**.

* Provide post/response/comment guidelines. You can post information from the
  :ref:`overview<Overview_discussions>` in this section, or the :ref:`anatomy
  of edX discussions<Anatomy of edX Course Discussions>` in the next section,
  in a course-wide discussion topic (such as General) to provide guidance about
  when to start a new thread by adding a post, responding to an existing post,
  or commenting on a response.


.. _Moderating_discussions:

***********************
Moderate Discussions
***********************

The members of a course discussion team monitor discussions and keep them
productive. They can also collect information, such as areas of particular
confusion or interest, and relay it to the course team.

Developing and sustaining a positive discussion culture requires that
sufficient moderator time is dedicated to reviewing and responding to
discussions. Keeping up-to-date with a large MOOC forum requires a commitment
of 5 or more hours per week, and involves reading threads, replying to and
editing posts, and communicating with the rest of the discussion administration
team and other members of the course team.

For information on setting up moderators for your course, see
:ref:`Assigning_discussion_roles`.

====================================================
View Profile Information for Discussion Participants
====================================================

To find out more about a specific discussion participant, you can view that
learner's edX profile from their linked username on discussion posts.

To access a learner's profile from a discussion post that they contributed,
follow these steps.

#. On the **Discussion** page, select a username in a post, response, or
   comment.

#. On the discussion page for that learner, select the linked username.

   The learner's account profile page opens. Learners can have either a limited
   profile or a full profile.

For more information about profiles, see :ref:`openlearners:SFD Dashboard
Settings Profile`.

========================================
Provide Guidelines for Learners
========================================

You can develop a set of best practices for discussion participation and make
them available to learners as a course handout file or on a defined page in
your course. These guidelines can define your expectations and optionally
introduce features of edX discussions.

.. only:: Partners

 You can also refer learners to the :ref:`learners:Course Discussions Index`
 section in the *EdX Learner's Guide*. Consider referring learners in your
 courses to that section, which describes the structure and features of edX
 course discussions, and provides useful information to help learners make the
 most of their participation in course discussions.

.. only:: Open_edX

 You can also refer learners to the :ref:`openlearners:Course Discussions
 Index` section in the *Open EdX Learner's Guide*. Consider referring learners
 in your courses to that section, which describes the structure and features of
 edX course discussions, and provides useful information to help learners make
 the most of their participation in course discussions.

.. For a template that you can use to develop your own guidelines, see
.. :ref:`Discussion Forum Guidelines`.

.. _Develop a Positive Discussion Culture:

========================================
Develop a Positive Discussion Culture
========================================

Discussion monitors can cultivate qualities in their own discussion
interactions to make their influence positive and their time productive.

* Encourage quality contributions: thank learners whose posts have a positive
  impact and who answer questions.

* Check links, images, and videos in addition to the text of each message. Edit
  offensive or inappropriate posts quickly, and explain why.

* Review posts with a large number of votes and recognize "star posters"
  publicly and regularly.

* Stay on topic yourself: before responding to a post, be sure to read it
  completely.

* Maintain a positive attitude. Acknowledge problems and errors without
  assigning blame.

* Provide timely responses. More time needs to be scheduled for answering
  discussion questions when deadlines for homework, quizzes, and other
  milestones approach.

* Discourage redundancy: before responding to a post, search for similar posts.
  Make your response to the most pertinent or active post and then copy its URL
  and use it to respond to the redundant threads.

* Publicize issues raised in the discussions: add questions and their answers
  to an FAQ topic, or announce them on the **Home** page.

For a template that you can use to develop guidelines for your course
moderators, see :ref:`Guidance for Discussion Moderators`.

.. _Find Question Posts and Discussion Posts:

==========================================
Find Questions and Discussions
==========================================

When learners create posts, they specify the type of post to indicate whether
they are asking for concrete information (a question) or starting an open-ended
conversation (a discussion).

On the **Discussion** page, a question mark image identifies posts that ask
questions, and a conversation bubble image identifies posts that start
discussions. When an answer is provided and marked as correct for a question, a
check or tick mark image replaces the question mark image. For more
information, see :ref:`Answer Questions`.

The titles and icons of posts that you have not yet read appear in blue, with
a blue vertical bar on the post's left side. Posts that you have read have
dark gray titles and icons. When new responses and comments are made on posts
that you have read, a "new" indicator displays with the number of new
responses or comments that you have not yet read.

.. image:: ../../../shared/images/Discussion_ReadUnreadNew.png
  :width: 300
  :alt: The discussion navigation pane, showing some unread and some read
     posts, including a post that has been read but now has additional new
     responses or comments.

In addition to these visual cues, filters can help you find questions and
discussions that need review. In the discussion navigation pane on the
**Discussion** page, you can also select the following options from the **Show
all** drop-down menu.

* **Unread**, to list only the discussions and questions that you have not yet
  viewed.

* **Unanswered**, to list only questions that do not yet have any responses
  marked as answers.

* **Flagged**, to list only posts that learners have reported as inappropriate.


==================
Edit Messages
==================

Discussion moderators, community TAs, and discussion admins can edit the
content of posts, responses, and comments. Messages that include spoilers or
solutions, or that contain inappropriate or off-topic material, should be
edited quickly to remove text, images, or links.

.. removed note for open edx re edit behavior in mobile apps. Posts can
.. now be edited in the mobile apps (though ability depends on permissions)
.. CT April 25, 2016

#. Log in to the site and then select the course on your **Current Courses**
   dashboard.

#. Open the **Discussion** page and then open the post with the content that
   requires editing. You can select a single topic from the drop-down list of
   discussion topics, apply a filter, or search to locate the post.

#. For the post or for the response or comment that you want to edit, select
   the "More" icon and then **Edit**.

#. Remove the problematic portion of the message, or replace it with standard
   text such as "[REMOVED BY MODERATOR]".

#. Communicate the reason for your change. For example, "Posting a solution
   violates the honor code."

==================
Delete Messages
==================

Discussion moderators, community TAs, and discussion admins can delete the
content of posts, responses, and comments. Posts that include spam or abusive
language may need to be deleted, rather than edited.

.. removed note for open edx re deletion behavior in mobile apps. Posts can
.. now be deleted in the mobile apps (though ability depends on permissions)
.. CT April 25, 2016

#. Log in to the site and then select the course on your **Current Courses**
   dashboard.

#. Open the **Discussion** page and then open the post with the content that
   requires deletion. You can select a single topic from the drop-down list of
   discussion topics, apply a filter, or search to locate the post.

#. For the post or for the response or comment that you want to delete, select
   the "More" icon and then **Delete**.

#. Select **OK** to confirm the deletion.

.. how to communicate with the poster?

.. important:: If a message is threatening or indicates serious harmful
 intent, contact campus security at your institution. Report the incident
 before taking any other action.

==================================
Respond to Reports of Misuse
==================================

Learners have the option to report contributions that they find inappropriate.
Moderators, community TAs, and admins can check for messages that have been
flagged in this way and edit or delete them as needed.

.. removed note for open edx re flag behavior in mobile apps. Posts can
.. now be flagged in the mobile apps. CT April 25, 2016

#. View the live version of your course and select **Discussion** at the top of
   the page.

#. In the discussion navigation pane at the side of the page, use the filter
   drop-down list (set to **Show all** by default) to select **Flagged**.

#. Review listed posts. A post is listed if it or any of its responses or
   comments has been reported. The reported contribution includes a
   **Reported** identifier.

#. Edit or delete the post, response, or comment. Alternatively, remove the
   flag: select the "More" icon and then **Unreport**.

===============
Block Users
===============

For a learner who continues to misuse the course discussions, you can unenroll
the learner from the course. For more information, see :ref:`unenroll_student`.
If the enrollment period for the course is over, the learner cannot re-enroll.

.. _Close_discussions:

******************************
Close Discussions
******************************

You can close the discussions for your course so that learners cannot add
messages. Course discussions can be closed temporarily, such as during an exam
period, or permanently, such as when a course ends.

.. note:: You can only close discussions when you work in a web browser. You
   cannot close discussions when you work in an edX mobile app.

When you close the discussions for a course, all of the discussion topics in
course units and all of the course-wide topics are affected.

* Existing discussion contributions remain available for review.

* Learners cannot add posts, respond to posts, or comment on responses.
  However, learners can continue to vote on existing threads, follow threads,
  or report messages for misuse.

* Course team members with the Staff, Admin, Discussion Admins, Discussion
  Moderators, and Discussion Community TAs roles are not affected when you
  close the discussions for a course. Users with these roles can continue to
  add to discussions.

.. note:: To make sure your learners understand why they cannot add to
  discussions, you can add the dates that discussions are closed to the
  **Home** page and post them to a General discussion.

.. _Start-End Date Format Specification:

=====================================
Start-End Date Format Specification
=====================================

To close course discussions, you supply a start date and time and an end date
and time in Studio. You enter the values in the following format.

``["YYYY-MM-DDTHH:MM", "YYYY-MM-DDTHH:MM"]``

where:

* The dates and times that you enter are in Coordinated Universal Time (UTC),
  not in your local time zone. You might want to verify that you have specified
  the times that you intend by using a time zone converter such as `Time and
  Date Time Zone Converter`_.

* You enter an actual letter **T** between the numeric date and time values.

* The first date and time indicate when you want course discussions to close.

* The second date and time indicate when you want course discussions to reopen.

* If you do not want the discussions to reopen, enter a date that is far in the
  future.

* Quotation marks enclose each date-time value.

* A comma and a space separate the start date-time from the end date-time.

* Square brackets enclose the start-end value pair.

* You can supply more than one complete start and end value pair. A comma and a
  space separate each pair.

For example, to close course discussions temporarily for a final exam period in
July, you enter these start and end dates.

``["2016-07-22T08:00", "2016-07-25T18:00"]``

To add a blackout date that closes course discussions permanently on 9 August
2016, you add these start and end dates.

``["2016-07-22T08:00", "2016-07-25T18:00"], ["2016-08-09T00:00", "2099-08-09T00:00"]``

You enter these values between an additional pair of square brackets which are
supplied for you in Studio.

============================================
Define When Discussions Are Closed
============================================

To define when discussions are closed to new contributions and when they
reopen, follow these steps.

#. Open your course in Studio.

#. Select **Settings**, and then select **Advanced Settings**.

#. Locate the **Discussion Blackout Dates** field.

#. If the **Discussion Blackout Dates** field is empty, place your cursor
   between the brackets ``([ ])``.

   If the field already contains one or more blackout dates, place your cursor
   before the final bracket ``(])``.

#. Enter the start and end date for the time period during which you want
   discussions to be closed. Be sure to use the required :ref:`date format
   specification <Start-End Date Format Specification>`.

  * To define the temporary blackout period in the example above, the field
    contains start and end dates in the following format.

    ``[["2016-07-22T08:00", "2016-07-25T18:00"]]``

  * To add the dates that close the discussions permanently, the field contains
    a second pair of start and end dates in the following format.

    ``[["2016-07-22T08:00", "2016-07-25T18:00"], ["2016-08-09T00:00", "2099-08-09T00:00"]]``

#. Select **Save Changes**.

   Studio checks the syntax of your entry and reformats your entry to add line
   feeds and indentation. A message lets you know whether your changes were
   saved successfully.

For examples of email messages that you can send to let learners know when the
course discussions are closed (or open), see :ref:`Example Messages to
Students`.


.. _Discussions on Mobile Apps:

***************************************
Discussions in the edX Mobile App
***************************************

Learners can participate in course discussions using the edX mobile app as
they do on the edX site, but there are some differences in the actions that
moderators can take in discussions using the mobile app. To perform moderation
or administrative tasks for your course discussions, you need to work in a web
browser.

The following actions are not supported on the edX mobile apps.

  * Pinning posts
  * Marking responses to question posts as answers
  * Endorsing responses to discussion posts
  * Closing posts


.. include:: ../../../links/links.rst
