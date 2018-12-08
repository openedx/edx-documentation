.. _RecommenderXBlock:

##################
Recommender Tool
##################

.. note:: EdX does not support this tool.

The recommender provides learners with a list of online resources related to
the course content. These resources are jointly managed by course team members
and the learners.

.. contents::
  :local:
  :depth: 2

***********
Overview
***********

The most common use of the recommender is for remediation of errors and
misconceptions, followed by providing additional, more advanced resources.

For example, if a learner is working through a physics problem, the recommender
could be used to show links to concepts used in the problem on Wikipedia, PhET,
and OpenStax, as well as in the course itself. The recommender can help fill
complex knowledge gaps and help move learners in the right direction.

Learners and course team members can complete the following tasks with the
recommender.

* Add new resources.
* Edit existing resources and work jointly to improve the quality of resources
  (for example, give an informative resource summary).
* Manage quality by voting for high quality resources or flagging resources as
  spam or abuse.

Course team members can endorse useful resources or remove irrelevant entries.

If you use the recommender, you should inform learners through course content
or :ref:`course updates <Adding Course Updates and Handouts>` about the tool.

An example of a recommender in a course follows. The upper part of the figure
illustrates a question in a problem set where the recommender is attached. The
middle of the figure shows a list of resources and several gadgets for users to
work on the resources. The bottom portion shows additional information about a
given resource on mouse-over event.

.. image:: ../../../shared/images/RecommenderXBlockExample.png
  :alt: An overview of the RecommenderXBlock.

Course team members should be sure to review all supplemental materials to
assure that they are accessible before making them available through your
course. For more information, see :ref:`Accessibility Best Practices for Course
Content Development`.

**************************************************
Enable the Recommender Tool
**************************************************

Before you can add a recommender component to your course, you must enable the
recommender tool in Studio.

To enable the recommender tool in Studio, you add the ``"recommender"`` key to
the **Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

********************************
Add a Recommender
********************************

To add a recommender to a course, follow these steps.

#. Go to the unit in the course outline where you want to add the
   recommender.

#. Under **Add New Component**, select **Advanced**.

#. Select **recommender**.

#. In the component that appears, select **Edit**, and then specify settings as
   needed.

   * Whether to take users on an introduction tour when they see the tool the
     first time. If selected, the first time (and only the first time) a user
     sees the recommender, there will be a short guided tutorial.

   * Whether to disable the user interface functions which are under
     development. Because these are untested and under development, please leave
     these disabled unless otherwise advised by edX staff.

   * How many resources you want to show in each page of the resource list.

   * How many page icons you want to show in the pagination control (that is,
     the page range). The icons for pages from (current page - page range) to
     (current page + page range) will be shown.

#. Select **Save**.

#. Optionally, open the unit in the LMS and suggest some resources.
