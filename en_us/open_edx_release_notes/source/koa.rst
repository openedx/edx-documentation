.. _Open edX Koa Release:

####################
Open edX Koa Release
####################

These are the release notes for the Koa release, the 11th community release of the Open edX Platform, spanning changes from May 23 to November 12 2020.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_ if you are new to Open edX.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://open.edx.org

.. contents::
 :depth: 1
 :local:

===================
Learner Experiences
===================

Course Experience
-----------------

Special Exams Experience
........................

**Self-Service Proctoring Provider Selection**: Proctored exam settings have been added to the new front end created to contain future course authoring improvements. A new view, exposed within Studio, has been created to surface proctoring provider selection and settings related to proctoring. This also includes a drop down for selecting a proctored exam provider from a list of available providers.

**IDV experience improvements**: The ID verification (IDV) workflow user experience has been improved by breaking down the steps with clear instructions and examples. Accessibility improvements such as face tracking and voice-over have also been added. This new experience can be viewed in the account micro-frontend.

Course Dates & Milestones
.........................

**Personalized Learner Schedules** present learners in self-paced courses with suggested assignment due dates based on their enrollment date and the expected course duration. Learners are able to adjust the schedule if they fall behind and miss an assignment. By providing flexibility while also encouraging accountability, Personalized Learner Schedules help keep learners on track to complete their course.

**Progress Milestones** are in-course celebrations that mark key achievements in the learner's course journey.  When a learner achieves one of these milestones, they see a celebration modal with a congratulatory message and links to share the achievement with friends on social media.

Content Search Tools
....................

**Course Content Search Updates**: Visual updates to the course content search results page now clarifies the result location and type for learners.


Mobile Application Experiences
------------------------------

**Mobile Log In & Registration**: A few updates to the iOS and Android registration experiences are important to call out with the aim of improving ease of use. Instead of scrolling and selecting a country now a user can write into the spinner view and this will filter accordingly. Input fields are now validated once a user's focus changes to the next field (previously the validation used to happen on the fly as the user typed into a field). A new API is now used to validate the registration prior to submission. Please see details in the `full API list`__.

__ https://openedx.atlassian.net/wiki/spaces/LEARNER/pages/17727783/Endpoints+Mobile+Talks+To

Mobile Course Experience
........................

**Native Dates Area**: Previously we used to display a webview on the Dates screen which loaded a course's important dates. This has now been implemented in a native view fully built on mobile. More implementation details of the native dates tab can be found `here`__.

__ https://openedx.atlassian.net/wiki/spaces/LEARNER/pages/2043118110/Full+Page+Dates+View+implementation+on+Mobile

**Personalized Learning Schedules on Mobile**: As in the desktop experience, our mobile users will also have the ability to shift their courses' due dates!
The API details for updated course experience can be found in the 'course' section of the `full API list`__.

__ https://openedx.atlassian.net/wiki/spaces/LEARNER/pages/17727783/Endpoints+Mobile+Talks+To

=====================
Authoring Experiences
=====================

Core Course Content Blocks
--------------------------

**xModule to xBlock Conversions**:  We have continued our migration away from the legacy xModule format in support of its eventual deprecation. The Conditional, Library Content Descriptor, Randomize Descriptor, Split Test Descriptor, Annotatable Descriptor, and Word Cloud Descriptor have all been converted to XBlocks as part of this work.

Open Response Assessments
-------------------------

**Username details Added to ORA Report Download**: In several moderation situations, course teams rely on the downloadable ORA report from the Data Downloads tab. We have added usernames to this report to help make triage of issues faster, as this report previously only included anonymous IDs. We have kept anonymous IDs in the report for now in case anyone has scripts that rely on the anonymous user ID.

**Problem Name and Location Added to ORA Report Download**: Another part of the offline ORA problem triage process involved manual work to process the Item ID in the report. The problem name and course location of the ORA problem is now included in the report.

