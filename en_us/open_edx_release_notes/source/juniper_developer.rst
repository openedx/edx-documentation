.. _juniper_developer:

############################################
Juniper release notes: Developer Experiences
############################################

=================
Platform Services
=================

Notifier Service
----------------

**Notifier Service Deprecation:** We made the decision to deprecate the
notifier service powering the discussion forum daily digest feature. In the
future we hope to find a maintainable path for this feature, perhaps using the
edX ACE infrastructure.

..
    Registrar Service
    ------------------

    Internal Notes on v1.1 Content: Cut from v1, TBD on what the update is for this service. Referenced already in program operations / console


===================================
Continuous Integration & Deployment
===================================

Front End Pipeline
------------------

**Shared Frontend Platform Services:** In support of centralized configuration
of baseline micro-frontend requirements, we have created the `Frontend
Platform`_ repository. As part of this work various services (previously also
described as "runways") were built to speed up configuration of analytics,
logging, authentication, internationalization, as well as a set of other
miscellaneous utilities and configuration details that affect all
micro-frontends.

.. _Frontend Platform: https://github.com/edx/frontend-platform

**MFE Template Application:** For new micro-frontends, you can start from the
`Frontend Template Application`_ GitHub repository, a way to quickly spin up a
new MFE using consistent tools and configuration details employed by other open
edx platform MFEs. It is flagged as a template repository, meaning it can be
used as a basis for new GitHub repositories via the "Use this Template" action.

.. _Frontend Template Application: https://github.com/edx/frontend-template-application

**MFE Service - Build:**  In order to standardize MFE configuration of styles,
tests, and builds, a GitHub repository was created called `Frontend Build`_ to
package as a single dev dependency. It aims to provide common sense defaults
that should be good for most edX projects out of the box, but can be extended
or overridden where needed.

.. _Frontend Build: https://github.com/edx/frontend-build

**MFE Service - Logging:** In support of expanded use of micro-frontends, a
foundational service focused on logging and reporting was built into the
`Frontend Platform repository`__, with an out-of-the-box concrete
implementation for NewRelic.

.. __: https://github.com/edx/frontend-platform/blob/master/src/logging/interface.js

**MFE Service - Analytics:** In support of expanded use of micro-frontends, a
foundational service focused on eventing and analytics was built into the
`Frontend Platform repository`__, with an out-of-the-box concrete implementation
for Segment.

.. __: https://github.com/edx/frontend-platform/blob/master/src/analytics/interface.js

Mobile Site Build Pipeline
--------------------------

**Mobile Test Automation Pipeline:** A major investment was made into `test
automation tooling`__ and containers for both the iOS and Android applications,
enabling improved mobile app test suite automation and builds.

.. __: https://github.com/edx/edx-app-test

Authentication & Account Services
---------------------------------

**MFE Service - Authentication:** In support of expanded use of
micro-frontends, a foundational service focused on configuring authentication
access and maintaining JSON web tokens through to the MFE was built into the
`Frontend Platform repository`__.

.. __: https://github.com/edx/frontend-platform

**Deprecation of Legacy Implementations:** A number of legacy implementations
and views to power login and registration pages on edX platform were cleaned up
and removed in favor of a single secure implementation. Details are in the
:jira:`DEPR-52`.

.. _DEPR-52: https://openedx.atlassian.net/browse/DEPR-52


Internationalization Pipeline
-----------------------------

**MFE Service - Internationalization:** In support of expanded use of
micro-frontends, a foundational service focused on internationalization support
was built into the `Frontend Platform repository`__. The goal of this service
is to standardize the way micro-frontends reference and update their text
strings from Transifex, our crowdsource platform text translation community.

.. __: https://github.com/edx/frontend-platform


Devstack
--------


..
    Deployment Pipeline
    --------------------

    Remote Configuration:
    Remote config (Platform Health) --?

    Kubernetes pilot - Notes service

Video Delivery Pipeline
-----------------------

**VEDA Performance Enhancements:** The team put time into making key VEDA
performance enhancements, improving stability and scaling of our video uploads
pipeline. This includes changes to reduce and mitigate unexpected upload
failures, scaling the system to adequately handle increased loads, and reducing
the need to re-encode videos unexpectedly.

**VEDA Deprecation Process:** After the performance and stability improvements,
the team next set its sights on building a new Video Encoding Manager (VEM)
which will utilize AWS and Media Convert as a replacement for the existing VEDA
video pipeline. This is not available today but we are flagging for Juniper
that VEDA is marked for deprecation, and our next release should include more
details about its replacement - VEM.

..
    Testing Infrastructure
    ----------------------

    Automated dependency updates: ,...
    Optimize developer testing capabilities
    BokChoy Updates: ...

Accessibility Support
---------------------

**WCAG 2.1 Enhancements:** Across many areas of the platform we have completed
improvements that move our platform's target WCAG support level up to 2.1 from
2.0. Many areas of the platform have been updated to improve key requirements
such as improved contrast and visibility, semantic page structure updates, as
well as landmark container improvements that are all a part of the 2.1
specification.

