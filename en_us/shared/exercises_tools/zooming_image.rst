.. _Zooming Image:

##################
Zooming Image Tool
##################

.. note:: EdX does not support this tool.

If you present information to your learners using very large or very detailed
images, learners might not be able to clearly see all the information in the
image. Use the zooming image tool to provide learners with the ability to zoom
in to and enlarge selected areas of your image.


.. image:: ../../../shared/images/Zooming_Image.png
  :alt: Example zooming image tool showing a chemistry exercise.

***********************************
Components of a Zooming Image Tool
***********************************

To create a zooming image tool, you need the following files.

* The image that you want learners to see when they access the unit.

* The image that appears in the magnified area when a learner selects the
  regular image. This image can be larger than the regular image.

* The ``jquery.loupeAndLightbox.js`` JavaScript file from
  ``http://files.edx.org/jqueryloupeAndLightbox.js``.


****************************
Create a Zooming Image Tool
****************************

#. Download the ``jquery.loupeAndLightbox.js`` file by right-clicking the
   following link, and then selecting the option to save or download the linked
   file.

   http://files.edx.org/jqueryloupeAndLightbox.js

#. In Studio, select **Content** and then select **Files & Uploads** to upload
   your regular-sized image file, your small image file, and the
   ``jquery.loupeAndLightbox.js`` file. For more information about uploading
   files for your course, see :ref:`Add Files to a Course`.

#. Add a zooming image tool to your course. In the course outline in Studio,
   select **Add New Component**, select **Text**, and then select **Zooming
   Image Tool**.

#. In the new component that appears, select **Edit**.

#. In the component editor, replace the default problem text with your own
   text.

#. Select **HTML** from the toolbar to edit the HTML source code.

#. Scroll down in the file, and then replace the following placeholders with
   your own content.

   - Replace the following file name and path with the name and path of the
     image that you want to appear magnified when the user hovers over the
     regular image.

     ``https://studio.edx.org/c4x/edX/DemoX/asset/pathways_detail_01.png``

     For example, your file name and path might be ``/static/Image1.jpg``.

   - Replace the following file name and path with the name and path of the
     image that you want to appear when the page opens.

    ``https://studio.edx.org/c4x/edX/DemoX/asset/pathways_overview_01.png``

     For example, your file name and path might be ``/static/Image2.jpg``.

   - Replace the following name and file path with the name and path of the
     JavaScript file that you downloaded from ``files.edx.org``.

     ``https://studio.edx.org/c4x/edX/DemoX/asset/jquery.loupeAndLightbox.js``

     Because you uploaded the ``jquery.loupeAndLightbox.js`` file to the
     **Files & Uploads** page, your file name and path is
     ``/static/jquery.loupeAndLightbox.js``.

   - (Optional) If you want the magnified area to be larger or smaller, change
     the ``width`` and ``height`` values from 350 to larger or smaller numbers.
     For example, you can change both numbers to 450. Or, if you want a
     horizontal oval instead of a circle, you can change the ``width`` value to
     a number such as 500 and the ``height`` value to a number such as 150.

   The HTML in your zooming image tool might resemble the following.

   .. image:: ../../../shared/images/ZoomingImage_Modified.png
     :alt: Example HTML for a zooming image tool.

#. Select **Save**.


