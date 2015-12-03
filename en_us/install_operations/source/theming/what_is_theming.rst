.. _What is Theming:

****************
What is Theming?
****************

Any application, including Open edX, can be loosely divided into two parts:
the user interface ("how it looks"), and the application logic ("how it works").
For example, when considering a multiple choice problem in Open edX, the
user interface consists of how the options are laid out on the page, how the
option selectors look, how the submit button is labelled, what sort of
fonts and colors are used to display the text, and so on. The application logic
consists of how Open edX determines if the student's answer is
correct or incorrect, and how it records that information to be displayed
in the future.

Theming consists of changing the user interface without changing the application
logic. When setting up an Open edX website, the website operator often wants
to use their own logo, modify the color scheme, change links in the
header and footer for SEO (search engine optimization) purposes, and so on.
However, although the user interface may look different,
the application logic must remain the same so that Open edX continues
to work properly. A well-designed theme preserves the general layout
and structure of the user interface, so that users of the website still
find it familiar and easy to use. Be careful about making sweeping changes
to the user interface without warning: your users will be very confused!

From a technical perspective, theming consists of overriding core templates
and core assets with themed templates and themed assets.

* Templates are text files that transform raw data
  (like a student's history of answered problems)
  into HTML pages
  (like a graph of the student's score in the course over time).
* Assets are images, CSS, JavaScript, and any other files
  that are referenced by the HTML files created by the templates.
  For example, a logo image is an asset.

The Open edX platform already comes with a set of templates and assets
that are used in the default user interface; these are known as core templates
and core assets. To create a theme, you simply replace some or all of these
core templates with your own themed templates, as well as replacing some or
all of the core assets with your own themed assets.

There is no limit to the number of themes you can have installed on
your Open edX servers, but only one can be active at a time. Multitenancy
(the ability to have different themes active in different contexts) is not yet
supported.

What Can Be Themed?
*******************

Currently, the LMS and Studio can be themed. All other parts of the Open edX
software do not yet support theming. This includes Insights, XBlocks,
certificates, notification emails, and so on.

Within the LMS and Studio, only a few templates and assets are currently
supported for theming. All templates and assets *can* be themed, but unsupported
templates and assets may be renamed or used differently in the future, and
these changes may occur without notice. The following pages describe the
currently supported templates and assets.

* :ref:`Supported Themable Templates`
* :ref:`Supported Themable Assets`
* :ref:`Supported Themable Sass Variables`
