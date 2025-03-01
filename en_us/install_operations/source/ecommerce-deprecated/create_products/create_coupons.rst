.. _Create and Manage Coupons:

##################################
Create and Manage Coupons
##################################

This topic covers how to create and distribute coupons and their associated
coupon codes. You can use coupons to provide discounted or free course
enrollments, also called "course seats", to your learners.

.. contents::
   :depth: 1
   :local:

.. _Create a Coupon:

***************
Create a Coupon
***************

To create a coupon, you create one or more coupon codes that learners use to
receive their discounts. You then use your email system to distribute the
discount or enrollment codes for that coupon.

Creating a coupon code has several steps.

.. contents::
   :depth: 1
   :local:

You create coupons and their associated discount or enrollment codes on the
**Create New Coupon** page in the E-Commerce Coupon Administration tool, which
is located at ``http://localhost:8002/coupons/``. In the tool, you enter basic
information and select the options for your coupon.

.. _Enter Basic Coupon Information:

===============================
Enter Basic Information
===============================

Each coupon requires some basic information. To enter basic information for
your coupon, follow these steps.

#. Start the E-Commerce Service on your site. For details, see :ref:`Start
   ECommerce Service`.

#. In a browser on your E-Commerce server, go to
   ``http://localhost:8002/coupons/`` to access the E-Commerce Coupon
   Administration tool.

#. On the **Coupon Codes** page, select **Create Coupon**.

#. On the **Create New Coupon** page, enter the following information.

   * **Coupon Name**: The name you want to give the coupon, such as "January
     15% Promotion". The name must have fewer than 30 characters.
   * **Category**: A list of possible classifications for your coupon,
     such as "Course Promotion" and "Financial Assistance". Categories
     can help you keep track of your coupons.
   * **Valid from** and **Valid until**: The dates and times when the discount
     or enrollment code is valid for use. The time zone is set to Universal
     Coordinated Time (UTC).
   * **Email Domains**: Optional. A list of comma separated domains. If
     specified, only users registered with an email address that matches can
     use the coupon. If null, any user can use the coupon.
   * **Discount Value**: The discount that you want to apply to the course fee,
     specified as a percentage between 1% and 99% or a fixed amount in U.S.
     dollars.
   * **Client**: The name of the organization that you create the codes for.
     Note that the current system cannot automatically send this organization
     an invoice for the codes you create. For more information, see
     :ref:`Specify Invoicing Options` and :ref:`View the Invoice for a Coupon`.
   * **Note** (optional): Any additional information that you want to add to
     your coupon, such as why the coupon was created. The note is visible on
     the coupon page in the coupon administration tool and in the .csv file for
     the coupon. It is not visible to learners.
   * **Tax Deducted Source (TDS)**: This field is not yet active.

After you specify basic information for your coupon, you must specify the
coupon code type.

.. _Specify the Coupon Code Type:

===============================
Specify the Coupon Code Type
===============================

In addition to entering basic information, you must specify a coupon code type.
The coupon code type is either "enrollment code" or "discount code".

* An enrollment code covers the entire fee for a course seat.
* A discount code offers between 1% and 99% or a fixed dollar amount off the
  fee for a course seat.

A "course seat" is a single course enrollment in a specific course track.

To specify the coupon code type, follow these steps.

#. For **Code Type**, select **Enrollment Code** if you want the coupon code to
   cover the entire course fee, or select **Discount Code** if you want to
   provide a discount for the course.

#. If you selected **Enrollment Code**, locate the **Number of Codes** field,
   and then enter the number of enrollment codes that you want to create.

   If you selected **Discount Code**, the following fields are visible.

   * **Discount per Code** (required): Enter the percent or U.S. dollar amount
     of the discount that you want to offer, then select **Percent** or
     **Fixed**. Do not add a percent sign or a dollar sign.

   * **Code** (optional): If you want to specify your own discount code, such
     as ``SCHOLAR15``, enter the code that you want in this field. This code
     can have 1 to 16 characters.

     If you want the system to generate a discount code for you, leave this
     field empty, and then enter the number of discount codes that you want to
     create in the **Number of Codes** field.

After you complete this step, you must specify the courses that you want your
coupon to apply to.

.. _Coupons Specify Courses:

==================
Specify Courses
==================

In addition to specifying your coupon's code type, you must specify the courses
for your coupon. Your coupon can apply to a single course or to multiple
courses.

.. note::
  If you want your coupon to apply to multiple courses, you must use the edX
  Course Catalog API. The Course Catalog API is in beta and is not documented
  or fully supported.

To specify the courses for your coupon, follow these steps.

#. On the **Create New Coupon** page, select **Single Course** or **Multiple
   Courses**.

#. Specify the courses for your coupon.

   If you selected **Single Course**, follow these steps.

   #. For **Course ID**, enter the ID of the course that you want. To find the
      course ID, open the course administration tool at
      ``http://localhost:8002/courses``, select your course name in the list of
      courses, and then locate the **Course ID** field on the page for the
      course.

   #. For **Seat Type**, select the type of seat for the coupon. A "seat" is
      a single course enrollment in a specific course track. For example, the
      seat type might be "verified" or "professional". The options for this
      field appear after you enter a valid value in the **Course ID** field.

   If you selected **Multiple Courses**, follow these steps.

   #. In the **Valid for** field, enter a query to retrieve the courses that
      you want. For more information about creating a query, see :ref:`Create a
      Query for Multiple Courses`.

      To see a preview of the results that your query will return, enter your
      query in the **Valid for** field, and then select **Preview**. A dialog
      box opens that lists the courses in your query results.

   #. For **Seat Types**, select **Non-credit** or **Credit**.

      If you select **Non-credit**, you must also select **Verified**,
      **Professional**, or both.

After you complete these steps, you must :ref:`specify usage limitations for
your coupon <Specify Coupon Usage Limitations>`.

.. _Create a Query for Multiple Courses:

Create a Query for Multiple Courses
*************************************

.. note::
  To create a query, you must use the edX Course Catalog API. The Course
  Catalog API is in beta and is not documented or fully supported.

The coupon administration tool uses queries to return a catalog of courses. The
coupons that you create apply to each course in that catalog.

These queries use the following syntax.

``field_name:search_terms``

Your query can contain operators such as quotation marks ("), asterisks (*),
and hyphens (-).

For example, your query might resemble one of the following queries.

::

  org:(Company OR University)

  org:(-Company OR -University)

  start:[2016-01-01 TO 2016-12-31]

  number:6.002x*

For more information about queries, including syntax and operators, see `Query
string syntax`_.

The following table lists the field names that you can use in your query, along
with a description for each field name.

.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - Field Name
     - Description
   * - ``announcement``
     - The date the course is announced to the public, in YYYY-MM-DD format.
   * - ``end``
     - The course run end date, in YYYY-MM-DD format.
   * - ``enrollment_end``
     - The enrollment end date, in YYYY-MM-DD format.
   * - ``enrollment_start``
     - The enrollment start date, in YYYY-MM-DD format.
   * - ``key``
     - The course run key, sometimes also called the course ID.
   * - ``language``
     - The language in which the course is administered.
   * - ``max_effort``
     - The estimated maximum number of hours necessary to complete the course.
   * - ``min_effort``
     - The estimated minimum number of hours necessary to complete the course.
   * - ``number``
     - The course number (for example, 6.002x).
   * - ``org``
     - The organization associated with the course (for example, MITx).
   * - ``pacing_type``
     - The pacing for the course run. Options are ``instructor_paced`` or
       ``self_paced``.
   * - ``start``
     - The course run start date, in YYYY-MM-DD format.
   * - ``title``
     - The course title.

.. _Specify Coupon Usage Limitations:

===========================
Specify Usage Limitations
===========================

In addition to specifying courses for your coupon, you must specify usage
limitations. Usage limitations control whether one or more customers can use
the coupon, as well as the number of times each customer can use the coupon.

To specify usage limitations, follow these steps.

#. On the **Create New Coupon** page, locate **Usage Limitations**.

#. Select one of the following options.

   * **Can be used once by one customer**

     If you select this option, the **Number of Codes** field is visible. In
     this field, specify the number of individual discount or enrollment codes
     you want to create. The value must be between 1 and 1000. Make sure that
     you create enough discount or enrollment codes so that each person receives
     one code.

   * **Can be used once by multiple customers** or
   * **Can be used multiple times by multiple customers**

     If you select one of these options, the **Maximum Number of Uses** field is
     visible. In this field, specify the number of times customers can use the
     coupon code.

     For example, if you want to create a single coupon code that is available
     for use by 10 different customers, and each customer can use the code
     only one time, select **Can be used once by multiple customers** , ``1``
     for **Number of Codes**, and ``10`` for **Maximum Number of Uses**.

     If you want to create a coupon code that is available for 10 uses,
     whether by one customer or multiple customers, select **Can be used
     multiple times by multiple customers**, ``1`` for **Number of Codes**,
     and ``10`` for **Maximum Number of Uses**.

After you specify usage limitations, you must specify invoicing options for
your coupon.

.. _Specify Invoicing Options:

===========================
Specify Invoicing Options
===========================

In addition to setting usage limitations for your coupon, you must specify
invoicing options. You can send an invoice when you create the coupon or after
one or more customers have redeemed the coupon. The invoice can be for the
total amount or for part of the total amount.

To specify the way you want to invoice your client, follow these steps.

#. On the **Create New Coupon** page, locate **Invoice Type**.

#. Select one of the following options.

   * **Already invoiced**: Select this option if you have already sent an
     invoice to your client.

     If you select this option, you must also enter information in the
     following fields.

     * **Invoice Number**: Your internal invoice number.

     * **Invoice Amount**: The amount that you have already invoiced the
       client.

     * **Payment Date**: The date when payment is due from the client.

   * **Invoice after redemption**: Select this option if you will send an
     invoice to your client after one or more coupon codes have been redeemed.

   * **N/A**: Select this option if neither of the other options
     applies to your situation.


===============================
Finish and Review Coupon
===============================

* After you have :ref:`entered all the basic coupon information <Enter Basic
  Coupon Information>` and specified the options that you want, select **Create
  Coupon**.

When you select **Create Coupon**, the system generates one or more discount or
enrollment codes as well as the URLs where users can redeem these codes.

When the system has finished generating the coupon, a page for the coupon
opens. This page lists the information for your coupon, including all discount
or enrollment codes for the coupon, the coupon's status, URLs where users can
redeem the codes, dates the coupon is valid, and the course that the coupon
applies to. You can also :ref:`download a .csv file with the coupon information
<Download Coupon Information>` from this page.

.. _Download Coupon Information:

***********************************
Download Coupon Information
***********************************

After you create a coupon, you can download a .csv file that lists the
information that you entered when you created the coupon. The .csv file also
includes additional information, such as the discount or enrollment codes that
are associated with your coupon and the system-generated URL where a user can
redeem each code.

#. In your browser, go to ``http://localhost:8002/coupons/`` to open the coupon
   administration tool.
#. On the **Coupon Codes** page, locate the coupon that you want in the table,
   and then select the name of the coupon. The page for the coupon opens.
#. On the page for the coupon, select **Download**. Your .csv file begins
   downloading automatically.

The .csv file for your coupon lists the following information.

.. list-table::
   :widths: 25 60
   :header-rows: 1

   * - **Coupon Name**
     - The name of the coupon.
   * - **Code**
     - The 16-digit alphanumeric discount or enrollment code. The .csv file
       lists at least one entry for each code. The system creates an additional
       entry for the code each time the status of the code changes (for
       example, when the status changes from **Active** to **Redeemed**).
   * - **Maximum Coupon Usage**
     - The number of times that the discount code or enrollment code that is
       associated with the coupon can be used. For single-use coupons, this
       value is 1. For multi-use coupons, this is the value that you specified
       in the **Maximum Number of Uses** field.
   * - **Redemption Count**
     - The number of times the coupon has been redeemed. The initial value is
       0, and the value is incremented each time that a discount code or
       enrollment code for the coupon is redeemed.
   * - **Coupon Type**
     - The type of coupon code associated with this coupon. Possible values are
       **Enrollment** and **Discount**.
   * - **URL**
     - The URL where the user redeems the coupon code.
   * - **Catalog Query** (for multi-course coupons only)
     - The query that was used to determine which courses the coupon applies
       to.
   * - **Course Seat Types** (for multi-course coupons only)
     - The seat type that the coupon applies to. For example, the seat type
       might be "verified" or "professional". For more information about seat
       types, see :ref:`Coupons Specify Courses`.
   * - (for single-course coupons only) **Course ID**
     - The ID of the course that the coupon applies to.
   * - (for single-course coupons only) **Organization**
     - The organization that provides the course.
   * - **Client**
     - The organization that purchased the coupon codes.
   * - **Category**
     - The value that you selected for the **Category** field when you created
       the coupon.
   * - **Note**
     - The text, if any, that you entered in the **Note** field when you
       created the coupon.
   * - **Price**
     - The regular fee for the course.
   * - **Email Domains**
     - The email domains allowed to use this coupon.
   * - **Invoiced Amount**
     - The text, if any, that you entered in the **Total to Invoice to Client**
       field when you created the coupon.
   * - **Discount Percentage**
     - The percent discount, if any, that you specified when you created the
       coupon.
   * - **Discount Amount**
     - The dollar amount discount, if any, that you specified when you created
       the coupon.
   * - **Status**
     - The status of the coupon. Possible values are **Active**, **Redeemed**,
       or **Expired**.
   * - **Order Number**
     - The order number associated with the redemption of the enrollment or
       discount code.
   * - **Redeemed By Username**
     - The username of the customer who redeemed the enrollment or discount
       code.
   * - (for multi-course coupons only) **Redeemed for Course ID**
     - The course ID of the course for which the coupon was redeemed.
   * - **Created By**
     - The username of the user who created the coupon.
   * - **Create Date**
     - The date the coupon was created.
   * - **Coupon Start Date**
     - The first date the coupon can be used.
   * - **Coupon Expiry Date**
     - The last date the coupon can be used.


.. _Edit Coupons:

*************
Edit a Coupon
*************

You edit a coupon by using the coupon administration tool.

.. note::
 You cannot edit the following fields.

 * **Code Type**
 * **Course ID**
 * **Single course** or **Multiple courses**
 * **Seat Type**
 * **Usage Limitations**
 * **Number of Codes** or **Maximum Number of Uses**

#. In your browser, go to ``http://localhost:8002/coupons/`` to open the coupon
   administration tool.

#. On the **Coupon Codes** page, locate the coupon that you want in the table,
   and then select the name of the coupon. The page for the coupon opens.

#. On the page for the coupon, select **Edit Coupon**.

#. Make the changes that you want.

#. Select **Save Changes**.

.. _Deactivate Coupons:

************************
Deactivate a Coupon
************************

To deactivate a coupon, change the **Valid from** and **Valid until** date
fields so that both dates are in the past. For more information, see :ref:`Edit
Coupons`.


.. _Distribute Coupon Codes:

***************************************
Distribute Coupon Codes to Learners
***************************************

You can distribute both discount codes and enrollment codes to learners in two
ways.

* You provide a coupon code that learners enter on the **Checkout** page for
  the verified or professional certificate track. If you do this, edX
  recommends that you also provide the URL for the course About page to make
  signing up for the course easier.

* You provide a URL for an offer landing page. This automatically generated
  page presents information about the course, lets the learner know that the
  coupon code has been applied, and provides the opportunity for the learner to
  enroll. Learners can access this URL if they do not have an edX account or
  they are not signed in. However, learners must sign in or create an edX
  account to redeem the coupon and enroll in the course.

  A URL for an offer landing page has the following format.

  ``http://localhost:8002/coupons/offer/?code=################``

.. note::
  If the coupon code is a discount code, the learner must pay any balance due
  before enrolling in the course for a verified or professional certificate.

To distribute the coupon code or URL to learners, you determine the coupon code
or the URL for the learner to use, and then you create and send an email that
includes the coupon code or the URL. For suggestions for email message text,
see :ref:`Example Email Messages`.

.. _Find a Coupon Code or URL:

===========================
Find a Coupon Code or URL
===========================

You can find coupon codes, whether discount codes or enrollment codes, and
their associated URLs in two places: on the page for the coupon in the coupon
administration tool, and in a downloadable .csv file. You can use either option
to find the coupon code or URL for your learners.


Find a Code or URL on the Coupon Page
*************************************

To find a coupon code or URL on the page for the coupon in the coupon
administration tool, follow these steps.

#. In your browser, go to ``http://localhost:8002/coupons/`` to open the coupon
   administration tool.
#. On the **Coupon Codes** page, locate the coupon that you want in the table,
   and then select the name of the coupon. The page for the coupon opens.
#. On the page for the coupon, locate the table under **Codes**.
#. In the table, locate the information that you want.

   * For a coupon code that the learner will enter on the **Checkout** page,
     use the value in the **Code** column.

   * For an offer landing page, use the URL in the **Redemption URL** column.

Find a Code or URL in a Downloaded File
***************************************

To find a coupon code or URL in the .csv file for a coupon, follow these steps.

#. :ref:`Download a .csv file <Download Coupon Information>` that lists
   the information for your coupon, and then open the .csv file.
#. In the .csv file, locate the information that you want.

   * For a coupon code that the learner will enter on the **Checkout** page,
     use the value in the **Code** column.

   * For an offer landing page, use the URL in the **URL** column.

.. _Send an Email Message:

===========================
Send an Email Message
===========================

After you :ref:`locate the coupon code or URL <Find a Coupon Code or URL>` that
you want to use, you use your email system to provide that information in a
message to potential learners.

.. note::
    When you send a coupon code for a learner to use on the **Checkout** page,
    edX recommends that you include the About page URL for the course as well
    as the coupon code to help the learner enroll more easily.


.. _Example Email Messages:

Example Email Messages
************************

You can use the following email messages as examples of the communication that
you send to your learners.

If Learners Enter a Coupon Code on the Checkout Page
====================================================

.. code::

 Dear learner,

 This message includes a discount <or an enrollment> code for edX101: Overview
 of Creating an edX Course. For more information about the course, see
 https://www.edx.org/course/overview-creating-edx-course-edx-edx101.

 To redeem this code, sign up for a verified <or professional> certificate, and
 then enter the following coupon code in the **Coupon Code** field on the
 **Checkout** page:

 ZDPC3AQV3732RQT5

 We look forward to learning with you!

 The edX101 course team


If Learners Visit an Offer Landing Page
=======================================

.. code::

 Dear learner,

 This message includes a discount <or an enrollment> code for edX101: Overview
 of Creating an edX Course. To redeem this code and enroll in the course, visit
 the following URL:

 http://localhost:8002/coupons/offer/?code=ZDPC3AQV3732RQT5

 We look forward to learning with you!

 The edX101 course team

.. _View the Invoice for a Coupon:

********************************
View the Invoice for a Coupon
********************************

When you create a coupon, the E-Commerce service generates and fulfills an
order. The Invoice Payment Processor module in the service then records the
fulfilled order. Because the Invoice Payment Processor module assumes that you
have sent or will send an invoice to the client who purchased the coupon, the
module also records the order in the Invoice table in the Django administration
panel so that you can view and reconcile the order.

To view your coupon invoices in the Invoice table, go to
``http://localhost:8002/admin/invoice/invoice/``. The table lists all of the
invoices for your coupons, along with information such as the client name and
the invoice status.

For more information about the way that the E-Commerce service manages orders,
see :ref:`Manage Orders`.

.. include:: ../../../../links/links.rst

