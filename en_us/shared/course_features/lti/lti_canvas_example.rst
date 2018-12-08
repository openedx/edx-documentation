.. _edX as an LTI Provider to Canvas:

##########################################
Example: edX as an LTI Provider to Canvas
##########################################

.. only:: Partners

  .. note:: Support for this feature is provisional. EdX is currently working
   with a limited number of partners to test this feature on edX Edge.

To use edX course content in the Canvas LMS, you add a new app to the course and then add external tool module items.

.. note:: This example relies on the use of a third-party tool. Because this
  tool is subject to change by its owner, the steps and illustrations provided
  here are intended as guidelines and not as exact procedures.

#. In Canvas, select your course. In **Settings**, select **Add New App**.

   .. image:: ../../../../shared/images/lti_edit_external_app_Canvas.png
     :alt: The Canvas page where you enter identifying values for the edX host
         site as a LTI tool provider.

#. In **Modules**, add a new **External Tool** item. The **URL** is the LTI
   URL that you determined for the edX course content, such as
   ``https://edx-lti.org/lti_provider/courses/course-v1:edX+DemoX+2014/block-v1:edX+DemoX+Demo_Course+type@problem+block@d2e35c1d294b4ba0b3b1048615605d2a``.

   .. image:: ../../../../shared/images/lti_edit_problem_Canvas.png
     :alt: The Canvas page where you add an external tool and supply the LTI
         URL.

   For more information, see :ref:`Determining Content Addresses`.

#. Review the content to verify that it appears as you expect.

   .. image:: ../../../../shared/images/lti_canvas_example2.png
     :alt: An edX drag and drop problem shown as part of a course running on a
      Canvas system.
