.. _eliminating_pii_third_party_authentication:

###############################################
Eliminating PII From Third-Party Authentication
###############################################

Open edX sites and edX Edge do not require any personally identifying
information (PII) about learners during third-party authentication. Your
identity provider (IdP) service can send only non-personal identifiers to
create edX site user accounts for learners. If you configure third-party
authentication in this way, the edX site never holds any PII.

After you have configured third-party authentication at an edX site, the log in page for the edX site includes a link to your IdP service. Learners follow that link, log in using authentication credentials for your institution, and the IdP redirects them back to the edX log in page, including an authentication token containing information about the learner.

The IdP authentication token includes an identifying string for a learner. This identifier serves as a link between the personal identifying information that your institution maintains for a learner and the edX account for that user. The identifier must be unique both within your institution and within the edX site. For example, a URI containing a rand

When learners use third-party authentication to log into an edX site for the first time, they create an edX learner account. The new edX learner account is permanently associated with

When your IdP directs learners to the edX site for the first time, the learner

The following diagram shows how an IdP can direct a learner to an edX site, and create a learner account, without transmitting any PII.

.. image:: ../../../../shared/images/tpa-idp-create-non-personal-account.png
  :width: 900
  :alt: A diagram showing how an identity provider (IdP) service can create a learner account on an edX site without transmitting any personally identifying information (PII).

The following diagram shows how an institution that uses third-party authentication can match non-personally identifying edX learner usernames with the records that the institution holds for those learners.

.. image:: ../../../../shared/images/tpa-institution-associate-edx-id-with-personal-id.png
  :width: 900
  :alt: A diagram showing how an institution that uses third-party authentication can match non-personally identifying edX learner usernames with the records that the institution holds for those learners.

*****************************************
Creating edX Learner Accounts Without PII
*****************************************

When


.. _excluding_pii_from_saml_attributes:

***************************************
Excluding PII From SAML Attributes
***************************************

When you configure your IdP to send authentication requests to an edX site, you choose the identifying information that the IdP includes in authentication tokens. The set of information



***************************************
Retrieving Learner Data Without PII
***************************************



***************************************************
Ensuring Learner Email Addresses Do Not Contain PII
***************************************************

