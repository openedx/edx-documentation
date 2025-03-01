.. _Enable and Create Enrollment Codes:

#####################################
Enable and Create Enrollment Codes
#####################################

Enrollment codes allow users to purchase bulk enrollments for a course.

.. note::

   Enrollment codes used for bulk enrollments, as described in this topic,  are
   not related to the "enrollment code" coupon code type that is referred to in
   the :ref:`Create and Manage Coupons` topic.


************************
Enable Enrollment Codes
************************

Before you create enrollment codes that can be used for bulk enrollments for a
course, you must enable enrollment codes in the E-Commerce service and in
individual courses.

#. To enable enrollment codes in the E-Commerce service, run the site
   configuration command together with the following option.

   ::

     ``--enable-enrollment-codes=True``

   For more information, see :ref:`Add Another Site Partner and Site
   Configuration`.

#. To enable enrollment codes in individual courses, follow these steps.

   #. Follow step 1 through step 5 in :ref:`Create Course Seats` to access and
      select options on the **Add New Course** page. Do not select **Create
      Course** after you complete step 5.
   #. Select **Include Enrollment Code**.
   #. Select **Create Course**.

After you select **Create Course**, enrollment codes are enabled for that
course.

************************
Create Enrollment Codes
************************

#. Go to the enrollment page for the course.
#. On the enrollment page, select **Buy enrollment**. Do not select **Enroll in
   the course**.

   The basket page opens.

#. For **Number of Enrollment Codes**, enter the number of enrollment codes
   that you want. Each enrollment code is for one course seat.
#. Select **Purchase**.

After you select **Purchase**, you receive an e-mail message that contains a
link to a .csv file. The .csv file lists the enrollment codes.



.. include:: ../../../../links/links.rst
