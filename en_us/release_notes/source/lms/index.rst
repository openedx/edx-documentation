####################################
edX Learning Management System
####################################

******************
February 12, 2015
******************

* In grade reports, the name of the "Group Configuration Group Name" column has
  changed to "Experiment Group." (TNL-1244)

* In the **Help** menu on the left side of the LMS, the X button to close the
  **Report a Problem** option did not work. This problem has been resolved.
  (TNL-1336)

* Students who enroll in the verified certificate track for a course, but do not
  verify their identity before the verification deadline, now receive a
  "Verification Deadline Has Passed" message in the browser when they try to
  verify their identity. Previously, students who missed the verification
  deadline saw a "Page Not Found" error message in the browser. (ECOM-1045)

* In courses that have cohort-specific content, the **Generate Grade Report** option on
  the **Data Download** tab of the Instructor Dashboard sometimes did not create
  a grade report. This problem has been resolved. (TNL-1351)

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