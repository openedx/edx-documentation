.. _Adding Pages to a Course:

###########################
Adding Pages to a Course
###########################

This topic describes the pages, or tabs, that are included in your course by
default, how you can modify them, and how you can add more pages to your
course.

.. contents::
  :local:
  :depth: 2

.. _Default Pages:

*******************
Default Pages
*******************

By default, your course includes these pages.

* Home
* Course
* Discussion
* Wiki
* Progress

You can :ref:`change the order<Reorder Pages>` of the **Discussion**, **Wiki**,
and **Progress** pages, and you can :ref:`hide<Show or Hide the Course Wiki
Page>` the **Wiki** and **Progress** pages. You can also add more pages.

.. _Add Page:

****************
New Pages
****************

You can add pages to your course. Each page appears for learners in the
navigation bar for your course.

For example, the following navigation bar includes the default pages as well as
the additional **Introduction to Music Theory**, **Course Schedule**, and
**Supplements** pages.

.. image:: ../../../shared/images/page_bar_lms.png
 :width: 600
 :alt: Image of the navigation bar in the LMS.

You can create other pages for the grading policy, course slides, or any other
purpose. For example, you can add a dynamic HTML calendar, using the template
in :ref:`Code for Dynamic HTML Schedule`.


==============
Add a Page
==============

To add a page, follow these steps.

#. In Studio, from the **Content** menu, select **Pages**. A page titled
   **Pages** opens. This page contains a list of the pages that appear in the
   navigation bar in your course.

#. Select **Add a New Page**. A page with the title **Empty** is added to the
   list.

#. In the row for the new page, select **Edit**. The HTML editor opens.

#. Enter content for your page.

   For more information about using the editor, see :ref:`Options for Editing
   HTML Components`.

   .. note::
    If you copy text from another source and paste it into the HTML editor, be
    sure to proofread the result carefully. Some applications automatically
    change quotation marks and apostrophes from the "straight" version to the
    "smart" or "curly" version. The HTML editor requires "straight" quotation
    marks and apostrophes.

#. Select **Settings** to edit the **Display Name**. The display name is the
   name of the page visible to learners in the course.

#. Select **Save**.

The new page is immediately available to learners if the course has started.

.. _Show or Hide the Course Wiki Page:

********************************************
Hiding or Showing the Wiki or Progress Page
********************************************

By default, your course includes a **Wiki** page and a **Progress** page. For
more information about how you can use these pages in a course, see
:ref:`Course_Wiki` or :ref:`A Students View`.

As part of your course design, you can decide whether you want to learners to
have access to these pages. You can hide the pages, and if you change your
mind, you can show the pages again.

.. note:: The information on the **Progress** page can be motivating for
  learners, particularly in courses that include graded subsections, but also
  for courses that include only ungraded exercises. Before choosing to hide the
  **Progress** page for your course, consider the possible effect on learner
  engagement.

As a best practice, you should avoid changing the visibility of these pages
after your course starts. For example, your course includes the **Wiki** page
when it starts. A learner adds a page to the course wiki, and bookmarks the new
page. If you then hide the **Wiki** page, the learner's bookmark will continue
to provide access to the course wiki.

=======================================
Hide or Show the Wiki or Progress Pages
=======================================

To hide or show the **Wiki** or **Progress** pages, follow these steps.

#. Select **Content**, and then **Pages**.

   On the list of pages, each page that you can hide includes a **Show/hide
   page** icon.

   .. image:: ../../../shared/images/pages_wiki_on.png
    :alt: The list of default course pages, with a show/hide icon for the Wiki
      and Progress pages only.

   .. note:: The options to show or hide a page are available only for the
     **Wiki** and **Progress** pages.

#. Select the **Show/hide page** icon to hide a page. The appearance of the
   icon changes to indicate that the page is now hidden, as shown in this
   example.

   .. image:: ../../../shared/images/pages_wiki_off.png
    :alt: The default wiki page on the list of course pages, with the show/hide
     icon indicating that the page is currently hidden.

#. Select the **Show/hide page** icon again to make the page visible.

.. _Reorder Pages:

****************
Reorder Pages
****************

To reorder the pages in your course you can drag a page to different location
in the list of pages and drop it there.

To move a page, move your pointer over the **Drag to reorder** icon for the
page. Your pointer changes to a four-headed arrow. Then select and drag the
page to the location that you want.

.. note:: You cannot change the order of the **Home** or **Course** pages.

.. _Delete a Page:

****************
Delete a Page
****************

You can only delete a page that the course team added to the course. To delete
a page, select the **Delete** icon for the page. You are prompted to confirm
the deletion.

.. note::
  You cannot delete any of the :ref:`default pages<Default Pages>`. However,
  you can :ref:`hide<Show or Hide the Course Wiki Page>` the **Wiki** and the
  **Progress** pages.

.. _Code for Dynamic HTML Schedule:

********************************
Code for a Dynamic HTML Schedule
********************************

You can use the following code in a page to provide a dynamic HTML schedule in
your course.

.. note::
  To paste the following code into a page, use the :ref:`raw HTML editor <The
  Raw HTML Editor>`. Do not paste the code directly into the visual editor.

