.. _Content Libraries:

##################
Content Libraries 
##################

In Studio, use content libraries to build a pool of components that can be
shared across multiple courses to create randomized assessments. You can add
HTML components, problems, and video components to a library. Peer assessment
and discussion components are not supported in randomized content blocks.

Create randomized assessments in your course by adding a randomized content
block to a unit, and specifying the number and type of problems that each
student is assigned, to be drawn from the specified content libraries. If you
specify more than one library from which to randomly draw components for the
randomized assessment, the content from all specified libraries is combined
before the random selection is made.

The libraries that you create or have access to are listed on the **Libraries**
tab on the Studio Home page.

See the following sections for details about creating and managing content
libraries.

* :ref:`Enable the Library Content Feature`
* :ref:`Create a New Library`
* :ref:`Add Components to a Library`
* :ref:`View the Contents of a Library`
* :ref:`Edit Components in a Library`
* :ref:`Give Other Users Access to Your Library`

See the following sections for details about using content library components in
a course.

* :ref:`Use Components from Libraries in a Course`
* :ref:`Add a Randomized Content Block to Your Course`
* :ref:`View the Matching Contents of a Randomized Content Block`
* :ref:`Edit Components in Randomized Content Blocks`
* :ref:`Get the Latest Version of Library Content`


.. _Create a New Library:

********************
Create a New Library
********************

To create a new :ref:`library<Content Libraries>`, follow these steps.

#. Log in to Studio.
#. Click **New Library**.
#. Enter mandatory information for your new library, then click **Create**.

  .. image:: ../Images/ContentLibrary_NewCL.png
     :alt: Image of the library creation page

  * For **Library Name**, enter the public display name for your library. Choose
    a meaningful name that will help you and other course team members to
    identify the contents of the library. For example, "Level 200 Math
    Problems".

  * For **Organization**, enter the identifier for your university. For
    example, enter HarvardX or MITx. Do not include spaces or special
    characters.

  * For **Library Code**, enter an identifier for your library that is unique
    within your organization. This code becomes part of the URL for your
    library, so do not include spaces or special characters in the code.

.. note:: Enter new library information carefully. After you create a new
     library, you cannot delete it. The Library Code becomes part of the URL
     for your library.   

4. Click **Create**.

You see the new library, to which you can now add components. For details about
adding components to a library, see :ref:`Add Components to a Library`.

The system-generated Library ID for the new library is shown in the sidebar.

  .. image:: ../Images/ContentLibraryID.png
     :alt: The Library ID for the new library is shown the sidebar

.. note:: You might want to copy or make a note of the Library ID for the    new
   library. When you add a randomized content block to a course unit, you use
   the Library ID to specify this library as a source for the randomized
   content.


.. _Edit a Library:

**************
Edit a Library
**************

After you create a new library, the only change you can make to the initial
library information is to the name. However, at any time, you can make changes
to the components in your library, including adding or deleting components, and
editing the settings of components.

To change the name of a library, follow these steps.

#. Log in to Studio.
#. Click **Libraries**, then click the library whose name you want to edit.
   
#. Click the **Edit** icon next to the library name. 
   
   The library name field becomes editable.
   
  .. image:: ../Images/ContentLibrary_EditName.png
     :alt: The Edit icon to the right of the Library Name

4.  In the library name field, make edits or enter a new library name.
#. Click anywhere outside the library name field to save your changes.

For details about editing the contents of a library, refer to :ref:`Edit
Components in a Library`. See also :ref:`Add Components to a Library` and
:ref:`Delete a Library`.


.. _Add Components to a Library:

****************************
Add Components to a Library
****************************

To add new :ref:`components<What is a Component>` to your library, follow these
steps.

#. Log in to Studio.
#. Click **Libraries**, then click the library that you want to add components to.

#. Click **Add Component**, then click the component type that you want to add
   under **Add New Component**.

For more information about the various types of components, see these topics.

* :ref:`Working with HTML Components`
* :ref:`Working with Problem Components`
* :ref:`Working with Video Components`

