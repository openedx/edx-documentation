.. _Discussions:

##################################
Managing Course Discussions
##################################

Discussions, or discussion forums, foster interaction among learners and
between learners and the course team. You can set up different topics to guide
these interactions when you create your course, and then run and moderate
discussions throughout the course to encourage participation and develop course
community.

Discussions are also excellent sources of feedback and ideas for the future.

For information about running and moderating discussions, see the following
sections.

.. contents::
 :local:
 :depth: 1
  
For information about how using cohorts in your course affects how your course
team might moderate course discussions, see :ref:`Moderating Discussions for
Cohorts`.

.. note:: The :ref:`Discussions for Students and Staff` section describes
   features that are available to all discussion participants, and might be
   useful to learners who are new to online discussion forums. You can share
   the section with your learners by, for example, adding a "Never Used a
   Discussion Forum Before?" post that includes the information you think will
   be most useful to them.


.. _Overview_discussions:

********************************
Overview
********************************

Learners and the course team use course discussions to share ideas, exchange
views, consider different viewpoints, and ask questions. In a discussion, there
are three hierarchical levels of interaction.

* A post is the first level of interaction. A post opens a new subject. Posts
  can be made as questions, to solicit a concrete answer, or as discussions,
  to start a conversation. When you add a post, you decide whether to add it
  as a **Question** or as a **Discussion**.

* A response is the second level of interaction. A response is a reply made
  directly to a post to provide a solution or continue the conversation.

* A comment is the third level of interaction. A comment is often a
  clarification or side note made to a specific response, rather than to the
  post as a whole.
 
The dialog created by a post, its responses, and the comments on those
responses is sometimes called a thread. Discussion threads are saved as part
of the course history.

All course team members and enrolled learners can add posts, responses, and
comments, and view all of the posts, responses, and comments made by other
course participants. 

Members of the course community, learners as well as the course team, can be
given permission to moderate or administer course discussions through a set of
discussion administration roles.

.. note:: The course team members that you set up in Studio or on the 
 Instructor Dashboard in the LMS are not granted discussion administration
 roles automatically. Only people who have a discussion administration role can
 view all of the discussion contributions, for example in courses using
 cohorts.

 Discussion administration roles must be explicitly granted to members of the
 course team for them to moderate or administer course discussions. The
 course author, and any team members with the Admin role, can grant discussion
 administration roles. For information about assigning discussion privileges,
 see :ref:`Assigning_discussion_roles`.

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

 .. image:: ../../../shared/building_and_running_chapters/Images/Discussion_Add_initial.png
  :alt: Policy value of {"General": {"id": "i4x-edX-Open-edx_demo_course"}}.

4. Copy the three lines provided for the General topic and paste
   them above the closing brace character (``}``).

 .. image:: ../../../shared/building_and_running_chapters/Images/Discussion_Add_paste.png
  :alt: Policy value of {"General": {"id": "i4x-edX-Open-edx_demo_course"} 
        "General": {"id": "i4x-edX-Open-edx_demo_course"}}.

5. Replace the second "General" with the quoted name of your new topic.

#. Change the value for the second "id" to a unique identifier. For example,
   append a reference to the name of the topic.

.. note:: In discussion topic IDs, you can use only alphanumeric characters
   and these special characters: underscore, hyphen, and period.

7. Add a comma after the first closing brace (``},``).

 .. image:: ../../../shared/building_and_running_chapters/Images/Discussion_Add_name.png
  :alt: Policy value of {"General": {"id": "i4x-edX-Open-edx_demo_course"}, 
        "Course Q&A": {"id": "i4x-edX-Open-edx_demo_course_faq"}}.

8. Select **Save Changes**. Studio resequences and reformats your entry. Scroll
   back to the **Discussion Topic Mapping** field to verify that your entry was
   saved as you expect. Entries that do not contain all of the required
   punctuation characters revert to the previous value when you save, and no
   warning is presented.

When learners select the **Discussion** page for your course, the drop-down
Discussion list now includes the topic you added.

 .. image:: ../../../shared/building_and_running_chapters/Images/NewCategory_Discussion.png
  :alt: Image of a new topic named Course Q&A in the list of discussions.

.. note:: In courses that use cohorts, the course-wide discussion topics that
   you add are unified. All posts can be read and responded to by every
   learner, regardless of the cohort that they belong to. You can optionally
   configure these topics to be divided by cohort. For more information, see :ref:`Coursewide
   Discussion Topics and Cohorts`.

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
   create discussion topics by using the **Duplicate** button in Studio, and
   do not reference the same discussion ID in more than one place in your
   course. Duplicated discussion components will result in discussion topics
   containing the same conversations, even if learners post in different
   discussion topics.

For more information about the visibility of content-specific discussion
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

.. important:: The course team members that you set up in Studio or on the 
 Instructor Dashboard are not automatically granted discussion administration
 roles.

 Discussion administration roles must be explicitly granted to members of the
 course team for them to moderate or administer course discussions. The course
 author and team members with Admin access (Studio) or Instructors (LMS
 Instructor Dashboard) can grant discussion administration roles.

