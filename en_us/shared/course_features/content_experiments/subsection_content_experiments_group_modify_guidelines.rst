.. Section is shared in CA and OLX guides

.. _Guidelines for Modifying Group Configurations:

*********************************************
Guidelines for Modifying Group Configurations
*********************************************

Review these guidelines if you must modify a group configuration after a course
starts. These guidelines apply for courses built in Studio or using OLX (open
learning XML).

==================================
Modifying a Group Configuration
==================================

After the course starts, **do not**:

* Delete group configurations.

* Change the ``id`` value of a group configuration.

============================
Modifying Experiment Groups
============================

After the course starts, **do not** change the ``id`` value of an experiment
group.

You can change experiment group names at any time.

==========================================================
Removing Experiment Groups from Group Configurations
==========================================================

After a course in which you are running a content experiment has started,
learners in a specific experiment group might have difficulties with the
content or with the course experience. In this situation, you can remove the
experiment group from the group configuration. Content that was specified for
that experiment group is then no longer visible to learners.

Learners in the removed experiment group are reassigned evenly to one of the
other experiment groups in the group configuration. Any problems that these
learners completed in the removed experiment group content do not count toward
their grades. The learners must begin the problem set again and complete all
the problems in the experiment group content to which they are reassigned.

Removing an experiment group affects event data for the course. Ensure that
researchers who are evaluating your course results are aware of the experiment
group that you removed and the date on which you removed it.
