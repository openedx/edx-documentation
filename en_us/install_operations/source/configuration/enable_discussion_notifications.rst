.. _Enabling Discussion Notifications:

##########################################
Enabling Discussion Notifications
##########################################

You can set up notifications that learners receive the first time that anyone
adds a response to a discussion post that they have made.

For more information, including the text of the discussion notification
message, see :ref:`Automatic Email` and
:ref:`openlearners:Receiving Discussion Notifications`.

.. contents::
   :depth: 1
   :local:

.. _Requirements for Discussion Notifications:

*****************************************
Requirements for Discussion Notifications
*****************************************

To create discussion notifications for your instance of the Open edX platform,
you need the following items.

* edX Automated Communication Engine (ACE). For more information about how to
  install and configure ACE, see `edX Automated Communication Engine`_.
* A third party email client, such as Sailthru. For information about how to
  configure your email client, see the documentation for the client.

.. _Enable Discussion Notifications:

*******************************
Enable Discussion Notifications
*******************************

After you have set up ACE and the third party email client, you enable
discussion notifications in the Django administration console for your instance
of Open edX.

#. Sign in to the LMS Django administration console for your base URL. For
   example, ``http://{your_URL}/admin``.

#. On the **Site Administration** page, locate **Site_Configuration**.

#. In the **Site_Configuration** section, next to **Site configurations**,
   select **Change**.

#. On the **Change site configuration** page, locate the **Values** field, and
   then add the following value.

   ::

     {
      "enable_forum_notifications":true
      }

#. Select **Save**.



.. include:: ../../../links/links.rst
