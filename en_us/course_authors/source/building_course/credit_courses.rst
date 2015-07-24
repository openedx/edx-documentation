.. _Offering Academic Course Credit:

#####################################
Offering Academic Course Credit
#####################################

If your institution has an agreement with edX, you might be able to offer
academic credit for your course. Courses that offer academic credit have
additional safety features to help prevent cheating. Learners will be able to
purchase academic credit after they earn a verified certificate in the course.

If your course will include academic credit, your edX program manager will
complete the initial setup of your course. You must then complete two steps.

#. :ref:`Specify the minimum score that a student must earn to receive academic
   credit in the course <Specify Passing Score>`.
#. :ref:`Add security features to the course <Add Security Features>`.

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

.. _Add Security Features:

****************************
Add Security Features
****************************

For courses that offer academic credit, edX has two security features:
proctored exams and :ref:`in-course reverification (ICRV) <In Course
Reverification>`. You can use either feature or both features in your course.

================
Proctored Exams
================

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

You can require in-course reverification for a specific course track.
For example, you can require in-course reverification for learners in
the verified track, but not the honor code track.

.. Should this be mandatory? It doesn't make sense to have ICRV for honor code
.. students. And, if it's mandatory, should ICRV only be associated with the
.. verified track by default, getting rid of the second step below?

To use ICRV, you must complete the following steps.

#. Enable the ICRV XBlock in your course.
#. (Optional) Associate ICRV with a course track.
#. Create specific ICRV checkpoints.


Enable In-Course Reverification
*********************************

To enable ICRV for your course, follow these steps.

#. In Studio, select **Settings**, and then select **Advanced Settings**.
#. ...

Associate the Course Track
****************************

To associate ICRV with a specific course track, follow these steps.

#. In Studio...
#. ...

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
   want students to be able to attempt to verify their identity.
#. Select **Save**.

After you create an ICRV checkpoint, the checkpoint appears on the learner's
**Progress** page.






