.. _Checking Student Progress and Issuing Certificates:

###################################################
Assign Final Grades and Issue Certificates
###################################################
.. This chapter will be renamed and expanded to include course wrap-up activities and best practices.

This topic describes how to assign grades and issue certificates to learners in
your course.

.. contents::
   :local:
   :depth: 1

****************************************
Overview
****************************************

As you prepare for the end of your course, you can send learners a :ref:`course
farewell<Course Farewell and Certificates>` email message.

To assign a final grade to each learner enrolled in a course, you generate
grades after the **Course End Date** and **Time** have passed. See
:ref:`Access_grades`.
 
The learner's final grade and the grading configuration you set in Studio are
used to determine whether the learner has earned a certificate for the course.

.. note:: You set up certificates when you are building your course. For more
  information, see :ref:`Setting Up Course Certificates`.


****************************************
On-Demand Certificates
****************************************

If you have a self-paced course, you can allow your learners to download their
certificates as soon as they have completed enough of the course with a high
enough grade to qualify for a certificate. 

Learners can request a certificate at any time after they qualify. Learners may
want to request a certificate right away, or they may wait until they have
completed the course. For more information, see `On-Demand Certificates
<http://edx.readthedocs.org/projects/edx-guide-for-
students/en/latest/SFD_certificates.html#on-demand-certificates>`_.

If your course offers on-demand certificates, we encourage you to include this
information on your course About page, on the **Course Info** page, and in
communication with your learners.

.. only:: Partners

   Course teams should also discuss additional self-paced settings with their
   edX Partner Manager during the course announcement process.

==============================================================
Allow Learners to Download Certificates when they Qualify
==============================================================

To allow learners to download certificates when they qualify for them, you must
modify the **Certificates Display Behavior** advanced setting in Studio.

#. From the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate **Certificates Display Behavior**.

#. In the **Certificates Display Behavior** field, enter ``"early_no_info"``.
   Be sure that you include the double quotation marks.

#. Select **Save Changes**.
