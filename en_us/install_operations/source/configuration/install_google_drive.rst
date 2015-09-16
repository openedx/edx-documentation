.. _Add the Google Drive and Google Calendar XBlock:

######################################################
Adding the Google Drive and Google Calendar XBlock
######################################################

In the Open edX Birch release, course teams can embed Google calendars and
Google Drive files in courseware.

To enable this feature on your instance of Open edX, you install the `Google Drive XBlock`_.

For information about using Google calendars and Google Drive files in courses,
see the *Building and Running an Open edX Course* guide.

.. Note::  
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

To install the Google Drive XBlock, follow these steps.

#. In the edX Platform installation directory, edit the file
   ``requirements/edx/github.txt``

#. Add a line to include the XBlock utilities.

   .. code-block:: bash

     git+https://github.com/edx-solutions/xblock-
     utils.git@349d6e05dbd553e1f18d3ad1f7ca02c0497f39d7#egg=xblock-utils

#. Add a line to add the Google Drive XBlock.
   
   .. code-block:: bash

     git+https://github.com/edx-solutions/xblock-google-drive.
     git@138e6fa0bf3a2013e904a085b9fed77dab7f3f21#egg=xblock-google-drive

#. Save the ``requirements/edx/github.txt`` file.

After you configure the edX Platform, to use Google Drive files or a Google
Calendar in a course, you must add the XBlock to the advanced settings for the
course. See the following documentation:

* :ref:`opencoursestaff:Enable Google Drive Files in edX Studio`
* :ref:`opencoursestaff:Enable Google Calendars in the Course`

.. include:: ../../../links/links.rst
