*******************
Code Considerations
*******************

This is a checklist of all of the things that we expect developers to consider
as they are building new, or modifying existing, functionality.

.. contents::
   :local:
   :depth: 1

Operational Impact
==================

* Are there new points in the system that require operational monitoring?

    * External system that you now depend on (Mathworks, SoftwareSecure,
      CyberSource, etc...)
    * New reliance on disk space?
    * New stand process (workers? elastic search?) that need to always be
      available?
    * A new queue that needs to be monitored for dequeueing
    * Bulk Email --> Amazon SES, Inbound queues, etc...

* Am I building a feature that will have impact on the performance of the
  system? Keep in mind that Open edX needs to support hundreds of thousands if
  not millions of students, so be careful that you code will work well when the
  numbers get large.

    * Deep Search
    * Grade Downloads

* Are reasonable log messages being written out for debugging purposes?
* Will this new feature easily start up in the Vagrant image?
* Do we have documentation for how to start up this feature if it has any
  new startup requirements?
* Are there any special directories/file system permissions that need to be
  set?
* Will this have any impact to the CDN related technologies?
* Are we pushing any extra manual burden on the Operations team to have to
  provision anything new when new courses launch? when new schools start?
  etc....
* Has the feature been tested using a production configuration with vagrant?

See also: :ref:`Deploy a New Service`.

Documentation/Training/Support
==============================

* Is there appropriate documentation in the context of the product for this
  feature, in the form of labels, on-screen help, or mouse over hints? In
  Studio, each page has a context-sensitive link to the edX documentation. If
  users will need more information to understand how to set up and use the
  feature, how can we get that information to the users?

  For more information about the types of information that technical writers
  typically try to find out when they document a new feature, see
  :ref:`Contributing to the Documentation for your Open Source Feature`.

* Is this feature big enough that we need to have a session with stakeholders
  to introduce this feature BEFORE we release it? (PMs, Support, etc...)

  * Paid Certificates

* Do I have to give some more information to the Escalation Team
  so that this can be supported?
* Did you add an entry to CHANGELOG?
* Did you write/edit docstrings for all of your modules, classes, and
  functions?

Development
===========

* Did you consider a reasonable upgrade path?
* Is this a feature that we need to slowly roll out to different audiences?

  * Bulk Email

* Have you considered exposing an appropriate amount of configuration options
  in case something happens?
* Have you considered a simple way to "disable" this feature if something is
  broken?

  * Centralized Logging

* Will this feature require any security provisioning?

  * Which roles use this feature? Does it make sense to ensure that only those
    roles can see this feature?
  * Assets in the Studio Library

* Did you ensure that any new libraries are added to appropriate provisioning
  scripts and have been checked by OSCM for license appropriateness?
* Is there an open source alternative?
* Are we locked down to any proprietary technologies? (AWS, ...)
* Did you consider making APIs so that others can change the implementation if
  applicable?
* Did you consider Internationalization (I18N) and Localization (L10N)?
* Did you consider Accessibility (A11y)?
* Will your code work properly in workers?
* Have you considered the large-scale modularity of the code? For example,
  xModule and XBlock should not use Django features directly.

Testing
=======

* Did you make sure that you tried boundary conditions?
* Did you try Unicode input/data?

  * The name of the person in paid certificates
  * The name of the person in bulk email
  * The body of the text in bulk email
  * etc.

* Did you try funny characters in the input/data? (~!@#$%^&*()';/.,<>, etc...)
* Have you done performance testing on this feature? Do you know how much
  performance is good enough?
* Did you ensure that your functionality works across all supported browsers?
* Do you have the right hooks in your HTML to ensure that the views can be
  automated?
* Are you ready if this feature has 10 times the expected usage?
* What happens if an external service does not respond or responds with a
  significant delay?
* What are possible failure modes?  Do your unit tests exercise these code
  paths?
* Does this change affect templates and/or JavaScript?  If so, are there
  Selenium tests for the affected page(s)?  Have you tested the affected
  page(s) in a sandbox?

Analytics
=========

* Are learning analytics events being recorded in an appropriate way?

  * Do your events use a descriptive and uniquely enough event type and
    namespace?
  * Did you ensure that you capture enough information for the researchers
    to benefit from this event information?
  * Is it possible to reconstruct the state of your module from the history
    of its events?
  * Has this new event been documented  so that folks downstream know how
    to interpret it?
  * Are you increasing the amount of logging in any major way?

* Are you sending appropriate/enough information to MixPanel,
  Google Analytics, Segment?

Collaboration
=============

* Are there are other teams that would benefit from knowing about this feature?

  * Forums/LMS - email

* Does this feature require a special broadcast to external teams as well?

Open Source
===========

* Can we get help from the community on this feature?
* Does the community know enough about this?

UX/Design/Front End Development
===============================

* Did you make sure that the feature is going to pass
  :ref:`Accessibility Guidelines for Developers`?
* Did you make sure any system/instructional text is I18N ready?
* Did you ensure that basic functionality works across all supported browsers?
* Did you plan for the feature's UI to degrade gracefully (or be
  progressively enhanced) based on browser capability?
