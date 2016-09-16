.. _Create a Site:

#############################
Create an Open edX Site
#############################

To create an Open edX site, follow these steps.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. Select **Sites** to open the ``http://{your_URL}/admin/sites/site`` page.

#. Enter the domain name for the site. This is the domain name in the URL for
   the site. For example, ``myuniversity.edu``.

   To make a site available on a non-default port that is entered as part of
   the URL, the domain name must include the port number. For example, if an
   LMS site is available at ``my-site.localhost:8000``, the domain name for
   the site must be ``my-site.localhost:8000``.

#. Select **Save**.
