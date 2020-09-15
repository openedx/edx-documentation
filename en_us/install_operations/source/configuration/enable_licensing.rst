.. _Enable Licensing:

####################################
Enabling Course and Video Licensing
####################################

This topic describes how to enable licensing in your instance of Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Course teams can specify licensing options for course content as well as for
each video in a course.

Course teams can select one of the following license options.

* All Rights Reserved
* Creative Commons

By specifying the license, course teams communicate to learners whether and how
they can reuse course content.

To enable this feature on your instance of Open edX, you must enable licensing
in both Studio and the Learning Management System.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

*****************************
Enable Licensing in Studio
*****************************

To enable licensing, you modify the ``lms.yml`` and ``studio.yaml``
files, which are located one level above the ``edx-platform`` directory.

#. In the ``lms.yml`` and ``studio.yaml`` files, in the ``FEATURES``
   dictionary, add ``'LICENSING':True``:

   .. code-block:: none

      FEATURES = {
          'LICENSING': True,
          . . .

#. Save the ``lms.yml`` and ``studio.yaml`` files.

.. include:: ../../../links/links.rst
