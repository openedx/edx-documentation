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

.. _contributor agreement: https://open.edx.org/wp-content/uploads/2019/01/individual-contributor-agreement.pdf

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

    #. Find an INCR ticket to work on from the INCR Epics section of the INCR 
       project dashboard. The INCR tickets are grouped together into JIRA epic 
       tickets.
    #. Select an epic from the dashboard and navigate to **Stories in this epic** 
       to see all of the tasks associated with it.
    #. Each ticket should be self-documenting as to what steps to take to complete it.
    #. When you find a ticket that you want to try, comment on it that you are 
       starting it, so that other developers are less likely to duplicate your work.
    #. Click **Start watching this issue** to get email about any future 
       updates to the ticket.

************
Get to Work!
************

Get started with the edX :ref:`installation:Installing and Updating Devstack` 
environment and follow the information in the ticket you selected to complete it.

****************
Getting Support
****************

Join the #`incr Slack`_ channel on Open edX Slack to ask questions and get 
support. There may also be other channels to get technical support mentioned 
in your specific ticket.

.. _incr Slack: https://openedx.slack.com/messages/CFSA1T268/

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

    #. Be sure to reference which INCR ticket your code is resolving.
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
