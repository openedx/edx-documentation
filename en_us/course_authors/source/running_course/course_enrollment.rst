.. _Enrollment:

##########################
Enrollment
##########################

Course authors and instructors can enroll students in a course, see how many
people are enrolled, and, when necessary, unenroll students on the Instructor
Dashboard.

Students can enroll themselves in a course during its defined enrollment
period. For a ``www.edx.org`` course, enrollment is publicly available to
anyone who registers an edX account. For other courses, such as those on
``edge.edx.org``, enrollment is limited to students who know the course URL
and students you explicitly enroll.

* :ref:`registration_enrollment`

* :ref:`enroll_student`

* :ref:`view_enrollment_count`

* :ref:`unenroll_student`

Data about course enrollment is also available from edX Insights. You access
Insights from the Instructor Dashboard for your live course: after you click
**Instructor**, click the link in the banner at the top of each page. For more
information, see `Using edX Insights`_.

.. note:: Some courses have fees that are separate from the fees for an edX 
 verified certificate. If your course has a fee, organizations can purchase
 enrollment for students in your course directly from you. When an organization
 purchases enrollments in your course, you can create *enrollment codes* that
 you can provide to the organization. The organization then distributes these
 enrollment codes to its students to simplify the enrollment process. For more
 information, see :ref:`Paid Enrollment`.

 You must work with your edX program manager if you want to offer a course that
 has a fee.

.. _registration_enrollment:

*********************************
Registration and Enrollment
*********************************

Before a student can enroll in a course, he or she must:

#. Register a user account, which includes supplying a valid email address, on
   ``www.edx.org``, ``edge.edx.org``, or your implementation of the edX
   platform. Each platform requires a separate user account.

#. Activate the registered account by following the emailed instructions.

As long as the course **Enrollment End Date** has not passed, students who
have registered and activated user accounts can enroll themselves in
``www.edx.org`` courses, or can enroll in other courses if they know the URL.
For a more detailed description of this process from a student's point of
view, see :ref:`Sample Student Login Guide`.

Course authors and instructors, however, can enroll students in a course either
before or after the students register their user accounts.

To work on a course, all course staff members must also have registered and
activated user accounts and be enrolled in the course.

.. _enroll_student:

*********************************
Enroll Students in a Course
*********************************

You enroll students, and other course staff members, in your course by
supplying their email addresses. After the **Enrollment End Date** for a
course students can no longer enroll themselves; however, you can still
explicitly enroll students.

When you enroll people in a course you have these options:

* **Auto Enroll**. When you choose this option, the people who you enroll do
  not need to complete an explicit course enrollment step. Of the list of email
  addresses that you supply, those that correspond to a registered user account
  are immediately enrolled in the course, and your course displays on the
  **Current Courses** dashboard for those users on log in. Email addresses on
  the list that do not match a registered user account are enrolled as soon as
  that account is registered and activated.

  If you do not select **Auto Enroll**, the people who you enroll must also actively locate your course and enroll themselves in it. These students see the course on their dashboards after they have done so.

* **Notify students by email**. When you choose this option, an email message is
  automatically sent to each of the email addresses that you supply. The message
  includes the name of the course and, for students who are not already
  enrolled, a reminder to use that same email address to enroll.

  An example of the email message that a student received when this option was
  selected during enrollment follows. In this example, the student already had a
  registered and activated edx.org account, and both **Auto Enroll** and
  **Notify students by email** were selected.

  .. image:: ../Images/Course_Enrollment_Email.png
        :alt: Email message inviting a student to enroll in an edx.org course

To enroll students or staff members:

#. View the live version of your course.

#. Click **Instructor**, then click **Membership**. 

#. In the **Batch Enrollment** section of the page, enter the username or email
   address of the student, or enter multiple names or addresses separated by
   commas or new lines.

  You can copy and paste data from a CSV file of email addresses. However,
  note that this feature is better suited to courses with smaller enrollments,
  rather than courses with massive enrollments.

4. To streamline the course enrollment process, leave **Auto Enroll** selected.

#. To send students an email message, leave **Notify students by email**
   selected.

#. Click **Enroll**.

.. _Paid Enrollment:

==========================
Enrollment in Paid Courses
==========================

If your course has a fee, an organization might want to purchase enrollments in
your course. For example, if your course is a business training course, another
company may want some of its employees to enroll in your course. To allow the
organization to purchase multiple enrollments in one transaction, you create
*enrollment codes* for the enrollments that the organization purchases. You send
these codes to the organization, and the organization then distributes the codes
to learners. Each learner must use a separate code to enroll.

If your course is set up to offer enrollment codes, the Instructor Dashboard
includes an **E-Commerce** tab. On this tab, you create, view, and manage
enrollment code transactions.

