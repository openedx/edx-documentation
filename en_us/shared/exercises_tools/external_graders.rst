.. _External Grader:

###########################
External Grader
###########################

.. note:: EdX offers provisional support for this tool.

.. contents::
  :local:
  :depth: 1

.. _External Grader Overview:

*******************
Overview
*******************

An external grader is a service that receives learner responses to a problem,
processes those responses, and returns feedback and a problem grade to the edX
platform. You build and deploy an external grader separately from the edX
platform.

.. _External Grader Example:

***************************
External Grader Example
***************************

An external grader is particularly useful for software programming courses
where learners are asked to submit complex code. The grader can run tests that
you define on that code and return results to a learner.

For example, you define a problem that requires learners to submit Python code,
and create a set of tests that an external grader can run to verify the
submissions. When a learner enters Python code for the problem and selects
**Check**, the code is sent to the grader for testing.  If the code passes all
tests, the grader returns the score and a string indicating that the solution
is correct.

.. image:: ../../../shared/images/external-grader-correct.png
 :alt: Image of a learner's view of a programming problem that uses an external grader, with a correct result.
 :width: 600

The external grader can return a string with results, which the learner can see
by selecting **See full output**. This can be particularly useful when the
solution is not correct and you want to return information about the failed
tests. For example:

.. image:: ../../../shared/images/external-grader-incorrect.png
 :alt: Image of a learner's view of a programming problem that uses an external grader, with an incorrect result

.. _External Graders and XQueue:

**************************************
External Graders and XQueue
**************************************

The edX platform communicates with your external grader through XQueue. XQueue
provides learners' input to the grader; it then receives results from the
grader and returns them to learners.

Submissions are collected in XQueue, where they remain until the grader
actively retrieves, or pulls, the next submission from the queue for grading.

The external grader polls the XQueue through a RESTful interface at a regular
interval. When the external grader retrieves a submission, it runs the tests on
it, then pushes the response back to XQueue through the RESTful interface.
XQueue then delivers the response to the edX Learning Management System.

For example code of an external grader that uses Pull mode, see the `Stanford-
Online repository xqueue_pull_ref <https://github.com/Stanford-
Online/xqueue_pull_ref>`_.

============================
External Grader Workflow
============================

The following steps describe the complete process of an external grader
evaluating a problem.

#. The learner either enters code or attaches a file for a problem, then
   selects **Check**.

#. The external grader pulls the code from XQueue.

#. The external grader runs the tests that you created on the code.

#. The external grader returns the grade for the submission, as well as any
   results in a string, to XQueue.

#. The XQueue delivers the results to the edX Learning Management System.

#. The learner sees the problem results and the grade.

==================
The XQueue Name
==================

Your course will use a specific XQueue name. You use this name when you create
problems in Studio.

EdX partners who are using external graders should use the base URL
``https://xqueue.edx.org`` as the XQueue name.

If you are an edX partner, contact your edX partner manager for more
information. Because edX hosts many XQueues for different courses, you must use
the exact XQueue name in your problems, as described in  :ref:`Create a Code
Response Problem`.

.. _The XQueue Interface:

**************************************
The XQueue Interface
**************************************

The learner submission sent from XQueue to the grader, and the response sent
from the grader to XQueue, are JSON objects, as described below.

.. note::
  XQueue does not send the the learner ID to the external grader. Your grader
  cannot access IDs or associate learner IDs with submissions.

For the code for the XQueue interface, see the file `urls.py in the edX XQueue
repository <https://github.com/edx/xqueue/blob/master/queue/urls.py>`_.

======================================================
Inputs to the External Grader
======================================================

The grader receives a submission as a JSON object that has the following keys:

* **xqueue_header**: A dictionary that contains information that is required
  for xqueue to link results to the corresponding submission.

* **xqueue_files**: A dictionary that contains a list of files that were
  submitted by the learner. The dictionary is structured such that the
  filename is the key and the location of the file is the value.

* **xqueue_body**: A dictionary that contains the actual submission as JSON.

  * **student_info**: A dictionary that contains the following
    information about the student in relation to this submission.

    * **anonymous_student_id**: A string that contains an anonymized identifier
      of the student.

    * **submission_time**: A string that contains a timestamp with the time
      of submission (yyyymmddhhmmss).

    * **random_seed**: An integer that contains the seed that was used to
      initialize the randomization script that may be attached to the problem.

  * **student_response**: A string that contains the learner's code
    submission. A learner can submit code by entering a string in the LMS or by
    attaching a file.

  * **grader_payload**: An optional string that you can specify when you
    create the problem. For more information, see the section
    :ref:`Create a Code Response Problem`.

