.. _Teams Setup:

##########################################
Using Teams in Your Courses
##########################################

This section provides conceptual and procedural information about using teams
in your courses.


.. contents::
  :local:
  :depth: 2


.. _CA_Teams_Overview:

*******************************
Teams Overview
*******************************

Using teams in your course is an effective way for learners to interact and
collaborate on small group projects or activities. You can define a variety of
topics from learners to choose from, within which teams can be formed. Teams
must be formed within a topic.

After browsing topics, learners can join a team or create their own team
within a topic. When learners create a new team, they add names and
descriptions to identify them but also, optionally, a primary communication
language and a primary country that members identify with. Team
characteristics might serve as the basis for attracting new members, resulting
in small groups of learners with similar interests and goals who will work
together on projects or activities within the same topic area.

Teams are most effective when learners have a clear reason for joining a team,
and a clear outcome to achieve with fellow team members. For example, you
might create an assignment that consists of a group project or activity, with
a choice of topics, and ask learners to join teams within the topic of their
choice to complete the assignment. Team members can use the discussion forums
within the team to communicate and collaborate on the assignment.

Teams are not as effective when members have no obvious team tasks or goals.
In general, edX does not recommend using teams in your course only to provide
a way for learners to connect socially.


.. _Enable and Configure Teams:

*******************************
Enable and Configure Teams
*******************************

To use teams in your course, follow these steps.

.. note:: The Teams page in the LMS becomes available only after you have
   specified at least one topic for teams in your course.

#. In Studio, from the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, select **Show Deprecated Settings**,
   then locate the **Teams Configuration** policy key.

.. Remove deprecated settings limitation in future

3. Within this policy key you define two entries: topics and maximum team size.

#. To specify the maximum team size for teams in your course, enter the
   ``max_team_size`` parameter in double quotation marks, followed by a colon,
   then a positive integer value representing the maximum number of team
   members allowed. For example, to set the maximum number of learners per
   team in your course to 5, your entry would look like this example.

   ``"max_team_size": 5``

#. To specify topics within which teams can be created, add entries under
   ``"topics"``. For each topic, provide a description, name, and ID as shown
   in the example.

   .. note:: For topic IDs, you can use only alphanumeric characters and the
      underscore, hyphen, and period characters.

::


   {
    "topics": [
        {
            "name": "Sustainability in Corporations",
            "description": "Description for Sustainability in Corporations",
            "id": "Sustain_Corporations"
        },
        {
            "name": "Water Conservation Projects",
            "description": "Description for Water Conservation",
            "id": "Water_Conservation"
        },
        {
            "name": "Sustainability Standards and Reporting",
            "description": "Description for Sustainability Standards",
            "id": "Standards_Reporting"
        }
    ],
    "max_team_size": 5
   }


.. note:: If you create more than one topic, make sure there is a comma after
   the closing curly brace of each topic that has another topic following it.

   Make sure all of the sets of topic values are enclosed within a set of square
   brackets, with a comma after the closing square bracket.

The topics you have created are shown on the **Teams** page in the LMS when
learners browse teams by topic. The **Teams** page is not visible until you
have created at least one topic.


.. image:: ../../../shared/building_and_running_chapters/Images/Teams_TopicsView.png
  :width: 800
  :alt: A screen capture showing 3 topics on the Browse Teams page.


.. _Create a Team:

******************
Create a Team
******************

As a course team member with the Staff, Admin, or Discussion Moderator role,
you can create new teams within topics.

.. Is it true that when course staff, admin, moderators or TAs create a team, they are not automatically made members of the team(s) that they create?

To create a team, follow these steps.

#. From the **Teams** page in the LMS, select **Browse**, then select the
   topic in which you want to create a team.

#. At the bottom of the list of teams within the topic, select the **create a
   new team in this topic** link.

   .. image:: ../../shared/students/Images/Teams_CreateNewTeamLink.png
     :width: 500
     :alt: The "create a new team in this topic" link at the bottom of the page
           showing all teams in a topic

.. update this screenshot with new footer text

4. On the **Create a New Team** page, add a name and description for the team. 

   In the description, include details about the proposed project or activity
   to help learners to decide whether they want to join this team.

   .. image:: ../../shared/students/Images/Teams_CreateNewTeamForm.png
     :width: 500
     :alt: Empty form with fields to be completed when you create a new team.   

#. Optionally, add some characteristics for your team. You can specify a
   language that members would primarily use to communicate with each other,
   and a country that members would primarily identify with. Keep in mind that
   if your team details make the team membership seem too selective, learners
   might be discouraged from joining.

#. When you have finished entering details for the team, select **Create**.

   Your new team is added to the list of team under your selected topic.



.. _Search for a Team:

******************
Search for a Team
******************

Use the search field to find a team within a topic.

.. note:: Partial strings are not supported for searching teams.

To get a list of teams that match your search keywords, follow these steps.

#. From the **Teams** page in the LMS, select **Browse**, then select the
   topic in which you want to find a team.
   
#. In the search field, enter one or more keywords to search for, then press
   **Enter** or select the search icon.

   .. note:: Partial strings are not supported for searching teams.

.. add image   

   Teams within the topic that match your search are displayed. 

To clear the existing search term, select the **X** next to the search field,
or select all the text within the field and enter text to replace it.


.. _Edit a Team:

******************
Edit a Team
******************

As a course team member with the Staff, Admin, or Discussion Moderator role,
you can edit any of a team's details. You can also remove members from a
team. For more details about removing team members, see :ref:`Remove Learner
from Team`.

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

As a course team member with the Staff, Admin, or Discussion Moderator role,
you might need to remove one or more learners from a team. For example, if a
learner joined a team but is not participating, or has unenrolled from the
course without leaving the team, you should remove that learner so that the
place on the team is made available to other learners.

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
#. On the team's **Membership** page, select **Remove** next to the name of
   the learner who you want to remove from the team. 
#. In the confirmation message, select **Remove**. 
#. Repeat steps 9 and 10 to remove additional members.

   Updates to the team membership are reflected when you refresh the page. 


.. _Delete a Team:

******************
Delete a Team
******************

As a course team member with the Staff, Admin, or Discussion Moderator role,
you might need to manage the teams in your course, including deleting teams
that remain empty or are dysfunctional. 

When you delete a team, all learners are removed from the team membership, and
team discussions can no longer be accessed.

.. note:: Deleting a team removes it permanently from the course, and cannot
   be undone.


To delete a team, follow these steps.

#. In the LMS, select the **Teams** tab.
#. On the **Teams** page, select **Browse** to show all topics.
#. Select the arrow button for the topic to show all teams in that topic. 
#. Locate the team that you want to edit. To find the team, you can search
   using keywords or sort teams by last activity or open slots.
#. Select **View** for the team that you want to delete.
#. Select **Edit Team**. 
#. On the **Instructor Tools** bar, select **Delete Team**.
#. In the confirmation message, select **Delete**. 

   You are returned to the topic page where you are notified that the team has
   been successfully deleted. The team no longer appears in the teams list
   within its topic. Learners who were previously members of this team no
   longer belong to a team.

