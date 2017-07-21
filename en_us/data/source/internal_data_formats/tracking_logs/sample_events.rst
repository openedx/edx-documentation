.. _sample_events:

*************************
Reviewing a Sample Event
*************************

A sample event from an edX.log file follows. This sample was edited to remove
personally identifiable information. Events are stored in JSON documents, which
can be difficult to read before standard formatting is applied. If you use a
JSON formatter to "pretty print" this event, a version that is more readable is
produced.

.. code-block:: json

 {
   "username": "staff",
   "event_type": "problem_check",
   "ip": "10.0.1.1",
   "agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
   "host": "precise64",
   "referer": "http://localhost:8000/courses/course-v1:edX+DemoX+Demo_Course/courseware/d8a6192ade314473a78242dfeedfbf5b/330cf4d0c87b4bddbbd2eb4a466ff9f4/1?activate_block_id=block-v1%3AedX%2BDemoX%2BDemo_Course%2Btype%40vertical%2Bblock%40541e3597470c4c0d8ab11f6ac443fd5d",
   "accept_language": "en;q=1.0, en;q=0.8",
   "event": {
     "submission": {
       "29c5cbd840324d94be8ba51db1864277_2_1": {
         "input_type": "checkboxgroup",
         "question": "Which of the following is a fruit?",
         "response_type": "choiceresponse",
         "answer": [
           "apple\n      <choicehint selected=\"true\">You are correct that an apple is a fruit because it is the fertilized ovary that comes from an apple tree and contains seeds.</choicehint>\n      <choicehint selected=\"false\">Remember that an apple is also a fruit.</choicehint>\n"
         ],
         "variant": "",
         "correct": false
       }
     },
     "success": "incorrect",
     "grade": 0,
     "correct_map": {
       "29c5cbd840324d94be8ba51db1864277_2_1": {
         "hint": "",
         "hintmode": null,
         "correctness": "incorrect",
         "npoints": null,
         "answervariable": null,
         "msg": "<div class=\"feedback-hint-incorrect\"><div class=\"hint-label\">Incorrect: </div><div class=\"feedback-hint-multi\"><div class=\"hint-text\">You are correct that an apple is a fruit because it is the fertilized ovary that comes from an apple tree and contains seeds.</div><div class=\"hint-text\">Remember that a pumpkin is also a fruit.</div><div class=\"hint-text\">You are correct that a potato is a vegetable because it is an edible part of a plant in tuber form.</div><div class=\"hint-text\">Many people mistakenly think a tomato is a vegetable. However, because a tomato is the fertilized ovary of a tomato plant and contains seeds, it is a fruit.</div></div></div>",
         "queuestate": null
       }
     },
     "state": {
       "student_answers": {

       },
       "seed": 1,
       "done": null,
       "correct_map": {

       },
       "input_state": {
         "29c5cbd840324d94be8ba51db1864277_2_1": {

         }
       }
     },
     "answers": {
       "29c5cbd840324d94be8ba51db1864277_2_1": [
         "choice_0"
       ]
     },
     "attempts": 1,
     "max_grade": 1,
     "problem_id": "block-v1:edX+DemoX+Demo_Course+type@problem+block@29c5cbd840324d94be8ba51db1864277"
   },
   "event_source": "server",
   "context": {
     "course_user_tags": {

     },
     "user_id": 3,
     "org_id": "edX",
     "asides": {

     },
     "module": {
       "usage_key": "block-v1:edX+DemoX+Demo_Course+type@problem+block@29c5cbd840324d94be8ba51db1864277",
       "display_name": "Checkboxes with Hints and Feedback"
     },
     "course_id": "course-v1:edX+DemoX+Demo_Course",
     "path": "/courses/course-v1:edX+DemoX+Demo_Course/xblock/block-v1:edX+DemoX+Demo_Course+type@problem+block@29c5cbd840324d94be8ba51db1864277/handler/xmodule_handler/problem_check"
   },
   "time": "2016-08-04T13:43:34.967980+00:00",
   "page": "x_module"
 }

For more information about fields that are included in every event, see
:ref:`common`. For more information about this ``problem_check`` event and
other types of events, see :ref:`Student_Event_Types` or
:ref:`Instructor_Event_Types`.
