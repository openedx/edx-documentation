.. _Teams Setup:

##########################################
Using Teams in Your Courses
##########################################

This section provides information about setting up teams in your courses.

.. contents::
  :local:
  :depth: 2

For information about managing teams in your courses, see the following topics.

* :ref:`Teams Discussions`
* :ref:`CA Learner Experience of Teams`


.. _CA_Teams_Overview:

*******************************
Teams Overview
*******************************

Using teams in your course is an effective way for learners to interact and
collaborate on small group projects or activities. You define topics that
learners choose from; learners choose a topic they are interested in, and
either join a team or create their own team within that topic. Each learner
can belong to only one team.

When learners create a new team, they add names and descriptions to identify
their team. They can also optionally specify a primary communication language
and a primary country that members identify with. Team characteristics might
serve as the basis for attracting new members, resulting in small groups of
learners with similar interests and goals who will work together on projects
or activities within the same topic area.

Teams are most effective when learners have a clear reason for joining a team,
and a clear outcome to achieve with fellow team members. For example, you
might create an assignment that consists of a group project or activity, with
a choice of topics, and ask learners to join teams within the topic of their
choice to complete the assignment. Team members can use discussions within the
team to communicate and collaborate on the assignment. If you want only to
provide a way for learners to connect socially, consider using discussions
within the course rather than teams. For more information about
using discussions, see :ref:`Running_discussions`.


.. _Enable and Configure Teams:

*******************************
Enable and Configure Teams
*******************************

To disable or enable the Teams application, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Click the gear icon on the **Teams** card shown on this page.
#. From the **Configure teams** modal, select the toggle to enable or disable the **teams application**.
#. Select **Apply** to save your configuration changes.


.. note:: The **Teams** page in the LMS becomes available only after you have
   specified at least one team topic.

There are several configuration options available to the Teams application.
Many basic configuration options are provided within Studio’s Pages & Resources area,
and course management capabilities are available to instructors directly from the Teams application.
Included below are details about both the configuration options and management tools.

To change access to the course team configuration options, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Click the gear icon on the **Teams** card shown on this page.
#. From the Configure team modal, adjust any of the configuration settings as described below to fit your course needs.
#. Select **Apply** to save your configuration changes.

**Default Team Size**

This specifies the maximum number of learners that can join a team, a default value for all teams in your course.
This default value can be overridden for a specific team category as well.

**Team Categories:**

Each team category is a grouping for multiple learner teams, and each category has several
configuration details and options. To start, each of these team categories must be given a
unique name, and optionally a description can also be set.

These names and descriptions are visible to learners in the Teams application as shown in the visual below.

    .. image:: ../../../shared/images/teams_application_screen.png
    :alt: The navigation bar in the LMS, showing the default pages.


.. note::  EdX recommends that you do not delete topics once your course is
   running, and if learners might have already joined teams within topics. If
   you delete a topic from the **Teams Configuration** policy key, that topic
   is no longer visible in the LMS, and learners will not be able to leave
   teams associated with the deleted topic.


**Types of Team Categories**

There are several types of team categories that can be created, each of which behaves
differently for both instructors and learners.

* **Open** sets up a team category where learner can create, join, leave, and see all teams within the category
* **Public managed** allows only course staff to control team creation and membership.
  Learners can see other teams but cannot join or leave their team.
* **Private managed** allows only course staff to control team creation and membership.
  Additionally, learners can only see the teams they are members of, unlike other options
  that give them visibility into other teams. This type is helpful in particular if team
  assignments are being used in a course.

.. note:: If you do not see all team category type options, check with your platform administrator
   to see if the relevant teams application features have been enabled.

**Team Category Size Override**

Separate from the team maximum size setting, it is possible to override the specific team size for
a given team category, allowing you to adjust team sizes to fit your course needs. An example of
when you might need this is ….

.. _Create a Team:

******************
Create a Team
******************

Although learners in your course can create their own teams, you can seed each
topic with a few teams to give learners some ideas for their own teams.

Course team members who have the **Staff**, **Admin**, **Discussion Admin**,
or **Discussion Moderator** role can create new teams within topics.
**Community TAs** and learners in the course can also create teams, although
learners can create a new team only if they do not already belong to one.

To create a team, follow these steps.

#. From the **Teams** page in the LMS, select **Browse**, then select the
   topic in which you want to create a team.

#. At the bottom of the list of teams within the topic, select the **create a
   new team in this topic** link.

   .. image:: ../../../../shared/images/Teams_CreateNewTeamLink.png
     :width: 600
     :alt: The "create a new team in this topic" link


3. On the **Create a New Team** page, add a name and description for the team.

   In the description, include details about the proposed project or activity
   to help learners to decide whether they want to join this team.

   .. image:: ../../../../shared/images/Teams_CreateNewTeamForm.png
     :width: 600
     :alt: Empty form with fields to be completed when you create a new team.

