.. _Add Files to a Course:

###########################
Adding Files to a Course
###########################

To use images in your course content, or to use other documents such as a
syllabus, you must upload the files to the **Files and Uploads** page, then link
to the uploaded files from a component in your course.

*******************
Overview
*******************

You can manage your uploaded course files on the **Files and Uploads** page
under the **Content** menu in Studio.

* :ref:`Upload a File`
* :ref:`File URLs`
* :ref:`Sort Files`
* :ref:`Filter Files`
* :ref:`Find Files`
* :ref:`Lock a File`
* :ref:`Delete a File`


.. _Upload a File:

*******************
Upload a File
*******************
 
You can upload files that you want students to access in the course. After you
upload a file, you can link to it from a component, from a course update, or in
the course handouts, using the generated URLs on the **Files and Uploads** page.
Students can see a file only if you create a link to it.

.. note:: When URLs are generated for uploaded files, the file name becomes part
   of the URL and is visible to students when they access the file. You should
   avoid using file names that contain information about the file contents that
   should not be shared, for example, Answerkey.pdf.

.. warning::
   For PDF and image files, edX recommends that you use standard compression
   tools to reduce the file size before you add them to your course.

   If you have files that are larger than 50 MB after compression and need them
   for your course, contact your edX program manager.

   Furthermore, do not add video or audio files, or large data sets that are to
   be used by students. You should use YouTube or another hosting service to
   host multimedia files for your course. For information about storing large
   data sets for student use, contact your edX program manager.

To upload files:
 
#. From the **Content** menu, select **Files & Uploads**.
#. Click **Upload New File**.
#. In the **Upload New File** dialog box, click **Choose File**.
   
#. In the **Open** dialog box, select one or more files to upload, then click
   **Open**.

   .. note::
      If you upload a file that has the same name as an existing course file, the
      original file is overwritten without warning.

5. To upload additional files, click **Load Another File** and repeat the
   previous step.

6. To close the dialog box, click the **X** in the top right corner.

You see the new files on the **Files & Uploads** page.


.. _File URLs:

********************************************
Use File URLs to Reference Uploaded Files
********************************************


After you upload a file, you can link to it from a component, from a course
update, or in the course handouts, using the generated URLs on the **Files and
Uploads** page. On the **Files & Uploads** page, the **URL** column lists the
Studio URL and web URL for each file.

* To link to the file or image from within a course (that is, from a component,
  a course update, or a course handout), use the Studio URL. You cannot use
  the web URL to link to a file or image from within your course.

* To provide a link to the file or image from outside the course, use the
  web URL. 


.. note:: If you lock a file, the web URL no longer works for external access
   to the file, unless the person accessing the URL is enrolled in and logged in to
   the course.

To copy a URL from the file list, double click the URL in the **URL** column so
that the value is selected, then copy it.


.. _Sort Files:

*********************
Sort Files
*********************

On the **Files & Uploads** page, by default, files are sorted by the **Date
Added** column, with the most recently added files at the top.

You can sort your files by any column that has a blue column header. For
example, to sort the list by name, click the **Name** column header.

Change the sort order by clicking a sortable column header. The direction of the
arrow in the column header indicates whether the order is ascending or
descending. Each time you click the column header, the sort order reverses.

The current sort order is shown at the top of the file list, and the active sort
column header is underlined.


.. _Filter Files:

*********************
Filter Files
*********************

You can filter the list of files by type so that only a selected type of file is
visible. The list remains in the current sort order.


.. list-table::
   :widths: 10 20

   * - **Type**
     - **File Types Include**
   * - Images
     - .gif, .ico, .jpg, .jpeg, .png, .tif, or .tiff
   * - Documents 
     - .pdf, .txt, Microsoft Office and Open Office documents, presentations, or
       spreadsheets
   * - Other
     - Files not included in the other types, such as .html, .js, or .sjson


To filter the list of files by type:
 
#. On the **Files & Uploads** page, click the **Type** column header.

#. In the dropdown list, select the type of file that you want to view. 

The list refreshes to show only the type of file you selected, and the column
header changes to reflect the type of file that you have filtered by.

To reset the list and view files of all types, click **Show All** in the **Type**
dropdown list.


.. _Find Files:

*******************
Find Files
*******************

The **Files & Uploads** page lists up to 50 files.  If your course has more than
50 files, additional files are listed on other pages.

The range of the files listed on the page, and the total number of files, are
shown at the top of the page.

You can navigate through the pages in these ways:

* Use the **<** and **>** buttons at the top and bottom of the list to navigate
  to the previous and next pages.

* At the bottom of the page, you can edit the first number in the page range.
  Click the number to place your cursor in the field, then enter the page number
  you want to jump to.

  .. image:: ../../../shared/building_and_running_chapters/Images/file_pagination.png
   :alt: Image showing the pair of page numbers at the bottom of the Files and
         Uploads pages with the first number in editable mode and circled


.. _Lock a File:
 
*******************
Lock a File
*******************

By default, anyone can access a file you upload if they know the URL, even
people not enrolled in your class.

To ensure that those not in your class cannot view the file, click the lock
icon.

.. note:: If you lock a file, the web URL no longer works for external access
   to the file, unless the person accessing the URL is enrolled in and logged in to
   the course.
 

.. _Delete a File:

*******************
Delete a File
*******************

To delete a file, click the **x** icon next to the file.  You are prompted to
confirm the deletion.

.. warning:: If you delete a file that has been linked from a course component,
   those links will be broken. Before deleting files that are used in a course,
   make sure you update the links to those files in the course.
 