After you add a component to a library, you can edit its settings, which are
retained when the component is selected from the library and used in a course.
Within a course, you can further edit the component settings or revert to the
library settings. For details, refer to :ref:`Edit Components in a Library` and
:ref:`Get the Latest Version of Library Content`.


.. _View the Contents of a Library:

******************************
View the Contents of a Library
******************************

To view the entire contents of a library in Studio, follow these steps.

#. Log in to Studio.
#. Click **Libraries**, then click the library whose components you want to
   view.

The components in the library are displayed in the order in which they were
added, with the most recently added at the bottom. Each page shows up to 10
components. If your library has more than 10 components, additional components
are shown on other pages.

The range of the components shown on the current page, and the total number of
components, are shown at the top of the page.

You can navigate through the pages in these ways:

* Use the **<** and **>** buttons at the top and bottom of the list to navigate
  to the previous and next pages.

* At the bottom of the page, you can edit the first number in the page range.
  Click the number to place your cursor in the field, then enter the page number
  you want to jump to.

  .. image:: ../Images/file_pagination.png
     :alt: Image showing a pair of page numbers with the first number circled

To view the list of matching components in the library, see :ref:`View the
Matching Contents of a Randomized Content Block`.

To view the randomized content as a student would see it, see :ref:`View the
Randomized Content as a Student`.


.. _Edit Components in a Library:

****************************
Edit Components in a Library
****************************

You can perform the same tasks with components in a library as you can with
components that you have added to a course. 

For step-by-step instructions for editing, duplicating, or deleting components,
refer to the following topics:

* :ref:`Edit a Component`
* :ref:`Duplicate a Component`
* :ref:`Delete a Component`

.. note:: If you modify components in your library that are in use in a course,
   including deleting components, these updates in the "source" library are not
   reflected in the course unless you manually update the randomized content
   block in the course outline. For details about updating library components
   used in your course to match the latest version in the content library, see
   :ref:`Get the Latest Version of Library Content`.


.. _Delete a Library:

*****************
Delete a Library
*****************

You cannot delete a library after creating it. Instead, you can simply
discontinue use of an unwanted library. To do so, first make sure that none of
its components are in use in any courses, then delete all components in the
library. You can also :ref:`edit the name of the library<Edit a Library>` to
make it clear to other course staff that the library should not be referenced in
courses.

For details about deleting components in a library, see :ref:`Edit Components in
a Library`.


.. _Give Other Users Access to Your Library:

***************************************
Give Other Users Access to Your Library
***************************************

You can give other Studio users access to your library. Depending on their role,
additional library users can view and use library content in courses, edit
library content, or add and manage other library users. All course team members
must be registered with Studio and have an active account.

There are three levels of access for libraries:

* **User** -- Users can view library content and can reference or use library
  components in their courses, but they cannot edit the contents of a library.

* **Staff** -- Staff are content co-authors. They have full editing privileges
  for a library.

* **Admin** -- Admins have full editing privileges for a library. In addition,
  they can add and remove other team members. There must be at least one user
  with Admin privileges in a library.

.. note:: New library members are first added with User privileges only. After
   they are added with User privileges, you can then grant them Staff or Admin
   access.


=========================
Add a User to the Library
=========================

To grant initial User access to a team member, follow these steps.

#. Ensure you have Admin access. 
#. Ensure that the new team member has an active Studio account. 
#. In Studio, click the **Libraries** tab and locate the library to which you
   are adding this user.
#. From the **Settings** menu select **User Access**.
#. On the **User Access** page, click **Add a New User**.
#. Enter the new user's email address, then click **ADD USER**.
   
   The new user is added to the list of people with access to the library, with
   their role indicated.


=========================
Add Staff or Admin Access
=========================

After you add new members to the library and give them User access, you (or
another library user with the Admin role) can grant them additional privileges.
To grant a user Admin privileges, you must first assign them to the Staff role,
then assign them to the Admin role.

To assign a library member to a role with higher privileges, follow these steps.

