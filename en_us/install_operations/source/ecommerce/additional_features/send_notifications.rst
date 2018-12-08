.. _Sending Notifications:

#######################
Sending Notifications
#######################

The edX E-Commerce service uses the `Communications API`_ that is part of
`Oscar`_ to create and send notifications in the form of email messages. To
send notifications, you must set up notifications, create one or more email
messages, and then send the email messages.

*************************
Set Up Notifications
*************************

#. Enable the E-Commerce service to send notifications. To do this, change the
   value of the ``ENABLE_NOTIFICATIONS`` feature flag to True.
#. Define communication type codes to refer to particular types of
   notification. For example, you might define a communication type code named
   ``COURSE_SEAT_PURCHASED`` to correspond to the purchase of a course seat.

*************************
Create an Email Message
*************************

The E-Commerce service can send both HTML and plain text email messages. To
create an email message, create the following three files in the
``ecommerce/ecommerce/templates/customer/emails/`` folder.

   * An HTML template that extends ``email_base.html`` and includes the body of
     the email.
   * A plain text file that contains the email's subject line.
   * A plain text file that contains the body of the email.

Use the following convention to name these files.

``commtype_{communication type code}_body.html``

For example, if the communication type code is ``course_seat_purchased``, the
three files would have the following names.

* ``commtype_course_seat_purchased_body.html``
* ``commtype_course_seat_purchased_body.txt``
* ``commtype_course_seat_purchased_subject.txt``

.. note::
 To add a custom email body, override ``block body`` in the email_base.html
 file. To add a custom footer, override ``block footer`` in the email_base.html
 file.

*******************
Send Email Messages
*******************

To send email messages, use the ``send_notification(user, commtype_code,
context)`` method. This method is implemented in
``ecommerce/ecommerce/notifications/notifications.py``.



.. include:: ../../../../links/links.rst
