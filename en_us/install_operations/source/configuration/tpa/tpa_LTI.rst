.. _Configuring Open edX for LTI Authentication:

###############################################################
Configuring Open edX for LTI Authentication
###############################################################

After you :ref:`configure your edX instance as an LTI tool provider<Configuring
an edX Instance as an LTI Tool Provider>`, you can configure LTI authentication
between your Open edX installation and an LTI tool consumer.

Every learner who accesses content on an Open edX system must have a user
account. The Open edX system uses the accounts to collect data, including
grades, for learner interactions with courseware.

When you use LTI authentication between your Open edX system and the system
that is the tool consumer, when learners first encounter content from your Open
edX system in the context of the LTI tool consumer they are prompted to
register Open edX accounts. The Open edX account that each learner creates is
linked to that learner's credentials for the tool consumer. As a result, after
the initial account registration the learner is not prompted separately for
account credentials.

Your organization might prefer this authentication workflow if legal
requirements or privacy concerns require learners to knowingly establish an
identity in an Open edX system.

.. contents::
   :local:
   :depth: 1

**************************************************
Configure LTI Authentication
**************************************************

To configure LTI authentication between your Open edX installation and an LTI
tool consumer, follow these steps.

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

#. To customize the registration process for learners, you make selections for
   these optional fields.

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
