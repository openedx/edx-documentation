.. _Cohorted Courseware Overview:


#############################
Creating Cohorted Courseware
#############################

If you have :ref:`cohort groups enabled<Enabling and Configuring Cohorts>` in
your course, you can create different course experiences for students in
different cohort groups.

You can design your course so that students in one cohort group are given
different content than students in another cohort group. You do this by
associating one or more cohort groups with a cohorted content group, and
designating specific course components as visible to particular content groups.
Any course components that do not have an explicitly restricted visibility
setting remain visible to all students, regardless of their cohort group. For
more details about cohorted content groups, see :ref:`About Cohorted Content
Groups`.

Complete these steps to create cohorted content in your course. Optionally, you
can transpose the order of steps 4 and 5.

#. :ref:`Enable cohorts for your course<Enabling and Configuring Cohorts>`.
#. :ref:`Assign students to cohort groups<Options for Assigning Students to
   Cohorts>`. 
#. :ref:`Create cohorted content groups in Studio<Creating Content Groups>`.
#. :ref:`Associate one or more cohort groups with a cohorted content
   group<Associate Cohort Groups with Content Groups>`.
#. In your course outline, :ref:`Specify Components in Courseware as Visible Only to Certain Content Groups`.
#. :ref:`View the Course as a Member of a Content Group`.


.. _Cohorted Courseware Example:

********************************
Example: Cohorted Courseware
********************************

You have four cohort groups in your course: A, B, and C. In one subsection in
your course, you want the students in cohort group A to see a video, while the
students in the remaining two cohort groups see a reading assignment. You want
to provide the same quiz to all students, regardless of cohort group, at the end
of that subsection.

To achieve this, on the **Group Configurations** page in Studio, you create two
cohorted content groups, one called "Video" and the other called "Reading". In
the Instructor Dashboard, on the **Membership** tab, you associate cohort group
A with the "Video" content group, and you associate cohort groups B and C with
the "Reading" content group. Then, in your course outline, in the relevant
subsection, you edit the video component so that it is visible only to the
"Video" content group (which consists of cohort group A) and you edit the
reading assignment component so that it is visible only to the "Reading" content
group (which consists of cohort groups B and C). You do not need to edit the
visibility settings of the quiz component, because if no content group is
specified in a component's visibility settings, it is visible to all students.

As a final step, in the Instructor Dashboard you preview the course to ensure
that students see the content that is intended for them. You view the course as
a member of each of the content groups to confirm that as a student in the
"Video" content group, you see a video and the final quiz but not the reading
assignment; and as a student in the "Reading" content group, you see a reading
assignment and the final quiz, but not a video.


.. _About Cohorted Content Groups:

********************************
Cohorted Content Groups Overview
********************************

Cohorted content groups, also referred to as content groups, are the means by
which you can designate specific course content as visible to particular cohort
groups of students. You create cohorted content groups and associate them with
one or more cohort groups, then indicate in your courseware when particular
content is visible to a content group. Each component in your course can be made
visible to one or more content groups.

Any course components that do not have an explicitly restricted visibility
setting remain visible to all students, regardless of their cohort group.

For an example of using content groups to create cohorted courseware, see
:ref:`Cohorted Courseware Example`.


.. _Creating Content Groups:

******************************
Create Cohorted Content Groups
******************************

#. In Studio, select **Settings** then select **Group Configurations**.
#. On the **Group Configurations** page, click **New cohorted content group**.
#. Enter a meaningful name for the content group, then click **Create**.
#. Repeat this step to create as many cohorted content groups as you want.

After you create a content group, you can go to the Instructor Dashboard to
associate it with one or more cohort groups, or work with your course outline to
specify which components are visible to specific content groups.

For details, see :ref:`Associate Cohort Groups with Content Groups` and
:ref:`Specify Components in Courseware as Visible Only to Certain Content Groups`.

.. note:: Once a content group is created, you cannot delete it. You can
   remove the association between a cohorted content group and its cohort groups
   by associating it with another cohort group, or by changing the association
   to **Not Selected**.


.. _Associate Cohort Groups with Content Groups:

************************************************
Associate Cohort Groups with Content Groups
************************************************

After you have created a content group, you can associate it with one or more
cohort groups. You can use content groups to specify that components in your
course are visible only to students in the cohort group or groups associated
with content groups.

#. In the LMS, select **Instructor**, then select **Membership**. 
   
#. Scroll to the **Cohort Management** section at the bottom.

#. From the drop down list, select the cohort group that you want to associate
   with your content group.

   If the cohort groups that you want to associate with your content group do
   not yet exist, you can create them here.
   
4. Click the **Settings** tab for the selected cohort group. Under **Associated Cohorted Content Group**, choose the **Select a Content Group** option.

#. From the drop down list, select the content group that you want your cohort
   group to be associated with. 
   
#. Click **Save**.
   
   You have now associated your cohorted content group with a cohort group. Any
   course content that you :ref:`designate as visible to that content
   group<Specify Components in Courseware as Visible Only to Certain Content
   Groups>` is visible to students in the associated cohort group or groups.

You can associate additional cohort groups with the same or a different content
group by repeating steps 3 to 6.

For an example of using content groups to create cohorted courseware, see
:ref:`Cohorted Courseware Example`.


.. _Specify Components in Courseware as Visible Only to Certain Content Groups:

***************************************************************************
Specify Components in Courseware as Visible Only to Certain Content Groups
***************************************************************************

After you have created at least one content group, you can edit your course in
Studio and designate whether all students, or only particular content groups,
can see certain components.

See :ref:`Associate Cohort Groups with Content Groups` for details about
associating cohort groups with content groups. You can complete the association
task either before or after designating courseware as visible to a cohorted
content group.

.. note:: You do not need to edit the visibility settings of components that are
   intended for all students. Components that you do not explicitly indicate as
   visible to a group are visible to all students enrolled in your course,
   regardless of the cohort group that they belong to.

#. In Studio, select **Content**, then select **Outline**.

#. For each component that you want to make visible only to a particular content
   group or groups, click the **Visibility Settings** icon.

#. In the **Editing visibility** dialog, select **Specific Content Groups**,
   then select the checkbox for each content group for which you want the current
   component to be visible.

#. Click **Save**.

The **Visibility Settings** icon for the component and the publishing details
for the course section in the sidebar refresh to indicate that some content is
visible only to particular groups.

For details about previewing your course to ensure that each cohorted content
group correctly sees the content intended for them, see :ref:`View the Course as
a Member of a Content Group`.


.. _View the Course as a Member of a Content Group:

***********************************************
View the Course as a Member of a Content Group
***********************************************

After you designate components in your course as being visible only to certain
content groups, you can preview your courseware to ensure that each group
correctly sees the content intended for them.

You can view the course as a member of these groups:

.. list-table::
    :widths: 15 30

    * - **Role**
      - **What You See When You "View As" This Role**
    * - Staff
      - You see all content in the course, including content
        that is hidden from students.
    * - Student
      - You see any content that is intended for all
        students.
    * - Student in <Cohorted Content Group Name>            
      - You see content that is intended for all students, as well
        as any content specifically set to be visible to this content group.

#. In Studio, in the course outline, click **Preview Changes**. You see your
   course section in the **Courseware** section of the LMS.

#. In the navigation bar at the top of the page, select one of the options in
   the **View this course as** drop down list, as described in the table above.

   The course view refreshes and the content is presented as a member of the
   selected group would see it.
