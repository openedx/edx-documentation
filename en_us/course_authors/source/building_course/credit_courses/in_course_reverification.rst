.. _In Course Reverification:

#################################
In-Course Reverification
#################################

To use in-course reverification, you must enable reverification in your
course, and then create specific verification checkpoints. Learners who must
complete identity reverification see these checkpoints on their **Progress**
pages and in the courseware.

.. contents:: 
 :local:
 :depth: 1

.. _Enable ICRV:

*********************************
Enable In-Course Reverification
*********************************

To enable in-course reverification for your course, follow these steps.

#. In Studio, select **Settings**, and then select **Advanced Settings**.
#. In the **Advanced Module List** field, place your cursor between the
   brackets (``[]``),and then add ``"edx-reverification-block"``. Make sure to
   include the quotation marks. 

   .. note:: If the **Advanced Module List** field already contains one or 
    more items, add a comma after the closing quotation mark for the last
    item, and then add ``"edx-reverification-block"``. The field should
    resemble the following example.

    ``["module_name","edx-reverification-block"]``

#. At the bottom of the page, select **Save Changes**.

.. _Create ICRV Checkpoint:

*************************************************
Create an In-Course Verification Checkpoint
*************************************************

Creating an in-course verification checkpoint has two steps.

#. :ref:`Create a verification checkpoint component <Create Checkpoint
   Component>`.
#. :ref:`Modify the settings of the components and units <Modify Settings>`
   that are behind the checkpoint.

 .. _Create Checkpoint Component:

================================================
Create a Verification Checkpoint Component
================================================

#. In the subsection that contains the assessment, create a new unit.

   If the subsection already contains one or more units, move the new unit so
   that it is the first unit in the subsection.

#. In the new unit, select **Advanced** under **Add New Component**, select
   **Verification Checkpoint**, and then select **Edit**.

#. In the **Verification Checkpoint Name** box, enter a name for the
   verification checkpoint.

#. In the **Verification Attempts** box, select the number of times that
   learners can attempt to verify their identities. You can specify up to
   three attempts.

The unit that contains the verification checkpoint component can contain other
components. If the unit contains other components, edX recommends that you
position the verification checkpoint as the first component in the unit.

.. _Modify Settings:

================================================
Modify Component and Unit Settings
================================================

After you create a verification checkpoint, that checkpoint appears in the
settings for all components and units in the course.

.. add image when sandbox ready (8/19: waiting for new sandbox)

.. image  
..  :width: 500
..  :alt: Image of the settings editor for a component and for a unit

To prevent learners from seeing components and units before they pass the
verification checkpoint, you must select that verification checkpoint in the
settings for each component and unit in the subsection that you do not want
learners to see.

Change Component Settings
**************************

.. note:: If you do not change the settings for a component, that component 
 is visible before the learner passes the checkpoint.

If the unit that contains the verification checkpoint contains one or more
additional components, follow these steps for each component.

#. On the unit page, locate the component that you want, and then select
   **Visibility Settings** for that component. The **Visibility Settings**
   control resembles an eye.

#. Under **Make visible to**, select **Specific Content Groups**, and then
   select the verification checkpoint that you want.

Change Unit Settings
***********************

.. note:: If you do not change the settings for a unit, that unit is 
 visible before the learner passes the checkpoint.

#. On the **Course Outline** page, locate the unit that you want, and then
   select **Configure** for that unit. The **Configure** control resembles a
   gear.

#. Under **Verification Checkpoint**, select the name of the verification
   checkpoint that you want.


******************
The Learner View
******************
 
Learners who must complete in-course reverification see the verification
checkpoints for their course in the list of course credit requirements on
their **Progress** pages.

.. update image when sandbox ready (8/19: waiting for new sandbox)

.. image
.. ../Images/SFD_Credit_ReqList.png
.. :width: 500
.. :alt: Learner's Progress page with a list of credit requirements below the
..     progress graph.

When learners arrive at a checkpoint in the courseware, learners receive a
message that lets them know that they must complete identity verification, and
that if they do not complete identity verification, they will not be eligible
for course credit.

.. add image when sandbox ready (8/19: waiting for new sandbox)

.. image
.. ../Images/
.. :width: 500
.. :alt: A verification checkpoint in the course.

When learners who do not have to complete in-course reverification arrive at a
checkpoint, the learners receive a message about identity verification and
verified certificates. They can access assessment content.

