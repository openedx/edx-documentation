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

Learners can create their own teams and use not only with names and
descriptions to identify them but also, optionally, a primary communication
language and a primary country that members identify with. Team
characteristics might serve as the basis for attracting new members, resulting
in small groups of learners with similar interests and goals who will work
together on projects within the same topic area.


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

#. To specify topics within which teams can be created, add entries under ``"topics"``. For each topic, provide a description, name, and ID as shown.  

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



