.. _Open edX Juniper Release:

########################
Open edX Juniper Release
########################

The Juniper release is the 10th named release of the Open edX Platform and our
largest yet. Our previous release (Ironwood) was released in January 2019, so
Juniper spans January 2019 through May 2020. You can also review details about
`earlier releases`_ or learn more about the `Open edX Platform`_ if you are new to
Open edX. Below is a summary of the changes for each of the main platform
areas, along with a way to jump down to each section of the release notes. 

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://open.edx.org

.. toctree::
   :numbered: 3
   :hidden:

   juniper_learner
   juniper_educator
   juniper_developer

===================
Learner Experiences
===================

Many areas of the learner experience have started their necessary transitions
to modern micro-frontends, including the Learner Profile, Account Settings,
Order History, Checkout Page, and even the Course Experience. Additionally,
advancements to our platform’s commerce capabilities enable feature based
enrollments for more configurable content access gating. Improvements have also
been added enabling learner schedule personalization, team assignment
submissions, as well as major updates to the mobile application video
experience.

:ref:`Read full Learner details <juniper_learner>`.

====================
Educator Experiences
====================

For Educators many updates have been made to the Studio experience in support
of improving authoring speed for frequent actions like component naming, unit
creation, problem markdown editing, and learning sequence navigation.
Additionally, updates to the platform grading tools are a key part of these
updates. For instances using programs, various program operations have been
updated through the introduction of a new registrar service and a way for
external systems to set enrollments for program learners. 

:ref:`Read full Educator details <juniper_educator>`.


=====================
Developer Experiences
=====================

Many things have changed in our largest release yet, but a few key highlights
include major core requirement upgrades to support Python 3 and Django 2.
Additionally, a major shift toward micro-frontends and a component pattern
library (Paragon) has led many platform areas to be marked for deprecation in
favor of their future MFE replacements. On a related note, the deprecation
process (DEPR project in Jira) has been a source of increased cleanup and
visibility into keeping the platform healthy.  Also in the spirit of improved
visibility and transparency, we have many new architecture decision records
that locate platform decisions in context within the code. These serve as
single repository versions of OEPs, and are also a key highlight for Juniper.

:ref:`Read full Developer details <juniper_developer>`.


.. include:: links.rst
.. include:: ../../links/links.rst
