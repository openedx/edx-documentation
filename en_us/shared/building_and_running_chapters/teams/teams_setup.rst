.. _Teams Setup:

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

The topics you have created are shown in the LMS when learners browse teams by
topic.

.. image:: ../../../shared/building_and_running_chapters/Images/Teams_Topics_Created.png
 :width: 800
 :alt: A screen capture showing 3 topics on the Browse Teams page.

   

