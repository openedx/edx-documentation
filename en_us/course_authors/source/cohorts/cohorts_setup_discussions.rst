.. _Set up Discussions in Cohorted Courses:


##########################################################
Setting up Discussions in Courses with Student Cohorts
##########################################################

In courses that have cohorts enabled, you can set up discussion topics to be either divided by cohort, or unified and accessible to all students.

When you first enable cohorts in your course, the initial behavior for course-wide discussion topics is different from the behavior of content-specific
(inline) discussion topics. By default, course-wide discussion topics are
unified, but content-specific discussion topics are divided by cohort. You can
configure either type of discussion to be divided or unified.

For overview information about discussions in a course, see :ref:`Discussions`.
For information about setting up cohorts in a course, see :ref:`Enabling and
Configuring Cohorts`.

******************************************
Course-Wide Discussion Topics and Cohorts
******************************************

When you first :ref:`create a course-wide discussion topic<Create CourseWide
Discussion Topics>`, it is unified, and all students in the course can post,
read, respond, and comment in the topic without regard to their cohort group
assignments. After you add a course-wide topic, you can configure it so that it
is divided by cohort instead.

.. _Identifying Private CourseWide Discussion Topics:

=============================================================
Example: Configuring Course-Wide Discussion Topics As Divided
=============================================================

This example assumes that you have added three course-wide discussion topics
called Course Q&A, Announcements, and Brainstorming to your course, so that in
addition to the system-supplied General topic, you have four course-wide
discussion topics. 

.. image:: ../Images/Discussion_Add_cohort_topics.png
 :alt: Discussion Topic Mapping field with four course-wide discussion topics 
       defined

You have now enabled cohorts for your course and would like
to take advantage of that feature as it applies to discussion topics.

The posts that you intend to make to the Course Q&A and General topics, and the
subjects you expect students to explore there, are appropriate for a unified
student audience. However, you also want to give students some course-wide
topics that are divided by cohort. You decide that the Announcements and
Brainstorming course-wide topics should be divided by cohort.

You also decide to apply a naming convention so that students will know the
audience for the discussion topics before they add any posts. For information on
how to achieve this, see :ref:`Apply Naming Conventions to Discussion Topics`.


.. _Configure CourseWide Discussion Topics as Private:

======================================================
Define Divided Course-Wide Discussion Topics
======================================================

This procedure shows how to configure the Brainstorming and Announcements
course-wide discussion topics (from the example in :ref:`Identifying Private
CourseWide Discussion Topics`) so that they are divided by cohort.

On the Studio **Advanced Settings** page, details of the two topics appear as
follows in the **Discussion Topic Mapping** field. You use the ID for each
discussion topic to identify it in the steps that follow.

.. code::

      "Brainstorming (private)": {
          "id": "i4x-edX-Open-edx_demo_course_brainstorming"
      },
      "Announcements (private)": {
          "id": "i4x-edX-Open-edx_demo_course_announcements"
      }

#. Open the course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Cohort Configuration** field, place your cursor after the opening
   brace character (``{``) and press **Enter**.

#. On the new line, you define the ``"cohorted_discussions":`` policy key,
   followed by one or more course-wide discussion topic IDs enclosed by
   square brackets (``[ ]``). You can define just one discussion topic or a set of discussion topics.

   For example, to define a single discussion topic, type
   ``"cohorted_discussions": ["discussion-topic-ID"]``, putting your discussion
   topic's ID inside the double quotations marks in place of the example ID.
   Press Enter.

   To define a set of topics, type the ID for each discussion topic on a new
   line, enclose it within quotation marks (``" "``), and separate the quoted ID
   values with commas. For example:

 .. code:: 

   "cohorted_discussions": [
       "i4x-edX-Open-edx_demo_course_announcements",
       "i4x-edX-Open-edx_demo_course_brainstorming"
   ]
   
5. If "cohorted_discussions" is followed by other policy keys within the
   **Cohort Configuration** field, make sure there is a comma after the closing square bracket character (``],``). You must include a comma to separate each of the policy keys that you define.

.. Adding a line to force a line space

6. Click **Save Changes**. Studio resequences and reformats your entry.

 .. image:: ../Images/Configure_cohort_topic.png
  :alt: Cohort Configuration dictionary field with the cohorted_discussions key
        defined

7. Scroll back to the **Cohort Configuration** field to verify that your
   entry was saved as you expect. Entries that do not contain all of the
   required punctuation characters revert to the previous value when you save,
   and no warning is presented.


**********************************************
Content-Specific Discussion Topics and Cohorts
**********************************************

