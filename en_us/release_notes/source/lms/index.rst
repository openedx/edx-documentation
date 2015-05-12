####################################
edX Learning Management System
####################################

*********************
May 12, 2015
*********************

=================================
Enhancements to the Grade Report
=================================

The grade report now includes new columns with certificate status and
enrollment track information. When course teams generate the grade report from
the instructor dashboard, they can see the following additional information
for each learner.
 
* Enrollment track: honor, verified, or professional education.
* Verification status, to identify learners in the verified or professional
  track who have completed identity verification with edX.
* Certificate eligibility status, to identify learners who have earned the
  passing grade in the course at the time of the grade report generation.
* Certificate delivery status, to identify learners who have received their
  certificates.
* The type of certificate, for learners who are eligible to receive a
  certificate.

For more information, see `Interpret the Grade Report`_.

=================================
Accessibility Improvements
=================================

This release includes accessibility improvements for learners who use a
keyboard or screen reader to access the LMS.

* The **My Profile** page now offers improved accessibility for learners who
  want to add or change their profile images. (TNL-2051)

* Several problems with numerical input problem types are now corrected.
  (TNL-1677)

  * The current status of the problem is now conveyed to screen reader
    users properly.
  * The workflow for checking how ASCII math is converted to MathML or MathJax
    format has been streamlined for screen reader users.
  * Nonessential information is no longer included in ``aria-live`` regions,
    which improves the experience for screen reader users.

* Improvements to the accessibility of discussion posts to screen reader users
  are included in this release. (AC-102)

*********************
May 5, 2015
*********************

* A problem in which some learners could not select **Change Email** to change
  their email addresses in Chrome has been fixed. (TNL-1745)

* A problem that prevented navigation buttons from appearing correctly on
  Windows computers in high-contrast mode has been fixed. (AC-36)

******************
April 28, 2015
******************

* Several updates were made in the LMS to support right-to-left languages. In
  right-to-left languages, the header on the **Course Info page** is now right-
  justified, courseware errors are properly reversed, and the Due icon is
  properly aligned. (UX-1632, UX-1634, UX-1724)

* A problem with linking to other units in the same subsection was fixed.
  (TNL-1844)

******************
April 22, 2015
******************

================
Profiles 
================

Learners and staff can now introduce themselves to the edX community through
personal profiles. A profile can include an image, a personal introduction,
and other information. Learners can access each others' profiles from within
course discussions.

Learners and staff can also use the new **Account Settings** page to update
account information, such as the account email address and password, and
demographic information, such as level of education and country or region. For
more information, see the `Exploring Your Dashboard, Settings, and Profile`_
section of the `EdX Guide for Students`_.

==========================
Video Start and Stop Times
==========================

If course teams define either one or both of the **Video Start Time** and
**Video Stop Time** values, learners no longer have the option to override
those values and watch the entire video file. Only the segment of the video
file that is delimited by your specified start and stop times plays.

.. note:: The **Video Start Time** and **Video Stop Time** values do not apply
   to videos that are downloaded or viewed using the native mobile app.
   Learners who use the mobile app can play the entire video file.

For more information, see `Video Advanced Options`_.

============================
Accessibility Improvements 
============================

In addition to some minor changes to enhance accessibility in the LMS and
Studio, the following changes were made.

* HTML ``iframe`` elements now show meaningful title attributes that describe
  the content embedded in the IFrame. (TNL-1675)

* The main blue colors used throughout the LMS user interface and on `edx.org`_
  were changed to meet WCAG AA guidelines for contrast. (UX-1810)


******************
March 31, 2015
******************

============================
Accessibility Improvements 
============================

* The LMS now includes a aria-live region to contain HTML for problems.
  Submission buttons have been removed from the aria-live ``div`` scope.
  (TNL-1699)

* Several accessibility fixes have been implemented in the course header.
  (ECOM-1233)

* An aria label has been added to the LMS footer. (ECOM-803)


******************
March 25, 2015
******************

