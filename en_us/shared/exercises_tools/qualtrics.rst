.. _Qualtrics Survey:

#########################
Qualtrics Survey Tool
#########################

.. note:: EdX offers provisional support for this tool.

You can administer Qualtrics surveys to your learners in your edX course. The
Qualtrics survey appears in an iframe inside the course.

.. image:: ../../../shared/images/Qualtrics.png
  :width: 500
  :alt: A Qualtrics survey with several responses filled in.

Course staff can view the overall results of the survey as well as responses
from individual learners.

.. note:: To use a Qualtrics survey, you must have a Qualtrics license.
 Qualtrics licenses are available for a fee at the `Qualtrics website
 <http://www.qualtrics.com>`_. If you want to include a survey but you do not
 have a Qualtrics license, you can use the :ref:`edX survey tool<Survey Tool>`
 or a :ref:`Google form<Google Drive Files Tool>`.

For more information, see the following sections.

.. contents::
  :local:
  :depth: 1

Be sure to review all supplemental materials to make sure that they are
accessible before making them available through your course. For more
information, see
:ref:`Accessibility Best Practices for Course Content Development`.

*************************************
Add a Qualtrics Survey to Your Course
*************************************

To add a Qualtrics survey to your course, you must :ref:`create the survey in
Qualtrics <Create the Qualtrics Survey>`, and then :ref:`create a Text
component in Studio <Create the Text Component in Studio>`.

.. _Create the Qualtrics Survey:

==============================
Create the Qualtrics Survey
==============================

.. note:: Because Qualtrics is a third-party tool, the following steps might
 change without notice. See the `Qualtrics website
 <http://www.qualtrics.com>`_ for the most up-to-date Qualtrics documentation.

#. Using your Qualtrics account, create your survey.
#. Add the statements and options that you want the survey to include.
#. Add the **user ID** element. This element imports data from your course
   into Qualtrics.

   #. At the top of the page, make sure the **Edit Survey** tab is selected,
      and then select **Survey Flow**.
   #. In the upper left corner, select **Add a New Element Here**.
   #. Select **Embedded Data**.
   #. Under **Set Embedded Data**, replace **Enter Embedded Data Field Name
      Here** with ``uid``.
   #. Select **Save Flow**.

#. At the top of the page, make sure **Edit Survey** is selected, and then
   select **Launch Survey**.
#. On the page that opens, select **Activate Survey** in the upper right
   corner.
#. On the page that opens, locate the URL that is listed under **Your
   Anonymous Survey Link**. You will add this URL to the Text component for
   your survey in Studio.

   .. note:: If you need to find this URL in the future, open your survey
    in Qualtrics, and then select the **Distribute Survey** tab at the top of
    the page.

.. _Create the Text Component in Studio:

=====================================
Create the Text Component in Studio
=====================================

#. Open the unit where you want the survey to appear.
#. Under **Add New Component**, select **Text**, and then select **IFrame
   Tool**.
#. Select **Edit** to open the component editor, and then select **HTML** in
   the menu bar.
#. At the end of the instructions, locate the example iframe element, and
   replace the placeholder values with the values for your survey. The iframe
   element starts with the following text.

   ``<iframe title="Euler Line Demo"``

  * In the ``title`` attribute, replace ``Euler Line Demo`` with the title of
    your survey.
  * In the ``src`` attribute, replace the placeholder URL with the URL from
    step 6 in :ref:`Create the Qualtrics Survey`.
  * In the ``src`` attribute, add the following value to the end of the URL.

    ``?uid=%%USER_ID%%``

    The resulting ``src`` attribute resembles the following example.

    ``src="https://qtrial2015az1.az1.qualtrics.com/SE/?SID=SV_9N27VuruRdNcpHT?uid=%%USER_ID%%"``

  * Replace the values in the ``width`` and ``height`` attributes with values
    that allow your survey to appear the way you want it to. For example, you
    might change ``width`` to 800 and ``height`` to 1000.
  * (Optional) If your survey might be taller than the value that you set for
    ``height``, in the ``scrolling`` attribute, change the value to ``yes``.
    If you do not change the value to ``yes`` and your survey is taller than
    the ``height`` value, learners cannot scroll down to respond to all the
    survey statements.
  * Leave the other default values, and then select **OK** at the bottom
    of the HTML source code editor to return to the component editor.

#. In the component editor, delete all of the default instructional text, or
   replace it with introductory text for your Qualtrics survey.
#. Select **Save**.

*******************************
View Survey Responses
*******************************

You can view both overall survey responses and responses for individual
learners.

=======================
View Overall Responses
=======================

To view your overall survey results and analyze data, open your survey on the
`Qualtrics website <http://www.qualtrics.com>`_.

=========================================================
View Survey Responses for an Individual Learner
=========================================================

To view a specific learner's survey responses, you must download data both
from the Insructor Dashboard and from Qualtrics, and then review the data.

Download Data from the Instructor Dashboard
**********************************************

#. In the LMS, select **Instructor**.
#. Select **Data Download**.
#. Under **Data Download**, select **Get Student Anonymized IDs CSV**. If you
   receive a prompt, specify the location where you want to save the file.

   The .csv file is saved to your computer. The file has the following name.

   ``<course name>_<course number>_<year>_<term>_anon-ids.csv``

   For more information about anonymized student IDs, see
   :ref:`Access_anonymized`.

#. Under **Reports**, select **Download profile information as a CSV**.
#. When the profile information report appears in the list under **Reports
   Available for Download**, select the report to download the .csv file to
   your computer. The file has the following name.

   ``<course name>_<course number>_<year>_<term>_student_profile_info_<date and time>.csv``

For more information about accessing learner data, see :ref:`Student Data`.

Download Data from Qualtrics
*******************************

.. note:: Because Qualtrics is a third-party tool, the following steps might
 change without notice. See the `Qualtrics website
 <http://www.qualtrics.com>`_ for the most up-to-date Qualtrics documentation.

#. In Qualtrics, select the **View Results** tab.
#. On the page that opens, select **Download Data** in the upper left corner
   of the page.
#. On the page that opens, clear the **Compress the desired format into a .zip
   file before downloading** check box. Accept all the other default values.
#. Under **Format**, select the **This is a Comma
   Separated Values format...** link to download the .csv file.

Review the Data
******************

To associate learners' responses with their learner profiles, open the three
.csv files that you have downloaded in a program such as Microsoft Excel.

* The Qualtrics file has a **uid** column that contains each learner's
  anonymized ID, as well as columns that contain each learner's answers to the
  survey.

* The anonymized user ID file (``<course name>_<course number>_<year>_<term
  >_anon-ids.csv``) contains each learner's anonymized ID and the learner's
  edX user ID.

* The student profile data file (``<course name>_<course
  number>_<year>_<term>_student_profile_info_<date and time>.csv``) contains
  each learner's edX user ID and profile information, such as user name and
  real name.

To merge the data in the three spreadsheets so that you can see a learner’s
edX user ID, profile information, and survey responses in one place, you can
use functions such as VLOOKUP in Microsoft Excel.


