.. include:: ../links.rst

.. _Enable Course Search:

######################################################
Enable Course Search
######################################################

In the Open edX Birch release, a new feature allows learners to search
courseware. To enable this feature on your instance of Open edX, you must
enable both indexing and search.

You should enable course indexing before enabling search, so that the course is
indexed before learners can search course content.

For information about searching courseware, see the *Open edX Learner's* guide.

.. Note::  
  Before proceeding, review :ref:`Guidelines for Updating the edX Platform`.

*****************************
Enable Course Indexing
*****************************

To enable course indexing:

#. In the edX Platform installation directory, edit the file
   ``/cms/envs/common.py``

#. Set the value of ``ENABLE_COURSEWARE_INDEX`` to ``True``:
   
   .. code-block:: bash

      # Enable the courseware search functionality
      'ENABLE_COURSEWARE_INDEX': True,

#. Save the ``/cms/envs/common.py`` file.
   

**********************************************************
Enable Course Search in the Learning Management System
**********************************************************

To enable course search in the Learning Management System, after courses are
indexed:

#. In the edX Platform installation directory, edit the file
   ``/lms/envs/common.py``

#. Set the value of ``ENABLE_COURSEWARE_SEARCH`` to ``True``:
   
   .. code-block:: bash

      # Courseware search feature
      'ENABLE_COURSEWARE_SEARCH': True,

#. Save the ``/lms/envs/common.py`` file.

