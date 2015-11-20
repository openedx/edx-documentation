.. _Test Content Experiments:

##########################################
Test Content Experiments
##########################################

You should test content experiments in your course before the course starts, to
ensure that content is delivered to experiment groups as you intended.

When you view a unit that contains a content experiment in the LMS Staff view,
you can select one of the experiment groups from a drop-down list. The unit
page then shows the content as the selected group of learners sees it.

For example, in the following image, Group 0 is selected, and the HTML
component and video that is part of Group 0 is displayed.

.. The reason for conditionalizing the 2 images in this file is to get the to
.. render correctly in all guides. The OLX guide has a different number of file
.. levels than Partner and Open edX, so the relative path to the image cannot
.. work for all cases. You will see build errors were the build cannot find
.. images for the conditions that don't apply, but rendering in eacah guide is
.. correct. CT Nov 19 2015

.. only:: OLX

  .. image:: ../../../shared/images/a-b-test-lms-group-0.png
   :alt: An Image of a unit page in the LMS, with Group 0 selected.
   :width: 800


.. only:: Partners

  .. image:: ../../../../shared/images/a-b-test-lms-group-0.png
   :alt: An Image of a unit page in the LMS, with Group 0 selected.
   :width: 800


.. only:: Open_edX

  .. image:: ../../../../shared/images/a-b-test-lms-group-0.png
   :alt: An Image of a unit page in the LMS, with Group 0 selected.
   :width: 800


You can change the experiment group selection to view the content that a
different experiment group of learners sees.

.. only:: OLX

  .. image:: ../../../shared/images/a-b-test-lms-group-2.png
   :alt: An image of a unit page in the LMS, with Group 1 selected.
   :width: 800


.. only:: Partners

  .. image:: ../../../../shared/images/a-b-test-lms-group-2.png
   :alt: An image of a unit page in the LMS, with Group 1 selected.
   :width: 800


.. only:: Open edX

  .. image:: ../../../../shared/images/a-b-test-lms-group-2.png
   :alt: An image of a unit page in the LMS, with Group 1 selected.
   :width: 800


.. note:: The example course content in this section uses content experiment
 terminology ("Welcome to Group A", for example) to make the functionality
 clear. Typically, you would not use terminology in course content that would
 make learners aware of the experiment.
