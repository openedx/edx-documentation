.. _CA_Teams:

##########################################
Using Teams in Your Courses
##########################################

This section provides conceptual and procedural information about using teams
in your courses.


.. contents::
  :local:
  :depth: 1


.. _CA_Teams_Overview:

*******************************
Teams Overview
*******************************

Using teams in your course enables learners to interact and collaborate in
small groups around topics that you create.

Learners can create their own teams and use not only names and descriptions to
identify them but also, optionally, a primary communication language and a
primary country that members identify with. Team characteristics might serve
as the basis for attracting new members, resulting in small groups of learners
with similar interests and goals who will work together on projects within the
same topic area.


.. https://openedx.atlassian.net/browse/TNL-1889

*******************************
Enabling and Configuring Teams
*******************************

To enable teams in your course, follow these steps.

#. In Studio, from the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate the **Teams Configuration** policy key.

#. Within this policy key you define two entries, topics and maximum team size.

#. To specify the maximum team size for teams in your course, enter the
   ``max_team_size`` parameter in double quotation marks, a colon, then the
   value. For example, to set the maximum number of learners per team in your
   course to 5, your entry would be:

   ``"max_team_size": 5``

#. To specify topics within which teams can be created, add entries under
   ``"topics"``. For each topic, provide a description, name, and ID as shown.

   .. note:: In topic specifications, you can use only alphanumeric characters
      and these special characters: underscore, hyphen, and period.

.. is the above note true?      

.. ADD IMAGE - screen capture of Teams Configuration entries

   Make sure that each set of values for a team is enclosed in a set of curly
   braces, with a comma between consecutive values. If you create more than
   one topic, make sure there is a comma after the closing curly brace of each
   topic that has another topic following it.

   All of the sets of topic values are enclosed within a set of square
   brackets, with a comma after the closing square bracket.

   The topics you have created are shown in the LMS when learners browse teams
   by topic.


*********************************
The Learner's Experience of Teams 
*********************************

After you have enabled teams and created topics in your course, learners can
begin browsing and joining teams. Each learner can belong to only one team.

=======================
Browsing Teams by Topic
=======================

On the Teams page in the LMS, learners in your course can browse topics to
find a subject that they are interested in working on. Within each topic,
learners can see whether teams already exist for the topic. 

If there are existing teams, learners can view each team's name, description,
and, if these are defined, the team's primary language of communication and
country that members primarily identify with. Learners can also view
discussion posts that team members have made, but they cannot add posts unless
they belong to a team.


====================================
Joining, Creating, or Leaving a Team
====================================

When learners find a team that they want to join, they select **Join Team**
and are immediately added to the team membership, subject to the maximum team
size. 

If no teams exist, no teams exist that learners want to join, or if existing
teams have reached the maximum number of members, learners can create their
own teams. Under a topic, learners select **Create Team**. They specify a name
and description for their team, and optionally specify a country and language
that team members identify with. A learner who creates a team automatically
becomes a member of the new team.

.. note:: Encourage learners to join existing teams before creating new teams.

At any time, learners can leave teams that they have joined. Learners can only
belong to one team at a time. If they attempt to join a team while they belong
to another team, they see a message indicating that they already belong to a
team. To join a new team, they must first leave their existing team.



================================
Inviting Friends to Join a Team
================================

When learners join a team, they can invite friends to join that team by
copying a link and sending it to invitees so that they can locate the team.


===================================
Participating in Team Discussions
===================================

Only members of a team can post to the discussion forum in their team, but
their posts are visible to all learners in your course.

.. note:: Team discussions are not divided by cohort. Learners who are in the
   same team, but who belong to different cohorts can view and participate in
   their team discusssions without regard to the cohort they belong to.

For information about course discussions and managing discussions, see
:ref:`Discussions` and :ref:`Discussions for Students and Staff`.


*********************************
Managing Team Discussions 
*********************************

As in course discussions, different roles have different privileges in team
discussions.

.. note:: The members of the course team that you set up in Studio or on the
   Instructor Dashboard in the LMS are not automatically granted discussion
   administration roles.

   Discussion administration roles must be explicitly granted to members of the
   course team for them to be able to moderate or administer course discussions.
   The course author and any team members who have the Admin role can grant
   discussion administration roles.

For information about discussion administration roles, see
:ref:`Assigning_discussion_roles`. For information about managing discussions,
see :ref:`Running_discussions`.

===================================
Ability to Post in Team Discussions
===================================

Only team members, discussion community TAs, and course team members with the
roles of Discussion Admin or Discussion Moderator can post to the team
discussion.

Posts made by discussion community TAs are marked as "By: Community TA".
Responses and comments made by community TAs have a colored "Community TA"
identifier.

Posts made by discussion moderators or discussion admins are marked as "By:
Staff" in the lists of posts, and responses and comments made by discussion
moderators are have a colored "Staff" identifier.


===================================
Ability to Edit or Delete Posts
===================================

Discussion moderators or discussion admins can perform the following actions
in team discussions.

* Review, edit, or delete messages
* Pin, close, or reopen posts
* Endorse responses

