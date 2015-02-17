.. _Randomized Content Blocks:

#########################
Randomized Content Blocks
#########################

If your course has :ref:`content libraries<Content Libraries>` enabled and you
have access to a library whose content you want to use, you can reference that
library to create randomized assignments for students.

To create a randomized assignment, you add one or more randomized content blocks
to a course unit. For each randomized content block, specify one or more
libraries from which to draw the content, and indicate the number and optionally
the type of problem to randomly give each student. If you specify more than one
library from which to randomly draw components for the randomized assignment,
the content from all specified libraries is combined before the random selection
is made.

The libraries that you create or have access to are listed on the **Libraries**
tab on the Studio Home page. For details about content libraries, see
:ref:`Content Libraries`.

For details about using content library components in a course, see these
topics:

* :ref:`Use Components from Libraries in a Course`
* :ref:`Add a Randomized Content Block to Your Course`
* :ref:`View the Matching Components in a Randomized Content Block`
* :ref:`Edit Components in Randomized Content Blocks`
* :ref:`Get the Latest Version of Library Content`


.. _Use Components from Libraries in a Course:

*****************************************
Use Components from Libraries in a Course
*****************************************

To create randomized assignments that make use of components from content
libraries, you must have at least **User** level access to the libraries that
you want to use. If you do not have access to a library, members of your course
team who have **Admin** access to that library can grant you access.

The libraries that you create or have access to are listed on the **Libraries**
tab on the Studio Home page. For details about content libraries, see
:ref:`Content Libraries`.

Using components from content libraries in your course involves two steps.

#. :ref:`Enable Content Libraries`
#. :ref:`Add a Randomized Content Block to Your Course`
   
.. note:: After adding a randomized content block to your course, be aware that
   if components in the source library or libraries change, you must manually
   update the components in the course outline if you want to keep the components
   synchronized with the version in the library.

For details about working with randomized content blocks in your course, see
these topics.

* :ref:`View the Matching Components in a Randomized Content Block`
* :ref:`Edit Components in Randomized Content Blocks`
* :ref:`Get the Latest Version of Library Content`


.. _Enable Content Libraries:

========================
Enable Content Libraries
========================

You must enable content libraries before you can use randomized components from
:ref:`content libraries<Content Libraries>` in your courses.

#. In Studio, open the course in which you want to provide library content.

#. Select **Settings**, then **Advanced Settings**.

#. In the **Advanced Module List** field, place your cursor between the
   supplied pair of square brackets.

#. Type ``"library_content"``. 

#. Click **Save Changes**. 
   
   Studio reformats the policy key you just entered to indent it on a new line.

  .. image:: ../../../shared/building_and_running_chapters/Images/ContentLibraries_AdvancedSetting.png
     :alt: Advanced Module policy key "library_content"


.. _Add a Randomized Content Block to Your Course:

=============================================
Add a Randomized Content Block to Your Course   
=============================================

After you :ref:`enable content libraries<Enable Content Libraries>` you can add
library content to your courses using the Randomized Content Block advanced
component.