.. note:: You must work with your edX program manager if you want to offer 
 a course that has a fee.

 To see the **E-Commerce** tab, you must have the Sales Admin or 
 Finance Admin role in your course. If you do not have one of these roles,
 contact your edX program manager.

For more information, see the following sections:

* :ref:`Create Enrollment Codes`
* :ref:`Download Enrollment Code Reports`
* :ref:`Manage Enrollment Code Transactions`

.. _Create Enrollment Codes:

Create Enrollment Codes
*********************************

.. note:: To create enrollment codes, you must have the **Sales Admin** role 
 in the course.

You create enrollment codes from the Instructor Dashboard. If your course offers
redeem codes, the Instructor Dashboard has an **E-Commerce** tab.

#. On the Instructor Dashboard, select the **E-Commerce** tab.
#. In the **Enrollment Codes** section, select **Create Enrollment Codes**.
#. When the **Create Enrollment Codes** form opens, complete the form. Items
   with an asterisk (*) are required.
#. At the bottom of the form, select **Create Enrollment Codes**.

When you select **Create Enrollment Codes**, the system automatically creates a
comma-separated values (.csv) file and downloads the .csv file to your computer.
In addition to information about your course and the transaction, such as the
invoice number, the .csv file contains course enrollment codes and URLs. Each
enrollment code has a separate URL, and only one student can use each enrollment
code.

The system also sends a confirmation email to the purchasing organization. The
email has two attachments: an invoice and a .csv file. The email instructs the
purchasing organization to distribute enrollment codes to students and includes
a template that the organization can use. The .csv file contains only the
enrollment codes and their associated URLs. It does not contain additional
information about your course or the transaction.

.. _Download Enrollment Code Reports:

Download Enrollment Code Reports
*********************************

To help you keep track of the enrollment codes that have been issued for your
course, you can download .csv files that contain reports of your unused
enrollment codes, your used enrollment codes, or all of your enrollment codes.
You must have the Finance Admin or Sales Admin role to download reports.

To download an enrollment code report, select the **E-Commerce** tab on the
Instructor Dashboard, and then select the report that you want in the
**Enrollment Codes** section.

.. _Manage Enrollment Code Transactions:

Manage Enrollment Code Transactions
************************************

In addition to the **Registration Codes** section, the **E-Commerce** tab has a
**Sales** section that you can use to view and manage enrollment code
transactions. You must have the Finance Admin role to see the **Sales** section
and manage these transactions.

In the **Sales** section, you can:

* View the total dollar amount that the course has received for all credit card
  transactions.
* Download a .csv file of all the invoices for enrollment codes. To do this,
  select **Download All Invoices**.
* Download a .csv file of all credit card transactions. To do this, select
  **Download Credit Card Transactions**.

.. _view_enrollment_count:

***************************
View an Enrollment Count
***************************

After you create a course, you can access the total number of people who are
enrolled in it. When you view an enrollment count, note that:

* In addition to students, the enrollment count includes the course author,
  course team members, instructors, and course staff. (To work with a
  course in Studio or the LMS, you must be enrolled in that course.)

* Students can unenroll from courses, and course authors and instructors can
  unenroll students when necessary.

  **Note**: The enrollment count displays the number of currently enrolled
  students and course team staff. It is not a historical count of everyone who
  has ever enrolled in the course.

The total number of current enrollees is shown as the sum of the number of
people who selected each of the certification tracks (verified, audit, or
honor) that are available for your course.

To view the enrollment count for a course:

#. View the live version of your course.

#. Click **Instructor**, then click **Course Info** if necessary. 

  The **Enrollment Information** section of the page that opens shows the
  number of people who are currently enrolled in your course and in each of the
  certification tracks.

You can also view or download a list of the people who are enrolled in the
course. See :ref:`Student Data`.

.. _unenroll_student:

*********************************
Unenroll Students from a Course
*********************************

You can remove students from a course by unenrolling them. To prevent students
from re-enrolling, course enrollment must also be closed. You use Studio to
set the **Enrollment End Date** for the course to a date in the past. See
:ref:`Set Important Dates for Your Course`.

**Note**: Unenrollment does not delete data for a student. An unenrolled
student's state remains in the database and is reinstated if the student does
re-enroll.

To unenroll students, you supply the email addresses of enrolled students. 

#. View the live version of your course.

#. Click **Membership**. 

#. In the **Batch Enrollment** section of the page, enter a username or an email
   address, or multiple names or addresses separated by commas or new lines.

#. To send students an email message, leave **Notify students by email**
   selected.

.. note:: The **Auto Enroll** option has no effect when you click **Unenroll**.

5. Click **Unenroll**. The course is no longer listed on the students'
   **Current Courses** dashboards, and the students can no longer contribute to
   discussions or the wiki or access the courseware.

.. _Provide Enrollment Codes:



.. _Using edX Insights: http://edx-insights.readthedocs.org/en/latest/