For example::

 {
   "xqueue_header": {
     "submission_id": 12,
     "submission_key": "280587728458c29e1e66ae0c54a806f4"
   }
   "xqueue_files": {
     "helloworld.c": "http://download.location.com/helloworld.c"
   }
   "xqueue_body":
   "{
     "student_info": {
       "anonymous_student_id": "106ecd878f4148a5cabb6bbb0979b730",
       "submission_time": "20160324104521",
       "random_seed": 334
     },
     "student_response": "def double(x):\n return 2*x\n",
     "grader_payload": "problem_2"
    }"
 }

======================================================
External Grader Responses
======================================================

After running tests and recording results for a submission, the grader must
return information by posting a JSON response. The JSON string contains a value
that indicates whether the submission was correct, the score, and any message
the tests create.

In the following example, the learner's submission was correct, the score was
1, and the tests created a brief message.

.. Translators: The "msg" text that is included between the paragraph <p></p> tags can be translated.

::

  {
   "correct": true,
   "score": 1,
   "msg": "<p>The code passed all tests.</p>"
  }

.. _Building an External Grader:

****************************
Building an External Grader
****************************

The course team, not edX, is responsible for building and deploying the
external grader.

In addition to creating tests that are specific to the problems you use in your
course, there are four areas that you must plan for when you build an external
grader:

* :ref:`Scale`
* :ref:`Security`
* :ref:`Reliability and Recovery`
* :ref:`Testing`

.. _Scale:

==================
Scale
==================

Your external grader must be able to scale to support the number of learners in
your course.

Keep in mind that submissions will likely come in spikes, not in an
even flow.  For example, you should expect the load to be much greater than
average in the hours before an exam is due.  Therefore, you should verify that
the external grader can process submissions from a majority of learners in a
short period of time.

.. _Security:

==================
Security
==================

Learners submit code that executes directly on a server that you are
responsible for. It is possible that a learner will submit malicious code. Your
system must protect against this and ensure that the external grader runs only
code that is relevant to the course problems.  How you implement these
protections depends on the programming language you are using and your
deployment architecture. You must ensure that malicious code will not damage
your server.

.. _Reliability and Recovery:

==============================
Reliability and Recovery
==============================

After your course starts, many learners will submit code at any possible time,
and expect to see results quickly.  If your external grader is prone to failure
or unexpected delays, the learner experience will be poor.

Therefore, you must ensure that your grader has high availability and can
recover from errors. Before your course starts, you must have a plan to
immediately notify the team responsible for operating your grader, as well as
edX operations, when the grader fails. In collaboration with edX, you must
develop a procedure to quickly identify the cause of failure, which can be your
grader or edX's XQueue.

Contact your edX partner manager for more information.

If you know the grader will be unavailable at a certain time for maintenance,
you should :ref:`add a course update <Add a Course Update>`.

.. _Testing:

==================
Testing
==================

You should test your grader thoroughly before your course starts.  Be sure to
test incorrect code as well as correct code to ensure that the grader responds
with appropriate scores and messages.

.. _Create a Code Response Problem:

********************************
Create a Code Response Problem
********************************

You create a code response problem in edX Studio by adding a common blank
problem, then editing the XML problem definition in the
:ref:`advanced editor<Advanced Editor>`.

See :ref:`Working with Problem Components` for more information.

Following is a basic example of the XML definition of a problem that uses an
external grader::

 <problem display_name="Problem 6">
    <text>
        <p>Write a program that prints "hello world".</p>
    </text>
    <coderesponse queuename="my_course_queue">
        <textbox rows="10" cols="80" mode="python" tabsize="4"/>
        <codeparam>
            <initial_display>
              # students please write your program here
              print ""
            </initial_display>
            <answer_display>
              print "hello world"
            </answer_display>
            <grader_payload>
            {"output": "hello world", "max_length": 2}
            </grader_payload>
        </codeparam>
    </coderesponse>
 </problem>

Note the following details about the XML definition.

* **queuename**: The value of the queuename attribute of the ``<coderesponse>``
  element maps to an XQueue. Partners should contact their edX partner manager
  for more information. You must use this exact name in order for the problem
  to communicate with the correct XQueue.

  .. note::
    For edX partners, the base URL that graders must access is
    ``https://xqueue.edx.org``.

* **Input Type**: In this example, the ``<textbox>`` element specifies the
  input type.  When you use ``<textbox>``, the learner enters code in a browser
  field when viewing the course unit.  The other element you can use to specify
  the input type is ``<filesubmission>``, which enables the learner to attach
  and submit a code file in the unit.

* **<grader_payload>**: You can use the ``<grader_payload>`` element to send
  information to the external grader in the form of a JSON object. For example,
  you can use ``<grader_payload>`` to tell the grader which tests to run for
  this problem.
