.. _Enrollment:

##########################
Enrollment
##########################

Learners can enroll themselves in a course during its defined enrollment
period.

.. only:: Partners

  For a course running on `edx.org`_, enrollment is publicly available to
  anyone who registers an edX account. For other courses, such as those on
  `edx Edge`_, enrollment is limited to learners who know the course URL
  and learners you explicitly enroll.

The course creator and course team members with the Staff and Admin roles can
enroll learners in a course. These course team members can also unenroll
learners.

.. contents::
  :local:
  :depth: 1

.. Feature availability on the instructor dash applies to open edX installations only.
.. DOC-2218 A. Hodges 24 Aug 2015

.. only:: Open_edX

  Data about course enrollment is available in the LMS, by selecting
  **Instructor** to access the instructor dashboard and from Insights. For more
  information, see :ref:`Report Learners Not Yet Enrolled`.

.. Feature has been turned off for edx.org and Edge (the data is available in Insights instead).
.. DOC-2218 A. Hodges 24 Aug 2015

.. only:: Partners

  Data about course enrollment is available from edX Insights. You can access
  Insights for your course from the LMS: after you select **Instructor** to
  access the instructor dashboard, follow the link in the banner at the top of
  each page. For more information, see :ref:`insights:Using edX Insights`.

.. _registration_enrollment:

*********************************
Registration and Enrollment
*********************************

Before a learner can enroll in a course, he or she must complete these steps.

#. Register a user account, which includes supplying a valid email address, on
   ``www.edx.org``, ``edge.edx.org``, or your implementation of the edX
   platform. Each platform requires a separate user account.

#. Activate the registered account by following the emailed instructions.

As long as the course enrollment end date has not passed, learners who
have registered and activated user accounts can enroll themselves in
``www.edx.org`` courses, or can enroll in other courses if they know the URL.

Course creators, Admins, and Staff, however, can enroll learners in a course
either before or after the learners register their user accounts.

.. important:: Course team members are not automatically enrolled in courses,
   although they can access content in Studio, the LMS, and Insights. To work
   on a course, every course team member must register, activate a user
   account, and enroll in the course.

.. _enroll_student:

*******************************************
Options for Enrolling Learners in a Course
*******************************************

You enroll learners, and other course team members, in your course by
supplying their email addresses. After the enrollment end date for a
course learners can no longer enroll themselves. However, you can still
explicitly enroll learners.

.. note::
 When you enroll learners in a course, all learners are automatically enrolled
 in the audit enrollment track. For more information about course enrollment
 tracks, see :ref:`enrollment track<enrollment_track_g>`.

When you enroll people in a course, you have the following options.

* **Auto Enroll**. When you choose this option, the people who you enroll do
  not need to complete an explicit course enrollment step. Of the list of email
  addresses that you supply, those that correspond to a registered user account
  are immediately enrolled in the course, and your course displays on the
  **Current Courses** dashboard for those users on log in. Email addresses on
  the list that do not match a registered user account are enrolled as soon as
  that account is registered and activated.

  You can track the enrollment status of the learners who you auto enroll. For
  more information, see :ref:`Report Learners Not Yet Enrolled`.

  If you do not select **Auto Enroll**, the people who you enroll must also
  actively locate your course and enroll themselves in it. These learners see
  the course on their dashboards after they have done so.

* **Notify learners by email**. When you choose this option, an email message
  is automatically sent to each of the email addresses that you supply. The
  message includes the name of the course and, for learners who are not already
  enrolled, a reminder to use that same email address to enroll.

*********************************
Enroll Learners in a Course
*********************************

To enroll learners or course team members, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Membership**.

#. In the **Batch Enrollment** section of the page, enter the username or email
   address of the learner, or enter multiple names or addresses separated by
   commas or new lines.

   You can copy and paste data from a CSV file of email addresses. However,
   note that this feature is better suited to courses with smaller enrollments,
   rather than courses with massive enrollments.

#. For **Role of the users being enrolled**, select the role of the learner.

   * If the learner is a member of the course staff, select **Partner**.
   * If the learner is not a member of the course staff, select **Learner**.

   .. note::
    All of the users that you enroll at one time must have the same role. If
    you have some users who are partners and others who are learners, you must
    complete two batch enrollments.

#. In the **Enter the reason why the students are to be manually enrolled or
   unenrolled** field, enter a specific, detailed reason why you want to
   enroll these learners.

#. To streamline the course enrollment process, leave **Auto Enroll** selected.

#. To send learners an email message, leave **Notify students by email**
   selected.

#. Select **Enroll**.

You can view or download a list of the people who are enrolled in the course.
For more information, see :ref:`Student Data`.

.. note::
 When you enroll learners in a course, all learners are automatically enrolled
 in the audit enrollment track. For more information about course enrollment
 tracks, see :ref:`enrollment track<enrollment_track_g>`.

.. only:: Open_edX

  .. note:: If your course has a fee, and an organization wants to purchase
     enrollment for multiple seats in your course at one time, you can create
     enrollment codes for the organization. The organization then distributes
     these enrollment codes to its learners to simplify the enrollment process.
     You can also create coupon codes to give learners a discount when they
     enroll in your course. For more information, see :ref:`Enable
     and Create Enrollment Codes`.

  .. include:: ../../../shared/manage_live_course/Section_view_enrollment_count.rst


.. _Report Learners Not Yet Enrolled:

********************************
Report Learners Not Yet Enrolled
********************************

After you enroll learners in a course using the **Auto Enroll** option, any
learner who does not yet have a user account must register and activate an
account to complete the enrollment process. In addition, the learner must
register the account using the same email address that was used for auto
enrollment. You can download a report of auto enrolled email addresses that do
not yet correspond to an enrolled learner.

To download this report, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. In the **Reports** section of the page, select **Download a CSV of learners
   who can enroll**.

  A status message indicates that report generation is in progress. This
  process can take some time to complete, but you can navigate away from this
  page and do other work while it runs.

  To track the progress of the report process, reload the page in your browser
  and scroll down to the **Pending Tasks** section.

4. To open or save the report, select the
   ``{org}_{course_id}_may_enroll_info_{date}.csv`` file name at the bottom of
   the page.

.. _unenroll_student:

*********************************
Unenroll Learners from a Course
*********************************

You can remove learners from a course by unenrolling them. To prevent learners
from re-enrolling, course enrollment must also be closed. You use Studio to set
the **Enrollment End Date** for the course to a date in the past. For more
information, see :ref:`Scheduling Your Course`.

.. note:: Unenrollment does not delete data for a learner. An unenrolled
   learner's state remains in the database and is reinstated if the learner
   does re-enroll.

To unenroll learners, you supply the email addresses of enrolled learners.

#. View the live version of your course.

#. Select **Membership**.

#. In the **Batch Enrollment** section of the page, enter a username or an
   email address, or multiple names or addresses separated by commas or new
   lines.

#. In the **Enter the reason why the students are to be manually enrolled or
   unenrolled** field, enter a specific, detailed reason why you want to
   unenroll these learners.

#. To send learners an email message, leave **Notify students by email**
   selected.

   .. note:: The **Auto Enroll** option has no effect when you select
     **Unenroll**.

#. Select **Unenroll**. The course is no longer listed on the learners'
   **Current Courses** dashboards, and the learners can no longer access the
   course content or contribute to discussions or the wiki.

.. include:: ../../../links/links.rst
