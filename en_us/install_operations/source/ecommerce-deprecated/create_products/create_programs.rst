.. _Programs:

################
About Programs
################

Programs are collections of related courses that you make available on your
marketing site. Each program is of a particular type.

The cost for a program is the sum of the cost for each of its courses. You can
change the cost for a program by creating a program offer, which is a discount
on the program price of either a percentage or fixed amount. For more details,
see :ref:`Create Program Offers`.


********************
Create Program Types
********************

You add program types in the Discovery Service Django administration site for
your Open edX instance.

To add a program, follow these steps.

#. Sign into the Discovery Service Django Administration site for your Open
   edX instance. For example, ``https://<discovery-baseURL>/admin/``, or
   ``localhost:18381`` if you are testing locally.

#. In the **Course Metadata** section, select **Program types**.

#. Select **Add Program Type**.

#. On the **Add program type** page, specify a name for the new program type,
   and select the seat types that are applicable to programs of this type.

#. Optionally, add a program logo image and a slug for this program type for
   use on the marketing site.

#. When you have finished entering information for the program type, select one of
   the **Save** options: **Save**, **Save and add another**, or **Save and
   continue editing**.

   You can now specify this program type when you create new programs.


***************
Create Programs
***************

You add programs and specify the courses that are in each program in the
Discovery Service Django administration site for your Open edX instance.

To add a program, follow these steps.

#. Sign into the Discovery Service Django Administration site for your Open
   edX instance. For example, ``https://<discovery-baseURL>/admin/``, or
   ``localhost:18381`` if you are testing locally.

#. In the **Course Metadata** section, select **Programs**.

#. Select **Add Program**.

   On the **Add Program** page, a UUID is assigned to the new program.

#. Enter information for the new program. Required fields, for example
   **Title**, **Status** and **Type**, have boldface names.

   * In the **Courses** field, specify the courses that are part of the program.
     Names of current courses are automatically matched as you continue to type.
     To add a course that does not currently exist, click the plus sign (+) next
     to the field to create a new course.

   * To allow learners to purchase upgrades to the verified track for all
     the courses in the program with one click, select **One click purchase
     enabled**.

#. When you have finished entering information for the program, select one of
   the **Save** options: **Save**, **Save and add another**, or **Save and
   continue editing**.

.. This procedure completes the course and program structure. To provide "site
.. functionality" for programs, the LMS and the marketing site also need to know
.. about the program and the program offer, if any, that is associated with the
.. program.

.. Discovery service?



.. include:: ../../../../links/links.rst
