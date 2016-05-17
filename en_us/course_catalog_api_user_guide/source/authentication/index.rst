.. _edX API Authentication:

###############################################
Authenticating as an edX REST Web Service User
###############################################


The edX Course Catalog API is a set of REST web services. A REST web services
client is a program, utility, or other tool that you can use to exchange HTTP
messages with a REST web service. When you use edX REST web services, you use a
web services client to make requests and receive response data. Clients for
REST web services must authenticate when they make REST requests at
api.edx.org. Authenticating allows edX web services to verify the identity of
the client and associate that identity with a specific edX.org user.

When a REST client authenticates with an edX REST web service, the client
completes the following process.

* The client presents a client identifier and a secret string to the
  ``/oauth2/v1/access_token`` authentication resource and receives an access
  token.

* The client includes the access token when it makes another REST web services
  request.

An access token is a text string that includes encoded information about the
client, the user, and the period of time in which the token is valid. Access
tokens expire after a period of time that is specified when you request them.
After an access token expires, you must get a new token from the
``/oauth2/v1/access_token`` authentication resource.

The following diagram shows a REST client presenting its client ID and client
secret to the ``/oauth2/v1/access_token`` authentication resource. The
authentication resource returns an access token.

.. image:: ../../../shared/images/api-authentication-get-token.png
  :width: 800
  :alt: A diagram showing a REST client application presenting ID and secret
      credentials to the authentication web service and receiving an access
      token.

The following diagram shows a REST client presenting an access token when it
requests a REST resource. After the REST web service accepts the access token,
it returns the resource data.

.. image:: ../../../shared/images/api-authentication-present-token.png
  :width: 800
  :alt: A diagram showing a REST client application presenting an access
      token when it requests a REST resource from api.edx.org.

The edX REST web services use the OAuth 2.0 standard for authentication. OAuth
2.0 is an open standard used by many systems that require secure user
authentication. See the `OAuth 2.0 Standard`_ for more information.

The example REST requests shown in this guide use the ``curl`` command-line
program to send HTTP messages to edX web services. You can use any technology
to send REST requests. The examples use the ``curl`` program to show the syntax
and data for a request in a way that is easy to read. For more information
about the ``curl`` program, see `curl client program`_.

The following sections provide more information about authenticating as an edX
REST web services user.

.. contents::
   :local:
   :depth: 1

.. _getting_a_client_id_and_secret:

*************************************
Getting a Client ID and Client Secret
*************************************

Your API client credentials consist of a client ID and a client secret. EdX
generates your client credentials after you request access to the edX REST web
services.

To obtain your client credentials, complete the following steps.

.. contents::
   :local:
   :depth: 1

The following example shows a client ID and client secret.

.. code-block:: none

    Application Name: My REST Web Services Application

    API Client ID: VBn1F8ArNOiviEKq05UHu9oI0h4OkrEA29DPbzwe

    API Client Secret: wDSbtup7r7Ifr6s7vs5Xjlqu2I MD2TmaMutVMZF8AGXn9LqZv9P9oE7
    3pAV6L4iZxzqtQB3MPmrKEZbtaFMUqjZKzg98xMu5QzboPDQSBL72hfPdPjagkBdmLjQXuTmk

.. _Obtain EdX User Account and Sign In:

===================================
Obtain EdX User Account and Sign In
===================================

To obtain an edX user account, contact the edX marketing team. The team will
send you an account username and instructions for setting your password.

To sign in to edX and change your password, go to
https://courses.edx.org/login.


.. _CC API Complete Access Request Form:

========================================
Complete the EdX API Access Request Form
========================================

After you have signed in to edX, follow these steps.

#. Go to http://courses.edx.org/api-admin.
#. On the **EdX API Access Request** page, enter the information for your
   organization. All fields are required.

    * **Company Name**: The name of your company.
    * **Website**: The URL for your company's website.
    * **Company Address**: Your company's mailing address. This can be a street
      address or a post office box.
    * **Application Description**: A brief description of the main use for your
      application.

#. At the bottom of the form, select the **Terms of Service** check box.
#. Select **Request API Access** to submit your request.

After you submit the request form, edX will review your request, and then edX
will send you an email message approving your request or providing more
information.

.. _CC API Generate API Credentials:

========================
Generate API Credentials
========================

When you receive your approval email message from edX, follow these steps.

#. Go to http://courses.edx.org/api-admin/status.
#. On the page that opens, enter the following information.

   * Name: An identifying name that you assign to your application.
   * Redirect URIs (optional): The redirect URL or URLs for your application.
     Not all edX REST web services clients use redirect URLs. For example, you
     do not need a redirect URL to use the Course Catalog API.

#. Select **Generate API client credentials**.

The screen displays your application name, client ID, client secret, and any
redirect URIs that you entered. Make sure that you record your client ID and
client secret.

If you need to regenerate your credentials, go to http://courses.edx.org/api-
admin/status and select **Generate API client credentials** again. Do not
change the existing **Name** and **Redirect URIs** values.

.. _getting_an_access_token:

*********************************************
Getting an Access Token
*********************************************

To get an access token, you send a ``POST`` request to the
``/oauth2/v1/access_token`` authentication resource. The response you receive
contains the access token string.

To get an access token for edX REST web services, follow these steps.

#. Make sure you have the client ID and client secret strings for your REST
   HTTP client.

