.. _Add Files to a Course:

###########################
Adding Files to a Course
###########################

Adding files, such as images, that you can use in your course has the following
steps.

#. The course team uploads a file on the **Files** page in Studio.
#. Studio generates two URLs for the file.

   * The Studio URL is used to add the file inside the course, such as in a
     component or on a page.

   * The web URL is used to add the file outside the course, such as in an
     email message or external web page.

#. The course team adds a link to the file inside or outside the course.
#. The file is visible in the course, email, or external web page.

For more information, see the following topics.

.. contents::
  :local:
  :depth: 1

.. _The Files Page:

*************************
The Files Page
*************************

You manage most files for your course, including image files, on the **Files** 
page. This page lists the files that you have added, along with the
following capabilities and information regarding the files:

.. image:: ../../../shared/images/FilesPageTableView.png
 :alt: an image of the Files page in Studio. Each page shows up to 50 files 
     and includes a Search box, sort and filter capabilities, an Add files 
     button, and checkboxes so that you can bulk delete or bulk download files.

* A checkbox for Download and Delete bulk actions
* A thumbnail of the file
* The file name
* The file size 
* The file type
* An indication of whether the file is :ref:`locked<Lock a File>`.
* The three dot menu allows you to copy the Studio URL, copy the web URL, 
  lock the file, click on the Info button, and delete a file
* The Info button within the three dot menu allows you to additionally see
  the date added and details about whether the file is within the course as
 well as the number of times it appears in your course.

.. image:: ../../../shared/images/FilesPageInfoPop.png
 :alt: When you first select the three dot menu, then select Info, this 
     Info modal appears. The Info modal provides details such as date added, 
     file size, Studio URL, Web URL, ability to lock a file, as well as usage 
     data within the course. 

This page also includes a **Search** option to help you find specific files.
For more information, see :ref:`Find Files`.
56
57   .. _File Size:


*******************
File Size
*******************

The maximum size for each file is 10 MB. We recommend that you use standard
compression tools to reduce PDF and image file sizes before you add the files
to your course.

You can upload multiple files at a time.

If you have very large audio files or large data sets to share with your
students, do not use the **Files** page to add these files to your course. 
Instead, use another hosting service to host these files.

.. _Upload a File:

*******************
Upload Files
*******************

.. note::
  Ensure that you obtain copyright permissions for files and images you upload
  to your course, and that you cite sources appropriately.

To upload one or more files, follow these steps.

#. Create or locate the files on your computer.

   .. note::
     When Studio generates URLs for an uploaded file, the file name becomes
     part of the URL and is visible to students when they access the file.
     Avoid using file names that contain information that you do not want to
     share about the file contents, such as "Answerkey.pdf".

#. On the **Content** menu, select **Files**.

#. On the **Files** page, select the Add Files button at the top of the page 
   and select the files that you want to add.

   .. note::
     If you upload a file that has the same name as an existing course file,
     the original file is overwritten without warning.

The **Files** page refreshes to show the uploaded file or files.

.. _Find Files:

*********************
Find an Uploaded File
*********************

The **Files** page lists up to 50 files at one time.  If your course has more 
than 50 files, additional files are listed on other pages.

To find a file on the **Files** page, you can use the **Search** option, or 
you can view the page that lists the file.

* To use the **Search** option, enter one of the following search terms in the
  **Search** field.

  * The full file name.
  * The file name extension, or file type.
  * Part of the file name. You can also enter multiple parts of a file name.

  For example, if the file is named FirstCourseImage.jpg, you can enter any
  of the following search terms in the **Search** field.

  * ``FirstCourseImage.jpg``
  * ``.jpg``
  * ``First`` ``Image``
  * ``First`` ``.jpg``

You can also sort files by Name (A-Z), Name (Z-A), Newest, Oldest, File size 
(low to high), or filter files by Type (Code, Images, Documents, Audio).
For more information, see :ref:`Sort Files` or :ref:`Filter files`.

