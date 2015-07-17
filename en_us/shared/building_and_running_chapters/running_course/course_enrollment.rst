.. _Enrollment:

##########################
Enrollment
##########################

The course creator, and course team members with the Staff and Admin roles, can
enroll learners in a course, see how many people are enrolled, and, when
necessary, unenroll learners on the Instructor Dashboard.

Learners can enroll themselves in a course during its defined enrollment
period. For a ``www.edx.org`` course, enrollment is publicly available to
anyone who registers an edX account. For other courses, such as those on
``edge.edx.org``, enrollment is limited to learners who know the course URL
and learners you explicitly enroll.

.. contents:: Section Contents:
  :local:
  :depth: 1

Data about course enrollment is also available from edX Insights. You access
Insights from the Instructor Dashboard for your live course: after you select
**Instructor**, follow the link in the banner at the top of each page. For more
information, see `Using edX Insights`_.

.. _registration_enrollment:

*********************************
Registration and Enrollment
*********************************

Before a learner can enroll in a course, he or she must complete these steps.

#. Register a user account, which includes supplying a valid email address, on
   ``www.edx.org``, ``edge.edx.org``, or your implementation of the edX
   platform. Each platform requires a separate user account.

#. Activate the registered account by following the emailed instructions.

As long as the course **Enrollment End Date** has not passed, learners who
have registered and activated user accounts can enroll themselves in
``www.edx.org`` courses, or can enroll in other courses if they know the URL.

Course creators, Admins, and Staff, however, can enroll learners in a course
either before or after the learners register their user accounts.

.. important:: To work on a course, every course team member must register and
 activate a user account and enroll.

.. _enroll_student:

*******************************************
Options for Enrolling Learners in a Course
*******************************************

You enroll learners, and other course team members, in your course by
supplying their email addresses. After the **Enrollment End Date** for a
course learners can no longer enroll themselves; however, you can still
explicitly enroll learners.

When you enroll people in a course you have these options:

* **Auto Enroll**. When you choose this option, the people who you enroll do
  not need to complete an explicit course enrollment step. Of the list of email
  addresses that you supply, those that correspond to a registered user account
  are immediately enrolled in the course, and your course displays on the
  **Current Courses** dashboard for those users on log in. Email addresses on
  the list that do not match a registered user account are enrolled as soon as
  that account is registered and activated.

  You can track the enrollment status of the learners who you auto enroll. For
  more information, see :ref:`view_not_yet_enrolled`.

  If you do not select **Auto Enroll**, the people who you enroll must also
  actively locate your course and enroll themselves in it. These learners see
  the course on their dashboards after they have done so.

* **Notify learners by email**. When you choose this option, an email message
  is automatically sent to each of the email addresses that you supply. The
  message includes the name of the course and, for learners who are not already
  enrolled, a reminder to use that same email address to enroll.

  An example of the email message that a learner received when this option was
  selected during enrollment follows. In this example, the learner already had
  a registered and activated edx.org account, and both **Auto Enroll** and
  **Notify students by email** were selected.

  .. image:: ../../../shared/building_and_running_chapters/Images/Course_Enrollment_Email.png
        :alt: Email message inviting a student to enroll in an edx.org course

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

4. To streamline the course enrollment process, leave **Auto Enroll** selected.

#. To send learners an email message, leave **Notify students by email**
   selected.

#. Select **Enroll**.

.. only:: Open_edX

   .. note:: If your course has a fee, and an organization wants to purchase 
    enrollment for multiple seats in your course at one time, you can create
    *enrollment codes* for the organization. The organization then distributes
    these enrollment codes to its learners to simplify the enrollment process.
    You can also create coupon codes to give learners a discount when they
    enroll in your course. For more information, see :ref:`Manage Course Fees`.

.. _view_enrollment_count:

***************************
View an Enrollment Count
***************************

After you create a course, you can access the total number of people who are
enrolled in it. When you view an enrollment count, note the following

* In addition to learners, the enrollment count includes all course team
  members, including Admins and Staff. (To work with a course in Studio, the
  LMS, or Insights, you must be enrolled in that course.)

* Learners can unenroll from courses, and course Admins and Staff can
  unenroll learners when necessary.

  **Note**: The enrollment count displays the number of currently enrolled
  learners and course team members. It is not a historical count of everyone
  who has ever enrolled in the course.

The total number of current enrollees is shown as the sum of the number of
people who selected each of the certification tracks (verified, professional,
or honor) that are available for your course.

To view the enrollment count for a course, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Course Info** if necessary. 

  The **Enrollment Information** section of the page that opens shows the
  number of people who are currently enrolled in your course and in each of the
  certification tracks.

You can also view or download a list of the people who are enrolled in the
course. See :ref:`Student Data`.

.. _view_not_yet_enrolled:

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
from re-enrolling, course enrollment must also be closed. You use Studio to
set the **Enrollment End Date** for the course to a date in the past. See
:ref:`Scheduling Your Course`.

**Note**: Unenrollment does not delete data for a learner. An unenrolled
learner's state remains in the database and is reinstated if the learner does
re-enroll.

To unenroll learners, you supply the email addresses of enrolled learners. 

#. View the live version of your course.

#. Select **Membership**. 

#. In the **Batch Enrollment** section of the page, enter a username or an
   email address, or multiple names or addresses separated by commas or new
   lines.

#. To send learners an email message, leave **Notify students by email**
   selected.

.. note:: The **Auto Enroll** option has no effect when you select
 **Unenroll**.

5. Select **Unenroll**. The course is no longer listed on the learners'
   **Current Courses** dashboards, and the learners can no longer contribute to
   discussions or the wiki or access the courseware.

.. _Using edX Insights: http://edx-insights.readthedocs.org/en/latest/
