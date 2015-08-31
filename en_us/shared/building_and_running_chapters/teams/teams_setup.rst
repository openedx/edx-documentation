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

Using teams in your course enables learners to interact and collaborate in
small groups around topics that you create.

After browsing topics, learners can join a team or create their own team
within a topic. When learners create a new team, they add names and
descriptions to identify them but also, optionally, a primary communication
language and a primary country that members identify with. Team
characteristics might serve as the basis for attracting new members, resulting
in small groups of learners with similar interests and goals who will work
together on projects or activities within the same topic area.



*******************************
Enabling and Configuring Teams
*******************************

To enable teams in your course, follow these steps.

.. note:: The Teams page in the LMS becomes available when you have specified
   at least one topic for teams in your course.

#. In Studio, from the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, select **Show Deprecated Settings**,
   then locate the **Teams Configuration** policy key.

 .. Remove deprecated settings limitation in future

3. Within this policy key you define two entries, topics and maximum team size.

#. To specify the maximum team size for teams in your course, enter the
   ``max_team_size`` parameter in double quotation marks, a colon, then the
   value. For example, to set the maximum number of learners per team in your
   course to 5, your entry would be:

   ``"max_team_size": 5``

#. To specify topics within which teams can be created, add entries under
   ``"topics"``. For each topic, provide a description, name, and ID as shown in the example.

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
learners browse teams by topic.

.. image:: ../../../shared/building_and_running_chapters/Images/Teams_Topics_Created.png
 :width: 800
 :alt: A screen capture showing 3 topics on the Browse Teams page.


.. _Create a Team:

******************
Create a Team
******************

As a course team member with the Staff, Admin, or Discussion Moderator role,
you can create a new team.

To create a new team, follow these steps.

#. In the LMS, select the **Teams** tab.

#. On the **Teams** page, select **Browse**, then select the topic in which
   you want to create a team.




.. _Search for a Team:

******************
Search for a Team
******************

Use the search field within a topic to find an existing team in that topic.

#. In the LMS, select the **Teams** tab.

#. On the **Teams** page, select **Browse**, then select the topic in which
   you want to find a team.
   
#. In the search field, enter one or more keywords to search for within a
   team's description and title, then press **Enter** or the search icon.

   .. note:: Partial strings are not supported for searching teams.

   Teams within the topic that match your search are displayed. 

To clear the existing search term, select the **X** next to the search field
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
   members so that they are aware of the changes you will make, and their
   impacts.

#. In the LMS, select the **Teams** tab.
#. On the **Teams** page, select the topic that the team is in, then locate the team.
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
#. On the **Teams** page, select the topic that the team is in, then locate
   the team.
#. Select **View** for the team that you want to edit.
#. Select **Edit Team**. 
#. In the **Instructor Tools** bar, select **Edit Membership**.
#. On the team's **Membership** page, select **Remove** next to the name of
   the learner who you want to remove from the team.
#. Confirmation or update step??


.. _Delete a Team:

******************
Delete a Team
******************

As a course team member with the Staff, Admin, or Discussion Moderator role,
you might need to manage the teams in your course, including deleting teams
that remain empty or are dysfunctional. Deleting a team removes all learners
from the team membership, and removes the team from the teams listing view
within a topic.

#. In the LMS, select the **Teams** tab.
#. On the **Teams** page, select the topic that the team is in, then locate
   the team.
#. Select **View** for the team that you want to edit.
#. Select **Edit Team**. 
#. In the **Instructor Tools** bar, select **Delete Team**.
#. In the confirmation message, select **OK**. ..To be confirmed.

   The team no longer appears in the teams list within its topic, and learner
   who were previously members of this team no longer belong to a team.