#. Send a ``POST`` HTTP request to the ``/oauth2/v1/access_token``
   authentication resource. Include your client identifier and client secret in
   the message body of your ``POST`` request. Include the client ID and secret
   in a string that includes ``grant_type=client_credentials`` and
   ``token_type=jwt`` as shown in the following example.

   ``grant_type=client_credentials&client_id={client id}&client_secret={client secret}&token_type=jwt``

   For an example request, see :ref:`example_access_token_request`.

#. Find the access token string in the ``access_token`` object in the JSON
   response data. For more information about the authentication endpoint
   response data, see :ref:`authentication_endpoint_response`.

   The following example access_token object includes an access token string.

   .. code-block:: json

      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmYW1pbHlfbmFtZSI
      6IkJsYWNrYnVybiIsImF1ZCI6Iklua29jdWpMaWt5dWNzRWR3aVdhdGRlYnJFYWNrbWV2TGFr
      RHVpZktvb3Noa2FrV293IiwiaXNzIjoiaHR0cHM6Ly9jb3Vyc2VzLnN0YWdlLmVkeC5vcmcvb
      2F1dGgyIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiY2xpbnRvbmIiLCJnaXZlbl9uYW1lIjoiQ2
      xpbnRvbiIsImV4cCI6MTQ5NDA5ODQwOCwiaWF0IjoxNDYyNTYyNDA5LCJlbWFpbCI6ImNibGF
      ja2J1cm5AZWR4Lm9yZyIsIm5hbWUiOiJDbGludG9uIEJsYWNrYnVybiJ9.mumH2jIpUtweprF
      Av1JwlFnm13a4-UyFktzegFa9doE"


.. _example_access_token_request:

====================================
Example Access Token Request
====================================

The following example ``curl`` program command requests an access token from
the api.edx.org authentication endpoint.

.. code-block:: bash

    curl -X POST \
    -d "grant_type=client_credentials&client_id=VBn1AkrAE28ArNOiziEKq03UGu9oI0h
    4O9DPbvwe&client_secret=wERatup7r7ItaFMUqjZKzg98xLu6QzboPEQSBL72hfr6s7vx5Xj
    lqu2IMC2TnaMutVLZF9AGXn9LqZv9P9oE73pAV6L4iZxzpuQB3MPmrKEZbfPdPjagkBdmLjQXuT
    mk&token_type=jwt" \
    https://api.edx.org/oauth2/v1/access_token

.. _authentication_endpoint_response:

==================================================
Understanding the Authentication Endpoint Response
==================================================

The api.edx.org authentication endpoint returns JSON data that includes an
access token string and information about that access token.

The objects in the authentication endpoint response data are described in the
following list.

* access_token: The access token string that you can use to make REST requests.

* expires_in: The length of time, in seconds, that the access token will be
  accepted.

* scope: The internal resources that your REST client has access to. You do not
  need to use the information in the ``scope`` object.

* token_type: A description of the format of the access token. You specify the
  format of an access token when you use it to make REST requests.


The following example JSON response data shows the ``access_token`` object and
the access token string.

.. code-block:: json

    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmYW1pbHlfbmFtZ
        SI6IiIsImF1ZCI6Iklua29jdWpMaWt5dWNzRWR3aVdhdGRlYnJFYWNrbWV2TGFrRHVpZktv
        b3Noa2FrV293IiwiaXNzIjoiaHR0cHM6Ly9jb3Vyc2VzLnN0YWdlLmVkeC5vcmcvb2F1dGg
        yIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGRlc2phcmRpbnMiLCJnaXZlbl9uYW1lIjoiIi
        wiZXhwIjoxNDYyODQ2NjAyLCJpYXQiOjE0NjI4MTA2MDIsImVtYWlsIjoicGRlc2phcmRpb
        nNAZWR4Lm9yZyIsIm5hbWUiOiIifQ.xuHNeNYlPjeayZKRlyasqWNtfwnvF8PyK6Fp5PB50
        EM",
        "expires_in": 36000,
        "scope": "read write profile email",
        "token_type": "JWT"
    }

.. _using_an_access_token:

*********************************************
Using an Access Token to Make REST Requests
*********************************************

To make an api.edx.org REST request, you include an access token string in the
``Authorization`` HTTP header field. In addition to the access token string,
you specify the token type, for example ``JWT``.

The following example ``curl`` program command sends a REST request to an
api.edx.org endpoint. The example request includes the token type and access
token string in the ``Authorization`` HTTP header field.

.. code-block:: bash

  curl -X GET \
  -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmYW1pbHlfbmFtZ
      SI6IiIsImF1ZCI6Iklua29jdWpMaWt5dWNzRWR3aVdhdGRlYnJFYWNrbWV2TGFrRHVpZktv
      b3Noa2FrV293IiwiaXNzIjoiaHR0cHM6Ly9jb3Vyc2VzLnN0YWdlLmVkeC5vcmcvb2F1dGg
      yIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGRlc2phcmRpbnMiLCJnaXZlbl9uYW1lIjoiIi
      wiZXhwIjoxNDYyODQ2NjAyLCJpYXQiOjE0NjI4MTA2MDIsImVtYWlsIjoicGRlc2phcmRpb
      nNAZWR4Lm9yZyIsIm5hbWUiOiIifQ.xuHNeNYlPjeayZKRlyasqWNtfwnvF8PyK6Fp5PB50
      EM" \
  https://api.edx.org/catalog/v1/catalogs/

.. include:: ../../../links/links.rst
