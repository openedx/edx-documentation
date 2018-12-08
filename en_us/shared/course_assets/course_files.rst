.. _Add Files to a Course:

###########################
Adding Files to a Course
###########################

To use images and other files in your course, you upload the files to your
course by using Studio, and then you add links to the files in the course
content. You can also use uploaded files in the bulk email messages that course
team members can send from the LMS by selecting **Instructor** to access the
instructor dashboard.

.. contents::
  :local:
  :depth: 1

.. _File Size:

*******************
File Size
*******************

The maximum size for an uploaded file is 50 MB.

We recommend that you use standard compression tools to reduce PDF and image
file sizes before you add the files to your course. If you have to use files
that are larger than 50 MB after compression, contact your edX partner manager.

If you have video or audio files or large data sets to share with your
students, use YouTube or another hosting service to host these files. Do not
use the Files & Uploads page to add these files to your course. If you are an
edX partner and you need to store large data sets, contact your edX partner
manager.

.. _Upload a File:

*******************
Upload a File
*******************

You upload files on the **Files & Uploads** page in Studio.

.. note::
 Ensure that you obtain copyright permissions for files and images you upload
 to your course, and that you cite sources appropriately.

To upload a file, follow these steps.

#. Create or locate the file on your computer.

   .. note::
    When URLs are generated for uploaded files, the file name becomes part of
    the URL and is visible to students when they access the file. Avoid using
    file names that contain information about the file contents that you do not
    want to share, such as "Answerkey.pdf".

#. From the **Content** menu, select **Files & Uploads**.

#. Select **Upload New File**.

#. Select **Choose File**, and then select the file or files that you want to
   upload.

   .. note::
      If you upload a file that has the same name as an existing course file,
      the original file is overwritten without warning.

#. To upload additional files, select **Load Another File** and repeat the
   previous step.

   When you are finished, select the **X** to close the window.

The **Files & Uploads** page refreshes to show the uploaded file.

.. _File URLs:

********************************************
Use File URLs to Reference Uploaded Files
********************************************

To use an uploaded file for your course, you add a reference to one of the URLs
that is assigned to it. On the **Files & Uploads** page, the **URL** column
lists a **Studio** URL and a **Web** URL for each file you upload.

* To add a file or image to a component, a course update, or a course handout,
  you use the **Studio** URL.

  For more information, see :ref:`Add an Image to an HTML Component`.

* To provide a link to the file or image from outside the course, including in
  the body of an email message that you send to course participants from the
  LMS, you use the **Web** URL. Be sure that you do not use the ``/static/``
  URL in an email message.

  For more information about sending email messages, see
  :ref:`Send_Bulk_Email`.

.. note::
  You can lock a file if you do not want to allow access to that file from
  outside your course. When you lock a file, the web URL only allows file
  access to learners who are signed in and enrolled in your course. For more
  information, see :ref:`Lock a File`.

To copy a URL from the file list, select the URL in the **URL** column and copy
it.

.. _Sort Files:

*********************
Sort Uploaded Files
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
Filter Listed Files
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

To filter the list of files by type, follow these steps.

#. On the **Files & Uploads** page, select the **Type** column header.

#. In the drop-down list, select the type of file that you want to view.

The list refreshes to show only the type of file you selected, and the column
header changes to reflect the type of file that you have filtered by.

To reset the list and view files of all types, select **Show All** in the
**Type** drop-down list.

.. _Find Files:

*******************
Find a File
*******************

The **Files & Uploads** page lists up to 50 files.  If your course has more
than 50 files, additional files are listed on other pages.

The range of the files listed on the page, and the total number of files, are
shown at the top of the page.

You can navigate through the pages in these ways.

* Select the **<** or **>** control to navigate to the previous or next page.

* Specify the number of the page you want to view.

  .. image:: ../../../shared/images/file_pagination.png
   :width: 250
   :alt: Page navigation controls on the Files & Uploads page.

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

To delete a file, select the **X** in the row for file.  You are prompted to
confirm the deletion.

.. warning::
  After you delete a file, links to the file from course content will be
  broken. You must update links to files that you need to delete.
