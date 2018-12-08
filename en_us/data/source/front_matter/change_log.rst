.. _Change Log:

###########
Change Log
###########

The edX documentation team no longer maintains a change log for each guide. For
a weekly summary of platform changes, refer to the *EdX Release Notes* on the
`docs.edx.org`_ website.

For information about changes made to the edX documentation set, the
`edx-documentation`_ repository on GitHub provides a complete record.

.. include:: ../../../links/links.rst

**********************
October-December 2015
**********************

.. list-table::
   :widths: 20 70
   :header-rows: 1

   * - Date
     - Change
   * - 15 Dec 2015
     - Added descriptions of the :ref:`open response assessment<ORA2 Data>` and
       :ref:`course specific anonymized ID<student_anonymoususerid>` SQL tables
       that are now included in data packages.
   * -
     - Updated the :ref:`conventions<Conventions>` for SQL tables to reflect
       additional data cleaning steps now applied to most .sql output files.
   * - 14 Dec 2015
     - Corrected the events for :ref:`discussion forum<forum_events>` voting to
       include the ``category_id`` and ``category_name`` event member fields.
   * - 1 Dec 2015
     - Added new events for :ref:`discussion forum<forum_events>` voting to the
       Events in the Tracking Logs section.
   * -
     - Added new events for interactions with :ref:`Office Mixes<content>` to
       the Events in the Tracking Logs section.
   * -
     - Updated events in the :ref:`ora2` topic to reflect the addition of file
       types other than images.
   * - 23 Nov 2015
     - Updated the :ref:`Tracking Logs` section and the :ref:`event_list` to
       correct the names of several events.
   * - 10 Nov 2015
     - Corrected the description for the ``problem_show`` event in the
       :ref:`problem` section.
   * - 4 Nov 2015
     - Updates made throughout this guide to replace Python terminology
       (dictionary, integer, float) with JSON terminology (object, number)
       where appropriate.
   * - 27 Oct 2015
     - Added new events for interactions with :ref:`Oppia
       explorations<content>` to the Events in the Tracking Logs section.


**********************
July-September 2015
**********************

.. list-table::
   :widths: 20 70
   :header-rows: 1

   * - Date
     - Change
   * - 16 Sept 2015
     - Added new events for :ref:`teams<student_teams_events>` to the
       Events in the Tracking Logs section.
   * - 2 Sept 2015
     - Added new events for :ref:`digital certificates <certificate_events>`.
   * - 6 Aug 2015
     - Updated the :ref:`Package` section to include approximate sizes for
       the files in data packages.
   * - 8 Jul 2015
     - Added new events for :ref:`polls and surveys<Poll and Survey Events>` to
       the Events in the Tracking Logs section.
   * - 1 Jul 2015
     - Added new events for :ref:`problem hints<problem>` to the
       Events in the Tracking Logs section.


**********************
April-June 2015
**********************

.. list-table::
   :widths: 20 70
   :header-rows: 1

   * - Date
     - Change
   * - 10 Jun 2015
     - Added information about events for :ref:`pre-roll videos<pre-roll>` to
       the :ref:`Tracking Logs` section.
   * - 8 Jun 2015
     - Added descriptions of the ``video_show_cc_menu`` and
       ``video_hide_cc_menu`` events to the
       :ref:`video interaction events<video>` section.
   * - 19 May 15
     - Added information about new course team report events to the
       :ref:`Tracking Logs` section.
   * - 11 May 2015
     - Updated the descriptions of the ``pause_video``, ``play_video``, and
       ``stop_video`` :ref:`video interaction events<video>` to include the
       effects of a **Video Start Time** or **Video Stop Time**.
   * - 22 Apr 2015
     - Added information about the new ``student_languageproficiency`` table
       and two new columns in the ``auth_userprofile`` table to
       :ref:`Student_Info`.
   * - 6 Apr 2015
     - Added a section to describe the
       :ref:`course structure<course_structure>` file.


**********************
January-March 2015
**********************

.. list-table::
   :widths: 20 70
   :header-rows: 1

   * - Date
     - Change
   * - 18 Mar 2015
     - Added information about library events for students to the
       :ref:`Tracking Logs` section.
   * - 11 Mar 2015
     - Added information about additional video interaction events that are
       now emitted by the edX mobile app, and reorganized the :ref:`video` in
       the Tracking Logs section.
   * - 5 Mar 2015
     - Added new events for contributions to discussion forums to the
       :ref:`Tracking Logs` section.
   * -
     - Added events for the display of :ref:`Google components<content>` to the
       Tracking Logs section.
   * - 3 Mar 2015
     - Updated the :ref:`Preface` to include information about the :ref:`The
       edX Partner Portal` and the :ref:`The Open edX Portal`.
   * - 23 Feb 2015
     - Added new common fields for HTTP header values and new events for video
       caption use to the :ref:`Tracking Logs` section.
   * - 13 Feb 2015
     - Added the ``edx.course.enrollment.mode_changed`` event to the
       :ref:`Tracking Logs` section.
   * - 4 Feb 2015
     - Added information about the ``module.usage_key`` member field in the
       common ``context`` field to the :ref:`Tracking Logs` section.
   * - 16 Jan 2015
     - Added the :ref:`Institution_Data` section with information about the
       CSV file of student email preference settings.

