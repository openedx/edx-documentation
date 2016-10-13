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

*******************************
Working with the Default Pages
*******************************

By default, the system adds these pages to every new course.

* Home
* Course
* Discussion
* Wiki
* Progress

In the LMS, learners see these options in the navigation bar at the top of
every page.

.. image:: ../../../shared/images/page_bar_lms_orig.png
 :width: 600
 :alt: The navigation bar in the LMS with all of the default pages.

In addition, if you enable the :ref:`notes tool <Notes Tool>` for your course,
the system adds a **Notes** page. The system also adds a page for each
:ref:`textbook <Adding Textbooks>` that you add to the course. Note that in
Studio, all of your textbooks appear in one group, but in the LMS each one
appears as a separate page.

To customize your course, you can make the following changes to pages that the
system adds by default.

* You can :ref:`change the order<Reorder Pages>` in which the pages are
  presented. The exceptions are the **Home** and **Course** pages, which are
  always presented in the first and second positions.

* If you do not want to use the **Wiki** or **Progress** page in your course,
  you can :ref:`hide<Show or Hide the Course Wiki Page>` one or both of them.

* If you want to change the name of a page that appears for a textbook, you
  can change the name that you entered for the textbook.

You can also add other pages.

.. _Add Page:

****************
Adding Pages
****************

Each page that you add appears in the navigation bar for your course. For
example, the navigation bar for a course that includes a textbook named
**Introduction to Music Theory** and pages for the **Course Schedule** and
**Supplements** appears as follows.

.. image:: ../../../shared/images/page_bar_lms.png
 :width: 800
 :alt: The navigation bar in the LMS with the default pages, a textbook page,
  and two additional pages.

You can add pages to your course for the course syllabus, FAQ, or any other
content. When you add a page, you also add its content using an HTML editor.

.. Commenting this sentence out until we can figure out what's wrong with the HTML... For example, you can add a dynamic HTML calendar, using the template in :ref:`Code for Dynamic HTML Schedule`.

==============
Add a Page
==============

To add a page, follow these steps.

#. In Studio, from the **Content** menu select **Pages**. The page that opens
   lists the pages that appear in the navigation bar for your course.

#. Select **Add a New Page**. The system adds a page named **Empty** to the
   end of the list.

#. In the row for the new page, select **Edit**. The :ref:`visual editor <The
   Visual Editor>` opens.

#. Enter the content for your page.

   To add HTML tags to your content, select **HTML** to open the :ref:`raw HTML
   editor<The Raw HTML Editor>`. For more information about entering content,
   see :ref:`Options for Editing HTML Components`.

   .. note::
    If you copy text from another source and paste it into the visual editor,
    be sure to proofread the result carefully. Some applications automatically
    change quotation marks and apostrophes from the "straight" version to the
    "smart" or "curly" version. The raw HTML editor requires "straight"
    quotation marks and apostrophes.

#. To rename the page, select **Settings**, and then enter a  **Display Name**.
   The display name is the navigation option that is visible to learners in the
   course.

#. Select **Save**.

The new page is immediately available to learners if the course has started.

.. _Show or Hide the Course Wiki Page:

********************************************
Hiding or Showing the Wiki or Progress Pages
********************************************

By default, your course includes a **Wiki** page and a **Progress** page. For
more information about how you can use these pages in a course, see
:ref:`Course_Wiki` or :ref:`A Students View`.

As part of your course design, you can decide whether you want learners to
have access to these pages. You can hide the pages, and if you change your
mind, you can show the pages again.

.. note:: The information on the **Progress** page can be motivating for
  learners, particularly in courses that include graded subsections, but also
  for courses that include only ungraded exercises. Before choosing to hide the
  **Progress** page for your course, consider the possible effect on learner
  engagement.

As a best practice, you should avoid changing the visibility of these pages
after your course starts. For example, your course includes the **Wiki** page
when it starts. A learner adds a page to the course wiki, and adds a browser
bookmark to that page. If you later hide the **Wiki** page, the learner's
bookmark will continue to provide access to the entire course wiki.

=======================================
Hide or Show the Wiki or Progress Pages
=======================================

To hide or show the **Wiki** or **Progress** pages, follow these steps.

#. In Studio, from the **Content** menu select **Pages**.

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
Reorder a Page
****************

You can reorder the pages in your course in the same way that you
:ref:`reorganize the course outline<Reorganize the Course Outline>`: you drag a
page to different location in the list of pages and drop it there.

.. note:: You cannot change the order of the **Home** or **Course** pages,
  which are always presented in the first and second positions.

To reorder a page, follow these steps.

#. In Studio, from the **Content** menu select **Pages**.

   On the list of pages, each page that you can move includes a **Drag to
   reorder** icon.

#. Move your pointer over the **Drag to reorder** icon for the page. Your
   pointer changes to a four-headed arrow.

#. Click and drag the page to the new location, and then release.

.. _Delete a Page:

****************
Delete a Page
****************

You can delete a page that a member of the course team previously added to
the course.

* You cannot delete any of the :ref:`default pages<Default Pages>`. However,
  you can :ref:`hide<Show or Hide the Course Wiki Page>` the **Wiki** and the
  **Progress** pages.

* To delete a page that appears for a textbook, you delete the textbook.

To delete a page, follow these steps.

#. In Studio, from the **Content** menu select **Pages**.

   On the list of pages, each page that you can delete includes a **Delete**
   icon.

#. Select the **Delete** icon, and then confirm the deletion.

.. _Code for Dynamic HTML Schedule:

********************************
Code for a Dynamic HTML Schedule
********************************

You can use the following code in a page to provide a dynamic HTML schedule in
your course.

.. note::
  To paste the following code into a page, use the :ref:`raw HTML editor <The
  Raw HTML Editor>`. Do not paste the code directly into the visual editor.

.. this example isn't functioning correctly. Something wrong with the table style settings - A. Hodges 13 Oct 16

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
