.. _Configuring Credentials for a Tool Consumer:

###############################################################
Configuring Credentials for a Tool Consumer
###############################################################

For each external learning management system or application (external LMS) that
you want to allow access to your edX instances as an LTI tool consumer, you
create OAuth1 credentials, and then configure your edX instance to allow
access. Each external LMS that you :ref:`configure as a tool consumer
<Configure the Tool Consumer>` must have separate credentials.

.. Commenting out the following option until we understand it better, per Dave Ormsbee - Alison 8 Sep 15

.. While each external LMS that you configure as a tool consumer must have separate credentials, you can also choose to create and configure more than one set of credentials for each system.

.. For example, you can configure a single set of credentials for your campus LMS, or you can configure unique credentials for every course that embeds edX content on that remote LMS. The first approach results in faster configuration time. However, the second approach can lessen the disruption and reconfiguration that might result if you have to revoke access for a single course at a later time.

After you complete the configuration of a tool consumer on your edX system, you
can add the consumer credentials to your external LMS. For examples of how
course teams might set up a course on an external LMS as a consumer of edX
course content, see :ref:`opencoursestaff:Using Open edX as an LTI Tool
Provider` in the *Building and Running an edX Course* guide.

.. _Configure the Tool Consumer:

*********************************
Configure the Tool Consumer
*********************************

To configure an LTI tool consumer to have access to your Open edX installation,
follow these steps.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. In the **LTI Provider** section, next to **LTI Consumers** select
   **Add**.

#. Enter the following information.

   - **Consumer Name**: An identifying name for the tool consumer.

   - **Consumer Key**: The console generates a unique key value for this
     tool consumer. Alternatively, you can use an external application to
     generate the key, and then enter it here.

   - **Consumer Secret**: The console generates a unique secret value for this
     tool consumer. Alternatively, you can use an external application to
     generate the secret, and then enter it here.

     .. important::
       Do not supply a value for the **Instance guid** field. The
       tool consumer generates and supplies a globally unique identifier.

   - **Require User Account**: Checking this makes the content available only
     for the learners who already have an account on the Open edX instance. This
     is useful when learners need to be linked between different LMS systems.

     By default, :ref:`an anonymous Open edX system user<Anonymous User Authentication>`
     is created and all the data is associated with that user. This flag
     can be used when it is desirable to associate the data, generated
     via LTI interactions, to actual learner accounts instead of an
     anonymous account. When this is checked, instead of creating an
     anonymous user automatically, a message requesting the learner to sign
     into Open edX is displayed on the first LTI launch and the content
     is presented after a successful sign in.

     .. important::
       The account linking happens only when the LTI Consumer sends the
       learners' email to Open edX by setting the POST data attribute
       ``lis_person_contact_email_primary`` in the LTI Launch request.
       This feature has only been tested with **Canvas LMS**, with privacy
       setting set to "Email Only" or "Public".

     With this flag checked, the LTI content embedded in iframes will require
     the following Django configuration.

     .. code-block:: python

         # Needed for passing user session with the LTI Request
         SESSION_COOKIE_SAMESITE = 'None'
         SESSION_COOKIE_SECURE = True
         SESSION_COOKIE_SAMESITE_FORCE_ALL = True
         CSRF_COOKIE_SECURE = True
         CSRF_COOKIE_SAMESITE = 'None'

         # Needed for showing pages in iframe
         X_FRAME_OPTIONS = "ALLOW-FROM <your-lti-consumer-domain>"


     Caveats:
       - Setting this flag only associates future interactions of the learner.
         This flag cannot be used to migrate data from existing anonymous accounts
         to corresponding user accounts.
       - Unchecking the flag will not roll back the auto-linked users and
         might cause the LTI content to break completely. In situations
         requiring rollback of this feature, it is recommended to create a
         new LTI Consumer with this flag turned off and the new credentials
         be used in the LTI consumer application.


#. Select **Save** at the bottom of the page.

.. include:: ../../../../links/links.rst
