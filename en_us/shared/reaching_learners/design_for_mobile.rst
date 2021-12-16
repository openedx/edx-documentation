.. _Designing For a Mobile Experience:

###############################################
Designing Your Course For a Mobile Experience
###############################################

The percentage of learners who access MOOCs using smartphones is increasing
every day. Most courses on edx.org can be viewed on smartphones using the edX
Android and iPhone apps, although we still recommend that learners complete
graded assignments on a desktop computer, depending on the type of assessments
that their courses include. For information on which exercises and tools are
mobile-ready, see the table in the :ref:`Introduction to Exercises and
Tools<Create Exercises>` section.

To make the course experience for mobile learners as rewarding as it is for
learners using desktop computers, keep the following best practices in mind as
you design, test, and run your course.

* Course updates that you make might take longer to appear in the edX mobile
  apps than on the edX site. In particular, newly published content can take up
  to an hour to update on the Android app.

* Display names are critical for navigating through courses on smartphones. As
  you create course content, make sure you replace the default display names
  for every component with useful course component names.

* Keep display names and labels concise. Long display names and labels might
  wrap on smaller screens, or might not be easily viewable. For example, if
  several components have names that all start with the first five words and
  differ only after that, learners using smartphones to access your course
  might have difficulty distinguishing between components.

* Do not use Flash, which is not supported on mobile platforms, to create
  course content.

* Only use iFrames in course content where necessary, because iFrame content
  might not be responsive and cannot be optimized for viewing on a range of
  devices.

* If you develop course components in HTML, including course announcements, make
  sure you set relative rather than explicit sizes for objects such as images,
  tables, text, and so on, so that they will scale appropriately when viewed on
  displays of different sizes.

* Learners might be viewing your course materials on screens as large as a
  high-resolution Mac Thunderbolt display, or as small as a 5 inch smartphone
  screen, so it is difficult to size an image so that it displays well at all
  resolutions. In general, edX recommends keeping most images under 0.5MB in
  size so that learners who have low Internet bandwidth will not have trouble
  downloading the images. If you have a large image that requires zooming to
  view the full detail, in addition to providing an image that can be easily
  downloaded, link to a full resolution copy that can be opened separately
  from the course.

* When you make choices about the problem types to use for graded and ungraded
  assignments in your course, or which problem types to present in a single
  unit, keep the mobile experience in mind. Whenever possible, use mobile-
  ready assessment types. If you use assessment types that are not supported on
  smartphones, notify learners in the body of your course that they will not be
  able to complete assignments that contain unsupported assessment types using
  the edX iPhone and Android mobile apps.

* Timed and proctored exams cannot be completed using the mobile app.

* When learners access your course using the edX Android and iPhone apps, they
  progress from component to component by swiping through them. It might seem
  useful to include a Text component in a unit for the purpose of providing a
  demarcation point or guiding learners to the next unit, but having to swipe
  through too many "markers" with no real course content is not a good
  experience for mobile users.

* Make sure your JavaScript and CSS are compliant. You should verify that all
  components render correctly in the edX Android and iPhone apps as well as
  directly in the LMS.


.. _Testing Your Course For Mobile Devices:

**************************************
Testing Your Course For Mobile Devices
**************************************

If you have included some of the more complex problem types, or have highly
customized the way course content displays, edX recommends that you test your
course for multiple devices and displays.

To test the mobile experience of your course, sign in to your course using the
edX Android or iPhone app, and view each course unit to make sure that it
renders as you expect it to.

.. note:: Keep in mind that course updates that you make might not be
   immediately reflected in the edX mobile apps. In particular, newly
   published content can take up to an hour to update on the Android app.

