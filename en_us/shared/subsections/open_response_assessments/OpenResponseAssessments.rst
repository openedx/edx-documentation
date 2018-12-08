.. _Open Response Assessments 2:

#########################
Open Response Assessments
#########################

.. note:: EdX offers full support for this problem type.

The topics in this section provide an overview and details about open response
assessments.

.. contents::
   :depth: 1
   :local:

For additional information, see :ref:`PA Create an ORA Assignment`,
:ref:`Managing ORA Assignments`, and :ref:`Accessing ORA Assignment
Information`.

*****************************************
Introduction to Open Response Assessments
*****************************************

Open response assessments allow the course team to assign questions that might
not have definite answers, such as text responses or short essays. Learners
submit responses to questions, then each learner and the learner's peers
compare the responses to a rubric that you create. You can also allow learners
to upload an image, a .pdf file, or another file of a type that you specify,
to accompany their text responses.

Open response assessments can include self assessments, peer assessments, and
staff assessments. In self assessments, learners compare their own responses to
a rubric that you create. In peer assessments, learners compare their peers'
responses to the rubric. In staff assessments, a member of the course team
evaluates the learner's responses using the rubric.

In open response assessments, learners usually only see their own responses
and any peer responses they assess. You can also allow learners to see the top
scoring responses that their peers have submitted. For more information, see
:ref:`PA Top Responses`.

.. note::
  Open response assessments that are visible to all learners do not respect
  cohorts. In other words, it is possible for learners in one cohort to be
  asked to grade responses for learners in another cohort. If you want to make
  an open response assessment divided by cohort, you must create that
  assessment in a course component that is defined as cohort-specific. For more
  information about cohorts and creating cohort-specific course content, see
  :ref:`Cohorts Overview` and :ref:`Cohorted Courseware Overview`.


For more information about creating open response assessments, including step
by step instructions, see the following sections.

* :ref:`Best Practices for ORA`
* :ref:`PA Elements`
* :ref:`PA Scoring`
* :ref:`PA Create an ORA Assignment`
* :ref:`Accessing ORA Assignment Information`

For information about viewing metrics and learner responses for released open
response assessments, see :ref:`Accessing ORA Assignment Information`.

For information about the learner experience with open response assessments,
see :ref:`learners:SFD_ORA` in the *edX Guide for Learners*.

.. _Best Practices for ORA:

*********************************************
Best Practices for Open Response Assessments
*********************************************

Open response assessments can be a powerful teaching tool, but they are more
effective in some situations than in others. In general, open response
assessments are best suited to open-ended or project-based assignments with
subjective essay answers and discussion. For example, open response assessments
work well in humanities assignments where learners are encouraged to make
subjective assessments of text, images, or other contributions, but they might
not be the ideal tool in chemistry assignments where there are definitively
correct or incorrect answers to questions.

.. note:: Do not add more than one ORA component in a course unit. Multiple ORA
   assignments in a unit cause errors when learners submit their assessments.

EdX suggests that you follow these guidelines and best practices when you use
open response assessments in your courses.

* Make sure you have a well designed and clear :ref:`rubric <PA Rubric>`. A
  good rubric is very important in helping to eliminate ambiguity in the peer
  grading process.

* Make ORA assignments count toward only a small percentage of the final
  course grade, or make them ungraded.

* In graded ORA assignments, consider setting the lowest possible score to a
  number higher than zero, so that learners can earn some credit for the work
  they have done, even if their peer assessors give them low grades.

* Provide an ungraded practice ORA assignment prior to the first graded ORA
  assignment in the course, so that learners can understand the peer grading
  process and get the most out of the eventual graded ORA assignment.

* Consider using ungraded ORA assignments to generate learner interaction and
  feedback without affecting grades.

* Be wary of including too many ORA assessments in your course. :ref:`Peer
  assessments <Peer Assessment Step>` are hard work for learners, and having
  to perform too many peer assessments can have a negative impact on learners'
  course completion rates.

