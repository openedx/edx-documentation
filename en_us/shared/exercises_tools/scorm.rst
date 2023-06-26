.. _SCORM XBlock:

##################
SCORM
##################

.. note:: EdX offers full support for this tool.

This section describes how to include `SCORM <https://en.wikipedia.org/wiki/Sharable_Content_Object_Reference_Model>`_ content in your course.

.. contents::
  :local:
  :depth: 2

***********
Overview
***********

The SCORM XBlock provides the ability to display SCORM content within the Open edX LMS and Studio.
It can save a learners state and report scores to the progress tab of the course.
It currently supports SCORM 1.2 and SCORM 2004 standard.

**************************************************
Enable the SCORM XBlock
**************************************************

Before you can add SCORM content to your course, you must enable the SCORM XBlock.

To enable the SCORM XBlock in Studio, you add the ``"scorm"`` key to
the **Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

.. figure:: ../../../shared/images/AdvancedModuleListScorm.png
  :alt: Advanced Module List with "scorm" added.

**************************************************
Adding a SCORM component to a Unit
**************************************************

* In a unit where you want the SCORM content to display, click on the “Advanced” Icon.


.. figure:: ../../../shared/images/AddNewAdvancedComponent.png
  :alt: Add New Advanced Component



* Select ``Scorm module``


.. figure:: ../../../shared/images/AddScormModule.png
  :alt: Select Scorm module



* The SCORM module component will be added. Click on the **EDIT** button.


.. figure:: ../../../shared/images/ScormBlockStudio.png
  :alt: New SCORM Component in Studio


**************************************************
Uploading the SCORM content
**************************************************

.. figure:: ../../../shared/images/ScormStudioSettings.png
    :alt: Scorm Component settings in Studio



* Choose the SCORM .zip package you want to upload.
* If the SCORM content does not have any quizzes, set “Scored” to False.  
* If the "Scored" parameter is True, you must specify the weight of the quizzes' points.


.. note:: Only 1 SCORM component per Unit may be used. The component will be displayed under the **Units** title in the LMS. The Display Name is only used within Studio.


**************************************************
Technical information
**************************************************


There are 2 events a SCORM package can emit in order to communicate with the Open edX platform.

* For a SCORM module to set the Unit as complete (trigger the completion event of Open edX), the following event needs to be emitted: 
    ``scorm_set_values`` with the following key/name pair.

    * **name**: ``cmi.completion_status``
    * **value**: ``completed, incomplete, not attempted, unknown`` **(only 1)**
	
* For a SCORM module to send grading back to the Open edX platform, the following event need to be emitted: 
    ``scorm_set_values`` with the following key/name pair.

    * **name**: ``cmi.score.raw``
    * **value**: A number that reflects the performance of the learner relative to the range bounded by the values of min and max [e.g. if the quiz is out of 10, a number between 0 and 10. The maximum being the ``Weight`` you set in for the SCORM settings above.]
  