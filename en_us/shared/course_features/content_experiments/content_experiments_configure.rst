.. _Configure Your Course for Content Experiments:

#####################################################
Configure Your Course for Content Experiments
#####################################################

This section provides instructions for configuring your course to use
:ref:`content experiments<Overview of Content Experiments>`.

.. contents::
  :local:
  :depth: 1

.. _Enable Content Experiments:

****************************************
Enable Content Experiments
****************************************

To enable content experiments in your course, you add ``split_test`` to the
**Advanced Module List** in Advanced Settings.

.. note::
  ``split_test`` is the internal edX Platform name for a content experiment.

#. From the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate **Advanced Module List**.

#. In the **Advanced Module List** field, add ``"split_test"``. Be sure that
   you include the double quotation marks.

   If you have multiple values, ensure that they are separated by commas
   (``,``).

   For example, the text in the **Advanced Module List** field may resemble
   the following:

   .. code-block:: none

     [
       "lti_consumer",
       "word_cloud",
       "split_test"
     ]

#. Select **Save Changes**.

.. _Overview of Group Configurations:

****************************************
Overview of Group Configurations
****************************************

Before you can create :ref:`content experiments<Overview of Content
Experiments>`, you must specify at least one group configuration for your
course.

A group configuration defines how many groups of learners are in an experiment.
You can have any number of group configurations in your course. When you create
a content experiment, you select the group configuration to use.

For example, you might want to run two different content experiments at
different times during your course. In one content experiment, learners either
see a video or complete a reading assignment. You can then include problems so
that you can see which group learned the material more completely. For this
content experiment, you need a group configuration that assigns your learners
to two experiment groups.

In the other content experiment, you can present the same question using four
different types of problems. For this content experiment, you need a
group configuration that assigns your learners to four experiment groups.

=======================================
Assigning Learners to Experiment Groups
=======================================

The edX Platform assigns learners to each experiment group in a group
configuration.

Experiment group assignments have the following characteristics.

* Dynamic

  The edX Platform assigns a learner to an experiment group the first time he
  or she views a content experiment that uses the group configuration.

* Random

  You cannot control which learners are assigned to which experiment group.

* Evenly distributed

  The edX Platform keeps track of the size of experiment groups, and assigns
  new learners to groups evenly. For example, if you have two experiment groups
  in a configuration, each group includes 50% of the learners in the course; if
  you have four experiment groups, each group includes 25% of the learners.

* Permanent

  Learners remain in their assigned experiment groups regardless of how many
  content experiments you set up that use the same group configuration.

.. _Set up Group Configurations in edX Studio:

************************************************
Set up Group Configurations in edX Studio
************************************************

.. note::
  You must :ref:`enable content experiments<Enable Content Experiments>` before
  you can set up group configurations.

To set up group configurations, on the **Settings** menu, select **Group
Configurations**. The **Group Configurations** page opens.

From this page you can :ref:`create<Create a Group Configuration>`,
:ref:`edit<Edit a Group Configuration>`, and :ref:`delete<Delete a Group
Configuration>` group configurations. You can also :ref:`view content
experiments that use a group configuration<View Experiments that Use a Group
Configuration>`.

.. _Create a Group Configuration:

=============================
Create a Group Configuration
=============================

You can create a group configuration at any time.

#. On the **Group Configurations** page, under **Experiment Groups**, select
   **New Experiment Group**. The following page opens:

   .. image:: ../../../../shared/images/create-group-config.png
    :width: 800
    :alt: An image of the Create a New Group Configuration page in Studio.

#. Enter a name in the **Group Configuration Name** field. Use a meaningful
   name, because you will select from group configuration names when you create
   content experiments. Learners do not see the group configuration name.

#. Optionally, enter a description for the new group configuration.

#. By default, a new configuration already contains two groups. Modify the
   groups or add and delete groups as needed. A group configuration must have
   at least one group.

   * Modify group names as needed. You see group names in the unit page in
     Studio, but group names are not visible to learners.
   * Select **Add another group** to include another group as part of the
     configuration.
   * Select the **X** to the right of an existing group to remove it from the
     configuration. A group configuration must have at least one group.

#. Select **Create** to save the new group configuration.

The group configuration is then listed in the page. You can see the number of
groups that the configuration contains, as well as whether the configuration is
in use in the course:

.. image:: ../../../../shared/images/group_configurations_one_listed.png
 :width: 800
 :alt: The Group Configurations page with one group configuration listed.

.. _Edit a Group Configuration:

=============================
Edit a Group Configuration
=============================

.. important:: You can change the name of a group configuration at any time.
   However, before you modify any other characteristics of a group
   configuration that is currently used in a running course, review `Guidelines
   for Modifying Group Configurations`_.

#. On the **Group Configurations** page, hover over the group configuration and
   select **Edit**.

   .. image:: ../../../../shared/images/group_configurations_edit.png
    :alt: An image of the Group Configurations page with Edit button
        highlighted.
    :width: 800

   The following page opens:

   .. image:: ../../../../shared/images/save-group-config.png
    :alt: An image of the Edit a Group Configuration page.
    :width: 800

#. On the **Edit a Group Configuration** page modify the name and description as
   needed.

#. Modify groups in the configuration as needed. See :ref:`Create a Group
   Configuration` for details.

#. Select **Save** to save your changes.

.. _Delete a Group Configuration:

=============================
Delete a Group Configuration
=============================

.. note::
 You can only delete a group configuration that is not currently used in a
 content experiment. You cannot delete a group configuration that is used in a
 content experiment.

#. On the **Group Configurations** page, hover over the group configuration and
   select the Delete icon.

   .. image:: ../../../../shared/images/group-configuration-delete.png
    :alt: The Delete icon circled for a group configuration.
    :width: 800

#. When prompted to confirm the deletion, select **Delete**.

.. _View Experiments that Use a Group Configuration:

===============================================
View Experiments that Use a Group Configuration
===============================================

You can view the content experiments that use each of your group
configurations.

On the **Group Configurations** page, select the name of a group to see its
details. You see links to the content experiments that use this group
configuration.

.. image:: ../../../../shared/images/group_configurations_experiments.png
 :alt: An image of a group configuration with the content experiments using the
     configuration circled.
 :width: 800

Select a link to go to the unit that contains the content experiment.

===============================================
View a Group Configuration from an Experiment
===============================================

When working with a content experiment, you can view details about the group
configuration used by that experiment in two ways.

* In a unit that contains a content experiment, in the content experiment
  block, select the name of the group configuration.

  .. image:: ../../../../shared/images/content_experiment_group_config_link.png
   :alt: An image of the content experiment in the unit page with the group
     configuration link circled
   :width: 800

* At the top of the content experiment page, select the name of the group
  configuration.

  .. image:: ../../../../shared/images/content_experiment_page_group_config_link.png
   :alt: An image of the content experiment page with the group configuration
       link circled.
   :width: 800

In both cases, the group configuration opens.

.. image:: ../../../../shared/images/group_configurations_experiments.png
 :alt: An image of the Group Configuration page with the experiments using it
     circled.
 :width: 800

You can use the link in the group configuration to return to the unit that
contains the content experiment.

.. import OLX-content experiment doc that's shared in OLX guide.

.. include:: ../../../../shared/course_features/content_experiments/subsection_content_experiments_group_modify_guidelines.rst

.. include:: ../../../../shared/course_features/content_experiments/subsection_content_experiments_policies.rst
