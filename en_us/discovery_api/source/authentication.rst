.. _edX API Authentication:

###############################################
Authenticating as an edX REST Web Service User
###############################################

API clients must authenticate when they make API requests to the Discovery
API. Authenticating allows the Discovery API to verify the identity of the
client and associate that identity with a specific edX for Business customer.
To use the Discovery API, you need to generate a set of API credentials,
consisting of a client identifier and a client secret string. To obtain your
API credentials, complete the following steps.

#. Register at http://www.edx.org by creating a new user account for your
   company. The name you enter in the Public Username field must match the
   name of your company. For example, if your company is named Example, Inc.,
   enter a name like Example or ExampleInc in the Public Username field.

#. After you have created an account, go to ``http://courses.edx.org/api-admin``
   and fill out the API Access Request form. The name you enter in the
   **Company Name** field must be identical to the **Public Username** that you
   used to register on edx.org. For example,  if your Public Username is
   ExampleInc, the Company Name must also be ExampleInc.

#. After you submit the API Access Request form, edX will create a course
   catalog for you and then send you an email describing how to generate
   your client identifier and client secret string. You can then use the
   client identifier and secret string to access your Discovery APIs

When a client authenticates with the edX Enterprise API, the client
completes the following process.

* The client presents a client identifier and a secret string to the
  ``https://api.edx.org/oauth2/v1/access_token`` authentication resource and receives an access
  token.

* The client includes the access token when the client makes another API
  request.

An access token is a text string that includes encoded information
about the client, the user, and the period of time in which the token is valid.
Access tokens expire after a period of time that is specified when you request
them. After an access token expires, you must get a new token from the
``https://api.edx.org/oauth2/v1/access_token`` authentication resource.

**************************
Obtaining an Access Token
**************************

To obtain an access token, you submit a POST request to the
``https://api.edx.org/oauth2/v1/access_token`` authentication resource. Include a string in the
message body of your POST request that contains your client identifier,
client secret, grant type (``client_credential``), and token type (``jwt``),
as shown in the following example, replacing ``{client_id}`` and
``{client_secret}`` with your actual client ID and secret.
::

  curl -X POST https://api.edx.org/oauth2/v1/access_token -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&token_type=jwt"


The response you receive contains the access token value that you can use to
submit further requests to the edX Enterprise API. For example:
::

  {
    “access_token”: “g1Bb0usqwe345ty…”,
    “token_type”: “JWT”,
    “expires_in”: “36000”,
    “scope”: “read write profile email”
  }
