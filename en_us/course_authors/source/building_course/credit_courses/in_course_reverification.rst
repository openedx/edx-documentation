.. _In Course Reverification:

#################################
In-Course Reverification
#################################

To use ICRV, you must complete the following steps.

#. :ref:`Enable ICRV in your course <Enable ICRV>`.
#. :ref:`Create specific ICRV checkpoints <Create ICRV Checkpoint>`.

.. _Enable ICRV:

*********************************
Enable In-Course Reverification
*********************************

To enable ICRV for your course, follow these steps.

#. In Studio, select **Settings**, and then select **Advanced Settings**.
#. In the **Advanced Module List** field, place your cursor between the
   brackets (``[]``),and then add ``"edx-reverification-block"``. Make sure to
   include the quotation marks. 

   .. note:: If the **Advanced Module List** field already contains one or 
    more items, add a comma after the closing quotation mark for the last
    item, and then add ``"edx-reverification-block"``. The field should
    resemble the following example.

    ``"module_name","edx-reverification-block"``

.. _Create ICRV Checkpoint:

*******************************
Create an ICRV Checkpoint
*******************************

To create an ICRV checkpoint, follow these steps.

#. In the subsection for the assessment that requires ICRV, create a new unit.
#. In the unit, locate **Add New Component**, select **Advanced**, and then
   select **Reverification Checkpoint**.

   You can add more components to the unit that contains the reverification
   checkpoint. If you add more components, make sure that the reverification
   checkpoint is the first component in the unit.

#. In the reverification checkpoint component, select **Edit**.
#. In the component editor, locate **Associated Assessment**, and then type the
   display name of the subsection that contains assessment that you want to
   associate with the checkpoint. If you have not created the assessment yet,
   type the display name that the assessment will have.
#. In the **Verification Attempts** box, select the number of times that you
   want to allow learners to attempt to verify their identity. You can select
   up to three attempts.
#. Select **Save**.

After you create an ICRV checkpoint, the checkpoint appears in the list of
course credit requirements on the learner's **Progress** page.

.. image:: /Images/SFD_Credit_ReqList.png
 :width: 400
 :alt: The Progress page showing requirements for credit eligibility.

.. update image when sandbox ready (8/7: can't show anything but "Upcoming"
.. status)

.. image:: ../Images/
 :width: 500
 :alt: Learner's Progress page with a list of credit requirements below the
     progress graph.