============================
Pattern Library & Components
============================

Paragon
-------

We have updated the Paragon Component Library. Paragon now includes Bootstrap
SCSS directly and contains Paragon extensions. It should now be considered the
Paragon Pattern Library. Theming for Paragon works the same as themes for
Bootstrap and any Bootstrap-compatible theme should be compatible with Paragon.
This was done to help streamline the evolution of Paragon into a full-featured
pattern library that supports all micro frontend applications and increasingly
all areas of the platform. The effort to grow Paragon’s capabilities is
ongoing.

We intend to consolidate styling throughout the platform onto Paragon SCSS. To
that end, a parallel effort has begun to remove legacy pattern library styling
from the platform though this work was not fully completed in Juniper.

Site Headers & Footers
----------------------

For each MFE, the header and footer must be configured to echo the rest of the
site or product experience to which it is connected. We have published various
components, including the commonly `configured header and footer elements, a
cookie message banner, and others`__.

.. __: https://github.com/edx?q=frontend-component&type=&language=


==========================
Core Platform Requirements
==========================

Python
------

About 55% of the Open edX platform is written in Python, meaning a large
fraction of the code written over the past 8 or so years was reviewed and
updated to support Python 3 as part of the Juniper release. While much of the
work done for this effort was captured in JIRA as ":jira:`INCR-1`", many other
dependencies and related services were also updated to support Python 3. One
example of these service upgrades was CodeJail, which is used to sandbox code
written by course reams to assess or execute student problem submissions that
rely on Python themselves.

.. _INCR-1: https://openedx.atlassian.net/browse/INCR-1

Django
------

A major, Juniper-release-defining upgrade to the platform was completed in
service of upgrading the Open edX Platform and all its dependencies to support
Django 2.2, which reached its end of life on April 1st, 2020. A comprehensive
plan for this work was `built and maintained in Confluence`__, and we have captured
the team's `lessons learned from this project as well in Confluence`__. As we move
forward we will continue to find ways to make it easy for the community to
support distributed ownership of core platform health upgrades and maintenance
so that we do not have to do major updates with the added  time pressure of end
of life support dates.

.. __: https://openedx.atlassian.net/wiki/spaces/AC/pages/1073676521/Django+2.2+Upgrade+Plan
.. __: https://openedx.atlassian.net/wiki/spaces/AC/pages/1525252769/Django+2.2+Upgrade+Issues+and+Lessons+Learned


xModule / XBlocks
-----------------

**xModule to xBlock Conversions:**  Across several of the core course content
blocks, we have migrated away from the legacy xModule format in support of its
eventual deprecation. Discussions, HTML, Video, and Problems have all been
converted to XBlocks as part of this work.

==========================
Platform Health Monitoring
==========================

Repository Dashboard
--------------------

With nearly 400 git repositories across 4 different GitHub organizations, it's
becoming both more important and more difficult to answer questions like "which
repositories don't have clearly defined owners?" and "how many repositories
with Python code still don't work with Python 3?" We've done this manually in
the past with custom scripts and spreadsheets, but we need a more automated way
to collect this information rapidly when needed.

Towards this end, we've created various simple checks in `edx-repo-health`_.
The checks answer questions like: Does the openedx.yaml file exist in repo? Is
it parseable? Does Makefile have an upgrade target?

.. _edx-repo-health: https://github.com/edx/edx-repo-health

To run the checks, we've created the pytest plugin `pytest-repo-health`_. The
plugin will find the checks in the specified directory and run them on the
directory of your choice. The instructions to run the plugin can be found in
its readme file. For now, data from individual repos is output as a yaml file.
The aggregated data for many files is output as a csv.

.. _pytest-repo-health: https://github.com/edx/pytest-repo-health


==========================
LMS / Studio Configuration
==========================

JSON to YAML
------------

Most Open edX applications read a single YAML file.  However the LMS and Studio historically
read multiple JSON ones. We are making the LMS and Studio behave the same as other applications
by having them read a single YAML file instead of multiple JSON ones.
Technical details of converting your existing files are here:
`How to convert your LMS and Studio JSON configuration files to YAML`__.

.. __: https://openedx.atlassian.net/wiki/spaces/AC/pages/1822916664/How+to+convert+your+lms+and+studio+json+configuration+files+to+yaml


==============================
Feature & Update Documentation
==============================

Deprecation Process
-------------------

Building on the deprecation process defined in OEP-21 (`Open edX Proposal
21`_), we have flagged many areas for deprecation, including areas mentioned
above that have been replaced by new MFE experiences. A full listing of the
areas marked for deprecation during Juniper’s time frame can be seen in
`Confluence on the developer details and notes page for Juniper`__.

.. _Open edX Proposal 21: https://open-edx-proposals.readthedocs.io/en/latest/oep-0021-proc-deprecation.html
.. __: https://openedx.atlassian.net/wiki/spaces/COMM/pages/940048716/Juniper#Juniper-DeprecationsandRemovals
