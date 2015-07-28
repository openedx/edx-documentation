.. _Offering Academic Course Credit:

#####################################
Offering Academic Course Credit
#####################################

If your institution has an agreement with edX, you might be able to offer
academic credit for your course. Learners will be able to purchase this
academic credit after they meet requirements that you set. These requirements
typically include identity checks throughout the course as well as ID
verification at the beginning of the course. Learners can see a list of the
requirements on their **Progress** page.

If your course will include academic credit, your edX program manager will
complete the initial setup of your course, including setting the price and
enabling your course to offer credit. You must then complete two steps.

#. :ref:`Specify the minimum score that a student must earn to receive
   academic credit in the course <Specify Passing Score>`.
#. :ref:`Add identity checks to the course <Add Identity Checks>`.



.. _Specify Passing Score:

****************************
Specify the Passing Score
****************************

In addition to setting the usual grade scale for your course, you indicate a
specific score that a learner must receive to earn credit for your course.

#. In Studio, select **Settings**, and then select **Grading**.
#. In the **Credit Grade & Eligibility** section, specify a score followed by
   a percent sign (%)in the **Minimum Passing Grade to Earn Credit** box. This
   score can be any number from 1 to 100. Do not add a percent sign.

.. _Add Identity Checks:

****************************
Add Identity Checks
****************************

For courses that offer academic credit, edX has two identity checks:
proctored exams and :ref:`in-course reverification (ICRV) <In Course
Reverification>`. You can use either feature or both features in your course.

================
Proctored Exams
================

.. note:: sjfkla; wieoha; 

.. from Carol

.. _In Course Reverification:

=================================
In-Course Reverification
=================================

With ICRV, you add identity verification "checkpoints" at specific locations
in your course, such as before assessments or exams. When learners reach a
checkpoint, they must use their computer's webcam to verify their
identification, similar to the original ID verification process, before they
can access more course content.

To use ICRV, you must complete the following steps.

#. Enable the ICRV XBlock in your course.
#. Create specific ICRV checkpoints.


Enable In-Course Reverification
*********************************

To enable ICRV for your course, follow these steps.

#. In Studio, select **Settings**, and then select **Advanced Settings**.
#. In the **Advanced Module List** field, place your cursor between the
   brackets (``[]``),and then add ``"edx-reverification-block"``. Make sure to
   include the quotation marks. 

   .. note:: If the **Advanced Module List** field already contains one or 
    more items, add a comma after the closing quotation mark for the last
    item, and then add ``"edx-reverification-block"``.

    ``"module_name","edx-reverification-block"``

.. Info from https://openedx.atlassian.net/wiki/display/ECOM/How+to+Configure+Credit+Courses


Create an ICRV Checkpoint
****************************

To create an ICRV checkpoint, follow these steps.

#. In the unit where you want to add a checkpoint, select **Advanced** under
   **Add New Component**, and then select **Reverification Checkpoint**.
#. If the unit contains other components, move the reverification checkpoint
   component so that it is the first component in the unit.
#. In the reverification checkpoint component, select **Edit**.
#. In the component editor, locate **Related Assessment**, and then type the
   display name of the assessment that you want to associate the checkpoint
   with. If you have not created the assessment yet, type the display name
   that the assessment will have.
#. Next to **Verification Attempts**, specify the number of times that you
   want students to be able to attempt to verify their identity. You can
   specify up to three attempts. If you do not specify a number, [learners
   only have one attempt(?)].
#. Select **Save**.

After you create an ICRV checkpoint, the checkpoint appears on the learner's
**Progress** page.


Verify that all reverification events are captured (attempts, success, failures, retries, skips)
Verify that the course team can download a report for the course that displays who has both completed the course and has completed the reverifications successfully.