.. note:: Before starting these steps, obtain the Library ID for each library
   that you intend to reference in the randomized content block. The Library ID
   is found in the sidebar of each library's page. For details, see :ref:`Create
   a New Library`.

#. In Studio, open the course in which you want to add randomized problems from
   one or more content libraries.

#. Click **Content** then click **Outline**.

#. In the unit where you want to add a set of randomized problems, click **Add
   New Component** 

#. Click **Advanced**, then click **Randomized Content Block**.
   The randomized content block is added to your unit.

#. Click the **Edit** icon.
   
#. In the randomized content block settings, specify the details of the content
   you want to add in this block.

  - For **Count**, enter the number of problems to display to each student.

  - For **Display Name**, enter the name that you want students to see for this
    block.

  - For **Libraries**, enter the unique Library ID found in the sidebar of
    the Library page in Studio. To select problems from more than one content
    library, click **Add** to enter each additional Library ID.

  - For **Problem Type**, from the drop down list select a specific type of
    problem to be drawn from the library or libraries. Select **Any Type**
    if you do not want to select a particular type of problem.

    .. image:: ../../../shared/building_and_running_chapters/Images/ContentLibraries_SelectProblemType.png
     :alt: The Edit icon to the right of the Library Name    

  - For **Scored**, from the drop down list select **True** or **False** to
    indicate whether the assignment should be graded. 

.. note:: Grading is subject to the setting of this unit's subsection or
   section. If the subsection or section is not graded, selecting **True** here has
   no impact. Selecting **False** means that this assignment is not graded even if
   the subsection or section is graded.

7. Click **Save** when you have finished specifying the details of your
   randomized content block.

To view the list of components in the source library that match your filter
settings, see :ref:`View the Matching Components in a Randomized Content Block`.

To view the entire contents of the library in Studio, see :ref:`View the
Contents of a Library`.
   

.. _View the Matching Components in a Randomized Content Block:

***********************************************************
View the Matching Components in a Randomized Content Block
***********************************************************

In a unit that uses a randomized content block, you can view the list of all
components that match the filters specified in that block.

For example, if you have specified in the randomized content block that you want
to provide each student with 3 multiple choice problems, you see all the
multiple choice problems that exist in the referenced library or libraries. In
other words, you see every problem in the library that could potentially be
provided to a student.

#. In Studio, navigate to the unit containing the randomized content block that
   references your library.
#. In the randomized content block, click the **View** icon.
   
   .. image:: ../../../shared/building_and_running_chapters/Images/ContentLibraries_ViewMatching.png
      :alt: The View button for a randomized content block

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

To view the number and type of components from a randomized content block as a
student would see them, follow the steps described in the :ref:`Preview a Unit`
topic.

To view the list of matching components in the library, see :ref:`View the
Matching Components in a Randomized Content Block`.

To view the entire contents of the library in Studio, see :ref:`View the
Contents of a Library`.


.. _Edit Components in Randomized Content Blocks:

******************************************************
Editing Components in Randomized Content Blocks
******************************************************

In Studio, in the course unit that uses a randomized content block, you can edit
each component within the randomized content block in the same way as you do for
any other component in your course.

.. note:: Be aware that if you make changes on a component's **Editor** tab, if
   you update the randomized content block with the latest version of components
   from a library, these changes are overwritten. Only changes to a component's
   **Settings** tab are retained when you update the component. For details
   about getting the latest versions of library content in a randomized content
   block, see :ref:`Get the Latest Version of Library Content`.


The settings of a component that is supplied in a randomized content block are
initially inherited from the component in the content library that it is drawn
from. In the randomized content block, you can modify component settings so that
they are different from the "source" component in the library.

You can also reset a component's settings to the library default. If a
component's settings have been changed from the default settings in the library,
a **Clear** icon is shown next to the setting field.

 .. image:: ../../../shared/building_and_running_chapters/Images/ContentLibraries_ResetComponentField.png
    :alt: Clear button in the course component field reverts value to library value.

Click the **Clear** icon to restore the library default setting for that field.



.. _Get the Latest Version of Library Content:

*********************************************
Getting the Latest Version of Library Content
*********************************************

If you modify the contents of a library that is referenced by randomized content
blocks in one or more courses, those courses do not automatically use the
updated content. You can bring the randomized content blocks up to date with the
version in the library.

.. warning:: Be careful when you modify problems after they have been released!
   Changes that you make to published problems can affect the student experience
   in the course, as well as analysis of course data.

.. note:: Be aware that although you can retain changes to the settings of
   components in a randomized content block, changes to the **Editor** tab in
   components are overwritten if you update the component to the latest library
   version. If you do not want to bring components in the randomized content
   block up to date with the latest version in the library, you do not need to
   take any action.

* If the components in the randomized content block have not been edited in the
  course outline, when you next open the randomized content block in the course
  outline, you see a message indicating that the component is out of date in
  comparison with the library.

  .. image:: ../../../shared/building_and_running_chapters/Images/ContentLibraries_ComponentUpdateNow.png
     :alt: Error message shown when the source library has changed, with the
      Update Now link circled.

  To update your randomized content block components to the latest versions in the content library, click **Update now**.

  The randomized content block is brought up to date with the latest contents of
  the library or libraries that it references.

* If you edited only the settings of components in the randomized content block
  in your course so that they are different from the original version in the
  library, you do not lose your changes if you click **Update now**. In this case,
  the changes that were made in the randomized content block in the course outline
  are kept, but a **Clear** button becomes available next to the changed field in
  the component. However, any changes you made to the **Editor** tab of components
  in a randomized content block will be lost if you click **Update now** to get
  the latest library version.

  .. image:: ../../../shared/building_and_running_chapters/Images/ContentLibraries_ResetComponentField.png
     :alt: Clear icon in the course component field reverts value to library value.

  
  To clear any edits made in the course outline and bring your edited components
  up to date with the version in the library, click **Clear**.

  The value in that component field is reset to the current value in the library.