* Did you review the page/view under all browser/agent conditions -
  viewport sizes, images off, .css off?
* Did you write any HTML with ideal page/view semantics in mind?
* When writing HTML, did you adhere to standards/conventions around class/id
  names?
* When writing Sass, did you follow OOCSS/SMACSS philosophy ([1]_, [2]_, [3]_),
  variable/extend organization and naming conventions, and UI abstraction
  conventions?
* When writing Sass, did you document any new variables, extend-based classes,
  or mixins?
* When writing/adding JavaScript, did you consider the asset pipeline and page
  load timeline?
* When writing JavaScript, did you note what code is for prototyping vs.
  production?
* When adding new templates, views, assets (Sass, images, plugins/libraries),
  did you follow existing naming and file architecture conventions?
* When adding new templates, views, assets (Sass, images, plugins/libraries),
  did you add any needed documentation?
* Did you use templates and good Sass architecture to keep DRY?
* Did we document any aspects about the feature (flow, purpose, intent)
  that we or other teams will need to know going forward?

.. [1] http://smacss.com/
.. [2] http://thesassway.com/intermediate/avoid-nested-selectors-for-more-modular-css
.. [3] http://ianstormtaylor.com/oocss-plus-sass-is-the-best-way-to-css/


.. _Contributing to the Documentation for your Open Source Feature:

Contributing to the Documentation for Your Open Source Feature
===============================================================

Thank you for making a contribution to Open edX. To help ensure the widest
possible adoption for your contribution, it should have an appropriate level of
documentation. For features with user-facing changes, additions to the `edX
documentation`_ set might be needed to help different types of users understand
and use it successfully.

You can use the questions that follow as guidelines for providing in-depth
information about a change to the edX code base. The edX documentation team
typically tries to answer questions like these for every new feature.

Your pull request ("PR") `cover letter`_ might already include some, or all, of
this information, but we encourage you to consider each of these questions to
be sure that you have provided thorough context and detail.

The edX documentation set is created using RST files and Sphinx. If you want to
contribute documentation directly, you are welcome to make revisions and
additions to the files in the edX documentation team's `GitHub repository`_. If
you have questions, please contact us at docs@edx.org.

#. What problem or lack of functionality do users experience that made you
   decide to make this contribution?

#. How does your feature or revision address that problem? Consider providing
   one or more use cases.

#. Who is affected by your contribution, and in what ways? Please provide
   one or more screen captures.

   * Will the course team have access to a new tool or page in Studio, or see
     changes or additions to the Studio user interface?

   * How will learners experience the change in the course content? What
     learning outcomes can be expected?

   * How will course team members experience the change in the LMS, on the
     Instructor Dashboard as well as in the course content?

   * What questions are researchers likely to ask about student interaction
     with the feature? Will researchers need information about new or changed
     tracking log events, SQL tables, or JSON files?

   * Does this feature include tools for developers, such as a new API or
     changed or updated API endpoints?

#. Does your contribution affect any existing problem types or the video
   player? The events emitted by these features are used by Open edX Insights
   and by researchers to measure learner performance and engagement.

   * Performance analytics: What effect does your change have on existing data,
     reports, and metrics for student performance? Have you added reports or
     metrics?

   * Engagement analytics: What effect does your change have on existing data,
     reports, and metrics for student engagement? Have you added reports or
     metrics?

#. Are there any prerequisites?

   * Does a system administrator need to set a feature flag, grant permissions,
     set up a user account, configure integration with a third party tool, or
     perform any other installation or configuration steps? If so, be sure to
     provide those steps.

   * Do any Advanced Setting policy keys need to be added or changed in Studio?
     If so, be sure to provide an example of the syntax needed.

   * Is a particular course role needed to set up or use the feature? Some
     examples are discussion moderator, beta tester, and admin.

   * Is specialized background knowledge necessary? Examples are familiarity
     with, or authorization to access, other on campus systems or third party
     tools.

#. How will each affected audience (particularly system administrators, course
   teams, and learners) use the feature? Consider describing the workflow and
   referencing screen captures.



.. _cover letter: http://edx.readthedocs.io/projects/edx-developer-guide/en/latest/process/cover-letter.html
.. _GitHub repository: https://github.com/openedx/edx-documentation
.. _edX documentation: http://docs.edx.org
