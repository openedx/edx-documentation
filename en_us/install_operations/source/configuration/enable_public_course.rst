.. _Enable Public Course Content:

####################################
Enabling Public Course Content
####################################

By default, learners must create an Open edX account, be signed in to the LMS, 
and enroll in a course before they can see the course content. The *Public 
Course Content* feature gives you the option to make either a course outline 
or course content available to anyone, regardless of whether they have registered 
for an Open edX account or enrolled in the course. You can decide which courses, 
and which parts of those courses, that you want to make public. For example, 
you can:

  * **Make just the course outline public.** The LMS displays the course outline 
    without any links to internal course pages, giving potential learners an 
    overview of what they will see when they enroll.

  * **Make the entire course public.** Anyone visiting your course outline can 
    follow links to visit internal course pages, and freely navigate HTML and 
    Video course content and handouts.

  * **Show different content blocks to public learners vs. enrolled learners.** 
    You can create content tailored to the public view, while still supporting 
    the needs of your enrolled audit and paid learners. 

****************************************
Public Course Content and Search Engines
****************************************

In addition to making your course content visible to people who already use your
site, the public course content feature also allows Google and other search 
crawlers to index your public course contents. People who are searching for 
information about the topics you teach can then find your course through their 
normal search behaviors. This can increase the visibility of your organization's 
courses and boost enrollments for genuinely interested learners.

*****************************************
Enable Public Course Content in the Admin
*****************************************

The public course content feature is enabled in the Django LMS Admin with the 
**seo.enable_anonymous_courseware_access** waffle flag. You can use this flag 
in two different ways:

* Create a normal waffle flag to enable this flag for all courses. For more
  information, see the `Waffle documentation`_.

  .. image:: ../Images/enable_anonymous_courseware_access.png
         :alt: Setting a waffle flag in the Django LMS Admin.

* Create a **Waffle flag course override** with the ID of a course to enable 
  this flag for just that course.  

  .. image:: ../Images/course_enable_anonymous_courseware_access.png
         :alt: Setting a waffle flag in the Django LMS Admin.

*************************************
Set Visibility for a Course in Studio
*************************************

After you set the waffle flag to enable public course content in the Django
LMS Admin, you set the visibility for the course content and its About page
in Studio Advanced Settings.

=================================
Set Course Content Visibility
=================================

#. View your course in Studio, and navigate to the **Advanced Settings** page. 

#. Locate the **Course Visibility For Unenrolled Learners** setting.
   
   By default, this is set to ``"private"``, which ensures that only enrolled 
   learners can access your course content.

   If you change this to ``"public_outline"``, then your course outline, but not
   the other course content, will be visible to everyone.

   If you change this to ``"public"``, then all of your course content, including
   the course outline, will be visible to everyone.

=================================
Set Course About Page Visibility
=================================

If you want your course to be crawled by Google and other search engines, you 
should also ensure that your course's About page is visible, and that it is 
shown in the course catalog. Without these settings, only people with a link 
to your course outline or specific content blocks will be able to find your 
course.

#. View your course in Studio, and navigate to the **Advanced Settings** page. 

#. Locate the **Course Visibility in Catalog** setting and set it to ``"both"``.
   
   
********************
Feature Limitations
********************

The public course content feature is currently subject to some limitations, 
including the following.

* Anonymous or unenrolled learners are not members of any cohort, and so they
  only see course blocks that are not assigned to a content group. If you want
  to restrict public access to selected course blocks, you need create content
  groups for your private content, and ensure that your enrolled learners are
  members of a cohort that can see this content group.

* Only Text components, Video components, and course handouts have a "public"
  view. Unenrolled learners will see a message requesting that they enroll to 
  see more complex content types, such as discussion forums, problem blocks, 
  randomized content blocks, exams, Open Response Assessment, and other XBlocks.

* Unenrolled learners will not see course completion or progress updates as 
  they proceed through the course, and Open edX doesn't remember where they 
  left off if they leave the course and come back.

* The edX mobile apps do not support public course content.



.. include:: ../../../links/links.rst
