
*************************************
Setting Up User Retirement in the LMS
*************************************

This section describes how to set up and configure the user retirement feature
in the Open edX LMS.

Django Settings
***************

The following Django settings control the behavior of the user retirement
feature. Note that some of these settings values are lambda functions rather
than standard string literals.  This is intentional; it is a pattern for
defining *derived* settings specific to Open edX.  Read more about it in
`openedx/core/lib/derived.py
<https://github.com/edx/edx-platform/blob/fdc50c3/openedx/core/lib/derived.py>`_

RETIRED_USERNAME_PREFIX
    Default: ``'retired__user_'``

    The prefix part of hashed usernames.  Used in ``RETIRED_USERNAME_FMT``.
RETIRED_EMAIL_PREFIX
    Default: ``'retired__user_'``

    The prefix part of hashed emails.  Used in ``RETIRED_EMAIL_FMT``.
RETIRED_EMAIL_DOMAIN
    Default: ``'retired.invalid'``

    The domain part of hashed emails.  Used in ``RETIRED_EMAIL_FMT``.
RETIRED_USERNAME_FMT
    Default: ``lambda settings: settings.RETIRED_USERNAME_PREFIX + '{}'``

    The username field for a retired user gets transformed into this format,
    where ``{}`` is replaced with the hash of their username.
RETIRED_EMAIL_FMT
    Default: ``lambda settings: settings.RETIRED_EMAIL_PREFIX + '{}@' + settings.RETIRED_EMAIL_DOMAIN``

    The email field for a retired user gets transformed into this format, where
    ``{}`` is replaced with the hash of their email.
RETIRED_USER_SALTS
    A list of salts used for hashing usernames and emails.  Only the last item
    in this list is used as a salt for all new retirements, but historical
    salts are preserved in order to guarantee that all hashed usernames and
    emails can still be checked.

    The default value MUST be overridden!
RETIREMENT_SERVICE_WORKER_USERNAME
    Default: ``'RETIREMENT_SERVICE_USER'``
    The username of the retirement service worker.
RETIREMENT_STATES
    A list which defines the name and order of states for the retirement
    workflow.  See `Retirement States`_ for details.

Retirement States
*****************

The state of each user's retirement is stored in the LMS database, and the
state list itself is also separately stored in the database.  We expect the
list of states will be variable over time and across different Open edX
installations, so it is the responsibility of the administrator to populate
the state list.

The default states are defined in `lms/envs/common.py
<https://github.com/edx/edx-platform/blob/fe82954/lms/envs/common.py#L3421-L3449>`_
in the ``RETIREMENT_STATES`` setting.  There must be, at minimum, a ``PENDING``
state at the beginning, and ``COMPLETED``, ``ERRORED``, and ``ABORTED`` states
at the end of the list.  Also, for every ``RETIRING_foo`` state, there must be
a corresponding ``foo_COMPLETE`` state.

Override these states if you need to add any states.  Typically, these settings are set in ``lms.envs.json``.

After you have defined any custom states, populate the states table with the following management command:

.. code-block:: bash

   $ ./manage.py lms --settings=<your-settings> populate_retirement_states

   All states removed and new states added. Differences:
      Added: set([u'RETIRING_ENROLLMENTS', u'RETIRING_LMS', u'LMS_MISC_COMPLETE', u'RETIRING_LMS_MISC', u'ENROLLMENTS_COMPLETE', u'LMS_COMPLETE'])
      Removed: set([])
      Remaining: set([u'ERRORED', u'PENDING', u'ABORTED', u'COMPLETE'])
   States updated successfully. Current states:
   PENDING (step 1)
   RETIRING_ENROLLMENTS (step 11)
   ENROLLMENTS_COMPLETE (step 21)
   RETIRING_LMS_MISC (step 31)
   LMS_MISC_COMPLETE (step 41)
   RETIRING_LMS (step 51)
   LMS_COMPLETE (step 61)
   ERRORED (step 71)
   ABORTED (step 81)
   COMPLETE (step 91)

In this example, some states specified in settings were already present, so
they were listed under "Remaining" and were not re-added. The command output
also prints the "Current states"; this represents all the states in the
states table. The ``populate_retirement_states`` command is idempotent, and
always attempts to make the states table reflect the ``RETIREMENT_STATES``
list in settings.

.. _retirement-service-user:

Retirement Service User
***********************

The user retirement driver scripts authenticate with the LMS and IDAs as the
retirement service user with oauth client credentials.  Therefore, to use the
driver scrpits, you must create a retirement service user, and generate a DOT application and client credentials, as in the following command.

.. code-block:: bash

   app_name=retirement
   user_name=retirement_service_worker
   ./manage.py lms --settings=<your-settings> manage_user $user_name $user_name@example.com --staff --superuser
   ./manage.py lms --settings=<your-settings> create_dot_application $app_name $user_name

The client credentials (client ID and client secret) will be printed to the
terminal, so take this opportunity to copy them for future reference.  You
will use these credentials to configure the driver scripts. For more
information, see :ref:`driver-setup`.

The retirement service user needs permission to perform retirement tasks, and
that is done by specifying the ``RETIREMENT_SERVICE_WORKER_USERNAME`` variable
in Dango settings:

.. code-block:: python

   RETIREMENT_SERVICE_WORKER_USERNAME = 'retirement_service_worker'

.. _waffle-switch-for-ux:

Waffle Switch to Display the Delete My Account Feature
******************************************************

A waffle switch named ``course_experience.gdpr`` controls whether the Account
page displays the section named **Delete My Account****. If you do not
activate this switch, learners will have no available mechanism to request
account deletion.

You can manage waffle switches from the Django Admin section "Waffle" ->
"Switches".

Django Admin
************

The Django admin interface contains the following models under ``USER_API``
that relate to user retirement:

Retirement states : ``/admin/user_api/retirementstate/``
    Represents the table of states defined in ``RETIREMENT_STATES`` and
    populated with ``populate_retirement_states``.
User Retirement Requests : ``/admin/user_api/userretirementrequest/``
    Represents the table which simply tracks the user ids of every learner who
    has ever requested account deletion.  This table is primarily used for
    internal bookkeeping, and normally isn't useful for administrators.
User Retirement Statuses : ``/admin/user_api/userretirementstatus/``
    Model where the retirement state for each individual learner can be
    managed, if necessary.

In special cases where you may need to manually intervene with the pipeline,
you can use the User Retirement Statuses management page to change the
state for an individual user.  For more info on handling these cases, see
:ref:`handling-special-cases`.
