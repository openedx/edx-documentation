.. _RecommenderXBlock:

##################
Recommender
##################

The Recommender provides learners with a list of online resources related to
the course content. These resources are jointly managed by course team members
and the learners.

The most common use of the Recommender is for remediation of errors and
misconceptions, followed by providing additional, more advanced resources.

For example, if a learner is working through a physics problem, the Recommender
could be used to show links to concepts used in the problem on Wikipedia, PhET,
and OpenStax, as well as in the course itself. The Recommender can help fill
complex knowledge gaps and help move learners in the right direction.

Learners and course team members can complete the following tasks with the
Recommender.

* Add new resources.
* Edit existing resources and work jointly to improve the quality of resources
  (for example, give an informative resource summary).
* Manage quality by voting for high quality resources or flagging resources as
  spam or abuse.

Course team members can endorse useful resources or remove irrelevant entries.

If you use the Recommender, you should inform learners through course content
or :ref:`course updates <Adding Course Updates and Handouts>` about the tool.

An example of a Recommender in a course follows. The upper part of the figure
illustrates a question in a problem set where the Recommender is attached. The
middle of the figure shows a list of resources and several gadgets for users to
work on the resources. The bottom portion shows additional information about a
given resource on mouse-over event.

.. image:: ../../../shared/building_and_running_chapters/Images/RecommenderXBlockExample.png
  :alt: An overview of the RecommenderXBlock.

Course team members should be sure to review all supplemental materials to
assure that they are accessible before making them available through your
course. For more information, see :ref:`Accessibility Best Practices for Course
Content Development`.

*******************************************************
Add Recommender to the Advanced Module List Policy Key
*******************************************************

#. From the Studio **Settings** menu, select **Advanced Settings**.

#. In the **Advanced Module List** field, place your cursor between the
   brackets.

#. Enter ``"recommender"``. Be sure to include the quotation marks, but not the
   period. The text in the **Advanced Module List** field should resemble the
   following.

   ``["recommender"]``

   If the **Advanced Module List** field already contains text, place your
   cursor directly after the closing quotation mark for the final item, and
   then enter a comma followed by ``"recommender"`` (again, make sure that you
   include the quotation marks).

   ``["word_cloud","recommender"]``

4. At the bottom of the page, select **Save Changes**.

********************************
Add a Recommender
********************************

To add a Recommender to a course, follow these steps.

#. Go to the unit in the course outline where you want to add the
   RecommenderXBlock.

#. Under **Add New Component**, select **Advanced**.
#. Select **recommender**.
#. In the component that appears, select **Edit**, and then specify settings as
   needed.

   * Whether to take users on an introduction tour when they see the tool the
     first time. If selected, the first time (and only the first time) a user
     sees the RecommenderXBlock, there will be a short guided tutorial.
   * Whether to disable the user interface functions which are under
     development. Because these are untested and under development, please
     leave these disabled unless otherwise advised by edX staff.
   * How many resources you want to show in each page of the resource list.
   * How many page icons you want to show in the pagination control (that
     is, the page range). The icons for pages from (current page - page range)
     to (current page + page range) will be shown.

#. Select **Save**.
#. Optionally, open the unit in the LMS and suggest some resources.
