.. _Define Interval for Grade Aggregation:

####################################################
Define an Interval for Grade Aggregation (Optional)
####################################################

When an external LMS links to problem components in a graded edX subsection,
the edX system grades the answers to those problems, and then transfers the
grades back to the external LMS.

* If the link is to an individual problem component on the edX system, the edX
  system returns the grade for each learner immediately.

* If the link is to a unit or subsection, you can configure an interval of time
  for the edX system to delay before returning the grades. The edX system
  aggregates all of the problems in the unit or subsection that the learner
  answers during that interval. Aggregating grades can reduce the number of
  notification messages that learners receive.

By default, the edX system aggregates grades for units and subsections every 15
minutes.

To change the interval for returning aggregated grades, follow these steps.

#. In ``edx/app/edxapp/lms.env.json``, change the value for the following
   parameter.

   ``LTI_AGGREGATE_SCORE_PASSBACK_DELAY = 15 * 60``

   You specify a time value in seconds.

#. Save the ``/lms/envs/common.py`` file.

#. Restart the Learning Management System processes so that the
   updated environment configurations are loaded.