**ORA Zipped File Download for Submission Text + Attached Files**: Some course teams have expressed an interest in downloading all ORA submissions, enabling instructors to print out and read student submissions offline. While future efforts will focus on an enhanced staff grading experience within the platform, some course teams still prefer to review offline or through printed student submissions. A course report in the data downloads tab of the instructor dashboard now includes a zipped folder that contains student ORA submissions and any attached files.

**Ability to limit file uploads**: Course staff now have the ability in ORA settings to limit students to one file upload as part of their ORA submission, if file uploads are set to optional or required. This work was one of many `community contributions`__!

__ https://github.com/edx/edx-ora2/pulls?q=is%3Apr+is%3Aclosed+merged%3A%3E2019-01-01+-author%3Aedx-transifex-bot

**Separate Assessment Steps & Schedule Authoring Areas**: To support improved authoring ease, we have added a new “Assessment Steps” tab to the ORA authoring experience, making it easier to see at a glance which steps you have enabled for your ORA problem. A new “Schedule” tab summarizes all the configured dates for the ORA problem, including the overall problem submission deadline if set, as well as the release dates for each of the ORA steps if those have been specified.

**Grading Status Message**: Learners can now review a grading status message to understand their current grade as well as the way in which this was calculated. For example, ORA problem grades are determined by staff grading when this step is enabled, even if peer assessment is used elsewhere in the problem for feedback. Learners now see this explained in the final ORA problem section that shares final scores and feedback.  Additionally, this message explains for learners when their grade is still awaiting future peer responses or staff grading feedback, helping answer questions with fewer instructor interventions or direct support.


External Content Blocks
-----------------------

LTI Content Block
.................

**LTI v1.3 Support**: As part of a broader effort to enhance the platform's support for external content integrations, we have updated the LTI consumer XBlock to support the LTI v1.3 specification. For those unfamiliar with LTI, this is a specification widely used to integrate different learning tools and platforms through well defined rules of communication and configuration. Open edX previously supported the LTI 1.1 / 1.2 specification, but we now also support the latest LTI 1.3 specification.


Library Authoring
-----------------

**Content Libraries v2**: A new micro-frontend has been introduced to the platform for a revamped Content Library Authoring experience backed by Blockstore. The current experience renders "legacy" v1 content libraries not powered by blockstore while also introducing basic support for v2 blockstore-backed video, problem and complex libraries. The new experience also provides improved search and filtering capabilities for the Library listing view. This work is in active development, and interested parties should reach out to the Open edX team to explore potential contributions and improvements to this experience.



=========================
Administrator Experiences
=========================

Dependency updates
------------------

These dependencies were upgraded for the `Open edX Koa Installation`_:

- Ubuntu was upgraded from 16.04 to 20.04.

- MySQL was upgraded from 5.6 to 5.7.

- Python was upgraded from 3.5 to 3.8.


=============================
Researcher & Data Experiences
=============================


=====================
Developer Experiences
=====================

Pattern Library & Components: Paragon
-------------------------------------

Beyond the technical improvements noted below, people and processes supporting Paragon have undergone significant changes. Originally conceived as a React component library, Paragon has been expanded to serve as a design system for Open edX. To this end, the new `Design System Documentation`_ on Confluence is now the source of truth for all things Paragon. https://edx.github.io/paragon will continue to serve its critical function as technical documentation, but will not be expanded to include design documentation in the near term.

.. _Design System Documentation: https://openedx.atlassian.net/wiki/spaces/BPL/overview

Paragon has a new governance model
..................................

The edX Experience Team serves as owner and facilitator for Paragon. Questions, concerns, or ideas from the community regarding Paragon can be directed to the #paragon-design-system channel in the `Open edX Slack workspace`_.

.. _Open edX Slack workspace: https://open.edx.org/community/connect/#slack

Sections worth exploring in the Paragon Design System Documentation
...................................................................

- `Governance <https://openedx.atlassian.net/wiki/spaces/BPL/pages/1917977064/Governance>`_
- `Component Documentation <https://openedx.atlassian.net/wiki/spaces/BPL/pages/1916338871/Components>`_
- `Component Contribution Process <https://openedx.atlassian.net/wiki/spaces/BPL/pages/1773502564/Component+Contribution+Process>`_
- `Component Proposals <https://openedx.atlassian.net/wiki/spaces/BPL/pages/1918304774/Component+Proposals>`_

