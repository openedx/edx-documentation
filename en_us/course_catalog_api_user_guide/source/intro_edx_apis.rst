.. _Course Catalog API Introduction:

#############################
Introduction
#############################

Welcome to the Course Catalog API user guide. This guide will help you get set
up to use the edX Course Catalog API and give you the information you need to
return the results you want.

.. _EdX APIs:

******************************************
Accessing the edX Course Catalog API
******************************************

The edX Course Catalog API is a set of representational state transfer (REST)
web services. To access the edX REST web services (and the Course Catalog API),
you must authenticate as a client. When you authenticate, edX REST web services
verify your identity as a client and associate your identity with a specific
edx.org user. For more information about authentication, see :ref:`edX API
Authentication`.

To authenticate, you need the following items.

* Client credentials. Your credentials consist of a client ID and client
  secret. For more information, see :ref:`getting_a_client_id_and_secret`.

* An access token. You use this access token when you make API requests. For
  more information, see :ref:`getting_an_access_token`.

After you have received your credentials and access token, to use the edx
Course Catalog API, you use your access token to make REST web services
requests at api.edx.org. For more information, see
:ref:`using_an_access_token` and :ref:`Course Catalog API`.
