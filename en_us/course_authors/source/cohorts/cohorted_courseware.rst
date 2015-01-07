.. _Cohorted Courseware Overview:


###################################
Creating Cohort-Specific Courseware
###################################

If you have :ref:`cohorts enabled<Enabling and Configuring Cohorts>` in your
course, you can create different course experiences for students in different
cohorts. 

You can design your course so that some students are given different content
than others. You do this by creating content groups in Studio, and designating
specific components in your course as visible only to one or more content
groups. Then, if you associate one or more cohorts with a content group, only
the students in cohorts associated with that content group can see course
content that you have designated for it.

For more details about content groups, see :ref:`About Content Groups`. For an
example of cohort-specific course content, see :ref:`Cohorted Courseware
Example`.


Complete these steps to create cohorted content in your course. 

In Studio:

#. :ref:`Enable cohorts in your course<Enabling and Configuring Cohorts>`.
#. :ref:`Create content groups<Creating Content Groups>`.
#. :ref:`Specify Components in Courseware as Visible Only to Certain Content
   Groups`.
     
In the LMS: 

#. :ref:`Assign students to cohorts<Options for Assigning Students to Cohorts>`.  
#. :ref:`Associate one or more cohorts with a content group<Associate Cohorts
   with Content Groups>`.
#. :ref:`View the Course as a Member of a Content Group`.


.. _Cohorted Courseware Example:

***********************************
Example: Cohort-Specific Courseware
***********************************

Suppose that you have two cohorts in your course: University Alumni and Current
University Students. You intend all students to have substantially the same
course experience, with the exception that only students in the two university-
related cohorts will receive content that is specific to your university and
therefore only of interest to them.

At the end of every section, you intend to include a video message from various
university officials, including the university president and the dean of your
college. These videos will be shown only to students in the university and
alumni cohorts. Also at the end of each section, you intend to include a quiz to
test knowledge of the concepts taught in that section. The quiz will be shown to
all students enrolled in the course.

To achieve this, on the **Group Configurations** page in Studio, you create one
content group called "University-Specific Content". In the Instructor Dashboard,
on the **Membership** tab, you associate both the "University Alumni" and the
"Current University Students" cohorts with the "University Content" content
group.

Then, in your course outline, you change the visibility settings for the video
component at the end of each section so that so that it is visible only to the
"University-Specific Content" content group. You do not need to edit the
visibility settings of the quiz component, because if no content group is
specified in a component's visibility settings, it is visible to all students.

As a final step, you preview the course in the LMS to ensure that students see
the content that is intended for them. You confirm that when you view the course
as a student not in either of the cohort groups, you see a quiz at the end of
each section but not the university-related videos, and when you view the course
as a student in the "University-Specific Content" group, you see a university-
related video as well as the quiz at the end of each section.


.. _About Content Groups:

***********************
Content Groups Overview
***********************

Use content groups to designate specific course content as visible to particular
cohorts of students. You create content groups and associate them with one or
more cohorts. Then, in your course outline, for any components that you want to
make visible only to particular content groups, you select these groups in the
visibility settings. Each component in your course can be made visible to one or
more content groups. Any course components that do not have an explicitly
restricted visibility setting remain visible to all students, regardless of
their cohort.

For an example of using content groups to create cohorted courseware, see
:ref:`Cohorted Courseware Example`.


.. _Creating Content Groups:

*********************
Create Content Groups
*********************

#. In Studio, select **Settings**, then select **Group Configurations**.
#. On the **Group Configurations** page, click **New content group**.
   
.. add image AddContentGroup.png

3. Enter a meaningful name for the content group, then click **Create**.
   The page refreshes to show the name of your new content group.
#. Repeat this step to create as many content groups as you want.

After you create a content group, you can work with your course outline to
specify which components are visible to specific content groups. For details,
see :ref:`Associate Cohorts with Content Groups`.

On the Instructor Dashboard, you associate each content group with one or more
cohorts. For details, see :ref:`Specify Components in Courseware as Visible Only
to Certain Content Groups`.

.. note:: Once a content group is created, you cannot delete it. You can
   remove the association between a content group and its cohorts by associating
   it with another cohort, or by changing the association to **Not Selected**.


.. _Specify Components in Courseware as Visible Only to Certain Content Groups:

*****************************************************************************
Specify Components in Courseware as Visible Only to Particular Content Groups
*****************************************************************************

After you create at least one content group, you can edit your course in Studio
and modify the visibility settings of components that you want to make visible only to particular content groups. 

.. note:: You do not need to edit the visibility settings of components that are
   intended for all students. Components that you do not explicitly indicate as
   visible to a group are visible to all students enrolled in your course,
   regardless of the cohort that they belong to.

You can specify content as visible to content groups only at the component level
in a unit. You cannot specify entire units, subsections, or sections for
visibility to content groups.

In a separate task, you associate cohorts with content groups. Then, only the
cohorts associated with content groups which you selected in a component's
visibility settings can view the component. See :ref:`Associate Cohorts with
Content Groups` for details about associating cohorts with content groups.

To specify components as visible only to particular content groups, follow these steps.

#. In Studio, select **Content**, then select **Outline**. For each component
   that you want to make visible only to a particular content group or groups,
   click the unit name, then click the **Visibility Settings** icon.

.. add image VisibiitySettingInUnit.png  

3. In the **Editing visibility** dialog, select **Specific Content Groups**,
   then select the checkbox for each content group for which you want the current
   component to be visible.

.. add image EditVisibility.png

4. Click **Save**.

The **Visibility Settings** icon for the component is now black, and the
publishing details for the course section in the sidebar refresh to indicate
that some content is visible only to particular groups.

.. add image OnlyVisibleToParticularGroups.png
.. add image VisibilitySomeGroup.png

For details about previewing your course to ensure that each cohorted content
group correctly sees the content intended for them, see :ref:`View the Course as
a Member of a Content Group`.


.. _Associate Cohorts with Content Groups:

*************************************
Associate Cohorts with Content Groups
*************************************

After you create a content group, you can associate it with one or more cohorts
that should share the same visibility settings for special content in your
course.

.. note:: A content group can be associated with more than one cohort; a cohort
   cannot be associated with more than one content group.

To associate a cohort with a content group, follow these steps:

#. In the LMS, select **Instructor**, then select **Membership**. 
   
#. Scroll to the **Cohort Management** section at the bottom.

#. From the drop down list, select the cohort that you want to associate
   with your content group.

   If the cohort that you want to associate with your content group does not yet
   exist, you can create it here.
   
4. Click the **Settings** tab for the selected cohort.

#. Under **Associated Content Group**, choose the **Select a Content Group** option.

#. From the drop down list, select the content group that you want your cohort
   to be associated with.
  
.. add image CohortAssociateWithContentGroup.png   

#. Click **Save**.
   
   You have now associated your content group with a cohort. Any course content
   that you :ref:`designate as visible to that content group<Specify Components
   in Courseware as Visible Only to Certain Content Groups>` is visible to
   students in the associated cohort or cohorts.

You can associate additional cohorts with the same or a different content group
by repeating steps 3 to 7.

For an example of using content groups to create cohort-specific courseware, see
:ref:`Cohorted Courseware Example`.


.. _Preview Cohort Specific Courseware:

*************************************
Previewing Cohort-Specific Courseware
*************************************

After you designate components in your course as being visible only to certain
content groups, you can preview your courseware to ensure that each group
correctly sees the content intended for them.

You can view the course as a member of these groups:


.. list-table::
    :widths: 15 30
    :header-rows: 1

    * - Role
      - When You "View As" This Role
    * - Staff
      - You see all content in the course, including content
        that is hidden from students.
    * - Student
      - You see any content that is intended for all
        students.
    * - Student in <Content Group Name>            
      - You see content that is intended for all students, as well
        as any content specifically set to be visible to this content group.

#. In Studio, in the course outline, click **Preview Changes**. You see your
   course section in the **Courseware** section of the LMS.

#. In the navigation bar at the top of the page, select one of the options in
   the **View this course as** drop down list, as described in the table above.

.. add image ViewCourseAs.png

   The course view refreshes and the content is presented as a member of the
   selected content group would see it.
