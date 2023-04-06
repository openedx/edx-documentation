.. _Staff Debug Info:

############################
Staff Debug Info
############################

The edX system keeps track of learners' progress through a course -- recording
when the learner watches videos, responds to problems, and so on. If you are a
member of a course team, some of that data is visible to you for debugging
purposes. Under every problem is a **Staff Debug Info** button: selecting this
button opens a window with information about the problem.

None of this information should be necessary for day-to-day usage of edX,
but for the sake of clarity, some of these fields are documented here.

``is_released``
  Indicates whether the problem is visible to learners.

``location``
  An internal unique identifier that corresponds to this problem. 

  .. only:: Partners

    If you are having trouble with a problem, and need assistance from the edX
    support team, including this value will make it easier for them to track
    down the issue you are having with the problem.

``markdown``
  The text of the problem, in Markdown format. This is often written using
  Studio. Markdown is no longer supported with the release of the visual editors.

``display_name``
  The name of the problem, as shown to the learner.

``max_attempts``
  The maximum number of times that a learner can attempt to answer the problem
  correctly.

``attempts`` 
  The number of times that the currently logged in learner has
  attempted to answer the problem correctly, so far. Every time this learner
  attempts to answer this question, this number will go up, until it reaches
  ``max_attempts``.

``parent`` 
  An internal unique identifier that corresponds to the unit that
  contains this problem.