#. Optionally, add some characteristics for your team. You can specify a
   language that members would primarily use to communicate with each other,
   and a country that members would primarily identify with. Keep in mind that
   if your team details make the team membership seem too selective, learners
   might be discouraged from joining.

#. When you have finished entering details for the team, select **Create**.

   Your new team is added to the list of teams under your selected topic.



.. _Search for a Team:

******************
Search for a Team
******************

Use the search field to find a team within a topic.

.. note:: Partial words are not supported for searching teams.

To get a list of teams whose names, descriptions, or characteristics match
your search keywords, follow these steps.

#. From the **Teams** page in the LMS, select **Browse**, then select the
   topic in which you want to find a team.

#. In the search field, enter one or more keywords to search for, then press
   **Enter** or select the search icon.

   Teams within the topic that match your search are displayed.

To clear the existing search term, select the **X** next to the search field,
or select all the text within the field and enter text to replace it.


.. _Edit a Team:

******************
Edit a Team
******************

Course team members who have the **Staff**, **Admin**, **Discussion Admin**,
or **Discussion Moderator** role can edit any of a team's details, including
removing members from a team. **Community TAs** can also edit teams. For more
details about removing team members, see :ref:`Remove Learner from Team`.

To edit a team's details, follow these steps.

.. note:: Before making significant changes to a team, communicate with team
   members so that they are aware of the changes and their impacts.

#. In the LMS, select the **Teams** tab.
#. On the **Teams** page, select **Browse** to show all topics.
#. Select the arrow button for the topic to show all teams in that topic.
#. Locate the team that you want to edit. To find the team, you can search
   using keywords or sort teams by last activity or open slots.
#. Select **View** for the team that you want to edit.
#. Select **Edit Team**.
#. Make your changes, then select **Update**.
   The team's details are updated.


.. _Remove Learner from Team:

********************************
Remove a Learner from a Team
********************************

Course team members who have the **Staff**, **Admin**, **Discussion Admin**,
or **Discussion Moderator** role can remove members from a team. **Community
TAs** can also remove learners from a team. You might want to remove a learner
from a team and make the spot on the team available to other learners if, for
example, a learner joined a team but is not participating, or if a learner has
unenrolled from the course without leaving the team.

.. note:: Before making significant changes to a team, communicate with team
   members so that they are aware of the changes you will make, and their
   impacts.

To remove a learner from a team, follow these steps.

#. In the LMS, select the **Teams** tab.
#. On the **Teams** page, select **Browse** to show all topics.
#. Select the arrow button for the topic to show all teams in that topic.
#. Locate the team that you want to edit. To find the team, you can search
   using keywords or sort teams by last activity or open slots.
#. Select **View** for the team from which you want to remove a learner.
#. Select **Edit Team**.
#. On the **Instructor Tools** bar, select **Edit Membership**.

   .. image:: ../../../../shared/images/Teams_InstructorToolsEditMembers.png
     :width: 600
     :alt: The Edit Membership button on the "Instructor Tools" bar on the Edit Team page.

#. On the team's **Membership** page, select **Remove** next to the name of
   the learner who you want to remove from the team.
#. In the confirmation message, select **Remove**.


   The team member you removed no longer appears on the **Membership** page.

#. Repeat steps 8 and 9 to remove additional members.

   The team members you removed no longer appear on the **Membership** page,
   and the count of team members is updated wherever it appears on team pages.





.. _Delete a Team:

******************
Delete a Team
******************

Course team members who have the **Staff**, **Admin**, **Discussion Admin**,
or **Discussion Moderator** role can delete teams. **Community TAs** can also
delete teams. you might need to manage the teams in your course, including
deleting teams that remain empty or where members are experiencing abusive
situations.

When you delete a team, all learners are removed from the team membership.
Neither learners nor course team members can access discussions from deleted
teams.

.. note:: Deleting a team removes it permanently from the course, and cannot
   be undone.

To delete a team, follow these steps.

#. In the LMS, select the **Teams** tab.
#. On the **Teams** page, select **Browse** to show all topics.
#. Select the arrow button for the topic to show all teams in that topic.
#. Locate the team that you want to delete. To find the team, you can search
   using keywords or sort teams by last activity or open slots.
#. Select **View** for the team that you want to delete, then select **Edit
   Team**.
#. On the **Instructor Tools** bar, select **Delete Team**.

   .. image:: ../../../../shared/images/Teams_InstructorToolsDeleteTeam.png
     :width: 600
     :alt: The Edit Membership button on the "Instructor Tools" bar on the Edit Team page.

#. In the confirmation message, select **Delete**.

   You return to the topic page, where you receive a confirmation that the
   team has been successfully deleted. The team no longer appears in the teams
   list within its topic. Learners who were previously members of this team no
   longer belong to a team.

