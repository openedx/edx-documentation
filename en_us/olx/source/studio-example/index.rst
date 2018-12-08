.. _Example of OLX for a Studio Course:

##################################
Example of OLX for a Studio Course
##################################

You can export a course from edX Studio. When you export the course, you
download a .tar.gz file with the OLX (open learning XML) course content. You
can then extract the course OLX files for use with local tools or a source
control system such as GitHub.

As explained in this document, OLX provides for flexibility in how you
structure your course content.  However, edX Studio exports OLX content in a
specific structure.

This section documents the how edX Studio currently exports courses, so that
you can understand and manually navigate through the structure of exported
courses.

.. note::
  The format of Studio course exports is subject to change. As a result, any
  tools that you create specifically for the current Studio export format might
  not work for future versions. To avoid problems with manually authored OLX
  courses, we strongly recommend that you base any scripts that you create on
  the OLX format specification rather than on the current Studio export format.

In this section, we use a course that is part of the edX Platform, the `Manual
Testing`_ course, as an example of the OLX course exported from edX Studio. We
examine the overall structure of the `Manual Testing`_ course, as well as how
the courseware is defined.

The files for the `Manual Testing`_ course are stored in GitHub, so you can
explore how the course is structured for yourself.

For more information, see the following topics.

.. toctree::
   :maxdepth: 2

   manual-testing-structure

.. include:: ../../../links/links.rst
