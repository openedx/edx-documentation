.. _SCORM XBlock:

##################
SCORM
##################

.. note:: EdX offers full support for this tool via edx.org. The SCORM XBlock is not supported on the edX mobile app.

This section describes how to include `SCORM <https://en.wikipedia.org/wiki/Sharable_Content_Object_Reference_Model>`_ content in your course.

.. contents::
  :local:
  :depth: 2

***********
Overview
***********

The SCORM `XBlock <https://edx.readthedocs.io/projects/xblock-tutorial/en/latest/overview/introduction.html>`_ provides the ability to display SCORM content within the Open edX LMS and Studio.
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

* In a unit where you want the SCORM content to display, click on the ``Advanced`` Icon.


.. figure:: ../../../shared/images/AddNewAdvancedComponent.png
  :alt: Add New Advanced Component



* Select ``Scorm module``


.. figure:: ../../../shared/images/AddScormModule.png
  :alt: Select Scorm module


* ``Scorm module`` selected

.. figure:: ../../../shared/images/AddScormModuleSelected.png
  :alt: Selected Scorm module


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


.. note:: * Only 1 SCORM component per Unit may be used.
          * The SCORM component will be displayed under the **Unit** title in the LMS.
          * The **Display Name** is only used within Studio.


**************************************************
SCORM Content best practise
**************************************************

To ensure the best experience for learners it is recommend that you keep your SCORM packages small. (1MB - 15MB)
A larger package has a longer load time and can cause a bad learner experience.

Following the rule of 1 SCORM component per unit, it is recommended that you break your content up into unit sized chunks.
This will help maintain the smaller package size.

Try to limit the SCORM package to 1 quiz or scored component.


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
  