.. _Accessing ORA Assignment Information:

##########################################
Accessing Assignment and Learner Metrics
##########################################

After your open response assessment assignment has been released, you can access
information about the number of learners in each step of the assignment or the
performance of individual learners. This information is available in the **Staff
Info** and **Staff Tools** sections at the end of each assignment.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_CourseStaffInfo_Collapsed.png
   :alt: The Staff Info banner at the bottom of the peer assessment

When you access a specific learner's information for an open response assessment
using **Staff Tools**, you can view his responses and, if necessary,
:ref:`cancel the learner's submission<Remove a learner response from peer
grading>` so that it is not included in peer assessments.

.. _PA View Metrics for Individual Steps:

************************************************
View Metrics for Individual Steps
************************************************

You can check the number of learners who have completed, or are currently
working through, the following steps:

* Submitted responses.
* Completed peer assessments.
* Waiting to assess responses or receive grades.
* Completed self assessments.
* Completed the entire assignment.

To find this information, open the assignment in the courseware, scroll to the
bottom of the assignment, and then select **Staff Info**.

The **Staff Info** section expands, and you can see the number of learners who
are currently working through (but have not completed) each step of the problem.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_CourseStaffInfo_Expanded.png
   :alt: The Course Staff Information box expanded, showing problem status

.. _Access Information for a Specific Learner:

***********************************************
Access Information for a Specific Learner
***********************************************

You can access information about an individual learner's performance on a peer
assessment assignment, including:

* The learner's response.
* The peer assessments that other learners performed on the learner's
  response, including feedback on individual criteria and on the overall
  response.
* The peer assessments that the learner performed on other learners'
  responses, including feedback on individual criteria and on the overall
  responses.
* The learner's self assessment.

In the following example, you can see the performance information for a specific
learner. This learner's response received one peer assessment, and the learner
completed a peer assessment on one other learner's response. The learner also
completed a self assessment.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_SpecificStudent.png
   :width: 500
   :alt: Report showing information about a learner's response

To determine whether this learner has received the required number of
assessments from other learners and has completed the required number of
assessments for other learners, refer to the **Graded By** and **Must Grade**
values that were set for the open response assessment assignment in Studio. For
more information about these settings, see :ref:`Specify Step Settings<PA
Specify Step Settings>`.

For details about accessing information for a specific learner, and for an
example that shows a learner's response with more assessments, see :ref:`Access
Learner Information`.


.. _Access Learner Information:

=======================================
Access a Specific Learner's Information
=======================================

#. In the LMS, go to the peer assessment assignment that you want to see.

#. Scroll to the bottom of the problem, and select **Staff Tools**.

#. In **Staff Tools**, enter the learner's username or email address, then
   select **Submit**.

The learner's information appears.

The following example shows:

* The learner's response.
* The two peer assessments for the response.
* The two peer assessments the learner completed.
* The learner's self assessment.

For a larger view, select the image so that it opens by itself in the browser
window, and then click anywhere on the image that opens.

.. image:: ../../../../shared/building_and_running_chapters/Images/PA_SpecificStudent_long.png
   :width: 250
   :alt: Report showing information about a learner's response


.. _Remove a learner response from peer grading:

************************************************
Remove a Learner's Response from Peer Grading
************************************************

If you use open response assessments, learners might alert you to vulgar,
abusive, or otherwise inappropriate responses that they have seen while
performing peer assessments. In such a situation you can :ref:`locate<Locate a
specific ORA submission>` and cancel the submission. Doing so removes the
inappropriate response from peer assessments so that it is no longer shown to
other learners.

.. note:: Removing a learner's submission is an irreversible action.

When you cancel an inappropriate submission, the response is immediately removed
from the pool of submissions available for peer assessment. If the inappropriate
response has already been sent to other learners for peer assessment, it is also
removed from their queue. However, if any learner has already graded the
inappropriate response, it is counted as one of the submissions they have
graded.

.. note:: After you remove an inappropriate response from peer assessment, you
   decide whether the learner who submitted that response is allowed to submit
   a replacement response. If you do not want to allow the learner to submit a
   replacement response, you do not need to take any additional action. The
   learner receives a grade of zero for the entire submission. To allow the
   learner to resubmit a response for a cancelled submission, you must delete
   the learner's state for the problem. For information, see
   :ref:`delete_state`.

Remove a submission from peer assessment by completing these steps.

#. In the LMS, go to the peer assessment assignment that contains the submission
   you want to remove.

#. Scroll to the bottom of the problem, then select **Staff Tools**.

#. In **Staff Tools**, enter the learner's username or email address, then
   select **Submit**.

   The learner's information appears.

#. Scroll down to the **Learner Response** section and locate the submission you
   want to remove.

.. image:: ../../../../shared/building_and_running_chapters/Images/ORA_RemoveSubmission.png
   :alt: Dialog allowing comments to be entered when removing a learner submission

5. Enter a comment to document or explain the removal. This comment appears to
   the learner when she views her response in the open response assessment
   problem.

#. Click **Remove submission**.

   The inappropriate submission is removed from peer assessment. When you access
   this learner's information again, instead of the response, you see a note
   showing the date and time that the submission was removed, and the comments
   that you entered.

   Removed submissions are also removed from the list of Top Responses if they
   were previously listed.

.. image:: ../../../../shared/building_and_running_chapters/Images//ORA_CancelledStudentResponse.png
   :alt: The date, time and comment for removal of a learner response is shown instead of the original response.


.. _Locate a specific ORA submission:

*************************************************
Locate a Specific Submission in an ORA Assignment
*************************************************

If you are alerted to an inappropriate ORA submission that you want to cancel
and :ref:`remove from peer assessment<Remove a learner response from peer
grading>`, locate the specific submission by following these steps.

#. Ask the person who reported the incident to send you a sample of text from
   the inappropriate post.

#. Contact your edX Program Manager to request a data download of ORA
   responses for your course.

   You will receive the download as a spreadsheet or in .csv file format.

#. Search the spreadsheet for text that matches the sample text from the
   inappropriate post.

#. From any matching entries in the spreadsheet, locate the username of the
   learner who posted the submission.

#. Make a note of the username, and follow the steps to :ref:`remove a learner
   response from peer grading<Remove a learner response from peer grading>`.
