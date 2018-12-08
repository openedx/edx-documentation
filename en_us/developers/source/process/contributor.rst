***********
Contributor
***********

Before you make a pull request, it's a good idea to reach out to the edX
developers and the rest of the Open edX community to discuss your ideas. There
might well be someone else already working on the same change you want to make,
and it's much better to collaborate than to submit incompatible pull requests.
The `Community Discussions`_ page on the open.edx.org website lists different
ways you can ask, and answer, questions. The earlier you start the
conversation, the easier it will be to make sure that everyone's on the right
track -- before you spend a lot of time and effort making a pull request.

.. _Community Discussions: https://open.edx.org/resources/community-discussions

If you've got an idea for a new feature or new functionality for an existing
feature, and wish to contribute your code upstream, please `start a discussion
on JIRA`_ (you may first need to `create a free JIRA account`_). Do this by
visiting the JIRA website and clicking the "Create" button at the top. Choose
the project "Open Source Pull Requests" and the issue type "Feature Proposal";
in the description give us as much detail as you can for the feature or
functionality you are thinking about implementing. We encourage you to do this
before you begin implementing your feature, in order to get valuable feedback
from the edX product team early on in your journey and increase the likelihood
of a successful pull request.

.. _start a discussion on JIRA: https://openedx.atlassian.net/secure/Dashboard.jspa
.. _create a free JIRA account: https://openedx.atlassian.net/admin/users/sign-up

It's also sometimes useful to submit a pull request even before the code is
working properly, to make it easier to collect early feedback. To indicate to
others that your pull request is not yet in a functional state, just prefix the
pull request title with "(WIP)" (which stands for Work In Progress). Please do
include a link to a WIP pull request in your JIRA ticket, if you have one.

Once you're ready to submit your changes in a pull request, check the following
list of requirements to be sure that your pull request is ready to be reviewed:

#. Prepare a :doc:`pull request cover letter <cover-letter>`. When you open up
   your pull request, put your cover letter into the "Description" field on
   GitHub.

#. The code should be clear and understandable. Comments in code, detailed
   docstrings, and good variable naming conventions are expected. The
   `edx-platform GitHub wiki`_ contains many great links to style guides for
   Python, Javascript, and internationalization (i18n) conventions.

#. The pull request should be as small as possible. Each pull request should
   encompass only one idea: one bugfix, one feature, etc. Multiple features (or
   multiple bugfixes) should not be bundled into one pull request. A handful of
   small pull requests is much better than one large pull request.

#. Structure your pull request into logical commits. "Fixup" commits should be
   squashed together. The best pull requests contain only a single, logical
   change -- which means only a single, logical commit.

#. All code in the pull request must be compatible with edX's AGPL license.
   This means that the author of the pull request must sign a `contributor's
   agreement with edX`_, and all libraries included or referenced in the pull
   request must have `compatible licenses`_.

#. All of the tests must pass. If a pull request contains a new feature, it
   should also contain new tests for that feature. If the pull request fixes a
   bug, it should also contain a test for that bug to be sure that it stays
   fixed. (edX's continuous integration server will verify this for your pull
   request, and point out any failing tests.)

#. The author of the pull request should provide a test plan for manually
   verifying the change in this pull request. The test plan should include
   details of what should be checked, how to check it, and what the correct
   behavior should be. When it makes sense to do so, a good test plan includes
   a tarball of a small edX test course that has a unit which triggers the bug
   or illustrates the new feature.

#. For pull requests that make changes to the user interface, please include
   screenshots of what you changed. GitHub will allow you to upload images
   directly from your computer. In the future, the core committers will produce
   a style guide that contains more requirements around how pages should appear
   and how front-end code should be structured.

#. The pull request should contain some documentation for the feature or
   bugfix, either in a README file or in a comment on the pull request. A well-
   written description for the pull request may be sufficient.

#. The pull request should integrate with existing infrastructure as much as
   possible, rather than reinventing the wheel.  In a project as large as Open
   edX, there are many foundational components that might be hard to find, but
   it is important not to duplicate functionality, even if small, that already
   exists.

#. The author of the pull request should be receptive to feedback and
   constructive criticism. The pull request will not be accepted until all
   feedback from reviewers is addressed. Once a core committer has reviewed a
   pull request from a contributor, no further review is required from the core
   committer until the contributor has addressed all of the core committer's
   feedback: either making changes to the pull request, or adding another
   comment explaining why the contributor has chosen not make any change based
   on that feedback.

It's also important to realize that you and the core committers may have
different ideas of what is important in the codebase. The power and freedom of
open source software comes from the fact that you can fork our software and
make any modifications that you like, without permission from us; however, the
core committers are similarly empowered and free to decide what modifications
to pull in from other contributors, and what not to pull in. While your code
might work great for you on a small installation, it might not work as well on
a large installation, have problems with performance or security, not be
compatible with internationalization or accessibility guidelines, and so on.
There are many, many reasons why the core committers may decide not to accept
your pull request, even for reasons that are unrelated to the quality of your
code change. However, if we do reject your pull request, we will explain why we
aren't taking it, and try to suggest other ways that you can accomplish the
same result in a way that we will accept.

Once A PR is Open
-----------------

Once a pull request is open, our faithful robot "Botbro" will open up a JIRA
ticket in our system to track review of your pull request. The JIRA ticket is a
way for non-engineers (particularly, product owners) to understand your change
and prioritize your pull request for team review.

If you open up your pull request with a solid description, following the
:doc:`pull request cover letter <cover-letter>` guidelines, the product owners
will be able to quickly understand your change and prioritize it for
review. However, they may have some questions about your intention, need,
and/or approach that they will ask about on the JIRA ticket. A community
manager will ping you on GitHub to clarify these questions if they arise;
you are not required to monitor the JIRA discussion.

Once the product team has sent your pull request to the engineering teams for
review, all technical discussion regarding your change will occur on GitHub,
inline with your code.

Further Information
-------------------

For futher information on the pull request requirements, please see the
following links:

* :doc:`code-considerations`
* :doc:`../testing/jenkins`
* :doc:`../testing/code-coverage`
* :doc:`../testing/code-quality`
* `Python Guidelines <https://github.com/edx/edx-platform/wiki/Python-Guidelines>`_
* `Javascript Guidelines <https://github.com/edx/edx-platform/wiki/Javascript-Guidelines>`_

.. _edx-platform GitHub wiki: https://github.com/edx/edx-platform/wiki#development
.. _contributor's agreement with edX: http://open.edx.org/sites/default/files/wysiwyg/individual-contributor-agreement.pdf
.. _compatible licenses: https://github.com/edx/edx-platform/wiki/Licensing
