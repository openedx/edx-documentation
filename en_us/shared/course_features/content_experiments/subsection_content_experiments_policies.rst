.. Section is shared in CA and OLX guides

.. _Set Up Group Configuration for OLX Courses:

************************************************
Set Up Group Configuration for OLX Courses
************************************************

You define group configurations in the ``policy.json`` file in the ``policies``
directory of an OLX (open learning XML) course.

To specify group configurations, you modify the value for the
``user_partitions`` policy key.

.. note::
  ``user_partitions`` is the internal edX Platform name for group
  configurations.

The value for ``user_partitions`` is a JSON collection of group configurations,
each of which defines the experiment groups of learners.

.. note::
  Use names for group configurations that are meaningful. You select from the
  list of group configuration names when you add a content experiment.

See the following examples for more information.

=============================================
Example: One Group Configuration
=============================================

The following code shows an example JSON object that defines a group
configuration with two learner segments.

.. code-block:: none

    "user_partitions": [{"id": 0,
                       "name": "Name of the group configuration",
                       "description": "Description of the group configuration.",
                       "version": 1,
                       "groups": [{"id": 0,
                                   "name": "Group 1",
                                   "version": 1},
                                  {"id": 1,
                                   "name": "Group 2",
                                   "version": 1}]
                                }
                       ]

In this example:

* The ``"id": 0`` identifies the group configuration. For XML courses, the
  value is referenced in the ``user_partition`` attribute of the
  ``<split_test>`` element in the content experiment file.
* The ``groups`` array identifies the experiment groups to which learners are
  randomly assigned. For XML courses, each group ``id`` value is referenced in
  the ``group_id_to_child`` attribute of the ``<split_test>`` element.

==========================================================
Example: Multiple Group Configurations
==========================================================

The following code shows an example JSON object that defines two group
configurations. The first group configuration divides learners into two
experiment groups, and the second divides learners into three experiment groups.

.. code-block:: none

    "user_partitions": [{"id": 0,
                         "name": "Name of Group Configuration 1",
                         "description": "Description of Group Configuration 1.",
                         "version": 1,
                         "groups": [{"id": 0,
                                     "name": "Group 1",
                                     "version": 1},
                                    {"id": 1,
                                     "name": "Group 2",
                                     "version": 1}]}
                        {"id": 1,
                         "name": "Name of Group Configuration 2",
                         "description": "Description of Group Configuration 2.",
                         "version": 1,
                         "groups": [{"id": 0,
                                     "name": "Group 1",
                                     "version": 1},
                                    {"id": 1,
                                     "name": "Group 2",
                                     "version": 1}
                                     {"id": 2,
                                     "name": "Group 3",
                                     "version": 1}
                                     ]}
                       ]

.. note::
  As this example shows, each group configuration is independent.  Group IDs
  and names must be unique within a group configuration, but not across all
  group configurations in your course.