When you enable the cohort feature for a course, and :ref:`create content-
specific discussion topics<Create ContentSpecific Discussion Topics>` by adding
discussion components to units in Studio, these content-specific discussion
topics are divided by cohort by default. A student who is assigned to one cohort
group cannot read or add to the posts, responses, or comments contributed by the
members of another cohort group.

If you want all content-specific discussion topics in your course to remain
cohorted, you do not need to take any further action. However, if you want one
or more content-specific discussion topics to be accessible to all students
regardless of cohort, you must perform some configuration tasks.

=====================================================================
Example: Configuring Content-Specific Discussion Topics as Unified
=====================================================================

In this example, you decide that you want all content-specific discussion topics
you add to your course to be unified rather than divided by cohort. To achieve
this, you follow the steps to :ref:`Make ContentSpecific Discussion Topics
Unified`.

Later, while designing one of the final sections in the course, you add a
content-specific discussion topic that you decide should be divided by cohort,
rather than unified like all other discussion components. To achieve this, you
follow the steps to :ref:`Specify Cohorted Discussions as Exceptions`.

.. _Make ContentSpecific Discussion Topics Unified:

================================================================
Make All Content-Specific Discussion Topics Unified by Default
================================================================

.. note:: If you want all content-specific discussion topics in your course to
  be divided by cohort, you do not need to perform any configuration.

This procedure shows how to make all content-specific discussion topics in a course unified by default. 

#. Open your course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Cohort Configuration** field, place your cursor after the opening
   brace character (``{``) and after any existing policy key definitions, then press **Enter**.

#. Press **Enter** to create a new line. On the new line, type
   
    ``"always_cohort_inline_discussions": false``
   

5. Click **Save Changes**. Studio resequences and reformats your entry. 
 
 .. image:: ../Images/cohort_config_always_inline.png
  :alt: Cohort Configuration dictionary field with the cohort key set as true and the always cohort inline discussions key set as false

6. Scroll back to the **Cohort Configuration** field to verify that your entry was saved as you expect. Entries that do not contain all of the required punctuation characters revert to the previous value when you save, and no warning is presented.


.. _Specify Cohorted Discussions as Exceptions:

================================================================
Specify Exceptions to Unified Discussion Topics
================================================================

This procedure shows how, if you have made all content-specific discussion
topics in your course unified by default, you can specify exceptions, and
indicate which content-specific discussion topics should be divided by cohort.

#. Open your course in Studio. 
   
#. To specify a discussion topic as divided by cohort, find the discussion
component in the component editor in Studio, then copy or make a
note of its **Discussion ID**.

.. image:: ../Images/DiscussionID.png

#. If you make any changes in the component editor, click **Save** to save your changes.
#. Select **Settings**, then **Advanced Settings**.

#. In the **Cohort Configuration** field, if the ``cohorted_discussions`` policy
   key does not already exist, type ``"cohorted_discussions":``, followed by one
   or more course-wide discussion topic IDs enclosed by square brackets (``[
   ]``). You can define a set of discussion topics or just one.

   For example, to define a single discussion topic, type
   ``"cohorted_discussions": ["discussion-topic-ID"]``, replacing ``"discussion-
   topic-ID"`` with your discussion topic's ID, and then press Enter.

   To define a set of topics, type the value of the "id" for each discussion
   topic on a new line, enclose it within quotation marks (``" "``), and
   separate the quoted "id" values with commas. For example:

 .. code::  

    "cohorted_discussions": [

       "c2293fa2538a41eca7224b8a07c3d09d",
       "a9823gt3187i38itp2893a8d27f8f20c"
    ]
   
6. Between the opening and closing square brackets (``[ ]``) add one or more IDs
   for the discussion topics that you want to specify as being unified. Use a new
   line for each discussion topic ID that you add, and enclose each ID within
   double quotation marks (``"``), followed by a comma if there are additional IDs
   following.

.. Adding a line to force a line space

7. If ``"cohorted_discussions"`` is followed by other policy keys within the
   **Cohort Configuration** field, make sure there is a comma after the closing
   square bracket character (``],``). You must include a comma to separate each
   policy key that you define.

 .. image:: ../Images/cohort_config_cohorted_discussions.png
  :alt: Cohort Configuration dictionary field with the cohort key set as true, the always cohort inline discussions key set as false, and two discussion topics IDs entered under the cohorted discussions policy key


8. Click **Save Changes**. Studio resequences and reformats your entry.
   
.. Adding a line to force a line space

9. Scroll back to the **Cohort Configuration** field to verify that your entry was saved as you expect. Entries that do not contain all of the required punctuation characters revert to the previous value when you save, and no warning is presented.

