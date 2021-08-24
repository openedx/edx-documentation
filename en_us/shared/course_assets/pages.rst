.. _Adding Pages to a Course:

##################################
Managing the Pages in Your Course
##################################

This topic describes the applications and resources that your course experience
has enabled outside of the core content experience and how you can modify these
tools to fit your course needs.


.. contents::
  :local:
  :depth: 2

.. _Default Pages:

*******************************
Working with the Default Pages
*******************************

By default, every new course has the following key areas enabled:

* Course
* Progress
* Date
* Discussion


In the learner experience, these will be shown in the primary navigation bar at the top of every page,
consistently in this order for all courses.

.. image:: ../../../shared/images/page_bar_lms_orig.png
 :alt: The navigation bar in the LMS, showing the default pages.

As a course team member with the **Staff** or **Admin** role, you also see the Instructor
option in the navigation bar, shown at the end of the list of pages.
Learners do not see the Instructor option.

The progress page can be disabled and thus hidden from the learner experience,
though this is not commonly done and is not recommended. The information on
the Progress page is critical for motivating learners, particularly in courses
that include graded subsections, but also for courses that include only ungraded
exercises. Before choosing to hide the Progress page for your course, consider
the possible effect on learner engagement.

.. _Add Page:

***************************
Enabling Additional Applications & Resources
***************************

Additional applications and resources can be enabled depending on your course needs, including:

* Notes
* Teams
* Wiki
* Calculator
* Textbooks
* Custom Pages

===================
Add a Custom Page
===================

If you add a custom page to a course after its start date, and have specified
that the page should be visible to learners, the page is visible in the LMS as
soon as you save your work. As a best practice, be sure the following aspects
of your page design are ready before you add a page in Studio.

*  The content for the page, which can include HTML markup.
*  The name of the page.
*  The audience for the page (everyone, or course team members with the Admin
   or Staff roles only).

To add a custom page and its content to your course, follow these steps.

#. In Studio, from the **Content** menu select **Pages**. A list of the pages
   that appear in the navigation bar for your course appears.

#. Select **Add a New Page**. The system adds a page named **Empty** to the end
   of the list.

#. In the row for the new page, select **Edit**. The :ref:`visual editor <The
   Visual Editor>` opens.

#. Enter the content for your page.

   To add HTML tags to your content, select **HTML** to open the :ref:`raw HTML
   editor<The Raw HTML Editor>`. For more information about entering content,
   see :ref:`Options for Editing HTML Components`.

   .. note:: If you copy text from another source and paste it into the visual
    editor, be sure to proofread the result carefully. Some applications
    automatically change quotation marks and apostrophes from the "straight"
    version to the "smart" or "curly" version. The raw HTML editor requires
    "straight" quotation marks and apostrophes.

#. To rename the page, select **Settings**, and then enter a **Display Name**.
   The display name is the label that course participants use in the course
   navigation bar.

#. To hide the page from learners, select **Settings**, and then select
   ``true`` for **Hide Page from Learners**. By default, pages are visible to
   learners.

#. Select **Save**.

The new page is immediately available to the specified audience if the course
has started.

.. _Show or Hide the Course Wiki Page:

********************************************
Hiding or Showing the Wiki or Progress Pages
********************************************

By default, your course includes a **Wiki** page and a **Progress** page. For
more information about how you can use these pages in a course, see
:ref:`Course_Wiki` or :ref:`check_student_progress`.

As part of your course design, you can decide whether you want learners to have
access to one or both of these pages. While you cannot delete these pages
completely, you can hide them so that they do not appear in the navigation bar
in the LMS. If you change your mind, you can show the pages again.

.. note:: The information on the **Progress** page can be motivating for
  learners, particularly in courses that include graded subsections, but also
  for courses that include only ungraded exercises. Before choosing to hide the
  **Progress** page for your course, consider the possible effect on learner
  engagement.

As a best practice, you should avoid changing the visibility of these pages
after your course starts. For example, your course includes the **Wiki** page
when it starts. A learner adds a page to the course wiki, and adds a browser
bookmark to that page. If you later hide the **Wiki** page, the learner's
browser bookmark will continue to provide access to the entire course wiki.

=======================================
Hide or Show the Wiki or Progress Pages
=======================================

If you hide or show a page after the course start date, note that the
visibility of the page in the LMS changes immediately.

To hide or show the **Wiki** or **Progress** pages, follow these steps.

#. In Studio, from the **Content** menu select **Pages**.

   On the list of pages, each page that you can hide includes a **Show/hide
   page** icon.

   .. image:: ../../../shared/images/pages_wiki_on.png
    :alt: The list of default course pages. Only the Wiki and Progress pages
        have Show/Hide controls.

#. Select the **Show/hide page** icon to hide a page. The icon changes to
   indicate that the page is hidden, as shown in this example.

   .. image:: ../../../shared/images/pages_wiki_off.png
    :alt: The Wiki page on the list of course pages, with the show/hide
        icon indicating that the page is currently hidden.

#. Select the **Show/hide page** icon again to make the page visible.

.. _Reorder Pages:

*****************
Reorder the Pages
*****************

You can reorder the pages in your course in the same way that you
:ref:`reorganize the course outline<Reorganize the Course Outline>`: you drag a
page to different location in the list of pages and drop it there.

.. note:: You cannot change the order of the **Home** or **Course** pages,
  which are always presented in the first and second positions.

If you change the order of the pages after the course start date, note that the
change immediately affects the sequence of the options on the navigation bar in
the LMS.

To reorder the pages, follow these steps.

#. In Studio, from the **Content** menu select **Pages**.

   On the list of pages, each page that you can move includes a **Drag to
   reorder** icon.

#. Move your pointer over the **Drag to reorder** icon for the page. Your
   pointer changes to a four-headed arrow.

#. Click and drag the page to the new location, and then release.

.. _Delete a Page:

*********************
Delete a Custom Page
*********************

You can delete any of the custom pages that were previously added to the
course.

* You cannot delete any of the :ref:`default pages<Default Pages>`. However,
  you can :ref:`hide<Show or Hide the Course Wiki Page>` the **Wiki** and the
  **Progress** pages.

* To delete a page that appears for a textbook, you delete the textbook.

If you delete a page after the course start date, note that the
visibility of the page in the LMS changes immediately.

To delete a custom page, follow these steps.

#. In Studio, from the **Content** menu select **Pages**.

   On the list of pages, each page that you can delete includes a **Delete**
   icon.

#. Select the **Delete** icon, and then confirm the deletion.