#. In Studio, click the **Libraries** tab and locate your library. 
#. From the **Settings** menu select **User Access**. 
   
#. On the **User Access** page, locate the user to whom you are giving
   additional privileges. 

  - If they are currently in the User role, click **Add Staff Access**. 
  - If they are currently in the Staff role, click **Add Admin Access**.

  The user's display listing is updated to indicate their new role. In
  addition, their listing now includes a button to remove their current role
  and move them back to their previous level of access. For details about
  changing a library team member's role by reducing their level of access, see
  :ref:`Remove Staff or Admin Access`.


.. _Remove Staff or Admin Access:

============================
Remove Staff or Admin Access
============================

After you have granted a library team member Staff Access or Admin Access, you
(or another library user with the Admin role) can reduce their level of access.

To remove Staff or Admin access from a library user, follow these steps.

#. In Studio, click the **Libraries** tab and locate your library. 
#. From the **Settings** menu select **User Access**. 
   
#. On the **User Access** page, locate the user whose access level you are
   changing. If they are currently in the Staff role, click **Remove Staff
   Access**. If they are currently in the Admin role, click **Remove Admin
   Access**.

   The user's display listing is updated to indicate their new role. 

.. note:: There must always be at least one Admin for a library. If there is
   only one user with the Admin role, you cannot remove them from the Admin role
   unless you first assign another user to the Admin role.


.. _Use Components from Libraries in a Course:

*****************************************
Use Components from Libraries in a Course
*****************************************

After you create one or more content libraries and add components to them, you
can create randomized assessments in your course that draw a specified number
and type of problem randomly from your content libraries.

If you specify more than one library from which to randomly draw components, the
content from all specified libraries is combined before the random selection is
made.

Using components from content libraries in your course involves two steps.

#. :ref:`Enable the Library Content Feature`
#. :ref:`Add a Randomized Content Block to Your Course`
   
.. note:: After adding a randomized content block to your course, be aware that
   if components in the source library or libraries change, you must manually
   update the components in the course outline if you want to keep the components
   synchronized with the version in the library.

For details about working with randomized content blocks in the course outline,
see these topics.

* :ref:`View the Matching Contents of a Randomized Content Block`
* :ref:`Edit Components in Randomized Content Blocks`
* :ref:`Get the Latest Version of Library Content`


.. _Enable the Library Content Feature:

==================================
Enable the Library Content Feature
==================================

You must enable the library content feature before you can use randomized
problems from content libraries in your courses.

#. In Studio, open the course in which you want to provide library content.

#. Select **Settings**, then **Advanced Settings**.

#. In the **Advanced Module List** field, place your cursor between the
   supplied pair of braces.

#. Type ``"library_content"``. 

#. Click **Save Changes**. 
   
   Studio reformats the name:value pair you just entered to indent it on a new
   line.

  .. image:: ../Images/ContentLibraries_AdvancedSetting.png
     :alt: Advanced Module policy key "library_content"


.. _Add a Randomized Content Block to Your Course:

=============================================
Add a Randomized Content Block To Your Course   
=============================================

After you :ref:`enable the library content feature<Enable the Library Content
Feature>` you can add library content to your courses using the Randomized
Content Block advanced component.

#. In Studio, open the course in which you want to add randomized problems from
   one or more content libraries.

#. Click **Content** then click **Outline**.

#. In the unit where you want to add a set of randomized problems, click **Add
   New Component** 

#. Click **Advanced**, then click **Randomized Content Block**.
   The randomized content block is added to your unit.

#. Click the **Edit** icon or click the **Select a Library** link.
   
