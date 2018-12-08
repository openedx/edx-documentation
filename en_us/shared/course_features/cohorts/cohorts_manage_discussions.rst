.. _Moderating Discussions for Cohorts:

##########################################################
Managing Discussions in Courses with Learner Cohorts
##########################################################

This section provides information about managing discussions when cohorts are
enabled in your course.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

In courses that have cohorts enabled, every post has an indicator of who can
read it: either all learners, or only the members of a single cohort. For
learners, this is the only noticeable difference between discussions in
courses that include cohorts when compared to courses that do not.

.. only:: Partners

 You can share the examples in the :ref:`Read the Cohort Indicator in Posts`
 section with your learners. The :ref:`learners:Course Discussions Index`
 section in the *EdX Learner's Guide* also provides useful information to help
 learners make the most of their participation in course  discussions.

.. only:: Open_edX

 You can share the examples in the :ref:`Read the Cohort Indicator in Posts`
 section with your learners. The :ref:`openlearners:Course Discussions Index`
 section in the *Open edX Learner's Guide* also provides useful information to
 help learners make the most of their participation in course  discussions.


Course team members who have the discussion admin, discussion moderator, or
community TA role see the same indicator of who can read each post. Unlike the
learners, however, team members with discussion privileges can read and
contribute to every post, regardless of the cohort assignment of the learner
who posted it.

.. note:: Course team members must have the Discussion Moderator or Discussion
 Admin role in addition to the Staff or Admin role to be able to view posts
 that are divided by cohort. For information about assigning discussion
 moderation roles, see :ref:`Assigning_discussion_roles`.

   Learners who have the Community TA role can read and contribute to all
   posts.

In courses with the cohort feature enabled, course team members who have
discussion moderator or admin privileges can also:

* Choose who will be able to see the posts that they add to divided topics. See
  :ref:`Choosing the Visibility of a Post`.

* Filter the posts that are listed on the **Discussion** page by cohort.
  See :ref:`Viewing the Posts of a Cohort Group`.

All of the other options and features described in the :ref:`Discussions`
section continue to be available to the discussion moderation team.

.. _Finding Out Who Can See a Post:

********************************
Identifying Who Can Read a Post
********************************

In a course that includes cohorts, all posts include a cohort indicator above
the title. This indicator appears after any student or team member adds a
post. Other than naming the cohorts carefully when you add them, no
configuration is necessary to include this identifier.

Optionally, you can name your discussion topics to show students who will be
able to view their posts. See :ref:`Apply Naming Conventions to Discussion
Topics`.

.. _Read the Cohort Indicator in Posts:

==================================
Read the Cohort Indicator in Posts
==================================

Every post includes a sentence that identifies whether everyone can see and
contribute to it, or only the members of a cohort in the course. Examples
follow.

.. image:: ../../../../shared/images/post_visible_all.png
 :alt: A discussion topic post with "This post is visible to everyone" above
       the title.
 :width: 600

.. extra line

.. image:: ../../../../shared/images/post_visible_cohort.png
 :alt: A discussion topic post with "This post is visible to" and a cohort name
       above the title.
 :width: 600

You see this identifier after you add your post. All of the responses and
comments that other contributors add to a post are visible to the same group of
people as the post itself.

.. _Apply Naming Conventions to Discussion Topics:

=========================================================
Apply Naming Conventions to Discussion Topics
=========================================================

Optionally, course team members can give learners the audience context of their
posts before they add them. Indicating who will be able to read posts in the
names of the topics themselves can be useful when a cohort is particularly
sensitive about the privacy of their conversations.

For example, you add "(everyone)" to the names of the unified course-wide
discussion topics in your course.

.. image:: ../../../../shared/images/discussion_category_names.png
 :alt: An image showing the names you supply for course-wide topics in Studio
   on the dropdown list of discussion topics in the live course.
 :width: 800

When learners visit the **Discussion** page and use dropdown lists to select a
course-wide topic, the topic names indicate who can see the posts, responses,
and comments.

(In the illustration above, every topic name includes either "(everyone)" or
"(private)". You might find it necessary only to explicitly identify topics
that have a unified audience for all posts.)

For more information about adding and configuring course-wide discussion
topics, see :ref:`Create CourseWide Discussion Topics` and :ref:`Specify
Whether CourseWide Discussion Topics are Cohorted`.

If desired, you could also apply a naming convention to the content-specific
discussion topics that you add as Discussion components in Studio. For example,
you could include an identifier like "(private)" or "(small group)" in the
**Subcategory** name of every Discussion component that you add.

.. image:: ../../../../shared/images/discussion_topic_names.png
 :alt: An image showing the Subcategory name that you supply for a Discussion
       component in Studio on the dropdown lists of discussion topics in the
       live course.
 :width: 800

.. _Choosing the Visibility of a Post:

***************************************
Choosing the Visibility of a Post
***************************************

If you have the discussion admin, discussion moderator, or community TA role,
you can make posts to divided discussion topics visible to everyone who is
enrolled in the course or to the members of a selected cohort only. When
you :ref:`add a post<Add a Post>`, the **Visible to** dropdown list appears
above the **Title** field.

This example shows a new post being added to a content-specific
discussion topic.

.. image:: ../../../../shared/images/visible_to_contentspecific.png
 :alt: The fields and controls that appear when a team member clicks
       New Post for a content-specific topic

As a discussion team member, you can choose the visibility of your posts in
topics that are divided by cohort. This means that you can add a single post
with information that you want everyone to see, rather than having to write a
separate post for each cohort. It also means that it is possible for you
to unintentionally share information with a different audience than you
intended.

.. note:: Learners do not choose the visibility of their posts. The
 visibility of learner posts is determined by the configuration of the topic
 they post in. See :ref:`Finding Out Who Can See a Post`.

Posts that discussion team members add to unified discussion topics are always
visible to all students, regardless of cohort assignment.

.. _Considerations When Editing Posts:

===================================
Considerations When Editing Posts
===================================

It may be helpful to keep these additional considerations in mind when you edit
posts in a course that includes cohorts.

* You cannot change the visibility of a post after it has been added. If you
  notice that a post contains information that is not appropriate for the
  cohort who can read it, edit the content of the post or delete the post.

* If you change the topic that a post appears in, the visibility of the post
  and its responses and comments **does not change**. This ensures that
  learners who are following the post, or who have contributed responses or
  comments to it, will still be able to read it.

* All of the responses and comments that are contributed to a post will be
  visible to the same group of people as the post itself. You cannot change the
  visibility of individual responses or comments.

.. _Viewing the Posts of a Cohort Group:

*****************************
Viewing the Posts of a Cohort
*****************************

When a course includes learner cohorts, you can view posts and monitor
discussion activity for one cohort at a time. You can also view all
posts.

.. note:: Course team members must have discussion moderator or admin
   privileges in addition to their course team privileges to be able to view
   posts that are divided by cohort.

Above the discussion navigation pane on the **Discussion** page, the **in all
cohorts** filter is selected by default. You see every post when you make this
selection, as shown in the illustration on the left. To limit the list so that
you can view the same set of posts as the members of a cohort, select the name
of that cohort as shown on the right.

.. image:: ../../../../shared/images/viewing_all_or_cohort.png
 :alt: An image showing the discussion navigation pane on the Discussion page,
  first showing all posts then showing only posts that members of the
  University Alumni cohort can see.
 :width: 800

Note that both of these lists include posts that are visible to
everyone. When you filter the list by cohort, you see the same, complete
set of posts that the members of the cohort see.

For other options that you can use to view posts, see
:ref:`Moderating_discussions`.
