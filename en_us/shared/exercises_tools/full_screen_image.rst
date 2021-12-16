.. _Full Screen Image:

######################
Full Screen Image Tool
######################

.. note:: EdX does not support this problem type.

Some large images are difficult for learners to view in the courseware. The
full screen image tool allows learners to enlarge the image, so they can see
all the detail in context.

.. contents::
  :local:
  :depth: 1

****************************************
The Learner View of a Full Screen Image
****************************************

The learner sees the full screen image in a unit page. When the learner moves
the cursor over the image, the **Fullscreen** option appears.

.. image:: ../../../shared/images/image-modal.png
 :alt: Image of the full screen image tool with the Full Screen button.

When the learner selects **Fullscreen**, the image opens and expands in the
full browser window. **Close**, **Zoom In**, and **Zoom Out** options appear.

.. image:: ../../../shared/images/image-modal-window.png
 :alt: Image of the Image Modal tool with the Full Screen button.

The learner can then zoom in on the image, and drag the image to view a
specific part of it.

.. image:: ../../../shared/images/image-modeal-zoomed.png
 :alt: Image of the Image Modal tool with the Full Screen button.

******************************
Create a Full Screen Image
******************************

#. Upload your image file to the **Files & Uploads** page. For more
   information, see :ref:`Add Files to a Course`.

#. Under **Add New Component**, select **Text**, and then select **Full Screen
   Image Tool**.

#. In the new component that appears, select **Edit**.

#. In the component editor, replace the default title, remove the instructional
   paragraph, and add text as needed.

#. Select **HTML** from the toolbar to edit the HTML source code.

#. Scroll down in the file, and then replace the following placeholders with
   your own content.

   * Replace the value of the ``<a>`` element's ``href`` attribute with the
     path to your image. Do not change the value of the class attribute. For
     example:

     ``<a href="/static/Image1.jpg" class="modal-content">``

   * Replace the value of the ``<img>`` element's ``src`` attribute with the
     path to your image. For example:

     ``<img alt="Full screen image" src="/static/Image1.jpg"/>``

   * Ensure that the value of the ``href`` and ``src`` attributes are the same,
     and that you do not change the class attribute. Your sample code should
     look like the following example.

   .. code-block:: xml

     <h3>Sample Image Modal</h3>
     <a href="/static/Image1.jpg" class="modal-content">
     <img alt="Full screen image" src="/static/Image1.jpg"/>
     </a>

   .. note::
     You can use this same HTML code in any Text component, not just those
     components you created as full screen images.

#. Select **Save**.
