####################################
edX Studio
####################################

.. ******************
.. April 15, 2015
.. ******************

.. The video component **Advanced Settings** page includes a renamed field, 
.. **Video ID**. Previously, this field was named **EdX Video ID**.

.. For more information, see `Working with Video Components`_.

******************
March 25, 2015
******************

Cohort creation and management has moved from the **Advanced Settings** page in
Studio. Course teams can now use the new **Cohorts** tab on the Instructor
Dashboard in the LMS to add and rename cohorts, change a cohort's assignment
method, associate cohorts with content groups, and specify whether course-wide
and content-specific discussions are divided by cohort.

For more information, see `Cohorts`_.


******************
March 18, 2015
******************

* Course teams can now include a new type of component, a randomized content
  block, in their courses. These components randomly draw problems from a
  predefined library of components and present them to learners.

  You create and maintain libraries of components separately from courses. All
  of an organization's course teams can work collaboratively to develop the
  problems that the libraries contain. Each library can then be referenced by
  randomized content blocks in any of that organization's courses. For more
  information, see `Working with Libraries`_.

* Open response assessments can now include more than one prompt or
  question. A single rubric is used to grade all of the prompts in the
  assessment. For more information, see `Creating Peer Assessments`_.

* When you add an HTML component to a course outline and select the Full
  Screen Image Tool, IFrame Tool, or Zooming Image Tool, revised example
  templates now appear. The descriptions and procedures in the
  templates now include additional detail, including how to provide 
  accessible labels for your learners.

* A problem with the file locking feature on the **Files & Uploads** page is
  now resolved. To lock a file, click the lock icon that appears near it.
  (TNL-1461)

******************
March 11, 2015
******************

============================
Accessibility Improvements 
============================

* The **Schedule & Details**, **Group Configurations**, **Advanced Settings**,
  and **Grading** pages now include ``aria-label`` attributes. (TNL-1532)

* All navigation elements in Studio now have ``aria-label`` attributes. The
  ``aria-label`` attributes give these elements accessible labels, which make
  navigation regions easier to identify and navigate to. (TNL-1531, TNL-1520,
  TNL-1523)

******************
March 5, 2015
******************

Course teams can now include Google Drive files and calendars in courseware by
creating a link to the file or calendar in Studio. For more information, see
`Google Drive Files Tool`_ and `Google Calendar Tool`_.

******************
March 2, 2015
******************

* When course teams work with content groups on the **Group Configurations** page,
  they can now see which units in the course use a content group, and can link
  directly to those units from content group details. Course teams can now also
  delete content groups that are not in use in a course. See `Creating Cohort
  Specific Courseware`_ for more details.

* Previously, if a dropdown problem that was created with variables was
  answered, the chosen answer was not retained in the selection input. This
  problem has been fixed. (TNL-1419)
  
* Some issues with MATLAB problems were resolved. (TNL-1459)  


******************
February 12, 2015
******************

* A new video appears as the default video when you add a Video component.

******************
February 4, 2015
******************

* Previously, you received an error when opening the **Settings & Details** page in
  French. This problem is resolved. (TNL-1237)

******************
January 28, 2015
******************

* If you include cohorts in your course, you can now assign different course
  content to different cohorts. See `Creating Cohort Specific Courseware`_ for
  more details.

* All courses created after 14 Jan 2015 now use the `key introspection API`_
  format for internal course identifiers and the course URL. An example of the
  new URL format is:
  ``http://www.edx.org/courses/course-v1:edX+DemoX+Demo_2014/info``.

* MathJax, which Studio and the LMS use to render text as "beautiful math", is
  now upgraded to version 2.4 from version 2.2. For more information, see the
  descriptions of `MathJax 2.4`_ and `MathJax 2.3`_. (OSPR-21)

* When you create a new course in Studio, edit checks now identify special
  characters in the **Organization**, **Course Number**, or **Course Run**
  fields. An error message appears to prevent entry of spaces or characters
  such as ``!``, ``'``, ``(``, or ``)``. (SOL-233)

* For LTI components, you can now set the new **Accept grade past deadline**
  setting to True or False. The default for this setting is True. Previously,
  grading always included learner submissions that were submitted after the
  subsection due date. (TNL-805)


*****************
January 14, 2015
*****************

When you made multiple attempts to log in to edX Studio with the wrong
password, the error message was not refreshed and there was no indication of
the problem on subsequent attempts. This problem is resolved. (TNL-140)

***************
January 8, 2015
***************

* When a component with multiple parents had a draft version, you received an
  error when trying to export the course. This problem is resolved. (PLAT-332)

* You can now use a new advanced setting,
  ``always_cohort_inline_discussions``, to control whether content-specific
  discussion topics are unified or divided by cohort.  See 
  `Make All Content-Specific Discussion Topics Unified by Default`_ for 
  more information.

* The inline help for the **Discussion Topic Mapping** advanced setting is
  updated to note that discussion IDs must be unique. (TNL-752)

.. include:: ../links.rst