*****************
Community Manager
*****************

Community managers handle the first part of the process of responding to pull
requests, before they are reviewed by core committers. Community managers are
responsible for monitoring the GitHub project so that they are aware of incoming
pull requests. For each pull request, a community manager should:

#. Read the description of the pull request to understand the idea behind it
   and what parts of the code it impacts. If the description is absent or
   unclear, inform the author that the pull request cannot be reviewed until
   the description is clearer. Guide them to the :doc:`pull request cover letter <cover-letter>`
   guidelines.

#. Help the product team evaluate the idea behind the pull request.
   Is this something that Open edX wants? If you and the
   product owner(s) all believe that Open edX does not want this pull request,
   add a comment to the pull request explaining the reasoning behind that
   decision. Be polite, and remind them that they are welcome to fork the code
   and run their own fork on their own servers, without needing permission
   from edX. Try to suggest ways that they can build something that Open edX
   *does* want: for example, perhaps an API that would allow the contributor
   to build their own component separately. Then close the pull request.

#. Check that the author of the pull requests has submitted a
   `contributor's agreement`_, added name to AUTHORS file, and any other
   necessary administrivia (our bot will make an automated comment if this is not
   properly in place). If not, inform author of problems and wait for them to fix it.

#. Once you’ve verified that the code change is not malicious,
   run a Jenkins job on the pull request and check the result.
   If there are failing tests (and they are real failures, not flaky tests),
   inform the author that the pull request cannot be reviewed until the tests
   are passing.

#. When all the tests pass, check the diff coverage and diff quality.
   If they are too low, inform the author of how to check these metrics,
   and ask the author to write unit tests to increase coverage and quality
   Diff quality should be 100%, and diff coverage should be at least 95% unless
   there are exceptional circumstances.

#. Skim the contents of the pull request and suggest obvious fixes/improvements
   to the pull request. Note that this is *not* a thorough code review --
   this is simply to catch obvious issues and low-hanging fruit.
   The point is to avoid interrupting core committers for trivial issues.

#. Ask the author of the pull request for a test plan:
   once this code is merged, how can we test that it’s working properly?
   Whichever core committer merges this pull request will need to test it
   on a staging server before the code is deployed to production, so be sure
   that the test plan is clear enough for a core committer to follow.

#. If the PR includes any visual changes, or changes in user interaction,
   ask the author of the pull request to provide some screenshots.
   (For interaction changes, GIFs are awesome!) When a core committer starts
   reviewing the changes, it is often helpful to deploy the pull request to a
   sandbox server, so that the reviewer can click around and verify that the
   changes look good.

#. The core committers will put together a style guide.
   Pull requests that have visual/UX changes will be expected to respect this
   style guide -- if they don’t, point the author to the style guide and tell
   them to resubmit the pull request when it does.

.. _contributor's agreement: http://code.edx.org/individual-contributor-agreement.pdf

At this point, the pull request is ready for code review. There are two
different options: small PR review and large PR review. A PR is “small” if it
can be read and understood in less than 15 minutes, including time spent
context-switching, reading the description of the pull request, reading any
necessary code context, etc. Typically, “small” PRs consist of fixing typos,
improving documentation, adding comments, changing strings to unicode, marking
strings that need to be translated, adding tests, and other chores. A “small”
pull request doesn’t modify the code that will be run in production in any
meaningful way.

If the pull request is small, it can be reviewed immediately. If the community
manager that is handling this pull request feels comfortable doing the code
review, then he or she should do so rather than handing it off to a core
committer. If not, he or she should move the JIRA ticket for the PR review
into the "Awaiting Prioritization" state and add enough detail on the ticket for
the product team to understand the size and scope of the changes.
Inform the author that it might take a few days for the engineering team to review the PR.

If the pull request is not small, it will be handled by the full pull request process:

.. image:: pr-process.png
   :align: center
   :alt: A visualization of the pull request process

The community manager should:

* Make sure the pull request is ready for Product Review, if that has not yet happened.
  That means getting enough detail out of the contributor for the product owner
  to properly do a product review. Once this is done, move the JIRA ticket to the
  "Product Review" state.

* If questions arise from product owners during review, work with the contributor to
  get those questions answered before the next round of review.

* Once a PR has passed product review, do a first-round review of the PR with the
  contributor. That is, make sure quality and test coverage is up to par, and that
  the code generally meets our style guidelines. Once this has happened, move the
  ticket to the "Awaiting Prioritization" state.

* At each of these junctures, try to update the author with an estimate of how long
  the next steps will take. The product team will meet biweekly to review new
  proposals and prioritize PRs for team review. Direct the contributor to the JIRA ticket
  as well; the state of the JIRA ticket reflect the above diagram and can give a good
  sense of where in the process the pull request is.

* Once a PR has been prioritized for team review, ask the product owner for an estimate
  of how many sprints it will take for the pull request to be reviewed:
  if its more than one, try to push back and advocate for the contributor.
  However, the estimate is ultimately up to the product owner, and if he/she
  says it will really be more than one sprint, respect that.

* Add a comment to the pull request and inform the author that the pull request
  is queued to be reviewed. Give them an estimate of when the pull request
  will be reviewed: if you’re not sure what to say, tell them it will be in
  two weeks. If the product owner has estimated that it will take more than
  one sprint before the pull request can be reviewed, direct the contributor to
  JIRA to monitor progress.

For determining which teams that the pull request impacts, use common sense --
but in addition, there are a few guidelines:

* If any SASS files are modified, or any HTML in templates,
  include the UX (user experience) team.

* If any settings files or requirements files are modified,
  include the devops team.

* If any XModules are modified,
  include the blades team.

* If any logging events are modified,
  include the analytics team.

* Include the doc team on every contributor pull request that has a user-facing change.

Once the code review process has started, the community managers are also
responsible for keeping the pull request unblocked during the review process. If
a pull request has been waiting on a core committer for a few days, a community
manager should remind the core committer to re-review the pull request. If a
pull request has been waiting on a contributor for a few days, a community
manager should add a comment to the pull request, informing the contributor that
if they want the pull request merged, they need to address the review comments.
If the contributor still has not responded after a few more days, a community
manager should close the pull request. Note that if a contributor adds a comment
saying something along the lines of “I can’t do this right now, but I’ll come
back to it in X amount of time”, that’s fine, and the PR can remain open -- but
a community manager should come back after X amount of time, and if the PR still
hasn’t been addressed, he or she should warn the contributor again.