* For a manageable experience, use staff assessment steps only in assignments
  that are available to a limited number of learners. For example, in courses
  that have cohorts enabled, you make the assignment containing the staff
  assessment step available only to members of one or more cohorts.

* Set the **Must Grade** number higher than the **Graded By** number to
  minimize the chance that some responses will not be peer assessed. EdX
  recommends a setting such as **Must Grade** = 4 and **Graded By** = 3.

* In ORA assignments, to allow enough time for peer assessments to be
  performed after learners have submitted their own responses, set the
  response due date and time at least one week before the peer assessment due
  date and time. If the response due time and peer assessment due time are
  close together, and a learner submits a response just before responses are
  due, other learners may not have time to perform peer assessments before
  peer assessments are due.

* In discussion posts, provide guidance for peer grading of ORA assignments.

* Consider extending due dates to allow the discussion moderation team to
  monitor course discussions for questions about, or reactions to, peer
  grading, and to address issues when necessary.

  If learners raise concerns about ORA assignments in course discussions,
  course team members can perform actions such as :ref:`deleting a learner's
  history, or "state" <Adjust_grades>` for a problem so that he can submit his
  assignment again, :ref:`overriding a learner's grade<Override a learner
  assessment grade>`, or :ref:`removing a learner response <Remove a learner
  response from peer grading>` from peer grading. If there are more widespread
  issues with peer grading, the course team can reduce the weight of the peer
  assessment within the final course grade or allow learners to drop the
  lowest graded assignment from their grades.


.. _PA Elements:

******************************************
Elements of an Open Response Assessment
******************************************

When you create an open response assessment assignment, you include several
elements.

* One or more :ref:`prompts <PA Prompts>`, or questions.

* The :ref:`rubric <PA Rubric>`. One rubric is used to grade all the prompts in
  the assessment.

* One or more :ref:`assessment steps <PA Assessment Steps>`. Assignments can
  include a learner training step, a peer assessment step, a self
  assessment step, and a staff assessment step.

.. note:: If you include a learner training step, you must also include a peer
   assessment step. The learner training step must come first, before the peer
   and self assessment steps. If you include a staff assessment step, it should
   be the final step in the assignment.

For step-by-step instructions for creating an open response assessment, see
:ref:`PA Create an ORA Assignment`.

.. _PA Prompts:

=======
Prompts
=======

Each **prompt**, or question, that you want your learners to answer, appears
near the top of the page, followed by a field where the learner enters a
response. You can require your learners to enter text as a response, or you can
allow your learners to both enter text and upload another file, such as an
image or document.

.. note:: Uploaded files must be smaller than 5 MB in size. If learners upload
 an image, the file must be in .jpg, .gif, or .png format.

.. image:: ../../../../shared/images/PA_QandRField.png
   :width: 500
   :alt: Single ORA question and its corresponding blank response field.

When you write each question, you can include helpful information for your
learners, such as what they can expect after they submit responses, or the
approximate number of words or sentences that their response should have.

.. note:: Each learner is limited to a total word count of 10,000 for all
   responses in an ORA assignment.

For more information, see :ref:`PA Add Prompt`.

.. _Asking Learners to Upload Other Files in Responses:

Asking Learners to Upload Other Files in Responses
*******************************************************

For an open response assessment, you can ask your learners to upload an image,
a .pdf file, or a file of another type as a part of their responses. Other
learners evaluate the responses and their accompanying files during the peer
assessment. Offering the option to upload a file in addition to a text response
can give learners the opportunity to use tools and develop skills that are
relevant to your course.

Before you decide to ask learners to upload other files along with their text
responses, however, you should be aware of the following limitations and best
practices.

* During the peer assessment step, learners download the files that other
  learners uploaded. To reduce the potential for problems from files with
  malicious content, learners cannot upload files with certain file extensions.
  For a complete list, see :ref:`Prohibited File Extensions`.

* Course teams can only access uploaded files for one learner at a time.
  Uploaded file content is not included in the reports of answer submissions
  that are available from the instructor dashboard, and course data packages do
  not include any of the uploaded files.