Different options for working with discussions are available through
the following roles.

* Discussion moderators can edit and delete messages at any level, review
  messages flagged for misuse, close and reopen posts, pin posts, and endorse
  responses. 

  Posts made by moderators are marked as "By: Staff" in the list of
  posts. Responses and comments made by moderators have a colored "Staff"
  identifier. This role is often given to course team members who already have
  the Staff role.

.. removed this clause from 1st sentence per JAAkana and MHoeber: , and, if the
.. course is cohorted, see posts from all cohorts

* Discussion community TAs have the same options for working with discussions
  as moderators. 

  Posts made by community TAs are marked as "By: Community TA"
  in the list of posts on the **Discussion** page. Responses and comments made
  by community TAs have a colored "Community TA" identifier. This role is often
  given to learners.

* Discussion admins have the same options for working with discussions as
  moderators, and their posts, responses, and comments have the same "Staff"
  identifiers. 

  This role can be reserved for assignment to course team members
  who have the Admin role only: the discussion admins can then both
  moderate discussions and give other users discussion management roles
  whenever necessary.

.. The following paragraph applies to the edX mobile app for Open edX (with discussions)
.. Alison, DOC-1815, June 2015

.. only:: Open_edX

  .. note:: The options for working with discussions described above are only 
    available when members of the discussion administration team work in a web
    browser. The edX mobile apps do not currently offer the additional options.

Before you can assign roles to your discussion team, you need their email
addresses or usernames.

* To get this information for a course team member, on the Instructor Dashboard
  select **Membership**, and then select either **Staff** or **Admin**.

* To get this information for an enrolled learner, on the Instructor Dashboard
  select **Data Download**, and then **Download profile information as a CSV**.


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
particular section or subsection of the courseware, and are not subject to
release dates.


.. _Running_discussions:

*********************
Run a Discussion
*********************

On an ongoing basis, the members of your discussion team run the course
discussion by making contributions, endorsing responses, marking answers as
correct, and guiding learner messages into pertinent threads. Techniques that
you can use throughout your course to make discussions successful follow.

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
selecting the type for their posts, and encourage learners to do the same. For more information, see
:ref:`Find Question Posts and Discussion Posts`.

.. future: changing the type of a post, maybe resequence or separate  conventions from post types

========================
Seed Discussion Topics
========================

To help learners learn how to get the most out of course discussions, and find
the best discussion topic to use for their questions and conversations, you can
seed discussion topics in course-wide discussion topics before the course starts. 
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
posts, the discussion team can use these techniques. However, be aware that
long threads (with more than 200 responses and comments) can be difficult to
read, and can therefore result in an unsatisfactory experience in the
discussion.

* Pin a post. Pinning a post makes it appear at the top of the list of posts on
  the **Discussion** page. As a result, it is more likely that learners will
  see and respond to pinned posts. You can write your own post and then pin it,
  or pin a post by any author. Select the "More" icon and then **Pin**.

    .. image:: ../../../shared/building_and_running_chapters/Images/Pin_Discussion.png
     :alt: Image of the pin icon for discussion posts.

* Endorse a response. Endorsing a response indicates that it provides value to
  the discussion. Select the "check mark" (or tick mark) icon for the response.

    .. image:: ../../../shared/building_and_running_chapters/Images/Endorse_Discussion.png
     :alt: Image of the Endorse button for discussion posts.

* Mark a question as answered. You use the same procedure to mark a response as
  the correct answer to a question as you do to endorse contributions to a
  discussion: select the "check mark" (or tick mark) icon for correct answers.

* Close a post. You can respond to a redundant post by (optionally) pasting in
  a link to the post that you prefer learners to contribute to, and prevent
  further interaction by closing the post. Select the "More" icon and then
  **Close** to close it.

* Provide post/response/comment guidelines. You can post information from the
  :ref:`overview<Overview_discussions>` in this chapter, or the :ref:`anatomy
  of edX discussions<Anatomy of edX Course Discussions>` in the next chapter,
  in a course-wide discussion topic (such as General) to provide guidance about
  when to start a new thread by adding a post, responding to an existing post,
  or commenting on a response.

.. The following paragraph applies to the edX mobile app for Open edX (with discussions)
.. Alison, DOC-1815, June 2015

.. only:: Open_edX

    .. note:: You can only pin posts and mark questions as answered when you 
      work in a web browser. You cannot complete these activities when you work
      in an edX mobile app.

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

If you want to find out more about a specific discussion participant, you can
view that learner's edX profile. Learners can have either a limited profile or a
full profile.

To view a learner's profile, follow these steps.

#. On the **Discussion** page, select a username in a post,
   response, or comment.
#. On the **Active Threads** page for that learner, select the
   learner's username.

The following image shows a learner's username in a post, the learner's
username on the **Active Threads** page, and the learner's profile page.

.. image:: ../../../shared/building_and_running_chapters/Images/SFD_Prof_from_Disc.png
  :width: 600
  :alt: Image of a discussion with a learner's username circled, an image of
      that learner's active threads page in the course discussions, and an
      image of the learner's profile.