#. In the randomized content block settings, specify the details of the content
   you want to add in this block.

  - For **Count**, enter the number of problems to be drawn from the specified
    content library or libraries for each student.

  - For **Display Name**, enter name that you want students to see for this
    block.

  - For **Libraries**, enter the unique Library ID found in the upper right of
    the Library page in Studio. To select problems from more than one content
    library, click **Add** to enter each additional Library ID.

  - For **Problem Type**, from the drop down list select a specific type of
    problem to be drawn from the library or libraries, or select **Any Type**
    if you do not want to select a particular type of problem.

    .. image:: ../Images/ContentLibraries_SelectProblemType.png
     :alt: The Edit icon to the right of the Library Name    

  - For **Scored**, from the drop down list select **True** or **False** to
    indicate whether the supplied problems should be graded.

7. Click **Save** when you have finished specifying the details of your
   randomized content block.

To view the list of matching components in the library, see :ref:`View the
Matching Contents of a Randomized Content Block`.

To view the entire contents of the library in Studio, see :ref:`View the
Contents of a Library`.
   

.. _View the Matching Contents of a Randomized Content Block:

*********************************************************
View the Matching Contents of a Randomized Content Block
*********************************************************

In the course outline, in the unit that uses a randomized content block, you can
view the list of all components that match the specifications in that block. For
example, if you have specified in the randomized content block that you want to
assign problems of the "Multiple Choice" type, you see all the multiple choice
problems that exist in the referenced library or libraries.

#. In Studio, navigate to the unit containing the randomized content block that
   references your library.
#. In the randomized content block, click the **View** icon.
   
   You see all components that match the specifications in the randomized
   content block. The text at the top of the list of components indicates how
   many of these components are randomly selected and provided to each student.

To view the contents of a library in Studio, see :ref:`View the Contents of a
Library`.

To view the randomized content as a student would see it, see :ref:`View the
Randomized Content as a Student`.


.. _View the Randomized Content as a Student:

****************************************
View the Randomized Content as a Student
****************************************

To view components from a randomized content block as a student would see them,
follow the steps described in the :ref:`Preview a Unit` topic.

To view the list of matching components in the library, see :ref:`View the
Matching Contents of a Randomized Content Block`.

To view the entire contents of the library in Studio, see :ref:`View the
Contents of a Library`.


.. _Get the Latest Version of Library Content:

*********************************************
Getting the Latest Version of Library Content
*********************************************

If you modify the contents of a library that is references by randomized content
blocks in one or more courses, you can bring the course components up to date
with the version in the library.
   
* If the components in the randomized content block have not been edited in the
  course outline, when you next open the randomized content block in the course
  outline, you see a message indicating that the component is out of date in
  comparison with the library.

  .. image:: ../Images/ContentLibraries_ComponentUpdateNow.png
     :alt: Error message shown when the source library has changed, with the
      Update Now link circled.

  To update your randomized content block components to the latest versions in the content library, click **Update now**.

  The randomized content block is brought up to date with the latest contents of
  the library or libraries that it references.

* If you edited the components in the course outline so that they are different
  from the original version in the library, you do not lose your changes if you
  click **Update now**. In this case, the changes that were made in the randomized
  content block in the course outline are kept, but a **Clear** button becomes
  available next to the changed field in the component.

  .. image:: ../Images/ContentLibraries_ResetComponentField.png
     :alt: Clear button in the course component field reverts value to library value.

  
  To clear any edits made in the course outline and bring your edited components
  up to date with the version in the library, click **Clear**.

  The value in that component field is reset to the current value in the library.


.. _Edit Components in Randomized Content Blocks:

******************************************************
Editing Components in Randomized Content Blocks
******************************************************

From within your course outline, in the unit that uses a randomized content
block, you can edit component settings in the same way as you do for any other
component in your course.

The default settings of a randomized component might have been set when it was
saved in the library. You can modify component settings so that they are
different from the "source" component in the library.

You can also reset a component's settings to the library default. If a
component's settings have been changed from the default settings in the library,
a **Clear** icon is shown next to the setting field.

 .. image:: ../Images/ContentLibraries_ResetComponentField.png
    :alt: Clear button in the course component field reverts value to library value.

Click the **Clear** icon to restore the library default setting for that field.

For details about getting the latest versions of library content in a randomized content block, see :ref:`Get the Latest Version of Library Content`.

