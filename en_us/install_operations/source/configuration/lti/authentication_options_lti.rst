.. _Options for LTI Authentication and User Provisioning:

########################################################
Options for LTI Authentication and User Provisioning
########################################################

When you use your Open edX system as an LTI tool provider, data is collected by
the Open edX system for all learner activity. Each learner has a user account
on the Open edX system that is linked to the user account on the tool consumer
system, so that activity, grades, and state can be passed from one system to
the other.

The Open edX system supports these user authentication flows for LTI.

.. contents::
   :local:
   :depth: 1

.. _Anonymous User Authentication:

******************************
Anonymous User Authentication
******************************

The first time a learner encounters an Open edX resource in a course, the
Open edX content is immediately launched by a POST to the URL. Without
requiring any action from the learner, the Open edX system creates a user
account and provisions it with a system-generated username, and links it to
the tool consumer user account for that learner. Learners never interact with
the Open edX system directly.

This authentication flow presents a virtually seamless experience that
significantly reduces user error. The Open edX system passes learner data to
the tool consumer with no subsequent reconciliation of data between the
systems.

After you :ref:`configure your edX instance as an LTI tool provider<Configuring
an edX Instance as an LTI Tool Provider>`, no further configuration is needed
on your Open edX system for this user authentication flow.

******************************
Open edX User Authentication
******************************

The first time a learner encounters an Open edX resource in a course, he is
prompted to either sign in with existing credentials or create a user account.
The Open edX system creates a user account and provisions it with the supplied
values, and links it to the tool consumer user account for that learner. The
POST to the URL then delivers the Open edX resource in the tool consumer. After
the initial sign in or account creation step, learners do not interact with the
Open edX system directly.

In this authentication flow, learners knowingly establish or use credentials on
the Open edX system. This flow provides a smooth learner experience that can
also satisfy legal requirements or privacy concerns.

After you configure your edX instance as an LTI tool provider, you can
:ref:`configure Open edX user authentication<Configuring Open edX for LTI
Authentication>` between your Open edX system and the tool consumer.
