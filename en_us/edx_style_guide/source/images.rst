.. _Images:

#######
Images
#######

Images
Resources for making screen captures (existing dummy course with good data)

`AA Introduction to Music Theory <https://studio.edge.edx.org/course/sylviaX/TEST10/2014_T3>`_

`La Tierra Centroamericana <https://studio.edge.edx.org/course/edX/GEO101/2014_T1>`_

Because the UI can change rapidly, use images sparingly.

Add to images section. Need guidelines for created images such as flowcharts,
diagrams. What standard tools should we/can we use? Ultimately would be good
to have a library of styled graphics, shapes, etc. for consistency.

*****************
Guidelines
*****************

Guidelines for using screenshots in documentation (when is it necessary)
Guidelines for making screen captures (sizes, resolution, how much of window
to capture/exclude) Before you take a screen shot, narrow the window to avoid
extra white space - usually narrow until page is no longer responsive (unless
this will make screen shot too long)

The following image has a lot of white space inside the component editor,
which narrowing the window will correct.

.. image:: Images/DiscussionComponentEditor.png
  :width: 450
  :alt: Image with extra white space on the right

Keep images flush with text in bulleted and ordered lists.

.. image:: Images/Image_Flush.png
  :width: 500
  :alt: Image kept inline with a bulleted list

*****************
Capturing Images
*****************

You can use the Mac's built-in screen capture functionality to take screen shots. 

To capture part of the screen:

#. Press CMD + SHIFT + 4. The mouse pointer changes to a crosshairs symbol.
#. Click and drag from the upper-left corner of the area you want to capture
   to the lower-right corner, and let go of the mouse when you've captured the
   image you want.

.. note:: This method does not capture the mouse pointer.

*****************
Accessibility
*****************

Making images and accessible and easy to globalize
use alt text so that screenreaders have information for the image



*****************
Editing Images
*****************

Processing screenshots (colors for borders, overlay items) and how to make
higher res version available

Use Photoshop to edit images.

Screen shots must have a border:
2 pt
#b7b7b7

Save the screen shot as the original size and set size in document.

Save for web (CMD+OPTION+SHIFT+S): 

Preset: PNG-24
Accept other defaults
Save as .png.

=============
Annotations
=============

To annotate screen shots, use edX magenta (#b62364). If another color is
required, use edX blue (#2276b2). 

Make sure that callouts or other additions are in a separate layer from the
images.

Instead of using text, use numbered identifiers and provide a legend.

If text is used in graphics, leave 30% extra surrounding space for expansion.

**************************
Adding Images to Files
**************************

When you add an image to a file, include three lines.

* The image directive
* The image width
* Image alt text

.. code-block:: xml

  .. image:: Images/HTMLEditor_empty.png
    :width: 450
    :alt: An empty HTML component editor in Studio




***************
Image Sizes
***************

Save the screen shot as the original size. Set size in document. This way a
user can click the image in the document to enlarge it.

.. code-block:: xml

  .. image:: Images/image029.png
       :width: 600
       :alt: 




.. list-table::

  * - Full screen width
    - 600
  * - Courseware pane
    - 500
  * - Component editor
    - 450
  * - Dialog box
    - 300
  * - Sidebar
    - 250
  * - Extra-wide screen
    - 800
  * - 
    - 
  * - 
    - 

Full screen width

.. image:: Images/Course_Outline_LMS.png
  :width: 600
  :alt: 600-pixel-wide image

Courseware pane or Course Outline page

.. image:: Images/Units_LMS.png
  :width: 500
  :alt: 500-pixel-wide image

Component editor

.. image:: Images/HTMLEditor_empty.png
  :width: 450
  :alt: 450-pixel-wide image

Dialog box

.. image:: Images/HTML_Insert-EditLink_DBox.png
  :width: 300
  :alt: 300-pixel-wide image

Sidebar

.. image:: Images/unit-never-published.png
  :width: 250
  :alt: 250-pixel-wide image

Extra-wide screen

.. image:: Images/Rerandomize.png
  :width: 800
  :alt: 800-pixel-wide image


