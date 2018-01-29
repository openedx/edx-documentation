..  _ui_getting_started:

###############
Getting Started
###############

This topic contains a collection of best practices to consider when starting to
develop user interfaces for Open edX.

You should also read :ref:`Contributing to Open edX` to understand
more general best practices, as well as how to submit your new code for review.

--------------------------------------------
Language style guidelines should be followed
--------------------------------------------

To provide consistency for developers, edX defines style guidelines for each
of the languages that are in use. You can read more about these in the chapter
:doc:`../style_guides/index`.

-------------------------------------------
Use server-side rendering whenever possible
-------------------------------------------

Server-side rendering gives the content to the user immediately without
requiring additional round-trips. This can make for large performance
improvements on slow networks or mobile devices.

When a dynamic client-side experience is required, then the server-side page
should include JavaScript code along with the HTML. See the technical
recommendations below for more detail.

-----------------------------------
Front-ends should be self-contained
-----------------------------------

Front end applications require a variety of types of assets that need to be
managed together, including code, styles, templates, and images. These assets
should be co-located with the code for the feature, rather than living in
shared directories. This makes it simpler for new developers to work with the
feature, and it also simplifies the task of removing the feature at some point
in the future.

--------------------------------------------
Designs should be built upon common patterns
--------------------------------------------

In order to provide a consistent experience for all users, designs should be
built upon common patterns. In particular, `Bootstrap`_ provides a number of
standard design patterns that should be used whenever possible. Custom patterns
can be used when necessary, but they should ideally be composed from simpler
Bootstrap elements.

You can learn more in the chapter :doc:`bootstrap`.

------------------------------------------------------------
Front-ends should consume and extract reusable UI components
------------------------------------------------------------

When developing new applications, developers should prefer reuse of existing
components over building custom front end logic. For applications built with
`React`_, the `Paragon`_ library provides a number of accessible components.
All other applications should consider using `Bootstrap`_ components.

If a new component is required, you should consider whether it could itself be
added to Paragon as a reusable component. This ensures that future development
can reuse this component, while also standardizing how it behaves for the user
in terms of user interface, accessibility, theming and so on.

-------------------------------------------------------------
Features should work equally well on mobile and web platforms
-------------------------------------------------------------

Open edX provides iOS and Android applications in addition to its web
applications, and so new learner features need to be implemented for all three
platforms. The simplest way to achieve feature parity is to provide a
responsive web experience that can be used on phones and tablets as well as on
desktops and laptops. Using `Bootstrap`_ helps with this by providing a
responsive grid system along with components that work equally well on mobile
and web.

-----------------------------------------
Designs should be accessible to all users
-----------------------------------------

Open edX measures and evaluates accessibility using the World Wide Web
Consortium’s `Web Content Accessibility Guidelines (WCAG) 2.0`_. All features
merged into edX repositories are expected to conform to Level AA of this
specification and to satisfy the requirements outlined in the `edX Website
Accessibility Policy`_.

You can learn more about developing accessible applications in the chapter
:doc:`../conventions/accessibility`.

---------------------------------------------------
User interfaces should support internationalization
---------------------------------------------------

Open edX is used by learners all over the world, and so it is critical that all
new functionality can be localized. This means that every string in an
application should be marked for translation, as well as ensuring that all new
user interfaces will switch to right-to-left mode when the language requires it.

You can learn more about internationalization in the section
:doc:`../internationalization/index`.

------------------------------------------------
Front end implementations should support theming
------------------------------------------------

Open edX is used by many different organizations, and each one requires that
the user experience is based upon their own brand. This includes elements as
simple as overriding the fonts, imagery and color schemes, to more complex
customizations such as custom headers, footers and registration flows.

You can learn more about how Open edX supports theming with the guide `Changing
Themes for an Open edX Site`_.

-------------------------------------------------------
Front end code should be safe from cross site scripting
-------------------------------------------------------

Cross Site Scripting (XSS) vulnerabilities allow user-supplied data to be
incorrectly executed as code in a web browser. This can allow an attacker to
inject malicious scripts, which in the worst case can cause the loss of private
user data.

In order to keep your code safe from such attackers, you should follow the best
practices laid out in the chapter :doc:`../conventions/preventing_xss`.

.. Link destinations

.. _Bootstrap: https://getbootstrap.com/docs/4.0/getting-started/introduction/
.. _Changing Themes for an Open edX Site: http://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/open-release-eucalyptus.master/configuration/changing_appearance/theming/index.html
.. _edX UI Toolkit: http://ui-toolkit.edx.org/
.. _edX Website Accessibility Policy: https://www.edx.org/accessibility
.. _Paragon: https://github.com/edx/paragon
.. _React: https://facebook.github.io/react/
.. _Web Content Accessibility Guidelines (WCAG) 2.0: http://www.w3.org/TR/WCAG/
