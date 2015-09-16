.. _Enable Licensing:

####################################
Enabling Course and Video Licensing
####################################

This section describes how to enable licensing in your instance of Open edX.

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
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

*****************************
Enable Licensing in Studio
*****************************

#. In the edX Platform installation directory, edit the file
   ``/cms/envs/common.py``

#. In the ``FEATURES`` dictionary, add ``'LICENSING':True``:
   
   .. code-block:: bash

      FEATURES = {
          'LICENSING': True,
          . . .

#. Save the ``/cms/envs/common.py`` file.
   
**********************************************************
Enable Licensing in the Learning Management System
**********************************************************

#. In the edX Platform installation directory, edit the file
   ``/lms/envs/common.py``

#. In the ``FEATURES`` dictionary, add ``'LICENSING':True``:
   
   .. code-block:: bash

      FEATURES = {
          'LICENSING': True,
          . . .

#. Save the ``/lms/envs/common.py`` file.

.. include:: ../../../links/links.rst
