.. _Overview of Content Experiments:

#################################
Overview of Content Experiments
#################################

This section provides an introduction to using content experiments.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

You use content experiments to show different course content to different
groups of learners. Also known as "A/B tests" or "split tests", content
experiments enable you to research and compare the performance of learners in
different groups to gain insight into the relative effectiveness of your course
content.

Information on analyzing events from content experiments is included in the
`edX Researcher Guide`_.

.. _edX Researcher Guide: http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#a-b-testing-events

.. _Courses with Multiple Content Experiments:

******************************************
Courses with Multiple Content Experiments
******************************************

You can run multiple content experiments in your course. You can set up each
experiment to use the same groups of learners, or you can set up each
experiment to be independent and use a different grouping.

.. important::

  If your course has multiple experiments, it is critical that you decide
  in advance if the experiments share the same groups of learners or if each
  experiment has its own unique grouping. If two experiments share the same
  grouping, then any learner that is in Group A for the first experiment will
  also be in Group A for the second one. If you want the experiments to be
  independent, then the experiments must use different groupings so that
  learners are randomly assigned for each experiment.

To determine the available groupings of learners, you set up group
configurations :ref:`using Studio <Set up Group Configurations in edX Studio>`
or :ref:`using XML <Set Up Group Configuration for OLX Courses>`.

You then select which group configuration to use when you add a content
experiment :ref:`using Studio <Add a Content Experiment in Studio>` or
:ref:`using XML <Add a Content Experiment in OLX>`.
