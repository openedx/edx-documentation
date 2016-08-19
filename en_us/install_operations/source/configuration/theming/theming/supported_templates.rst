.. _Supported Themable Templates:

****************************
Supported Themable Templates
****************************

In theory, all core Mako templates in the LMS and Studio can be overriden
by themed templates. In practice, most of the system assumes that core templates
will *not* be overridden by themed templates, and you might see unexpected
behavior if you override certain templates.
So far, the list of supported themable templates is limited to the following set.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Component
     - Template
     - Description

   * - LMS
     - ``header.html``
     - The page header for the LMS. This template is used for the
       top of the ``<body>`` element on the page, not for the ``<head>`` element
       of the page. EdX recommends that you start by copying the contents of
       the ``navigation.html`` core template, and modifying it as necessary.

   * - LMS
     - ``footer.html``
     - The page footer for the LMS. EdX recommends that you start by copying the
       contents of the ``footer.html`` core template, and modifying it
       as necessary.

.. note::
   Currently, you can only override templates that are loaded by the
   Mako templating system.
   You can override Mako templates and Underscore templates that are
   loaded using the ``<%static:include%>`` Mako template tag.
   You cannot override Django templates.
