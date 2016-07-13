.. _eliminating_pii_third_party_authentication:

###############################################
Eliminating PII From Third-Party Authentication
###############################################

Open edX sites and edX Edge do not require any personally identifiable
information (PII) about learners during third-party authentication. PII is
information that can be used to reveal an individual's identity, such as a
name. Your identity provider (IdP) service can send only non-personal
identifiers to create edX site accounts for learners. If you configure third-
party authentication in this way, the edX site never receives PII from your
institution.

.. contents::
   :local:
   :depth: 1

.. note::
  The types of information that constitute PII and requirements for handling it
  depend on the laws and regulations that apply to your organization. The
  information in this documentation is intended to explain how edX sites can be
  configured to handle learner data. You cannot rely on this documentation as a
  source of legal guidance.

******************************************************
Creating edX Learner Accounts Without Transmitting PII
******************************************************

After you have configured third-party authentication at an edX site, the edX
site log in page displays a link to your IdP service. Learners follow that
link, log in using their authentication credentials for your institution, and
the IdP directs them back to the edX log in page, along with an authentication
token (a SAML attribute assertion statement) containing information about the
learner.

The IdP authentication token includes an identifying string for a learner. This
identifier serves as a link between the identifying information that your
institution maintains for a learner and the edX account for that learner. The
identifying string does not need to include any PII for the learner. The
identifying string is sometimes referred to as an opaque identifier because it
does not make the identity of the learner visible.

When a learner uses third-party authentication to log into an edX site for the
first time, the edX site creates a learner account. The new edX learner account
is permanently associated with the identifying string included in the IdP
authentication token. Learners will be prompted to create profiles by entering
edX usernames, email addresses, and other information in their accounts.
Learners can take steps to minimize the PII in their profiles. For more
information, see
:ref:`creating_learner_accounts_without_pii`.

The following diagram shows how an IdP can direct a learner to an edX site to
create a learner account, without transmitting any PII.

.. image:: ../../../../shared/images/tpa-idp-create-non-personal-account.png
  :width: 900
  :alt: A diagram showing how an identity provider (IdP) service can create a
      learner account on an edX site without transmitting any personally
      identifying information (PII).

You can download a report containing grades for all learners in the edX courses
that you run. The report includes the edX username for each learner enrolled in
the course, but the usernames may not correspond to learner records that your
institution maintains. If you need to match the scores for edX site learners to
the learner records that your institution maintains, you can use the third-
party authentication ID mapping REST API to retrieve the user ID SAML attribute
and matching edX username for a learner. For more information about grade
reports for edX courses that you run, see :ref:`opencoursestaff:Access_grades`.

.. Institutions may be able to access learner information in other ways. Make
.. the paragraph above more general when we know of those other methods.

The following diagram shows how an institution that uses third-party
authentication can match non-personally identifying edX learner usernames with
the records that the institution holds for those learners.

.. image:: ../../../../shared/images/tpa-institution-associate-edx-id-with-personal-id.png
  :width: 900
  :alt: A diagram showing how an institution that uses third-party
      authentication can match non-personally identifying edX learner usernames
      with the records that the institution holds for those learners.

.. TODO: Add documentation for the third-party authentication ID mapping API.

.. _creating_learner_accounts_without_pii:

**********************************
Minimizing PII in Account Profiles
**********************************

When your IdP directs a learner to an edX site for the first time, the learner
enters information to create an edX site account. The basic information
required for an edX site account is an email address, full name, public
username, password, and country.  Learners may also provide additional personal
details such as gender, year of birth, and educational background.  While
course teams have access to full registration information for learners enrolled
in their courses, only public usernames are used to identify learners in course
discussions and other public-facing course interactions.

To minimize PII stored on an edX site, learners can limit the information in
their edX account profiles to the basic information required for an edX site
account.  Additionally, learners may use random or nondescript public
usernames and create non-identifying email addresses to receive course updates.

If you want to avoid transmitting PII for the edX learner accounts that use
third-party authentication, you should not include personally identifying
information in the authentication token. The only piece of information that is
required in the authentication token is the user ID, which should not be
personally identifying.

For more information about configuring the information in a third-party
authentication token, see :ref:`Configuration Options for SAML Providers`.
