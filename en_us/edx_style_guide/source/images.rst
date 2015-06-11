.. _Images:

#######
Images
#######

Because the user interface can change rapidly and frequently, and because it is
very expensive for translation teams to re-create screen shots, the
documentation team uses screen shot images sparingly.

.. Add to images section: guidelines for created images such as flowcharts,
 diagrams. What standard tools should we/can we use? Ultimately would be good
 to have a library of styled graphics, shapes, etc. for consistency.

.. contents:: Section contents
  :local:
  :levels: 1

***************
Resources
***************

These resources for screen captures (existing dummy courses with good
data) are available on edX Edge.

* `AA Introduction to Music Theory <https://studio.edge.edx.org/course/sylviaX/TEST10/2014_T3>`_

* `La Tierra Centroamericana <https://studio.edge.edx.org/course/edX/GEO101/2014_T1>`_

*****************
Guidelines
*****************

Messages: Avoid using a screen shot to show an error, warning, or informational
message. Instead, just include the text of the message as part of the procedure
or concept.


.. when is it necessary? when to avoid?

Before you take a screen shot, reduce the window width to avoid extra white
space. Usually this means you narrow until page is no longer responsive (unless
this will make screen shot too long).

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

To capture part of the screen, follow these steps.

#. Press CMD + SHIFT + 4. The mouse pointer changes to a crosshairs symbol.
#. Click and drag from the upper-left corner of the area you want to capture
   to the lower-right corner, and let go of the mouse when you've captured the
   image you want.

.. note:: This method does not capture the mouse pointer.

*****************
Editing Images
*****************

Processing screenshots (colors for borders, overlay items) and how to make
higher res version available

Use Photoshop to edit images.

Add a border with the following characteristics to each screen shot.

* 2 pt
* #b7b7b7
  
To add a border, CMD+a to select the entire image, then Edit > Stroke. 

Save the screen shot as the original size and set size in document.

Save for web 

#. Press CMD+OPTION+SHIFT+S. 
#. Preset: PNG-24
#. Accept other defaults
#. Save as .png, original size. Specify width in RST file.

.. does setting the screen size in the rst work for both HTML and PDF? and is that the preferred method, or is it the save for web option that follows? Also, note that there is an image size section further down - Alison, 11 June 2015 

=============
Annotations
=============

To annotate screen shots, use edX magenta (#b62364). If another color is
required, use edX blue (#2276b2). 

Make sure that callouts or other additions are in a separate layer from the
images.

Instead of using text, use numbered identifiers and provide a legend in the
text.

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


*****************
Accessibility
*****************

Every image added to the documentation must have alt text that makes the
purpose of the image clear to those who are using screen readers.

The following examples are of useful alt text.

.. code-block:: xml

 :alt: Image of the feedback checkmark and x from a student's point of view.

 :alt: A stacked bar chart for three subsections. In one subsection, fewer
  than a third of the students who started videos finished watching them.


The following examples are of alt text that is less useful.

.. code-block:: xml

 :alt: Image of a multiple choice problem.

 :alt: Example response.

When you write alt text, follow these guidelines. 

* Be aware of how long the alt text is. Automated tests produce warnings for
  text that is longer than about 20 characters. However, your description must
  be long enough to be meaningful.
* Include punctuation in the alt text.
* To ensure that every image in an HTML file has alt text, try the 
  `Durham University Alt Text Checker`_.
* To check the alt text length and find other accessibility issues in an HTML
  file, try the `Web Accessibility Evaluation Tool`_.

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




.. _Durham University Alt Text Checker: https://www.dur.ac.uk/cis/web/accessibility/tools/alttext/

.. _Web Accessibility Evaluation Tool: http://wave.webaim.org/
