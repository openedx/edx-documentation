.. _Adding Tooltips to a Problem:

==============================
Adding Tooltips to a Problem
==============================

You can add inline tooltips to a problem, so that learners can hover over the
tooltip icon and see text that you write to help them understand the problem.

For example, in the following problem the learner hovers over the tooltip icon
to see a definition for the acronym "ROI":

.. image:: ../../../shared/building_and_running_chapters/Images/tooltip.png
 :alt: An example of a tooltip from a learner's point of view.

.. note:: 
  For learners using a screen reader, the tooltip expands to show the tooltip
  text when the screen reader focuses on the tooltip icon.

To add the tooltip, you wrap text that you want to appear as the tooltip in the
``clarification`` element.  For example, the following problem contains two
tooltips:

.. code-block:: xml

  <problem>
      <text>
          <p>Given the data in Table 7 <clarification>Table 7: "Example PV 
            Installation Costs", Page 171 of Roberts textbook</clarification>, 
            compute the ROI <clarification><strong>ROI</strong>: Return on 
            Investment</clarification> over 20 years.
          </p>
       . . .                    
