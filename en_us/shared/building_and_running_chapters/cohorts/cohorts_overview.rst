.. _Cohorts Overview:


#############################
Using Cohorts in your Courses
#############################

By :ref:`setting up cohorts<Enabling and Configuring Cohorts>` in a course, you
create smaller communities of students. You can design different course
experiences for students in different cohorts. In discussion topics that are
divided by cohort, students can also communicate and share experiences privately
within the cohort that they are assigned to. Cohort-only discussion
opportunities can help students develop a sense of community, provide
specialized experiences, and encourage deeper, more meaningful course
involvement.

If you use cohorts in your course, you define a set of cohorts to reflect
communities of students, then select a strategy for :ref:`assigning students to
cohorts<Options for Assigning Students to Cohorts>`.

.. note::    
   * Every student must be assigned to a cohort. This ensures that
     every student has the ability to read and contribute to course discussion
     topics.

   * Each student can be in one and only one cohort. 

   To provide students with a consistent experience throughout the course run,
   do not change a student's cohort assignment after the course begins.

For more information about using cohorts in courses, see:

* :ref:`Enabling and Configuring Cohorts`

* :ref:`Setting Up Discussions in Courses with Cohorts<Set up Discussions in
  Cohorted Courses>`

* :ref:`Moderating Discussions for Cohorts`

For information about discussions in general, see :ref:`Discussions`.


.. _Options for Assigning Students to Cohorts:

*****************************************
Options for Assigning Students to Cohorts
*****************************************

You can configure the cohort feature so that students are assigned to cohorts
automatically or manually. You can also use a combination of both assignment
methods. Typically, your purpose in including the cohort feature in your course
determines which assignment option you will use for your course.

* :ref:`All Automated Assignment`

* :ref:`All Manual Assignment`

* :ref:`Hybrid Assignment`

* :ref:`Default Cohort Group`


.. _All Automated Assignment:

========================================================
Automated Assignment: Making MOOC Discussions Manageable
========================================================

In very large courses, the number of posts made to course discussion topics can
make for a daunting amount of daily reading. In such courses, dividing the
enrollees into separate cohorts makes the volume of posts, responses, and
comments by the members of each one more manageable, and is more likely to
foster community feeling.

To implement this assignment strategy, you enable the cohort feature and create
a set of "auto" (automated) cohorts. The first time a student views the course
**Discussion** page or any of the content-specific discussion topics, he or she
is randomly assigned to one of the auto cohorts. Together, all of the students
who are assigned to the same group form a cohort.

These guidelines, which are based on the experiences of MOOC teams that have
used the cohort feature in this way, are suggested to help you determine how
many automated cohorts to define for your course.

* Each cohort should be large enough to inspire lively participation and
  diverse points of view, but small enough to allow a sense of community to
  develop. Cohorts formed by random assignment tend to be successful if they
  include between 200 and 500 members.

* For every 10,000 students who enroll, approximately 200 to 400 students
  remain active in the discussions throughout the course run. 

* Divide the estimated total enrollment of the course run by 10,000.

* Use the result as the number of automated cohorts to create.

For example, two days before it starts, a course has an enrollment of 80,000
students. To create small communities within the discussions, the course team
enables the cohort feature and creates eight automated cohorts. As they visit
the **Discussion** page and view the discussion components in the course
content, students are assigned to one of the cohorts. In divided discussion
topics, students read and respond to contributions made by other members of the
same cohort only.

For more information, see :ref:`Implementing the Automated Assignment
Strategy`.


.. _All Manual Assignment:

=====================================================
Manual Assignment: Grouping by Common Characteristics
=====================================================

In SPOCs and other courses with small- to medium-sized enrollments, known
existing commonalities can be used to identify cohorts. An example is a course
that enrolls students from different companies or with different educational
backgrounds, or members of alumni or parent groups. When students are assigned
to cohorts on the basis of a characteristic that they share, they can privately
discuss applications for what they are learning and explore resources and ideas
that are of particular interest.

To implement this assignment strategy, you identify the "real-world" cohorts
that your students belong to already. You enable the cohort feature and create a
"manual" cohort to represent each of those cohorts. You then assign each student
to one of the manual cohorts. Every student who enrolls, including those who
enroll after the course starts, must be assigned to a cohort.


.. note:: To ensure that every student is assigned to a cohort, you can set up a
   single automated cohort, as described for the :ref:`hybrid assignment strategy<Hybrid Assignment>`. If you do not create an automated cohort, the
   system automatically creates a :ref:`default cohort<Default Cohort Group>` and
   assigns students to it if necessary.

For more information, see :ref:`Implementing the Manual Assignment Strategy`.


.. _Hybrid Assignment:

=============================================================
Hybrid Assignment: Accommodating Small Groups Within a Course
=============================================================

For some courses, the manual assignment strategy isn't feasible to execute, and
the automated assignment strategy doesn't accommodate the existing cohorts that
exist in the student body. The enrollment may be too large to complete manual
assignments effectively, or only some of the students may have strong defining
characteristics among an otherwise diverse student body. For these courses, you
can use a hybrid of the two strategies to implement the cohort feature.

An example is a course that enrolls members of an alumni association. The alumni
want an opportunity for private interactions, so manual assignment of those
students to a cohort makes sense. For other students in the class, manual
assignment isn't needed: you create one or more automated cohorts for
those students.

Before you implement the hybrid strategy, you identify the characteristics that
define existing cohorts in the student body. You also decide whether you want
the rest of the students in the course to be divided into their own, similarly-
sized cohorts, or if you want them all to be in just one other cohort.

After you enable the cohort feature, you create a manual cohort for each
cohort that you identified. You manually assign students who belong to those
cohorts to the corresponding cohorts. You also set up automated cohorts for
the other students in the course, or rely on the default cohort. The
students who are not assigned to a manual cohort are automatically
assigned to one of the automated cohorts, or to the default cohort
if you choose to use it, when they view the **Discussion** page or a discussion
topic in the course content. (For best results when you use this strategy, you
complete all manual assignments before the course starts and students begin
viewing discussion topics.)

For more information, see :ref:`Implementing the Automated Assignment
Strategy` and :ref:`Implementing the Manual Assignment Strategy`.


.. _Default Cohort Group:

===========================================================
Ensuring That All Students Are Assigned: The Default Cohort
===========================================================

In a course that has the cohort feature enabled, all students must be assigned
to a cohort. To assure that all students are assigned, the system automatically
creates a default cohort and assigns students to it if necessary. Creation of
the default cohort only occurs if you do not define any automated cohorts for
your course. Any student who is not assigned to a manual cohort is assigned to
the default cohort automatically when they visit the **Discussion** page or a
discussion topic in the course content.

Students who are assigned to the default cohort see a cohort name of "Default
Group" in discussion posts.

.. image:: ../../../shared/building_and_running_chapters/Images/post_visible_default.png
 :alt: A discussion topic post with "This post is visible to Default Group" 
       above the title

If you want students to see a different cohort name when your course starts, you
can add an automated cohort with the name that you prefer. See :ref:`Define Auto
Cohorts`. (Adding an automated cohort to your course for this purpose is not
recommended after your course starts.)

You can check the :ref:`student profile information report<View and download
student data>` for your course to see if any students are assigned to the
default cohort in your course, and change their cohort assignments. Note,
however, that in divided discussion topics students can only see posts by
members of their currently assigned cohort: when a student is reassigned, posts
"disappear". As a result, any cohort assignment changes should be done as early
in the course run as possible so that students see discussion posts and
contributions that remain consistent over time.
