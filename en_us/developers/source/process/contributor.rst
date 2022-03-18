.. _Contributor:

***********
Contributor
***********

Before you make a pull request, it's a good idea to reach out to the
Open edX community to discuss your ideas. There
might well be someone else already working on the same change you want to make,
and it's much better to collaborate than to submit incompatible pull requests.
The `Community Discussions`_ page on the openedx.org website lists different
ways you can ask, and answer, questions. The earlier you start the
conversation, the easier it will be to make sure that everyone's on the right
track.

.. _Community Discussions: https://openedx.org/community/connect/

It's also sometimes useful to submit a pull request even before the code is
working properly, to make it easier to collect early feedback. To indicate to
others that your pull request is not yet in a functional state, just prefix the
pull request title with "(WIP)" (Work In Progress), or start the pull request
as a draft on GitHub. Please do include a link to a WIP pull request in any
discussion threads you start.

Once you're ready to submit your changes in a pull request, check the following
list of requirements to be sure that your pull request is ready to be reviewed:

#. Prepare a :doc:`pull request cover letter <cover-letter>`. When you open
   your pull request, put your cover letter into the "Description" field on
   GitHub.

#. The code should be clear and understandable. Comments in code, detailed
   docstrings, and good variable naming conventions are expected. See the
   :doc:`../style_guides/index` for more details.

#. Commit messages should conform to `OEP-51: Conventional Commits`_.
   This style categorizes commits to make them easier to understand.

#. The pull request should be as small as possible. Each pull request should
   encompass only one idea: one bug fix, one feature, etc. Multiple features
   (or multiple bug fixes) should not be bundled into one pull request. A
   handful of small pull requests is much better than one large pull request.

#. Structure your pull request into logical commits. "Fixup" commits
   should be squashed together. The best pull requests contain only a
   single, logical change -- which means only a single, logical
   commit. The person merging the pull request may choose to squash
   all commits to reduce the number of commits in the main
   branch. They will do so by using the `Squash and merge` button of
   the GitHub interface to preserve the logical commits in the pull
   request, for forensic purposes when trying to diagnose a regression
   or understand a bug.

#. All code in the pull request must be compatible with Open edX's AGPL
   license.  This means that the author of the pull request must sign a
   `contributor's agreement`_, and all libraries included or
   referenced in the pull request must have `compatible licenses`_.

#. All of the tests must pass. If a pull request contains a new feature, it
   should also contain new tests for that feature. If the pull request fixes a
   bug, it should also contain tests for that bug to be sure that it stays
   fixed. GitHub actions will verify this for your pull request, and point out
   any failing tests.

#. The author of the pull request should provide a test plan for manually
   verifying the change in this pull request. The test plan should include
   details of what should be checked, how to check it, and what the correct
   behavior should be. When it makes sense to do so, a good test plan includes
   a tarball of a small test course that has a unit which triggers the bug
   or illustrates the new feature.

#. For pull requests that make changes to the user interface, please include
   screenshots of what you changed. GitHub will allow you to upload images
   directly from your computer. In the future, the core committers will produce
   a style guide that contains more requirements around how pages should appear
   and how front-end code should be structured.

#. The pull request should contain some documentation for the feature or bug
   fix, either in a README file or in a comment on the pull request. A well-
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
make any modifications that you like, without permission from us. However, the
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

Once a pull request is open, automation will create a JIRA
ticket in our system to track review of your pull request. The JIRA ticket is a
way for non-engineers (particularly, product owners) to understand your change
and prioritize your pull request for team review.

If you open up your pull request with a solid description, following the
:doc:`pull request cover letter <cover-letter>` guidelines, the product owners
will be able to quickly understand your change and prioritize it for
review. However, they may have some questions about your intention, need,
and/or approach that they will ask about. A community
manager will ping you on GitHub to clarify these questions if they arise.

Once the product team has sent your pull request to the engineering teams for
review, all technical discussion regarding your change will occur on GitHub,
inline with your code.

Further Information
-------------------

For further information on the pull request requirements, please see the
following links:

* :doc:`code-considerations`
* :doc:`../testing/jenkins`
* :doc:`../testing/code-coverage`
* :doc:`../testing/code-quality`
* :doc:`../style_guides/python-guidelines`
* :doc:`../style_guides/javascript-guidelines`
* :doc:`../style_guides/sass-guidelines`

.. _contributor's agreement: http://openedx.org/cla
.. _compatible licenses: https://openedx.org/open-edx-licensing
.. _OEP-51\: Conventional Commits: https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0051-bp-conventional-commits.html
