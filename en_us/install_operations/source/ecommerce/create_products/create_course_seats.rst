.. _Create Course Seats:

####################
Create Course Seats
####################

You create course seats by creating a course on the **Create New Course** page
in the course administration tool, which is located at
``http://localhost:8002/courses/``. After you create a course, the E-Commerce
service creates the course seats that are associated with that course.

To create a course seat, follow these steps.

#. Follow the steps in :ref:`Create Products Overview` to start your E-Commerce
   server.
#. In a browser on your E-Commerce server, go to
   ``http://localhost:8002/courses`` to access the **Courses** page.
#. On the **Courses** page, select **Add New Course**.
#. On the **Add New Course** page, enter the information for your course in the
   following fields.

   * **Course ID**
   * **Course Name**

#. For **Course Type**, select a course type and the options for that course
   type.

   * If you select **Free (Audit)**, you must specify whether you want to allow
     honor code learners to earn an honor code certificate. To do this, select
     **Yes** under **Include Honor Seat**.

   * If you select **Verified**, you must add the following information.

     * **Price (in USD)**
     * **Upgrade Deadline**
     * **Verification Deadline**
     * **Include Honor Seat**: This option grants honor code certificates to
       learners who successfully complete the course.

   * If you select **Professional Education**, you must add the following
     information.

     * **Price (in USD)**
     * **ID Verification Required?**
     * **Upgrade Deadline**

   * If you select **Credit**, you must add the following information.

     * **Price (in USD)**: The price for a verified certificate.
     * **Upgrade Deadline**
     * **Credit Provider**
     * **Price (USD)**: The price for course credit.
     * **Credit Hours**
     * **Upgrade Deadline**
     * **Verification Deadline**
     * **Include Honor Seat**: This option grants honor code certificates to
       learners who successfully complete the course.

#. Select **Create Course**.

.. include:: ../../../../links/links.rst