Summary of release notes 9.0.0 to 12.4.1
........................................

Significant improvements and new features include the latest release (May to December 2020) include:

- **New components**

  - `Avatar`__ and `AvatarButton`__, `IconButton`__, `Toast`__

__ https://openedx.atlassian.net/wiki/spaces/BPL/pages/2103083206/Avatar
__ https://openedx.atlassian.net/wiki/spaces/BPL/pages/2102821019/AvatarButton
__ https://openedx.atlassian.net/wiki/spaces/BPL/pages/2097250669/Icon+Button
__ https://edx.github.io/paragon/components/toast

- **Augmented component offering via React Bootstrap**

  - The component offering in Paragon has been expanded by offering pass-through exports to React Bootstrap components (`10.0.0`_, `12.0.0`_). These include: Alert, Badge, Button, ButtonGroup, Card,  Carousel, Dropdown, Figure, Form, InputGroup, Image, Nav, Navbar, Overlay, Popover, ProgressBar, Spinner, Tabs, Tooltip

.. _10.0.0: https://github.com/edx/paragon/releases/tag/v10.0.0
.. _12.0.0: https://github.com/edx/paragon/releases/tag/v12.0.0

- **Component improvements and fixes**

  - The number of button variants have been expanded to include: tertiary, brand, and inverse variants (inverse-${variant}) for each. (`12.2.0`_, `12.3.0`_)
  - Minor bug fixes in SearchField (`9.0.2`_)
  - Bug fixes in Modal (`12.0.2`_)

.. _12.2.0: https://github.com/edx/paragon/releases/tag/v12.2.0
.. _12.3.0: https://github.com/edx/paragon/releases/tag/v12.3.0
.. _9.0.2: https://github.com/edx/paragon/releases/tag/v9.0.2
.. _12.0.2: https://github.com/edx/paragon/releases/tag/v12.0.2

- **Improved theming support**

  - The edx.org theme has been externalized to another package, `@edx/brand-edx.org`_, in accordance with `OEP-48 Brand Customization`_.

  - The technical documentation site at https://edx.github.io/paragon/ now reflects the unthemed version of Paragon used in open edx out of the box.
  - An edx.org themed doc site exists at https://paragon-edx.netlify.app/
  - The color system in Paragon, a descendant of Bootstrap 4, has been expanded to include SASS variables for theme color levels (e.g. $primary-100 to $primary-900). Similar to Bootstrap 5 these variables are available out of the box and have common sense defaults if a theme only defines the base theme color (e.g. $primary). See `v12.1.0 release notes`_ for detail.

  - A new theme color concept "brand" has been introduced. By default brand matches primary. In many themes this is desired. It was added to support edx.org's new brand colors that include a deep green "elm" that we use as primary and a red "garnet" we use as brand. Any theme for Paragon now has the ability to define a brand and a primary color to support more complex brand color schemes.

.. _@edx/brand-edx.org: https://github.com/edx/brand-edx.org/tree/master/paragon
.. _OEP-48 Brand Customization: https://open-edx-proposals.readthedocs.io/en/latest/oep-0048-brand-customization.html
.. _v12.1.0 release notes: https://github.com/edx/paragon/releases/tag/v12.1.0

Deprecations
------------

These components have been removed:

- `ShoppingCart removal <https://openedx.atlassian.net/browse/DEPR-43>`_
- `track.backends.TrackingLog <https://openedx.atlassian.net/browse/DEPR-57>`_
- `Notifier removal <https://openedx.atlassian.net/browse/DEPR-106>`_
- `Edx-pattern-library <https://openedx.atlassian.net/browse/DEPR-62>`_
- `ChordableDjangoBackend in edx-celeryutils <https://openedx.atlassian.net/browse/DEPR-89>`_


.. include:: links.rst
.. include:: ../../links/links.rst
