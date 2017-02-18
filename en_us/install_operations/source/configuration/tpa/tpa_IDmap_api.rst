.. _Third Party Auth ID Mapping API:

###############################
Third Party Auth ID Mapping API
###############################

Open edX has an API that can be used to retrieve the association between Open
edX user IDs and the unique user identifiers sent by the external platform.

When an Open edX course is used in an on-premise environment, and SAML, LTI, or
other SSO is enabled to allow learners to authenticate to edX using their on-premise credentials, normally an on-premise identity provider (IdP) sends an
identifier. This identifier is stored in edX and linked to the edX account.
Later, when learners return from an on-premise IdP, edX can authenticate the
learner using their edX account.

Because learners may create Open edX accounts using an alternative identity,
instructors may have difficulty identifying Open edX learners in their courses.
Grade records obtained from Open edX will only contain Open edX learner IDs,
which would be unknown to the on-premise system.

This API can be used for mapping between the edX user ID and the ID provided by
the IdP. This API provides information that allows instructors or course
support staff to figure out the identity of the on-premise learners who are
using the edX course. It also allows grade information coming from Open edX to
be appropriately associated to on-premise learners for uploading to an
on-premise learning management system (LMS) or learner information
system (SIS).

This API is intended to be consumed by on-premise middleware, which combines
the information from an on-premise system. The middleware communicates with the
premise system to get information about the course and enrollment, then uses
that information to control instructor access. The instructor can then perform
tasks such as obtaining the edX learner's on-premise identity, uploading grades
back to their LMS or SIS, and making groups based on on-premise activities.

This API also helps with the issue where learners enter incorrect email
addresses and cannot activate their accounts, and then cannot authenticate with
Open edX through SSO because of the inactive accounts. With this API,
on-premise course support staff or instructors can provide the Open edX
operator with the learner's real edX username instead of the ID that the
IdP passed over to Open edX, so that the Open edX operator does not have
to manually query the tables to figure out the mapping between the source
system ID and the Open edX username.

*****************************************
Using the Third Party Auth ID Mapping API
*****************************************

To use the Third Party Auth ID Mapping API, follow these steps.

#. Have one or more third party auth providers enabled, and have learners who
   have link their accounts to one or more of those providers.

#. Set up an OAuth2 client. To do this, open the Django administration panel,
   select **OAuth2**, select **Client**, select **Add Client**, and then enter
   the following information.

   #. For **User**, create a dedicated user for this API.
   #. For **URL, Redirect URL**, enter a dummy value such as
      ``http://localhost/``. The URL is not used for this API.
   #. For **Client Type**, specify **Confidential**.
   #. Leave other fields with the default values.

#. Give the new client permission to this API. To do this, go to
   **Third_Party_Auth**, select **Provider API Permissions**, and then select
   **Add Provider API Permission**.

#. Select the OAuth2 client that you just created, and select an external
   authentication provider. This will give the new client access to query that
   provider mapping.

The API is now available at ``{LMS base
URL}/api/third_party_auth/v0/providers/{provider_id}/users``. The API client
must use OAuth2 to authenticate before that endpoint will work. The
``{provider_id}`` value uses the same format as described in :ref:`Hinted Sign
In`.

To test the API, follow these steps.

#. Use client credentials (from the django admin) to get the access token, as
   follows.

    .. code-block:: python

        curl --data "client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=client_credentials" http://localhost:8000/oauth2/access_token

        Returns: {"access_token": "c1efde84445b2f256e1c80886b3f6d46339b84ee", "token_type": "Bearer", "expires_in": 31535999, "scope": ""}

#. Use the access token to issue requests to the API, as in the following
   examples.

    .. code-block:: python

        curl --header "Authorization: Bearer ACCESS_TOKEN" http://localhost:8000/api/third_party_auth/v0/providers/{provider_id}/users

        curl --header "Authorization: Bearer ACCESS_TOKEN" http://localhost:8000/api/third_party_auth/v0/providers/{provider_id}/users?username=USERNAME1,USERNAME2

        curl --header "Authorization: Bearer ACCESS_TOKEN" http://localhost:8000/api/third_party_auth/v0/providers/{provider_id}/users?username=USERNAME1&username=USERNAME2

        curl --header "Authorization: Bearer ACCESS_TOKEN" http://localhost:8000/api/third_party_auth/v0/providers/{provider_id}/users?remote_id=REMOTE_ID1,REMOTE_ID2

        curl --header "Authorization: Bearer ACCESS_TOKEN" http://localhost:8000/api/third_party_auth/v0/providers/{provider_id}/users?remote_id=REMOTE_ID1&remote_id=REMOTE_ID2

The following example shows a return value from the API.

    .. code-block:: python

       {
         "page": 1,
         "page_size": 200,
         "count": 8,
         "results": [
           {"username": "USERNAME1", "remote_id": "REMOTE_ID1"},
           {"username": "USERNAME2", "remote_id": "REMOTE_ID2"},
         ]
       }