* You cannot require your learners to upload files. You can only give them the
  option to do so.

* All responses must include some response text. Learners cannot submit a
  response that contains only an uploaded file.

* Learners can submit only one file with each response.

* Files must be smaller than 5MB in size.

* Image files must be in .jpg, .gif, or .png format.

For more information, see :ref:`PA Allow Images`.

.. _Prohibited File Extensions:

Prohibited File Extensions
***************************

This topic lists the file extensions for the set of file types that learners
are prohibited from uploading as part of an open response assessment on edx.org
or edX Edge. When you define a set of custom file types for learners to upload
with their responses, you cannot specify these file types. The extensions on
this list are selected and maintained by the development operations team at
edX, and are subject to change.

.. only:: Open_edX

  This set of file extensions is provided as the default for Open edX
  installations. Open edX system administrators can update this list. For more
  information, see
  :ref:`installation:Configuring ORA2 to Prohibit Submission of File Types`.

.. list-table::
   :widths: 15 75

   * - A through I
     - .action, .apk, .app, .application, .bat, .bin, .cmd, .com, .command,
       .cpl, .csh, .dmg, .exe, .gadget, .hta, .inf, .ins, .inx, .ipa,
       .isu
   * - J through P
     - .jar, .job, .jse, .lnk., msc, .msh, .msh1, .msh2, .mshxml, .msh1xml,
       .msh2xml, .msi, .msp, .mst, .osx, .out, .paf, .pif, .prg, psc1, .psc2,
       .ps1, .ps1xml, .ps2, .ps2xml
   * - Q through Z
     - .reg, .rgs, .run, .scf, .scr, .sct, .shb, .shs, .u3p, .vb, .vbe, .vbs,
       .vbscript, .workflow .ws, .wsc, .wsf, .wsh

.. _PA Rubric:

=======
Rubric
=======

Your assignment must include a **rubric** that you design. The same rubric is
used for all the types of assessments (self, peer, or staff). The person
performing the assessment sees the rubric when she begins grading, and
compares the submitted response to the rubric.

Rubrics consist of *criteria* and *options*.

* Each criterion has a *name*, a *prompt*, and one or more *options*.

   * The name is a very short summary of the criterion, such as "Ideas" or
     "Content". Criterion names generally have just one word. Because the
     system uses criterion names for identification, **the name for each
     criterion must be unique.** Criterion names do not appear in the rubric
     that learners see when they are completing peer assessments, but they do
     appear on the page that shows the learner's final grade.

     .. image:: ../../../../shared/images/PA_CriterionName.png
        :alt: A final score page with call-outs for the criterion names

   * The prompt is a description of the criterion.

   * Options describe how well the response satisfies the criterion.

* Each option has a *name*, an *explanation*, and a *point value*.

  .. image:: ../../../../shared/images/PA_Rubric_LMS.png
     :alt: Image of a rubric in the LMS with call-outs for the criterion prompt
         and option names, explanations, and points.

Different criteria in the same assignment can have different numbers of
options. For example, in the image above, the first criterion has three options
and the second criterion has four options.

.. note:: You can also include criteria that do not have options, but that do
   include a field where learners or staff can enter feedback. For more
   information, see  :ref:`PA Criteria Comment Field Only`.

You can see both criterion and option names when you access assignment
information for an individual learner. For more information, see
:ref:`Accessing ORA Assignment Information`.

.. image:: ../../../../shared/images/PA_Crit_Option_Names.png
   :width: 600
   :alt: Learner-specific assignment information with call-outs for criterion
       and option names.

When you create your rubric, decide how many points each option will receive,
and make sure that the explanation for each option is as specific as possible.
For example, one criterion and set of options may resemble the following.

**Criterion**

Name: Origins

Prompt: Does this response explain the origins of the Hundred Years' War? (5
points possible)

**Options**