.. _Sort Files:

*********************
Sort Files
*********************

.. image:: ../../../shared/images/FilesPageFilterAction.png
 :alt: an image of the Sort options, which include Name (A-Z), Name (Z-A), 
     Newest, Oldest, File size (High to low) and File size (Low to High). 
     Selecting Apply will sort the files accordingly. 

On the **Files** page, you can sort your files by Name (A-Z), Name (Z-A), 
Newest, Oldest, File size (high to low), and File size (low to high).
 To sort by one of these, select what you wish to sort by and click Apply.

.. _Filter Files:

*********************
Filter Files
*********************

You can filter files by type so that only a selected type of file is 
visible. The list remains in the current sort order.

You can filter by the following file types.

.. list-table::
   :header-rows: 1
   :widths: 10 20

   * - Type
     - Possible File Name Extensions
   * - Audio
     - .aac, .mpeg, .mp3, .ogg, .wav
   * - Code
     - .css, .html, .json, .php, .sql
   * - Documents
     - .pdf, .txt, Microsoft Office and Open Office documents, presentations,
       spreadsheets
   * - Images
     - .gif, .ico, .jpg, .jpeg, .png, .tif, .tiff

To filter the list of files by type, follow these steps:

#. On the **Files** page, click the Filters button.
#. In the list, select the checkboxes for the types of file that you want.

The list refreshes to show only the type or types of file you selected.

To reset the list and view files of all types, clear all checkboxes.

.. _File URLs:

*************************************************
Use an Uploaded File Inside or Outside the Course
*************************************************

When you upload a file, Studio assigns a Studio URL and a web URL to the file.
These URLs are found within the info modal (select three dot menu, then select
Info to view the modal).To use an uploaded file, you add a link to the Studio 
URL or the web URL in your content.

.. note::
  If you do not want to allow access to a file from outside your course, you
  can lock the file so that only learners who are signed in and enrolled in
  your course can access the file. For more information, see :ref:`Lock a
  File`.

.. _Add a File or Image Inside the Course:

=====================================
Add a File or Image Inside the Course
=====================================

To add a file or image inside the course, such as to a component, a course
update, or a course handout, follow these steps:

#. On the **Files** page, select the **Studio** option in the
   **Copy URLs** column.

#. In the component or other content, paste the Studio URL.

For more information, see :ref:`Add an Image to a Text Component`.

.. _Add a File or Image Outside the Course:

======================================
Add a File or Image Outside the Course
======================================

To add a file or image outside the course, such as to a bulk email message that
you send from the LMS, follow these steps.

#. On the **Files & Uploads** page, select the **Web** option in the
   **Copy URLs** column.

   The **Web** option text briefly changes to **Copied**.

#. In the external content, paste the web URL.

.. note::
  Be sure that you do not use the Studio URL in an email message. For more
  information about sending email messages, see
  :ref:`Send_Bulk_Email`.

.. _Lock a File:

*******************
Lock a File
*******************

By default, anyone can access a file you upload if they know the web URL, even
if they are not enrolled in your course. You can prevent outside access to a
file by locking the file. When you lock a file, the web URL only allows
learners who are enrolled in your course and signed in to access the file.

To lock a file, select the lock icon in the row for the file.

.. _Delete a File:

*******************
Delete a File
*******************

To delete a file, first click on the corresponding checkboxes of the files 
that you wish to delete, then click on the Actions button, and then select 
Delete. To deleteall files, select the very first checkbox, then select the 
Action button and then select Delete.


.. warning::
  After you delete a file, any links to the file from inside or outside the
  course are broken. You must update links to files that you delete.

.. _Download a File

**************************
Download a File
**************************
To download individual files, multiple files at once, or all of your files, 
first click on corresponding checkboxes of the files that you wish to 
download, then click on the Actions button, and then select Download. To 
download all files, select the very first checkbox, then select the Action 
button and then select Download.