.. code-block:: html

	<div class= "syllabus">

	<table style="width: 100%">
 		<col width="10%">
 		<col width="15%">
  		<col width="10%">
  		<col width="30%">
  		<col width="10%">
  		<col width="15%">
  		<col width="10%">

	<!-- Headings -->
 		 <thead>
    			<td class="day"> Wk of </td>
   			<td class="topic"> Topic </td>
   			<td class="reading"> Read </td>
    			<td class="video"> Lecture Sequence </td>
    			<td class="slides"> Slides </td>
    			<td class="assignment"> HW/Q </td>
			<td class="due"> Due </td>
  		</thead>

	<!-- Week 1 Row 1 -->
 		 <tr class="first">
   			<td class="day">10/22</td>
			<td class="topic">Topic 1</td>
			<td class="reading">Ch. 1</td>
    			<td class="video"><a href="#">L1: Title</a></td>
    			<td class="slides"><a href="#">L1</a></td>
    			<td class="assignment"><a href="#">HW 1</a></td>
    			<td class="due">11/04</td>
  		</tr>

	<!-- Week 1 Row 2 -->
    		<tr>
    			<td class="day"> </td>
    			<td class="topic"></td>
    			<td class="reading"></td>
    			<td class="video"><a href="#">L2: Title</a></td>
    			<td class="slides"><a href="#">L2</a></td>
    			<td class="assignment">     </td>
   			 <td class="due">      </td>
  		</tr>

   		 <tr> <td class="week_separator" colspan=7> <hr/> </td> </tr>

	<!-- Week 2 Row 1 -->
 		 <tr>
    			<td class="day">10/29</td>
    			<td class="topic">Topic 2</td>
    			<td class="reading">Ch. 2</td>
    			<td class="video"> <a href="#">L3: Title<a></td>
   			 <td class="slides"><a href="#">L3</a></td>
    			<td class="assignment"><a href="#">Quiz 1</a></td>
    			<td class="due">11/11</td>
 		 </tr>

	<!-- Week 2 Row 2 -->
 		<tr>
  			<td class="day"></td>
    			<td class="topic"></td>
    			<td class="reading"></td>
    			<td class="video"><a href="#">L4: Title</a></td>
    			<td class="slides"><a href="#">L4</a> </td>
    			<td class="assignment"></td>
    			<td class="due"></td>
  		</tr>
  		<tr> <td class="week_separator" colspan=7> <hr/> </td> </tr>

	<!-- Week 3 Row 1 -->
  		<tr>
    			<td class="day">11/05</td>
    			<td class="topic">Topic 3</td>
    			<td class="reading">Ch. 3</td>
    			<td class="video"><a href="#">L5: Title</a></td>
    			<td class="slides"><a href="#">L5 </a></td>
    			<td class="assignment"><a href="#">HW 2</a></td>
    			<td class="due">11/18 </td>
  		</tr>

	<!-- Week 3 Row 2 -->
		<tr>
    			<td class="day"> </td>
    			<td class="topic"> </td>
    			<td class="reading"></td>
    			<td class="video"><a href="#">L6: Title</a></td>
    			<td class="slides"><a href="#">L6 </a></td>
    			<td class="video"></td>
    			<td class="assignment"></td>
    			<td class="due"></td>
  		</tr>
  		<tr> <td class="week_separator" colspan=7> <hr/> </td> </tr>

	<!-- Week 4 Row 1 -->
  		<tr>
    			<td class="day">11/12</td>
    			<td class="topic">Topic 4</td>
    			<td class="reading">Ch. 4</td>
    			<td class="video"><!--<a href="#">L7: Title</a>--> L7: Title</td>
    			<td class="slides"><!--<a href="#">L7</a>-->L7</td>
    			<td class="assignment"><!--<a href="#">Quiz 2</a>-->Quiz 2</td>
    			<td class="due"> 11/25 </td>
  		</tr>

	<!-- Week 4 Row 2 -->
    		<tr>
    			<td class="day"></td>
    			<td class="topic"></td>
    			<td class="reading"></td>
    			<td class="video"><!--<a href="#">L8: Title</a>-->L8: Title</td>
    			<td class="slides"><!--<a href="#">L8</a>-->L8</td>
    			<td class="assignment"></td>
    			<td class="due"></td>
  		</tr>
  		<tr> <td class="week_separator" colspan=7> <hr/> </td> </tr>

	<!-- Week 5 Row 1 -->
  		<tr>
    			<td class="day">11/19</td>
    			<td class="topic">Topic 5</td>
    			<td class="reading">Ch. 5</td>
    			<td class="video"><!--<a href="#">L9: Title</a>-->L9: Title</td>
    			<td class="slides"><!--<a href="#">L9</a>-->L9</td>
    <			td class="assignment"><!--<a href="#">HW 3</a>-->HW 3</td>
    			<td class="due"> 12/02 </td>
  		</tr>

	<!-- Week 5 Row 2 -->
   		<tr>
    			<td class="day"></td>
    			<td class="topic"></td>
    			<td class="reading"></td>
    			<td class="video"><!--<a href="#">L10: Title</a>-->L10: Title</td>
    			<td class="slides"><!--<a href="#">L10</a>-->L10 </td>
    			<td class="assignment"></td>
    			<td class="due"></td>
  		</tr>
  		<tr> <td class="week_separator" colspan=7> <hr/> </td> </tr>

	<!-- Week 6 Row 1 -->
  		<tr>
    			<td class="day">11/26</td>
    			<td class="topic">Topic 6</td>
    			<td class="reading">Ch. 6</td>
    			<td class="video"><!--<a href="#"><L11: Title</a>-->L11: Title </td>
    			<td class="slides"><!--<a href="#">L11</a>-->L11</td>
    			<td class="assignment"><!--<a href="#">HW 4</a>-->HW 4</td>
    			<td class="due">12/09</td>
  		</tr>

	<!-- Week 6 Row 2 -->
    		<tr>
			<td class="day"> </td>
    			<td class="topic"> </td>
    			<td class="reading"></td>
    			<td class="video"><!--<a href="#">L12: Title</a>-->L12: Title</td>
    			<td class="slides"><!--<a href="#">L12</a>-->L12</td>
    			<td class="assignment"></td>
    			<td class="due">      </td>
		</tr>
	</table>
	</div>