.. list-table::
   :widths: 8 20 50
   :stub-columns: 1
   :header-rows: 1

   * - Points
     - Name
     - Explanation
   * - 0
     - Not at all
     - This response does not address the origins of the Hundred Years' War.
   * - 1
     - Dynastic disagreement
     - This response alludes to a dynastic disagreement between England and
       France, but doesn't reference Edward III of England and Philip VI of
       France.
   * - 3
     - Edward and Philip
     - This response mentions the dynastic disagreement between Edward III and
       Philip VI, but doesn't address the role of Salic law.
   * - 5
     - Salic law
     - This response explains the way that Salic law contributed to the
       dynastic disagreement between Edward III and Philip VI, leading to the
       Hundred Years' War.

.. note:: For peer grading, the most effective rubrics are as concrete
   and specific as possible. Many novice learners will be unqualified
   to make the types of value judgments required for more holistic
   rubrics. In addition, edX suggests using clear, simple language in
   rubrics.

For more information, see :ref:`PA Add Rubric`.

.. _PA Assessment Steps:

=================
Assessment Steps
=================

In your assignment, you also specify the **assessment steps**. You can set the
assignment to include some combination of the following steps.

.. contents::
   :depth: 1
   :local:

.. note:: If you include a learner training step, you must also include a peer
   assessment step. The learner training step must come before peer or self
   assessment steps. If you include both peer and self assessment steps, edX
   recommends that you place the peer assessment before the self assessment.
   If you include a staff assessment step, it should be the final step in the
   assignment.

You can see the type and order of the assessments when you look at the
assignment. In the following example, after learners submit a response, they
complete a learner training step ("Learn to Assess Responses"), complete peer
assessments on other learners' responses ("Assess Peers"), and then complete
self assessments ("Assess Your Response").

.. image:: ../../../../shared/images/PA_AsmtWithResponse.png
  :alt: A peer assessment with assessment steps and status labeled.
  :width: 600

.. _PA Student Training Step:

Learner Training Step
*****************************

Learner training steps teach learners to perform their own assessments. A
learner training assessment contains one or more sample responses that you
write, together with the scores that you would give the sample responses.
Learners review these responses and try to score them the way that you scored
them.

.. note:: If you include a learner training step, you must also include a peer
   assessment step. The learner training step must come before any peer and self
   assessment steps.

In a learner training assessment, the **Learn to Assess Responses** step opens
immediately after a learner submits a response. The learner sees one of the
sample responses that you created, along with the rubric. The scores that you
gave the response do not appear. The learner also sees the number of sample
responses that he or she will assess.

.. image:: ../../../../shared/images/PA_TrainingAssessment.png
   :alt: Sample training response, unscored.
   :width: 500

The learner selects an option for each of the assignment's criteria, and then
selects **Compare your selections with the instructor's selections**. If all of
the learner's selections match the selections defined by the course team, the
next sample response opens automatically.

If any of the learner's selections differ from those specified by the course
team, the learner sees the response again, and the following message appears
above the response.

.. code-block:: xml

  Learning to Assess Responses
  Your assessment differs from the instructor's assessment of this response. Review the
  response and consider why the instructor may have assessed it differently. Then, try
  the assessment again.

For each of the criteria, the learner sees one of the following two messages,
depending on whether the learner's selections matched those of the course team.


.. code-block:: xml

  Selected Options Differ
  The option you selected is not the option that the instructor selected.

.. code-block:: xml

  Selected Options Agree
  The option you selected is the option that the instructor selected.

For example, the following learner chose one correct option and one incorrect
option.

.. image:: ../../../../shared/images/PA_TrainingAssessment_Scored.png
   :alt: Sample training response, with one correct and one incorrect option.
   :width: 500

The learner continues to try scoring the sample response until the learner's
scoring for all criteria matches the scoring defined by the course team.

For more information, see :ref:`PA Student Training`.

.. _Peer Assessment Step:

Peer Assessment Step
*****************************

