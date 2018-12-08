.. _Configuring Open edX for LTI Authentication:

###############################################################
Configuring Open edX User Authentication for LTI
###############################################################

Every learner who accesses content on an Open edX system must have a user
account. The Open edX system uses the accounts to collect data for learner
interactions with course content.

After you :ref:`configure your edX instance as an LTI tool provider<Configuring
an edX Instance as an LTI Tool Provider>`, you can configure Open edX user
authentication between your Open edX installation and an LTI tool consumer.

For more information about the authentication flows that are available, see
:ref:`Options for LTI Authentication and User Provisioning`.

.. contents::
   :local:
   :depth: 1

**************************************************
Configure Open edX User Authentication for LTI
**************************************************

To configure Open edX user authentication between your Open edX installation
and an LTI tool consumer, follow these steps.

.. note:: A consumer key and secret are required. The Django administration
 console provides a hexadecimal string for the secret, but does not provide a
 hexadecimal string for the key. You must use an external tool to generate the
 key.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. In the **Third_Party_Auth** section, next to **Provider Configuration
   (LTI)** select **Add**.

#. Select **Enabled**.

#. Enter the **Name** of your Open edX system, as you want it to appear on the
   registration page that is presented to learners who access Open edX content
   from this LTI tool consumer.

#. To customize the registration process for learners, you can make selections
   for these optional fields.

  - **Skip Registration Form**: If you select this option, users are not asked
    to confirm any user account data that is supplied for them by the LTI tool
    consumer (name, email address, and so on).

    By default, this option is cleared and learners review a registration form
    with the account details supplied by the tool consumer.

  - **Skip Email Verification**: If you select this option, users are not
    required to confirm their email addresses, and their accounts are activated
    immediately upon registration.

    By default, this option is cleared and learners receive an email message
    and must select a link in that message to activate their user accounts.

6. Enter the following information.

  - **Lti consumer key**: Enter the hexadecimal string of the key.

  - **Lti consumer secret**: The system generates a hexadecimal string value
    for this field. Alternatively, you can replace it with a secret generated
    by an external tool.

7. Optionally, change the default value for the **Lti max timestamp age**.

#. Select **Save** at the bottom of the page.

*******************************************
Test LTI Authentication
*******************************************

To verify the sign in process for an LTI provider configuration, follow these
steps.

#. Have the LTI consumer key and secret for the LTI provider configuration
   available. For example, use the Django administration console to open the
   **Change Provider Configuration (LTI)** page.

#. Use a separate browser window or tab to open the `IMS LTI 1.1 Consumer
   Launch`_ page.

#. As the **Launch URL**, enter your base URL followed by ``/auth/login/lti/``.
   For example, ``http://{your_URL}/auth/login/lti/``.

#. Copy the **Lti consumer key** value, and then on the IMS LTI 1.1 Consumer
   Launch page paste it in as the **Key**.

#. Copy the **Lti consumer secret** value, and then on the IMS LTI 1.1 Consumer
   Launch page paste it in as the **Secret**.

#. Optionally, change the default values in the **Launch Data** section of the
   **IMS LTI 1.1 Consumer Launch** page to match the set of values that the
   tool consumer is configured to supply.

#. To test the workflow for a learner who does not yet have a user account on
   your Open edX system, follow these steps.

   - Use a separate browser window or tab to make sure that you are signed out
     of your Open edX LMS.

   - On the **IMS LTI 1.1 Consumer Launch** page, select **Recompute Launch
     Data** and then select **Press to Launch**.

   The page that is configured for delivery to an unauthenticated user loads at
   the bottom of the page. In the example that follows, the registration page
   appears (that is, it was not configured to be skipped) and the learner is
   prompted to complete required fields.

   .. image:: ../../Images/lti_test_auth.png
     :alt: Screen shot of the IMS LTI 1.1 Consumer Launch page with the
         registration page for the edX Edge loaded at the bottom.

#. To test the workflow for a learner who already has a user account on your
   Open edX system, follow these steps.

   - Use a separate browser window or tab to sign in to your Open edX LMS.

   - On the **IMS LTI 1.1 Consumer Launch** page, select **Recompute Launch
     Data** and then select **Press to Launch**.

   Your Open edX user account is linked to the LTI provider configuration, and
   your learner dashboard on the Open edX site loads at the bottom of the page.
   To unlink your user accounts, select the arrow next to your username, and
   then select **Account**. In the **Connected Accounts** section, select
   **Unlink** next to the LTI provider configuration name.


.. include:: ../../../../links/links.rst
