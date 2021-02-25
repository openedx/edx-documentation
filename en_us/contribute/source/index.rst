.. _document index:

###########################
Contributing to Open edX
###########################

This is a guide to help you get started in contributing code to the Open edX
open source project. It's for people who are interested in contributing to Open
edX, but don't know what contributions would be most valuable.

.. contents::
   :local:
   :depth: 1

***********
Start Here!
***********

Before we can merge your contribution, you'll need to sign a Contributor
Agreement. We suggest starting that process sooner rather than later.

    * If you are contributing as an individual, go ahead and sign the Individual
      `Contributor Agreement`_.
    * If your work will be contributed as part of a company or institution,
      email legal@edx.org.

.. _contributor agreement: https://openedx.org/cla

===================================================================================================
Should I sign the individual contributor agreement or contribute as part of an larger organization?
===================================================================================================

If you will be working on your contribution during school or work time or are
using a GitHub or email account administered by that organization, you likely
fall under our larger organization agreements. You may also be under
contractual obligation from your employer that all code you write is their
property or may be their property if written on a machine that they purchased.
If you have any questions about whether you should sign the individual
contributor agreement or contribute as part of an organization, email your
situation to legal@edx.org and they will help find the right agreement for you.

.. _Finding:

****************************
Finding Something To Work On
****************************

We manage our project work in Jira, so you will need to `create a Jira account`_
to interact with Open edX tickets.

.. _create a Jira account: https://openedx.atlassian.net/secure/ViewProfile.jspa

We recommend starting with tickets in the Jira INCR project because these are
tickets that are extremely contained in their scope. You don't need to
understand the entire codebase to make a contribution. The success criteria for
completing these tickets are very clear. These are great for anyone new to the
edX platform because the barrier to entry is low.

    #. Find an INCR ticket to work on from the INCR Epics section of the
       `INCR project dashboard`_. The INCR tickets are grouped together into JIRA epic
       tickets.
    #. Select an epic from the dashboard and navigate to **Stories in this epic**
       to see all of the tasks associated with it.  The "Python 3 in edx-platform"
       epic has its own `Kanban board`_.
    #. Each ticket should be self-documenting as to what steps to take to complete it.
    #. When you find a ticket that you want to try, comment on it that you are
       starting it, so that other developers are less likely to duplicate your work.
    #. Click **Start watching this issue** to get email about any future
       updates to the ticket.

.. _INCR project dashboard: https://openedx.atlassian.net/secure/Dashboard.jspa?selectPageId=18935
.. _Kanban board: https://openedx.atlassian.net/secure/RapidBoard.jspa?rapidView=529

************
Get to Work!
************

Get started with the Open edX `devstack`_
environment.  Please note:

    * If you are at an event with experienced Open edX contributors present, they
      may have a snapshot of Devstack which can be installed from a USB flash drive;
      this can save a lot of time and network bandwidth.
    * Pay careful attention to the system requirements.  If you have an unsupported
      operating system, insufficient memory, or insufficient disk space, please ask
      for help selecting a ticket which does not require Devstack.
    * If on macOS, don't forget to adjust your Docker settings as instructed
      (especially memory and CPUs) before trying to install Devstack.

Once you have a development environment, follow the information in the ticket you
selected to complete it.  Remember to fork the repository you're working on so you
can push changes to GitHub.  You can update your local clone if necessary via:

   .. code-block:: bash

    git remote set-url origin <URL from "Clone or download" button of your fork>


Remember to add the original Open edX repository as your upstream remote.

  .. code-block:: bash

    git remote add upstream <URL from "Clone or download" button of Open edX repository>

Pull the latest version of the code to prevent you from encountering conflicts when you send a Pull Request.

  .. code-block:: bash

    git pull upstream master


****************
Getting Support
****************

Join the `#incr Slack`_ channel on Open edX Slack to ask questions and get
support. There may also be other channels to get technical support mentioned
in your specific ticket.

.. _#incr Slack: https://openedx.slack.com/messages/CFSA1T268/

If you get stuck on a particular ticket, leave a comment on the ticket where
you got stuck.

We do our best to make these tickets clear and well-contained. But sometimes the
fix uncovers larger issues. It's always okay to stop working on a ticket, as
long as you make it clear that that is what you are doing and try picking up a
different ticket.

.. _Making Pull Request:

******************************
Making Your First Pull Request
******************************

When you are ready, create a :ref:`Pull Request<opendevelopers:contributor>`.
(Don't forget to sign the Contributor Agreement.)

    #. Be sure to reference in the title which INCR ticket your code is resolving.
    #. Mention **@edx/incr-reviewers** in the PR
    #. Communicate with the reviewer about the code and respond to feedback.
    #. Once your PR is approved, it will be merged by the reviewer.
    #. Celebrate 🎉

****************
Giving Feedback
****************

We are always looking to improve this process and make it easier for people to
contribute to the platform. Your feedback is a very important part of that
process.

Submit that feedback with this `feedback form`_.

.. _feedback form: https://docs.google.com/forms/d/e/1FAIpQLSc87h1h7ptJYb6bsnhQ6NyLOLmW8Tl1_zkd4cNiQrn-1GQ94Q/viewform


.. include:: ../../links/links.rst
