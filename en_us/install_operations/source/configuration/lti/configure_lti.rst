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

   .. important:: Do not supply a value for the **Instance guid** field. The
      tool consumer generates and supplies a globally unique identifier.

    - **Auto link users using email:** Check this if the learners accessing the
      content via LTI already have an account in the edX platform using the same
      email as the LTI Consumer and you want the data they generate (like
      submissions and grades) on the platform to be associated with that
      account instead of the Anonymous account that's created by default. This
      is done by making use of the ``lis_person_contact_primary_email``
      attribute shared by the LTI Consumer during the LTI Launch and the auto
      linking will not work if the LTI Consumer does not send this value or sends
      a default value due to stricter privacy settings.

   .. note:: The **Auto link users using email** field can only set when a new
        LTI Consumer is created. This helps the LTI Consumer to have consistency
        in the way it stores learner data.

#. Select **Save** at the bottom of the page.

.. include:: ../../../../links/links.rst
