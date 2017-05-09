.. _Managing Divided Discussion Topics:

###################################
Managing Divided Discussion Topics
###################################

This section provides information about managing discussions that are divided
based on one type of group in your course, either :ref:`cohorts<Cohort>` or
:ref:`enrollment tracks<enrollment_track_g>`.

For information about divided discussions, see :ref:`About Divided Discussions`.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

In discussion topics in your course, every post has an indicator of who can read
it: either all learners, or only the members of a particular group. For
learners, this is the only noticeable difference between discussions in courses
that use divided discussions, and courses that do not have groups and do not use
divided discussions.

.. only:: Partners

 You can share the examples in the :ref:`Read the Group Indicator in Posts`
 section with your learners. The :ref:`learners:Course Discussions Index`
 section in the *EdX Learner's Guide* also provides useful information to help
 learners make the most of their participation in course discussions.

.. only:: Open_edX

 You can share the examples in the :ref:`Read the Group Indicator in Posts`
 section with your learners. The :ref:`openlearners:Course Discussions Index`
 section in the *Open edX Learner's Guide* also provides useful information to
 help learners make the most of their participation in course discussions.


Course team members who have the discussion admin, discussion moderator, or
community TA role see the same indicator of who can read each post. Unlike the
learners, however, team members with discussion privileges can read and
contribute to every post, regardless of the group membership of the learner
who posted it.

.. note:: Course team members must have the discussion moderator or discussion
 admin role in addition to the Staff or Admin role to be able to view posts
 that are divided by group. For information about assigning discussion
 moderation roles, see :ref:`Assigning_discussion_roles`.

 Learners who have the Community TA role can read and contribute to all posts.

In courses where either cohorts or multiple enrollment tracks are enabled,
course team members who have discussion moderator or admin privileges can also
perform the following actions.

* Choose who will be able to see the posts that they add to divided topics. See
  :ref:`Choosing the Visibility of a Post`.

* Filter the posts that are listed on the **Discussion** page by group.
  See :ref:`Viewing the Posts of a Group`.

All of the other options and features described in the :ref:`Discussions`
section continue to be available to the discussion moderation team.

.. _Finding Out Who Can See a Post:

********************************
Identifying Who Can Read a Post
********************************

In discussion topics in your course, all posts include a group indicator above
the title. This indicator appears after any learner or team member adds a
post. No configuration is necessary to include this identifier, although if
you use divided discussions in your course, you should use care in naming your
groups, because learners see the group names in the group indicators for each
post. Enrollment track groups are automatically named based on the enrollment
track.

Optionally, you can name your discussion topics to make it clear to learners
who their posts will be viewed by. See :ref:`Apply Naming Conventions to
Discussion Topics`.

.. _Read the Group Indicator in Posts:

==================================
Read the Group Indicator in Posts
==================================

Every post includes a sentence that identifies whether everyone can see and
contribute to it, or only the members of a group in the course. Examples
follow.

.. image:: ../../../shared/images/post_visible_all.png
 :alt: A discussion topic post with the indicator "This post is visible to everyone".
 :width: 600

.. extra line

.. image:: ../../../shared/images/post_visible_group.png
 :alt: A discussion topic post with the indicator "This post is visible to Alumni".
 :width: 600

You see this identifier after you add your post. All of the responses and
comments that other contributors add to a post are visible to the same group of
people as the original post.

.. _Apply Naming Conventions to Discussion Topics:

=========================================================
Apply Naming Conventions to Discussion Topics
=========================================================

Optionally, course team members can give learners the audience context of their
posts before they add them. Indicating who will be able to read posts in the
names of the topics themselves can be useful when a group is particularly
sensitive about the privacy of their conversations.

For example, you could add "(everyone)" to the names of the unified course-
wide discussion topics in your course. Similarly, you could apply a naming
convention to content-specific discussion topics that you add as discussion
components in Studio. For example, you could include an identifier such as
"(private)" or "(small group)" in the **Subcategory** name of every Discussion
component that you add.

When learners visit the **Discussion** page and use dropdown lists to select a
discussion topic, the topic names indicate who can see the posts, responses,
and comments.

For more information about adding and configuring course-wide discussion
topics, see :ref:`Create CourseWide Discussion Topics` and :ref:`Specify
Whether CourseWide Discussion Topics are Cohorted`.


.. _Choosing the Visibility of a Post:

***************************************
Choosing the Visibility of a Post
***************************************

If you have the discussion admin, discussion moderator, or community TA role,
you can make posts to divided discussion topics visible to everyone who is
enrolled in the course or only to the members of a specified group. When you
:ref:`add a post<Add a Post>`, the **Visible to** dropdown list appears above
the **Title** field.

This example shows a new post being added to a content-specific
discussion topic.

.. image:: ../../../shared/images/discussion_add_post_group_selection.png
 :alt: The fields and controls that appear when a course team member with
    discussion admin privileges clicks "Add a Post" for a divided topic.

As a discussion team member, you can choose the visibility of your posts in
topics that are divided. This means that you can add a single post with
information that you want everyone to see, rather than having to write a
separate post for each group. It also means that it is possible for you to
unintentionally share information with a different audience than you intended.

.. note:: Learners do not choose the visibility of their posts. The
 visibility of learner posts is determined by the configuration of the topic
 they post in. See :ref:`Finding Out Who Can See a Post`.

Posts that discussion team members add to unified discussion topics are always
visible to all learners, regardless of what group they belong to.

.. _Considerations When Editing Posts:

===================================
Considerations When Editing Posts
===================================

Keep these additional considerations in mind when you edit posts in a course
that includes cohorts or multiple enrollment tracks.

* You cannot change the visibility of a post after it has been added. If you
  notice that a post contains information that is not appropriate for the
  group who can read it, edit the content of the post or delete the post.

* If you change the topic that a post appears in, the visibility of the post
  and its responses and comments **does not change**. This ensures that
  learners who are following the post, or who have contributed responses or
  comments to it, will still be able to read it.

* All of the responses and comments that are contributed to a post will be
  visible to the same group of people as the post itself. You cannot change the
  visibility of individual responses or comments.

.. _Viewing the Posts of a Group:

*****************************
Viewing the Posts of a Group
*****************************

When a course includes cohorts or multiple enrollment tracks, you can view
posts and monitor discussion activity for each of the groups within the group
type that you chose to divide discussions for. You can also view all posts.

.. note:: Course team members must have discussion moderator or admin
   privileges in addition to their course team privileges to be able to view
   and filter posts that are divided.

Above the discussion navigation pane on the **Discussion** page, the **in all
groups** filter is selected by default. You see every post when you make this
selection. To limit the list so that you can view the same set of posts as the
members of a particular group, select the name of that group.

.. image:: ../../../shared/images/discussion_filter_by_groups.png
 :alt: An image showing the discussion navigation pane on the Discussion page,
     with a dropdown menu showing the options to select "in all groups" or a
     specific group by name.

Note that both of these lists include posts that are visible to everyone. When
you filter the list by a specific group, you see the same, complete set of posts
that the members of that group see.

For other options that you can use to view posts, see
:ref:`Moderating_discussions`.