**********************
October-December 2014
**********************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Date
     - Change
   * - 12/24/14
     - Added information about video events that the edX mobile app emits to
       the :ref:`Tracking Logs` section.
   * - 12/18/14
     - Updated descriptions of the video events in the
       :ref:`Tracking Logs` section.
   * - 11/26/14
     - Expanded the background information on content experiments in
       :ref:`AB_Event_Types`.
   * - 11/13/14
     - Updated the ``student_courseenrollment.mode`` description.
   * - 11/5/14
     - Corrected descriptions for ``play_video`` and ``pause_video`` in
       :ref:`video`.
   * - 10/28/14
     - Added best practices for passphrases to the
       :ref:`Getting_Credentials_Data_Czar` section.
   * - 10/23/14
     - Added examples of the format used to identify course components to the
       :ref:`Student_Info` and :ref:`Tracking Logs` sections.
   * -
     - Updated the ``child_render`` event to reflect the name change for the
       ``child_id`` member field. See :ref:`Tracking Logs`.
   * - 10/20/14
     - Updated the :ref:`Package` section to remove instructions for
       downloading weekly event files.
   * - 10/16/14
     - Updated video events with new fields relating to mobile device use in
       the :ref:`Tracking Logs` section.
   * - 10/07/14
     - Added new student and course team events relating to cohort use to the
       :ref:`Tracking Logs` section.
   * -
     - Removed information about XML course formats. See the :ref:`olx:edX Open
       Learning XML Guide` for information about building XML courses.


**********************
July-September 2014
**********************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Date
     - Change
   * - 09/30/14
     - Added information about the data that is available to course teams to
       the :ref:`Package` section.
   * - 09/18/14
     - Added descriptions of two columns added to the :ref:`auth_userprofile
       table<auth_userprofile>`.
   * - 09/08/14
     - Added cautions to the :ref:`Getting_Credentials_Data_Czar` section.
   * - 09/04/14
     - Updated the :ref:`Discussion Forums Data` section to include the
       ``thread_type`` field for CommentThreads and the ``endorsement`` field
       for Comments.
   * - 08/25/14
     - Removed information on course grading. See
       :ref:`partnercoursestaff:Grading Index` in *Building and
       Running an edX Course*.
   * -
     - Removed information on the XML for drag and drop. See
       :ref:`partnercoursestaff:Drag and Drop` in *Building and Running an edX
       Course*.
   * - 08/12/14
     - Added the :ref:`ora2` section to the :ref:`Tracking Logs` section.
   * - 08/01/14
     - Added the :ref:`Package` section with information to help data czars
       locate and download data package files.
   * - 07/10/14
     - Added the :ref:`Getting_Credentials_Data_Czar` section with information
       to help new data czars set up credentials for secure data transfers.


**********************
April-June 2014
**********************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Date
     - Change
   * - 06/27/14
     - Made a correction to the ``edx.forum.searched`` event name in the
       :ref:`Tracking Logs` section.
   * -
     - Added the ``stop_video`` event to the :ref:`Tracking Logs` section.
   * -
     - Updated the ``seek_video`` event in the :ref:`Tracking Logs` section.
   * - 06/23/14
     - Added a :ref:`Preface` with resources for course teams, developers,
       researchers, and students.
   * - 05/23/14
     - Added descriptions of the enrollment upgrade events to the
       :ref:`Tracking Logs` section.
   * - 05/22/14
     - Added descriptions of five video- and problem-related events to the
       :ref:`Tracking Logs` section.
   * -
     - Added the new ``edx.forum.searched`` event to the
       :ref:`Tracking Logs` section.
   * - 05/06/14
     - Added enrollment event types to the :ref:`Tracking Logs` section.
   * - 05/05/14
     - Removed information on the Poll module. See
       :ref:`partnercoursestaff:Poll` in *Building and Running an edX Course*.
   * -
     - Removed information on the Word Cloud tool. See
       :ref:`partnercoursestaff:Word Cloud` in *Building and Running an edX
       Course*.
   * -
     - Removed information on CustomResponse XML and Python Script. See
       :ref:`partnercoursestaff:Write Your Own Grader` in the  *Building and
       Running an edX Course* guide.
   * -
     - Removed information on Formula Equation Input. See
       `partnercoursestaff:Math Expression Input` in the *Building and Running
       an edX Course* guide.
   * - 04/29/14
     - Corrected misstatement on how :ref:`Discussion Forums Data` is sent in
       data packages.
   * - 04/25/14
     - Added new event types to the :ref:`Tracking Logs` section for
       interactions with PDF files.


**********************
January-March 2014
**********************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Date
     - Change
   * - 03/31/14
     - Added new fields for the server ``problem_check`` event type to the
       :ref:`Tracking Logs` section.
   * -
     - Reformatted the :ref:`Tracking Logs` section to improve readability.
   * - 03/28/14
     - Added the :ref:`Data_Czar` section.
   * - 03/24/14
     - Added the ``user_api_usercoursetag`` table to the :ref:`Student_Info`
       section and the ``assigned_user_to_partition`` and ``child_render``
       event types to the :ref:`Tracking Logs` section.
   * - 03/19/14
     - Provided alternative formatting for the examples in the :ref:`Discussion
       Forums Data` section.
   * - 03/13/14
     - Updated the :ref:`Student_Info` section.
   * - 02/24/14
     - Added descriptions of new fields to the :ref:`Wiki_Data` section.
   * - 02/21/14
     - Added descriptions of new fields to the :ref:`Discussion Forums Data`
       section.
   * - 02/14/14
     - Added the ``seek_video`` and ``speed_change_video`` event types to the
       :ref:`Tracking Logs` section.

.. include:: ../../../links/links.rst
