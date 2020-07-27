.. _Enabling Proctored Exams:

########################################
Enable Proctored Exams
########################################

To create a proctored exam, you modify the course advanced settings in Studio
to enable proctored exams, and then you modify the settings of a subsection to
specify that the subsection is a proctored exam.

To enable proctored exams in your course, follow these steps.

#. In Studio, select **Settings**, then select **Proctored Exam Settings**.

#. Locate the **Enable Proctored Exams** policy key. The default value is
   ``false``.

#. Change the value of the setting to ``true``.

#. Select **Submit**. You can now create proctored exams in your course.


******************************
Configuring Proctoring Backend
******************************

The choice of proctoring backend can be configured. Since Fall 2019,
the default proctoring provider is **RPNow** by PSI.  To use
**Proctortrack** by Verificient, please follow these steps to change
the proctoring backend:

.. warning:: Changing the proctoring backend for a course after
   proctored exams have been created in course content is not
   supported. Please create proctored exams only after making a final
   decision of which proctoring backend your course will use.


#. In Studio, select **Settings**, then select **Proctored Exam Settings**.

#. Locate the **Proctoring Provider** policy key.

#. Change the value to the desired backend.

#. Select **Submit**.

After you enable proctored exams for your course and choose the
proctoring backend, you can create a proctored exam or a practice
proctored/onboarding exam.