For more information, or to create your own profile, see `View, Create, or
Edit an edX Profile <http://edx-guide-for-students.readthedocs.org/en/latest/sfd_your_information.html#sfd_profile_page>`_.

========================================
Provide Guidelines for Learners
========================================

You can develop a set of best practices for discussion participation and make
them available to learners as a course handout file or on a defined page in
your course. These guidelines can define your expectations and optionally
introduce features of edX discussions.

You can also share the :ref:`Discussions for Students and Staff` chapter with
your learners. It describes features that are available to all discussion
participants, and may be useful to learners who are new to online discussion
forums.

.. For a template that you can use to develop your own guidelines, see
.. :ref:`Discussion Forum Guidelines`.

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
  to an FAQ topic, or announce them on the Course Info page.

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
check or tick mark image replaces the question mark image. For more information, see :ref:`Answer
Questions`.

In addition to these visual cues, filters can help you find questions and
discussions that need review. Above the list of posts on the **Discussion**
page, the **Show all** filter is selected by default. You can also select:

* **Unread**, to list only the discussions and questions that you have not yet
  viewed.

* **Unanswered**, to list only questions that do not yet have any responses
  marked as answers.

==================
Edit Messages
==================

Discussion moderators, community TAs, and discussion admins can edit the
content of posts, responses, and comments. Messages that include spoilers or
solutions, or that contain inappropriate or off-topic material, should be
edited quickly to remove text, images, or links.

.. The following paragraph applies to the edX mobile app for Open edX (with discussions)
.. Alison, DOC-1815, June 2015

.. only:: Open_edX

  .. note:: You can only edit messages in a web browser. You cannot edit 
   messages when you work in an edX mobile app. 

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

.. The following paragraph applies to the edX mobile app for Open edX (with discussions)
.. Alison, DOC-1815, June 2015

.. only:: Open_edX

  .. note:: You can only delete messages in a web browser. You cannot delete 
   messages when you work in an edX mobile app.

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

.. The following paragraph applies to the edX mobile app for Open edX (with discussions)
.. Alison, DOC-1815, June 2015

.. only:: Open_edX

  .. note:: You can only respond to reports of misuse in a web browser. You 
   cannot edit, delete, or remove the report flag from messages when you work
   in an edX mobile app.

#. View the live version of your course and select **Discussion** at the top of
   the page.

#. In the list of posts on the left side of the page, use the filter drop-down
   list (set to **Show all** by default) to select **Flagged**.

#. Review listed posts. A post is listed if it or any of its responses or
   comments has been reported. The reported contribution includes a
   **Reported** identifier.

#. Edit or delete the post, response, or comment. Alternatively, remove the
   flag: select the "More" icon and then **Unreport**.

===============
Block Users
===============

For a learner who continues to misuse the course discussions, you can unenroll
the learner from the course. For more information, see :ref:`unenroll_learner`.
If the enrollment period for the course is over, the learner cannot re-enroll.

.. _Close_discussions:

******************************
Close Discussions
******************************

You can close the discussions for your course so that learners cannot add
messages. Course discussions can be closed temporarily, such as during an exam
period, or permanently, such as when a course ends.

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
  **Course Info** page and post them to a General discussion.

=====================================
Start-End Date Format Specification
=====================================

To close course discussions, you supply a start date and time and an end date
and time in Studio. You enter the values in this format:

``["YYYY-MM-DDTHH:MM", "YYYY-MM-DDTHH:MM"]``

where:

* The dates and times that you enter are in the Universal Coordinated (UTC)
  time zone, not in your local time zone.

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
July, and then permanently on 9 August 2014, you enter:

``["2014-07-22T08:00", "2014-07-25T18:00"], ["2014-08-09T00:00", "2099-08-09T00:00"]``

You enter these values between an additional pair of square brackets which are
supplied for you in Studio.

============================================
Define When Discussions Are Closed
============================================

To define when discussions are closed to new contributions and when they
reopen:

#. Open your course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. Scroll down to the **Discussion Blackout Dates** policy key. 

#. In the field for the value, place your cursor between the supplied square
   brackets. Use the required date format specification to enter the start and
   end dates for each time period during which you want discussions to be
   closed.

   When you enter the dates and times from the example above, the value field
   looks like the following example.

   .. image:: ../../../shared/building_and_running_chapters/Images/Discussion_blackout_unformatted.png
     :alt: Policy value of [["2014-07-22T08:00", "2014-07-25T18:00"],
         ["2014-08-09T00:00", "2099-08-09T00:00"]].

5. Select **Save Changes**.

   Studio reformats your entry to add line feeds and indentation, like this:

   .. image:: ../../../shared/building_and_running_chapters/Images/Discussion_blackout_formatted.png
     :alt: Same policy value but with a line feed after each bracket and comma,
         and an indent before each date.

For examples of email messages that you can send to let learners know when the
course discussions are closed (or open), see :ref:`Example Messages to
Students`.
