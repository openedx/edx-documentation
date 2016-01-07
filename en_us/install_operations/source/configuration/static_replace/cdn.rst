.. _Enabling a CDN for Course Assets:

######################################
Enabling a CDN for Course Assets
######################################

By default, all course assets are served directly from your Open edX instance.
For courses with large enrollments, or courses with large assets, such as high-
quality images, PDFs, or video files, this can increase not only the load on
the instance but also the time it takes for learners to load the courses on
their computers and mobile devices.

You can configure your Open edX instance to serve assets from a content
delivery network (CDN) instead. Using a CDN offloads the work required to
deliver assets from your Open edX instance.

.. note:: Whether you need a CDN depends on the type, and amount, of content
  in your courses. Not all installations need a CDN for their course assets.


.. contents::
   :local:
   :depth: 1

***************
Overview
***************

A CDN, or content delivery network, is a service that places servers all around
the world, and keeps copies of content on those servers. Instead of serving
files from one location, a CDN serves them from whichever server is closest to
the end user. This results in faster download speeds and, ultimately, faster
page loads.

********************************
Guidelines for CDN Configuration
********************************

When you configure a CDN for use with your Open edX instance, you should
identify your Open edX instance as the origin server.

Choose the cache expiration carefully: you want content to be cached long
enough to keep the load on your Open edX instance low, but not so long that
changes made to course assets are not realized within a reasonable amount of
time. As a starting point, edX recommends a cache expiration period of one
hour.

**********************
Enable the CDN
**********************

After you configure your CDN, follow these steps.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. In the **Static_Replace** section, next to **Asset base url configs**,
   select **Add**.

#. Select **Enabled**.

#. Enter the hostname for your CDN provider.

   For example, if you were using CloudFront, this would look something like
   ``d37djvu3ytnwxt.cloudfront.net``.

   Be sure not to include the scheme (``http://`` or ``https://``) when you
   specify the hostname.

#. Select **Save**.

.. include:: ../../../../links/links.rst
