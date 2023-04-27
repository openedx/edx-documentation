*****************************
Process for Contributing Code
*****************************

.. tip::

   Looking for fewer words? Checkout the `concise contributing guide <https://openedx.atlassian.net/wiki/spaces/COMM/pages/941457737/How+to+Start+Contributing+Code>`_

Open edX is a massive project, and we would love you to help us build
the best online education system in the world -- we can't do it alone!
However, the core committers on the project are also developing features
and creating pull requests, so we need to balance reviewing time with
development time. To help manage our time and keep everyone as happy as
possible, we've developed this document that explains what core committers
and other contributors can expect from each other. The goals are:

* Keep pull requests unblocked and flowing as much as possible,
  while respecting developer time and product owner prioritization.
* Maintain a high standard for code quality, while avoiding hurt feelings
  as much as possible.

Overview
--------

Get in touch with us right now! We want to talk to you about your work as early
as possible in your development cycle, ideally when you start designing your
feature. This will help you so much, we promise: we'll help guide your work so
you don't have to rearchitect it late in your development cycle. We'll help you
understand the analytics, performance, test, accessibility, and other various
requirements up front. We'll also be able to let you know if work you're
planning duplicates work edX or others are doing. Finally, we'll let you know
if your proposal, or parts of your proposal, would benefit from the `Open edX
Proposal (OEP) process`_.

You can get in touch with us using our `community discussion forums`_.

.. _community discussion forums: https://discuss.openedx.org/

You should get in touch with us regarding any work you intend to contribute
upstream, including but not limited to these types of contributions.

* Core platform changes (changes to the edx-platform repo).
* Changes to any associated repos (edx-analytics, configuration, XBlock, etc.).
* A new XBlock you're writing that you intend to have run on edx.org.

We do not need to review your code if you are writing a tool or customization for your own installation.

* An XBlock to be run on your own server, not intended to run on edx.org.
* LTI tools that are running on an external server.
* Code you are writing for your own installation, that won't be run on edx.org.

Make sure you've signed a `contribution agreement`_ before you submit code
upstream to any edX owned repo. Please be sure you've at least skimmed the
:doc:`contributor guidelines <contributor>`, especially the :doc:`pull request
cover letter <cover-letter>` guidelines.

If you have any process questions along the way, please reach out to us on the
`community discussion forums`_.

Once you open your pull request, we'll need to review it. What types of review
are necessary will be determined by the complexity of your pull request and
whether or not you've spoken to us before you open your pull request. An
overview of the process is here:

.. image:: pr-process.png
   :align: center
   :alt: A visualization of the pull request process
   :target: ../_images/pr-process.png

.. _Open edX Proposal (OEP) process: http://open-edx-proposals.readthedocs.io/en/latest/
.. _contribution agreement: https://openedx.org/cla

General Guidelines
------------------

Please follow these guidelines when writing code. Please note that not all of
these may be required for your feature; reach out to us if you have any
questions or concerns.

* `Internationalization Coding Guidelines`_
* `RTL UI Best Practices`_
* `Accessibility Guidelines`_
* `Analytics Guidelines`_
* `Eventing Design and Review Process`_

For XBlocks you intend to install on edx.org, please also read the `XBlock
Review Guidelines`_.

.. _Internationalization Coding Guidelines: https://openedx.atlassian.net/wiki/edx.readthedocs.io/projects/edx-developer-guide/en/latest/internationalization/i18n.html
.. _RTL UI Best Practices: https://github.com/openedx/edx-platform/wiki/RTL-UI-Best-Practices
.. _Accessibility Guidelines: http://edx.readthedocs.io/projects/edx-developer-guide/en/latest/accessibility.html
.. _Analytics Guidelines: http://edx.readthedocs.io/projects/edx-developer-guide/en/latest/analytics.html
.. _Eventing Design and Review Process: https://openedx.atlassian.net/wiki/display/AN/Eventing+Design+and+Review+Process
.. _XBlock Review Guidelines: https://openedx.atlassian.net/wiki/display/OPEN/XBlock+review+guidelines

Roles
-----

People play different roles in the pull-request review process.  Each role has
different jobs and responsibilities.

:doc:`core-committer`
    Can commit changes to an Open edX repository.  Core committers are
    responsible for the quality of the code, and for supporting the code in the
    future.  Core committers are also developers in their own right.

:doc:`product-owner`
    Prioritizes the work of core committers.

:doc:`community-manager`
    Helps keep the community healthy and working smoothly.

:doc:`contributor`
    Submits pull requests for eventual committing to an Open edX repository.


If you are a :doc:`contributor <contributor>` submitting a pull request, expect
that it will take a few weeks before it can be merged. The earlier you can
start talking with the rest of the Open edX community about the changes you
want to make, before you even start changing code, the better the whole process
will go.

Follow the guidelines in this document for a high-quality pull request: include
a detailed description of your pull request when you open it on GitHub (we
recommend using a :doc:`pull request cover letter <cover-letter>` to guide your
description), keep the code clear and readable, make sure the tests pass, be
responsive to code review comments. Small pull requests are easier to review
than large pull requests, so split up your changes into several small pull
requests when possible -- it will make everything go faster.  See the full
:doc:`contributor guidelines <contributor>` for details of what to do and what
to expect.

If you are a :doc:`product owner <product-owner>`, treat pull requests from
contributors like feature requests from a customer. Keep the lines of
communication open -- if there are delays or unexpected problems, add a comment
to the pull request informing the author of the pull request of what's going
on. No one likes to feel like they're being ignored! More details are in the
:doc:`product owner guidelines <product-owner>`.

If you are a :doc:`core committer <core-committer>`, allocate some time
in your normal work schedule to review pull requests from other contributors.
The community managers will make sure that these pull requests meet a
basic standard for quality before asking you to spend time reviewing them.
More details are in the :doc:`core committer guidelines <core-committer>`.

Feel free to read the other documentation specific to each individual role in
the process, but you don't need to read everything to get started! If you're
not sure where to start, check out the :doc:`contributor <contributor>`
documentation. Thanks for helping us grow the project smoothly! :)
