.. _Add Content Experiments to Your Course:

#########################################
Add Content Experiments to Your Course
#########################################

This section provides instructions for adding content experiments to your
course.

.. contents::
  :local:
  :depth: 1

********************************************
Before Adding Content Experiments
********************************************

Before you add content experiments to your course, ensure that you have
completed the following tasks.

* :ref:`Enable Content Experiments`
* :ref:`Set up Group Configurations in edX Studio`

.. _Add a Content Experiment in Studio:

********************************************
Add a Content Experiment in Studio
********************************************

You can add a content experiment in a unit or container page. In Studio, you
create and view content for all groups in the content experiment in a container
page for the experiment, as shown in `Create Content for Groups in the Content
Experiment`_.

When a learner views the unit with the content experiment, she has no
indication there is a content experiment in the unit, and the content
experiment display name is not shown. She sees only the content that you
configure for the group she is assigned to. To the learner, the unit with the
content experiment is no different than any other unit.

To configure a content experiment in Studio, you perform the following tasks.

#. `Create the content experiment`_.
#. `Create content for groups in the content experiment`_.

After you configure a content experiment, you can change its group
configuration. For more information, see `Change the Group Configuration for a
Content Experiment`_.

===============================
Create the Content Experiment
===============================

#. In the unit page, under **Add New Component**, select **Advanced**.

#. Select **Content Experiment**.

   A new content experiment is added to the unit.

   .. image:: ../../../../shared/images/content_experiment_block.png
    :width: 800
    :alt: An image showing the content experiment component in a unit page in
        Studio.

   You can work with the content experiment as you do any other component.
   For more information, see :ref:`Developing Course Components`.

#. Select either **Select a Group Configuration** or **Edit** to open the
   content experiment component.

   .. image:: ../../../../shared/images/content_experiment_editor.png
    :alt: An image of the content experiment editor in Studio.
    :width: 800

#. Next to **Group Configuration**, select a group configuration.

#. In the **Display Name** field, enter the name of the component. The display
   name is only used in Studio; learners do not see this value.

#. Select **Save**.

The content experiment is displayed as a component that contains other
components. For more information, see :ref:`Components that Contain Other
Components`.

.. note:: You cannot duplicate a content experiment.

You can now create content for the groups in the experiment.

=====================================================
Create Content for Groups in the Content Experiment
=====================================================

After you select a group configuration, in the content experiment component,
select **View**.

The content experiment page that opens automatically includes a container for
each group that is defined in the group configuration you selected. For
example, if you select a group configuration that defines Group A and Group B,
you see the following page.

.. image:: ../../../../shared/images/content_experiment_container.png
 :alt: An image of the content experiment page in Studio, with two groups.
 :width: 800

You add content for both groups as needed, just as you would add content to any
container page. For more information, see :ref:`Components that Contain Other Components`.

For example, you can add an HTML component and a video to Group A.

.. image:: ../../../../shared/images/a_b_test_child_expanded.png
 :alt: An image of an expanded content experiment component with an HTML and
     video component.
 :width: 800

.. note::
  It is valid, and can be useful, to have no content for a group in the
  experiment. For example, if one group has a video and another group has no
  content, you can analyze the effect of the video on learner performance.

========================================================
Change the Group Configuration for a Content Experiment
========================================================

You can change the group configuration for a content experiment. When you
change the group configuration, you must add components to any new groups that
you create. You can use the components from the previous groups, as well as
create new components.

.. warning::
  Changing the group configuration of a learner-visible experiment will affect
  the experiment data.

#. Open the unit page of the unit that contains the content experiment.

#. In the content experiment component, select **Edit**.

   .. image:: ../../../../shared/images/content_experiment_editor_group2.png
    :alt: An image of the content experiment editor in Studio, with a group
        configuration selected.
    :width: 800

#. Select a different group configuration.

#. Select **Save**.

#. You must now add components to the new groups in the experiment. Select
   **View** to open the content experiment.

   You see that groups for the new configuration are empty, and any components
   that you had added to groups in the previous configuration are now moved to
   a section called **Inactive Groups**.

   .. image:: ../../../../shared/images/inactive_groups.png
    :alt: An image of a content experiment in Studio, with components in an
        inactive group.
    :width: 800

#. Drag and drop components from the **Inactive Groups** section into the new
   groups. You can also create new components in the new groups.

.. import OLX-content experiment doc that's shared in OLX guide.

.. include:: ../../../../shared/course_features/content_experiments/subsection_content_experiments_OLX.rst
