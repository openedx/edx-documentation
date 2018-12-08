.. _EdX Learning Management System as an XBlock Runtime:

####################################################
EdX Learning Management System as an XBlock Runtime
####################################################

The edX Learning Management System (LMS) is the application in the edX Platform
that learners use to view and interact with courseware.

Because it presents XBlocks to learners and records their interactions, the LMS
is also an :ref:`XBlock runtime <XBlock Runtimes>` application.

As an XBlock developer, you must understand what XBlock properties the LMS
requires.

*****************************
LMS Requirements for XBlocks
*****************************

The LMS requires XBlocks to have the following properties.

* A :ref:`view method <View Methods>` named ``student_view``. This is the view that renders
  the XBlock in the LMS for learners to see and interact with. 

  In addition, the ``student_view`` method is used to render the XBlock in the
  Studio preview mode, unless the XBlock also has an ``author_view`` method.
  For more information, see :ref:`EdX Studio as an XBlock Runtime`.

* A class property named ``has_score`` with a value of ``True`` if the XBlock
  is to be graded.

* A method named ``get_progress`` that . . . TBD (
  x_module.py:XModuleMixin.get_progress)

* A class property named ``icon_class``, which controls the icon that is
  displayed to learners in the learning sequence header in courseware when the
  XBlock is in that unit.  The variable must have one of the following values.

  * ``problem``
  * ``video``
  * ``other``

.. include:: ../../../links/links.rst
