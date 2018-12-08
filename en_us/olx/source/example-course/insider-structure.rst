.. _The Structure of edX-Insider:

#############################
The Structure of edX-Insider
#############################

This topic describes the structure of the `edX-Insider`_ course.

.. contents::
  :local:
  :depth: 1

For information about how a generic OLX (open learning XML) course is
structured, see :ref:`OLX Directory Structure`.

For information about how a course exported from edX Studio is structured, see
:ref:`Example of OLX for a Studio Course`.

.. note::
  The structure and content of edX-Insider can change without corresponding
  updates being made to this reference guide.

******************************************
edX-Insider and Directory File Structures
******************************************

All files and subdirectories that comprise edX-Insider are stored in the
`Ongoing`_ directory in the edX-Insider Git repository.

.. Image:: ../Images/edx-insider-github.png
 :alt: The edX-Insider course in GitHub.

********************
Top-level Directory
********************

The `Ongoing`_ directory in the edX-Insider Git repository contains the
``course.xml`` file as well as XBlock and Platform directories.

* The `course.xml`_ file contains the XML for the courseware. All chapters and
  sequentials are defined in ``course.xml``.

* Most verticals are defined in ``course.xml``; two verticals are referenced in
  other files.

* The content of some HTML XBlocks is embedded within ``course.xml``; other
  HTML XBlocks are referenced in other files.

* Problems are referenced in other files.

For more information, see :ref:`The edX-Insider course.xml File`.

******************************
The HTML XBlock Directory
******************************

While some HTML content is embedded in ``course.xml``, many HTML XBlocks are
stored as separate files in the ``HTML`` directory.

==============================
Example of a Referenced XBlock
==============================

You can reference an XBlock from the ``course.xml`` file.

For example, in ``course.xml``, the first vertical in the courseware contains a
single HTML XBlock with the display name ``Week overview``, which references
``Week_overview`` in the ``url_name`` attribute:

.. code-block:: html

  <chapter display_name="Pedagogical Foundations: Constructive Learning"
      url_name="Week_2_Technology_enabled_constructive_learning">
      <sequential format="Learning Sequence" graded="true"
          display_name="Overview (go here first)"
          url_name="Overview_go_here_first">
          <vertical display_name="Week's overview" url_name="Week_s_overview">
              <html display_name="Week overview" filename="Week_overview"
                  url_name="Week_overview"/>

There is a file called ``Week_overview.html`` in the ``html`` directory that
contains the content for that HTML component. For detailed information, see the
`Week_overview.html`_ file in GitHub.

For a learner, that HTML component appears as the first unit of the course.

.. Image:: ../Images/Insider-first-image.png
 :alt: The HTML component as a learner sees it.


==============================
Example of an Inline XBlock
==============================

You can include XBlock content within the ``course.xml`` file. You can do
this for ease of reading and maintenance when you do not need to reuse the
content.

For example, in ``course.xml``, the sequential with the display name ``In-class
exercise`` contains embedded HTML content.

.. code-block:: html

  <sequential display_name="In-class exercise" url_name="in_class">
      <html display_name="Overview" url_name="overview">
          <p>In the on-line portion,
             we examined a way we used technology to allow efficient
             implementation of one theory from learning science – constructive
             learning – in edX. In designing the edX platform, we applied many
             such techniques. We took aspects of mastery learning, project-
             based learning, gamification and others. Other platforms have
             sophisticated techniques for targeting specific student
             misconceptions, enabling a range of student social experiences,
             assessing teacher performance, and hundreds of other research-
             based techniques. We would like to give you a chance to practice
             with designing software to enable good pedagogy.
          </p>
	      . . .
      </html>

For a student, that HTML component appears as a unit of the course in the same
way as a referenced HTML component does.

.. Image:: ../Images/Insider-first-exercise.png
 :alt: The HTML component as a student sees it.


********************
Platform Directories
********************

The edX-Insider course contains information in the course subdirectories as
described below.

====================
``about`` Directory
====================

The ``about`` directory contains the following files.

* ``overview.html``, which contains the content for the course overview page
  that students see in the the Learning Management System (LMS).

* ``short_description.html``, which contains the content for the course in the
  course list.

For more information, see :ref:`The Course About Pages`.

====================
``info`` Directory
====================

The ``info`` directory contains the following files.

* ``handouts.html``, which contains the content for the **Course Handouts**
  page in the course.

* ``updates.html``, which contains the course updates students see when opening
  a course.

=======================
``policies`` Directory
=======================

The ``policies`` directory contains the following files.

* ``assets.json``, which defines all files used in the course, such as images.

* A course directory named ``Ongoing``, which contains:

  * ``grading_policy.json``, which defines how student work is graded in the
    course.

  * ``policy.json``, which defines various settings in the course.

For more information, see :ref:`Course Policies`.

====================
``static`` Directory
====================

The ``static`` directory contains the files used in the course, such as images
or PDFs.

For more information, see :ref:`Course Assets`.

=======================
``vertical`` Directory
=======================

The ``vertical`` directory contains the XML for two verticals used in the
course.

* ``constructive_ora_exercise.xml``
* ``in_class_ora.xml``

You can embed verticals in the ``course.xml`` file, and this is usually the
most straightforward option. However, with OLX, you can also store XML for
verticals in separate files in the ``vertical`` directory.

In this case, verticals for open response assessments are stored in their own
files.

The vertical files are referenced in ``course.xml`` as follows:

.. code-block:: html

  <vertical url_name="constructive_ora_exercise"></vertical>

And:

.. code-block:: html

  <vertical url_name="in_class_ora"></vertical>


.. include:: ../../../links/links.rst
