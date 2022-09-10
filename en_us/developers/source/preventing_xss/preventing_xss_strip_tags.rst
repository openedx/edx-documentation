.. _Preventing XSS by Stripping HTML Tags:

Preventing XSS by Stripping HTML Tags
=====================================

.. contents::
   :depth: 2
   :local:

Overview
--------

.. note:: Having server-side HTML data was more likely with our legacy code, but is still possible. We should avoid data with HTML where possible.

There are certain cases where you have server-side HTML and don't want to see escaped HTML, but instead want to either:

-  Strip all HTML tags from your server-side data, or

-  Strip all HTML tags except safe HTML tags (e.g. "<br />") from your server-side data.

In both cases, we use a library called bleach.


Mako filters for bleaching
--------------------------

At the time of writing this, we do not yet have Mako filters for bleaching.  However, that would be very useful._ If you need this, please do the following:

1. See if this was already added, 

2. If not, implement it and add to the `xss-lint repo <https://github.com/openedx/xss-utils>`__.

3. Update this documentation to detail using the filters.

Strip all HTML tags
-------------------

You would typically do this when people have entered HTML tags inside a field in the past, and you no longer want to support HTML, but you also don't want escaped HTML tags to start appearing on the page.

Here is an \ `example using bleach to strip all
tags <https://github.com/openedx/edx-platform/blob/a864b450a889df77f1c7379271dc9a80b3c1a8ee/lms/templates/courseware/progress_graph.js#L76>`__.

Strip all but safe HTML tags
----------------------------

You would do this if you in fact want to allow a user to be able to use certain simple HTML tags, like "<br />", in their input.  Use this sparingly.  It is much simpler to deal with plain text fields.

Here is an \ `example using bleach to only allow basic/safe supported
tags <https://github.com/openedx/edx-platform/blob/e8a36957b1f732974260e7b9b42b9c25148b492c/common/lib/capa/capa/inputtypes.py#L792>`__.

In addition to adding in the HTML to your data, you will probably need to turn off HTML escaping when outputting this data inside a template. The following is an example of this in Mako.

.. code::

    # Sample Mako template with page level HTML-escaping on by default

    # Expression before:

    ${title}

    # Expression after:

    # Title was cleaned with bleach and is safe.
    ${title | n, decode.utf8}
