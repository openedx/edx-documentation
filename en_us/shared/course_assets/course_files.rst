.. _Add Files to a Course:

###########################
Adding Files to a Course
###########################

To use images and other files in your course, you upload the files to your
course by using Studio, and then you add links to the files in the course
content. You can also use uploaded files in bulk email messages sent from the
Instructor Dashboard.

* :ref:`File Size`
* :ref:`Upload a File`
* :ref:`File URLs`
* :ref:`Sort Files`
* :ref:`Filter Files`
* :ref:`Find Files`
* :ref:`Lock a File`
* :ref:`Delete a File`

.. _File Size:

*******************
File Size
*******************

The maximum size for an uploaded file is 50 MB.

We recommend that you use standard compression tools to reduce PDF and image
file sizes before you add the files to your course. If you have to use files
that are larger than 50 MB after compression, contact your edX Partner Manager.

If you have video or audio files or large data sets to share with your
students, use YouTube or another hosting service to host these files. Do not
use the Files & Uploads page to add these files to your course. If you are an
edX partner and you need to store large data sets, contact your edX program
manager.


.. _Upload a File:

*******************
Upload a File
*******************
 
You upload the files in Studio on the **Files & Uploads** page.

.. note:: 
 Ensure that you obtain copyright permissions for files and images you upload
 to your course, and that you cite sources appropriately.

To upload files:
 
#. Create or locate the file on your computer.
   
   .. note:: 
    When URLs are generated for uploaded files, the file name becomes part of
    the URL and is visible to students when they access the file. Avoid using
    file names that contain information about the file contents that should not
    be shared, such as ``Answerkey.pdf``.

#. From the **Content** menu, select **Files & Uploads**.

#. Select **Upload New File**.

#. In the **Upload New File** dialog box, select **Choose File**.
   
#. In the **Open** dialog box, select one or more files to upload, then select
   **Open**.

   .. note::
      If you upload a file that has the same name as an existing course file,
      the original file is overwritten without warning.

#. To upload additional files, select **Load Another File** and repeat the
   previous step.

#. To close the dialog box, select the **X** in the top right corner.

The **Files & Uploads** page refreshes to show the uploaded file.

.. _File URLs:

********************************************
Use File URLs to Reference Uploaded Files
********************************************

After you upload a file, you can use the URLs listed for it. On the **Files &
Uploads** page, the **URL** column lists a Studio URL and web URL for each
file.

Use the web URL if you want to perform either of the following actions.
Add a file or image to a bulk email message...
Provide a link to the file or image from outside the course.

* You use the **Studio URL** to add a file or image to a component, a course
  update, or course handouts. For more information, see :ref:`Add an Image to
  an HTML Component`. You cannot use the web URL to link to a file or image
  from within your course.

* Use the **Web URL** to:
  
  * Add a file or image to a bulk email message in the LMS. For more
    information, see :ref:`Send_Bulk_Email`.

  * To provide a link to the file or image from outside the course.

.. note:: 
  You can lock a file if you do not want anyone outside your course to view the
  file. When you lock a file, the web URL only allows file access to learners
  who are signed in to edX and enrolled in the course. For more information,
  see :ref:`Lock a File`.

To copy a URL from the file list, select the URL in the **URL** column
and copy it.

.. _Sort Files:

*********************
Sort Files
*********************

On the **Files & Uploads** page, you can sort your files by any column that has
a blue column header. For example, to sort the list by name, select the
**Name** column header.

Change the sort order by selecting a sortable column header. The direction of
the arrow in the column header indicates whether the order is ascending or
descending. Each time you select the column header, the sort order reverses.

The current sort order is shown at the top of the file list, and the active
sort column header is underlined.

.. _Filter Files:

*********************
Filter Files
*********************

You can filter the list of files by type so that only a selected type of file
is visible. The list remains in the current sort order.

.. list-table::
   :widths: 10 20

   * - **Type**
     - **File Types Include**
   * - Images
     - .gif, .ico, .jpg, .jpeg, .png, .tif, or .tiff
   * - Documents 
     - .pdf, .txt, Microsoft Office and Open Office documents, presentations,
       or spreadsheets
   * - Other
     - Files not included in the other types, such as .html, .js, or .sjson

To filter the list of files by type:
 
#. On the **Files & Uploads** page, select the **Type** column header.

#. In the drop-down list, select the type of file that you want to view. 

The list refreshes to show only the type of file you selected, and the column
header changes to reflect the type of file that you have filtered by.

To reset the list and view files of all types, select **Show All** in the
**Type** drop-down list.

.. _Find Files:

*******************
Find Files
*******************

The **Files & Uploads** page lists up to 50 files.  If your course has more
than 50 files, additional files are listed on other pages.

The range of the files listed on the page, and the total number of files, are
shown at the top of the page.

You can navigate through the pages in these ways.

* Select the **<** and **>** buttons at the top and bottom of the list to
  navigate to the previous and next pages.

* At the bottom of the page, you can edit the first number in the page range.
  Select the number to place your cursor in the field, then enter the page
  number you want to jump to.

  .. image:: ../../../shared/building_and_running_chapters/Images/file_pagination.png
   :width: 250
   :alt: Image showing page navigation on the Files & Uploads page.

.. _Lock a File:
 
*******************
Lock a File
*******************

By default, anyone can access a file you upload if they know the web URL, even
if they are not enrolled in your course. You can prevent outside access to a
file by locking the file. When you lock a file, the web URL only allows
learners who are enrolled in your course and signed in to edX to access the
file.

To lock a file, select the lock icon in the right column. 

.. _Delete a File:

*******************
Delete a File
*******************

To delete a file, select the **x** icon in the row for file.  You are prompted
to confirm the deletion.

.. warning:: 
  After you delete a file, links to the file from course content will be
  broken. You must update links to files that you need to delete.
 