Cohort creation and management has moved from the **Advanced Settings** page
in Studio to the Instructor Dashboard in the LMS. Course teams can use the new
**Cohorts** tab there to add and rename cohorts, change a cohort's assignment
method, associate cohorts with content groups, and specify whether course-wide
and content-specific discussions are divided by cohort.

For more information, see `Cohorts`_.


******************
March 11, 2015
******************

============================
Accessibility Improvements 
============================

* The main region in the Student dashboard now includes the `role` and `aria-
  label` attributes. (TNL-1567)

* Navigation controls in the LMS now have `aria-label` attributes. (TNL-1554)

******************
March 5, 2015
******************

* Course teams can now include Google Drive files and calendars in courseware.
  For more information, see `Embedded Google Files and Calendars`_.

* Several accessibility improvements have made navigating course content
  easier for screen readers.

******************
March 2, 2015
******************

When creating problems using XML, authors can now use HTML tags to add inline
markers that show additional information. Users see the additional text when
they hover their cursors over, or move keyboard focus to, markers in the problem
text. This feature includes enhanced support for screen reader users. (OSPR-353)

******************
February 12, 2015
******************

* In grade reports, the name of the "Group Configuration Group Name" column has
  changed to "Experiment Group." (TNL-1244)

* In the **Help** menu on the left side of the LMS, the X button to close the
  **Report a Problem** option did not work. This problem has been resolved.
  (TNL-1336)

* Students who enroll in the verified certificate track for a course, but do
  not verify their identity before the verification deadline, now receive a
  "Verification Deadline Has Passed" message in the browser when they try to
  verify their identity. Previously, students who missed the verification
  deadline saw a "Page Not Found" error message in the browser. (ECOM-1045)

* In courses that have cohort-specific content, the **Generate Grade Report**
  option on the **Data Download** tab of the Instructor Dashboard sometimes did
  not create a grade report. This problem has been resolved. (TNL-1351)

* In Safari, videos sometimes did not play at the selected speed. This problem
  has been resolved. (TNL-408)

******************
February 4, 2015
******************

  
* The first line of a Chinese video transcript was not visible. This problem is
  resolved. (TNL-935)

============================
Accessibility Improvements 
============================ 

* Focus now changes directly to the content area after the user selects a link
  to a new subsection or unit. (UX-1573)

* Unit navigation links are reorganized into a single list. The arrow
  navigation is converted from links to buttons and now includes the disabled
  attribute when appropriate. (UX-1572)

* Labels to bypass blocks now use the industry standard text **Skip to main
  content**. (TNL-1264)


******************
January 28, 2015
******************

* The first line of transcript files now appears for all videos. Previously,
  the first line did not appear if it contained a byte order mark. (TNL-935)

* Grade reports can now be generated successfully for all courses. Previously,
  an error caused grade reports to fail for courses with problem display names
  that contained Unicode characters. (TNL-1196)


****************
January 14, 2015
****************

* The grade report available in the Instructor Dashboard now includes columns
  for the content experiment groups and cohorts to which students belong.
  (TNL-498)

* When a pagination button is visually disabled, the button is now also
  disabled for screen readers. (TNL-997)

* When students checked their answers to a custom response problem with 10 or
  more inputs, the responses were not sorted correctly. This problem is
  resolved. (TNL-952)

* For numerical response problems, if the tolerance was set to greater than
  0.1, answers that varied from the correct answer by an amount equal to the
  tolerance were marked incorrect; that is, the correct answer was no inclusive of the tolerance setting. This problem is resolved. (TNL-904)

****************
January 8, 2015
****************

* In the Instructor Dashboard, when you unenrolled a student who enrolled in
  the Verified track, if that student was re-enrolled, he or she was
  automatically placed in the Verified track.  This problem is fixed; the
  student is no longer automatically enrolled in the Verified track. (ECOM-776)

* The Student Dashboard is updated to provide a visual indication of
  professional education courses the student is enrolled in. (ECOM-728)

.. include:: ../links.rst