In the peer assessment step, learners review the responses of other learners
in the course. For each response, they select an option for each criterion in
your rubric based on the response. Learners can also provide text feedback, or
comments, on each response.

If you include both peer and self assessment steps, edX recommends that you
place the peer assessment before the self assessment.

For information about how peer assessments affect a learner's assignment grade,
see :ref:`PA Scoring`.


Number of Responses and Assessments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you include a peer assessment step, you specify the number of responses
that each learner must assess (**Must Grade**) and the number of peer
assessments that each response must receive (**Graded By**) before the
step is considered complete.

.. note:: Because some learners might submit a response without performing any
   peer assessments, some responses might not receive the required number of
   assessments. To increase the chance that all responses receive a sufficient
   number of assessments, you must set the number of responses that learners
   must assess to be higher than the number of assessments that each response
   must undergo. For example, if you require each response to receive three
   assessments, you could require each learner to assess five responses.

If all responses have received assessments, but some learners have not
completed the required number of peer assessments, those learners can perform
peer assessments on responses that have already been assessed by other
learners. The learner who submitted the response sees the additional peer
assessments when he sees his score. However, the additional peer assessments
do not count toward the score that the response receives.

.. _Feedback Options:

Feedback Options
^^^^^^^^^^^^^^^^

By default, in peer assessment steps, learners see a single comment field
below the entire rubric. You can also add a comment field to an individual
criterion or to several individual criteria. This comment field can contain up
to 300 characters.

The comment field appears below the options for the criterion. In the following
image, both criteria have a comment field. There is also a field for overall
comments on the response.

.. image:: ../../../../shared/images/PA_CriterionAndOverallComments.png
   :alt: Rubric with comment fields under each criterion and under overall
       response.
   :width: 600

For more information, see :ref:`PA Add Rubric` and :ref:`PA Criteria Comment
Field Only`.


Assessing Additional Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Learners can assess more than the required number of responses. After a
learner completes the peer assessment step, the step "collapses" so that only
the **Assess Peers** heading is visible.

.. image:: ../../../../shared/images/PA_PAHeadingCollapsed.png
   :width: 500
   :alt: The peer assessment step with just the heading visible.

If the learner selects the **Assess Peers** heading, the step expands again.
The learner can then select **Continue Assessing Peers** to perform additional
peer assessments.

.. image:: ../../../../shared/images/PA_ContinueGrading.png
   :width: 500
   :alt: The peer assessment step expanded so that "Continue Assessing Peers"
       is visible.


.. _Self Assessment Step:

Self Assessment Step
*****************************

In self assessment steps, the learner sees her own response followed by the rubric.
As with peer assessments, the learner evaluates the response using the rubric,
selecting an option for each criterion.

If you include both peer and self assessments, edX recommends that you include
the peer assessment before the self assessment.


.. _Staff Assessment Step:

Staff Assessment Step
*****************************

In staff assessment steps, a member of the course team performs an evaluation
of the learner's response. Course team members grade the response using the
problem's rubric, in the same way that self and peer assessments are done, and
can include comments in their assessment.

.. note:: If a staff assessment step is included in an assignment, learners do
   not receive final grades until the staff assessment step has been completed.
   The scores that you give learners in staff assessment steps override
   scores from any other assessment type in the assignment, including peer
   assessments that are completed after the staff assessment.

Including a staff assessment step in an ORA assignment is best for courses with
smaller groups of learners. For example, in a course with cohorts, you might
create an ORA assignment that has both peer assessment and staff assessment
steps, and make it available only to the members of one or more specific
cohorts. For the members of the remaining cohorts, you create an ORA assignment
that has only the peer assessment step. For details about creating different
course experiences for learners in different cohorts, see
:ref:`Cohorted Courseware Overview`.

For details about performing grading in staff assessment steps, see
:ref:`Perform a Staff Assessment`.


.. _PA Scoring:

*******************************************************
How Scores for Open Response Assessments Are Calculated
*******************************************************

