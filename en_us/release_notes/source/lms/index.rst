####################################
edX Learning Management System
####################################

******************
January 28, 2015
******************

* The first line of transcript files now appears for all videos. Previously,
  the first line did not appear if it contained a byte order mark. (TNL-935)

* Grade reports can now be generated successfully for all courses. Previously,
  an error caused grade reports to fail for courses with problem display names
  that contained Unicode characters. (TNL-1196)

==================
Coming Soon
==================

A new notes feature will soon be available in edx.org and edge.edx.org
courses. This feature will allow a learner to highlight text and make notes
while he progresses through the course. The learner will then be able to
review his notes in the course content or collected on a new **Notes** tab.

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