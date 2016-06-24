.. _eliminating_pii_third_party_authentication:

###############################################
Eliminating PII From Third-Party Authentication
###############################################

Open edX sites and edX Edge do not require any personally identifying
information (PII) about learners during third-party authentication. Your
identity provider (IdP) service can send only non-personal identifiers to
create edX site user profiles for learners. If you configure third-party
authentication in this way, the edX site never holds any PII for your learners.

After you have configured third-party authentication at an edX site, the edX
site log in page displays a link to your IdP service. Learners follow that
link, log in using their authentication credentials for your institution, and the IdP
directs them back to the edX log in page, along with an authentication token
containing information about the learner.

The IdP authentication token includes an identifying string for a learner. This
identifier serves as a link between the personal identifying information that
your institution maintains for a learner and the edX profile for that user. The
identifying string does not need to include any PII for the learner. The
identifying string is sometimes referred to as an opaque identifier because it
does not make the identity of the learner visible.

When learners use third-party authentication to log into an edX site for the
first time, they create an edX learner profile. The new edX learner profile is
permanently associated with the identifying string included in the IdP
authentication token. Learners may enter an edX username, email address, and
other information in their profiles. The information that learners enter does
not need to be personally identifying. For more information, see
:ref:`creating_learner_accounts_without_pii`.

The following diagram shows how an IdP can direct a learner to an edX site to
create a learner profile, without transmitting any PII.

.. image:: ../../../../shared/images/tpa-idp-create-non-personal-account.png
  :width: 900
  :alt: A diagram showing how an identity provider (IdP) service can create a
      learner profile on an edX site without transmitting any personally
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

*****************************************
Creating edX Learner Profiles Without PII
*****************************************

When your IdP directs a learner to an edX site for the first time, the learner
enters information to create an edX site profile. The username in a profile
identifies the learner in course discussions and in records such as course
grades. The edX site sends course updates to the email address in a learner
profile.

To avoid storing PII on an edX site, learners can enter non-personally
identifying information in their profiles. For example, a learner can use an
alias as a username and create a non-identifying email address to receive
course updates.

You can include information that will be included in the edX learner profile in
the authentication token that your IdP sends during third-party authentication.
Authentication tokens can contain a username, first name, last name, and
username that will appear in the form fields that learners use to create an edX
learner profile.

If you want to eliminate PII from the edX learner profiles that use third-party
authentication, you should not include personally identifying information in
the authentication token. The only piece of information that is required in the
authentication token is the user ID, which should not be personally
identifying.

For more information about configuring the information in a third-party
authentication token, see :ref:`Configuration Options for SAML Providers`.

.. _ensuring_learner_email_addresses_do_not_contain_pii:

***************************************************
Ensuring Learner Email Addresses Do Not Contain PII
***************************************************

EdX site learners receive email messages that contain information about the
courses they are taking. An email address is required for every edX learner
profile. Because email addresses may be personally identifying, you might
choose to supply an alias email address for learners who use third-party
authentication.

You can include an email address in the third-party authentication token that
your IdP sends when it redirects learners to an edX site. The email address
will appear in the email address field of the edX registration page when a
learner visits the edX site for the first time.

If you supply a non-identifying email address in the authentication token, and
make that email address an alias for a learner's institutional email address,
the learner will receive edX course information at the instituional email
address.

For example, if a learner's institutional email address is jsmith@school.edu,
you might generate a non-identifying email address such as
650EAB0C-E750-4F5D-9426-74F5D078A220@school.edu and make that generated address
an alias of jsmith@school.edu. If you supply the non-identifying email address
in the third-party authentication token, the learner can receive course email
conveniently, without storing a personally identifying email address at the edX
site.

For more information about including an email address in a third-party
authentication token, see :ref:`Configuration Options for SAML Providers`.

.. note::
    Learners can alter the information in the fields of the edX site registration page, before they create their profiles. If you supply an alias email address, make sure that learners understand that they should not alter it before creating their profiles.
