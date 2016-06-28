.. _eliminating_pii_third_party_authentication:

###############################################
Eliminating PII From Third-Party Authentication
###############################################

Open edX sites and edX Edge do not require any personally identifiable
information (PII) about learners during third-party authentication. PII is
information that can be used to reveal an individual's identity, such as a
name, identification number, or email address. Your identity provider (IdP)
service can send only non-personal identifiers to create edX site accounts for
learners. If you configure third-party authentication in this way, the edX site
never receives PII from your institution.

.. contents::
   :local:
   :depth: 1

.. note::
  The types of information that constitute PII and requirements for handling it
  are different depending on the laws and regulations that apply to your
  organization. The information in this documentation is intended to explain
  how edX sites can be configured to handle learner data. You cannot rely on
  this documentation as a source of legal guidance.

*****************************************
Creating edX Learner Accounts Without PII
*****************************************

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
authentication token. Learners enter edX usernames, email addresses, and
other information in their accounts. The information that learners enter does
not need to be PII. For more information, see
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
the course. Because the edX site does not hold any personally identifying
information for learners, the usernames do not correspond to learner records
that your institution maintains. If you need to match the scores for edX site
learners to the learner records that your institution maintains, you can use
the third-party authentication ID mapping REST API to retrieve the user ID SAML
attribute and matching edX username for a learner. For more information about
grade reports, see :ref:`opencoursestaff:Access_grades`.

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

*******************************************************
Excluding PII from Authentication Token SAML Attributes
*******************************************************

When your IdP directs a learner to an edX site for the first time, the learner
enters information to create an edX site account. The username in a account
identifies the learner in course discussions and in records such as course
grades. The edX site sends course updates to the email address in a learner
account.

To avoid storing PII on an edX site, learners can enter non-personally
identifying information in their accounts. For example, a learner can use an
alias as a username and create a non-identifying email address to receive
course updates.

If you want to avoid transmitting PII for the edX learner accounts that use
third-party authentication, you should not include personally identifying
information in the authentication token. The only piece of information that is
required in the authentication token is the user ID, which should not be
personally identifying.

For more information about configuring the information in a third-party
authentication token, see :ref:`Configuration Options for SAML Providers`.

.. _specifying_user_account_information_to_exclude_pii

******************************************************
Specifying Non-PII User Account Information By Default
******************************************************

You can include some or all of the information that will be included in an edX
learner account in the SAML attributes of an authentication token. Doing this
can make it less likely that learners will choose to enter PII when they enter
that information themselves. Authentication tokens can contain a username,
first name, last name, and username that will appear in the form fields that
learners use to create an edX learner account. By default, learners do have an
opportunity to edit the information that you send in the authentication token
before creating their accounts.

You can configure third-party authentication to bypass the registration page
that allows learners to update the non-PII information that you send in
authentication tokens. If you do this, you should keep in mind that if the edX
site encounters problems creating an account with the information you supply,
the learner will have an opportunity to update the information and correct the
problem. Also, edX site usernames help learners recognize each other during
course discussions, and a username that you generate might make this more
difficult.

If you choose to supply non-PII information for learner accounts in
authentication tokens, you should help learners understand that they should not
alter that information.

For more information about specifying SAML attributes and skipping the
registration page, see :ref:`Configuration Options for SAML Providers`.

.. _ensuring_learner_email_addresses_do_not_contain_pii:

***************************************************
Ensuring Learner Email Addresses Do Not Contain PII
***************************************************

EdX site learners receive email messages that contain information about the
courses they are taking. An email address is required for every edX learner
account. Because email addresses can be personally identifying, you might
choose to supply an alias email address for learners who use third-party
authentication.

.. note::
    Learners can alter the information in the fields of the edX site
    registration page before they create their accounts. If you supply an
    alias email address, make sure that learners understand that they should
    not alter it before creating their accounts.

You can include an email address in the third-party authentication token that
your IdP sends when it redirects learners to an edX site. The email address
will appear in the email address field of the edX registration page when a
learner visits the edX site for the first time.

If you supply a non-identifying email address in the authentication token, and
make that email address an alias for a learner's institutional email address,
the learner will receive edX course information at the institutional email
address.

For example, if a learner's institutional email address is jsmith@school.edu,
you might generate a non-identifying email address such as 1234@school.edu and
make that generated address an alias of jsmith@school.edu. If you supply the
non-identifying email address in the third-party authentication token, the
learner can receive course email conveniently, without storing a personally
identifying email address at the edX site.

For more information about including an email address in a third-party
authentication token, see :ref:`Configuration Options for SAML Providers`.