In open response assessments that contain staff assessments, staff assessments
can be performed more than once, and the most recent staff assessment score is
equivalent to the assignment's final score. Peer and self assessment scores are
not taken into account, although learners can see scores and comments from all
assessments that were performed on their response.

In open response assessments that do not contain staff assessments but do
contain both peer assessment and self assessments, only the peer assessment
score counts toward the assignment's final score. The self assessment score is
not taken into account. There is no option for weighting the peer and self
assessment portions independently.

In open response assessments that include only self assessments, the
assignment's final score is equivalent to the self assessment score.

.. note:: Given the high level of subjectivity in peer assessments, edX
   recommends that you make ORA assignments count towards only a small
   percentage of a course's final grade.

The following topics detail how the scores for peer assessments and self
assessments are calculated.


=======================
Peer Assessment Scoring
=======================

.. note:: If an open response assessment includes peer and self assessments
   but not staff assessments, only the peer assessment score counts towards
   the assignment's final score. The self assessment score is not taken into
   account.

Peer assessments are scored by criteria. A number of peer assessors rate a
learner's response by each of the required criteria. The learner's score for a
particular criterion is the median of all scores that each peer assessor gave
that criterion. For example, if the Ideas criterion in a peer assessment
receives a 10 from one learner, a 7 from a second learner, and an 8 from a
third learner, the Ideas criterion's score is 8.

The learner's final score on a response is the sum of the median scores from
all peer assessors for all of the required criteria.

For example, a response might have received the following scores from peer
assessors.

.. list-table::
   :widths: 25 10 10 10 10
   :stub-columns: 1
   :header-rows: 1

   * - Criterion Name
     - Peer 1
     - Peer 2
     - Peer 3
     - Median
   * - Ideas (out of 10)
     - 10
     - 7
     - 8
     - **8**
   * - Content (out of 10)
     - 7
     - 9
     - 8
     - **8**
   * - Grammar (out of 5)
     - 4
     - 4
     - 5
     - **4**

To calculate the final score for the response, add the median scores that were
given for each criterion, as follows.

  **Ideas median (8/10) + Content median (8/10) + Grammar median (4/5) = final
  score (20/25)**

.. note:: Remember that final scores are calculated by criteria, not by
   individual assessor. Therefore, the score for the response is not the median
   of the scores that each individual peer assessor gave the response.

For information on scores for learner submissions that you have canceled and
removed from peer assessment, refer to :ref:`Remove a learner response from
peer grading`.

=======================
Self Assessment Scoring
=======================

.. note:: If an open response assessment includes both peer and self
   assessments, the self assessment score does not count toward the final
   grade.

If an open response assessment includes only self assessments, the
assignment's final score is equivalent to the self assessment score.

Self assessments are scored by criteria. Each learner rates herself on each
criterion, using the rubric. The learner's final score on a response is the
total number of earned points, out of the total possible points.

========================
Staff Assessment Scoring
========================

If an open response assessment includes a staff assessment step, the score
that is given in the staff assessment step overrides all other scores in the
assignment.

.. _PA Top Responses:

*****************************
Top Responses
*****************************

You can include a **Top Responses** section that shows the top scoring
responses that learners have submitted for the assignment, along with the
scores for those responses. The **Top Responses** section appears below the
learner's score information after the learner finishes every step in the
assignment.

.. image:: ../../../../shared/images/PA_TopResponses.png
   :alt: Section that shows the text and scores of the top three responses for
       the assignment.
   :width: 500

You can allow the **Top Responses** section to show between 1 and 100
responses. Keep in mind, however, that each response might be up to 300 pixels
in height in the list. (For longer responses, learners can scroll to see the
entire response.) EdX recommends that you specify 20 or fewer responses to
prevent the page from becoming too long.

.. note:: It can take up to an hour for a high-scoring response to appear in
 the **Top Responses** list.

   If a high-scoring response is :ref:`removed from peer assessment<Remove a
   learner response from peer grading>` it is also removed from the **Top
   Responses** list.

For more information, see :ref:`PA Show Top Responses`.
