.. _Enterprise API Introduction:

#############################
Introduction
#############################

Welcome to the Enterprise API user guide. This guide will help you get set
up to use the edX Enterprise API and give you the information you need to
return the results you want for your edX for Business integration.

.. _About the Enterprise API:

******************************
About the edX Enterprise API
******************************

The edX Enterprise API is part of edX for Business, which provides corporations
and other enterprises the ability to provide their employees with access to the
thousands of high-quality online courses on the edX platform. An enterprise
uses the edX Enterprise API to retrieve its custom course catalog and display
the course information in the enterprise LMS or other system. You can also use
the API to enroll learners in specified courses in your course catalog.

The edX Enterprise API is a REST web services API. You must provide an
API client (a program, utility, or other tool that you can use to exchange
messages with an API) to make requests and receive response data about courses
in your course catalog from the edX Enterprise API. The edX Enterprise API
uses JavaScript object notation (JSON) as the primary format for return data,
or representation. It can also return data in XML format. The enterprise’s
integration must take and transform this response data and display it to
learners in the enterprise LMS or other system where learners can discover
available edX learning opportunities.

The Enterprise API is designed for server-to-server communication. The best
practice is to develop an API client that makes requests for the course catalog
data not more frequently than daily. Do not embed Enterprise API calls directly
in user-facing pages. Instead, design your system to cache course catalog
information, which user-facing pages then retrieve from the cache.

To access the edX Enterprise API, you must authenticate as a client. When you
authenticate, the edX API verifies your identity as a client and associates your identity with a specific edx.org user. For more information about
authentication, see :ref:`edX API Authentication`.

After you have received your credentials and access token, to use the edx
Enterprise API, you use your access token to make API requests at
api.edx.org.

.. _Using Enterprise API:

*****************************************************
Using the edX Enterprise API with Your Course Catalog
*****************************************************

EdX works with you to create a curated course catalog for your enterprise. You
then use the edX Enterprise API to retrieve information about your course
catalog and display it to your learners, so that they can discover and enroll
in edX learning opportunities.

EdX offers over a thousand courses covering a wide variety of subjects, from
supply chain management to cybersecurity to jazz appreciation. EdX can help an
enterprise curate a list of courses and programs that are most relevant to the
enterprise’s learning needs. The curated list of edX courses that a learning
manager selects and makes available through the enterprise portal is called the
course catalog.

.. _Using Enrollment API:

******************************
Using the edX Enrollment API
******************************

The edX Enterprise API also includes an enrollment API, which you can use to
directly enroll your learners in selected courses. For more information, see
:ref:`course_enrollments Endpoint`.

