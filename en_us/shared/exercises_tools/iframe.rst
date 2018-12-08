.. _IFrame:

##################
IFrame Tool
##################

.. note:: EdX offers provisional support for this tool.

An IFrame allows you to integrate ungraded exercises and tools from any
Internet site into the body of your course. The IFrame appears inside an HTML
component, and the exercise or tool appears inside the IFrame. IFrames can
include your own tools or third-party tools.

.. image:: ../../../shared/images/IFrame_1.png
  :alt: IFrame tool showing a Euler line exercise
  :width: 500

Before you make content or a tool from an external site available through your
course, be sure to review the content or tool to ensure that it is accessible
to people with disabilities. For example, in addition to testing the IFrame
components that you add to your course, you can ask third party providers to
confirm that a tool is accessible, and, if available, contact your on campus
accessibility support services for additional guidance. For more information,
see :ref:`Accessibility Best Practices for Course Content Development`.

IFrames are well-suited for tools that demonstrate a concept, but that are not
graded or used to store student data. If you want to add a graded tool or
exercise, add the tool as a :ref:`custom JavaScript problem<Custom JavaScript>`
or an
:ref:`LTI component<LTI Component>`.

For more information about IFrames, see the `IFrame specification
<http://www.w3.org/wiki/HTML/Elements/iframe>`_.

****************************
Create an IFrame Tool
****************************

To add an exercise or tool in an IFrame, you create an IFrame HTML component
and add the URL of the page that contains the exercise or tool to the
component. You can also add text and images both before and after the IFrame.

.. note:: The URL of the page that contains the exercise or tool must start
 with ``https`` instead of ``http``. If the URL starts with ``http``, work with
 the owner of that page to find out if an ``https`` version is available. Some
 websites do not allow their content to be embedded in IFrames.

#. Under **Add New Component**, select **HTML**, and then select **IFrame**.

#. In the new component, select **Edit**.

#. In the visual editor toolbar, select **HTML**.

#. In the HTML source code editor, locate the following HTML (line 7). This
   HTML includes the ``<iframe>`` element.

   .. code-block:: html

      <p><iframe src="https://studio.edx.org/c4x/edX/DemoX/asset/eulerLineDemo.html" width="402" height="402" marginwidth="0" marginheight="0" frameborder="0" scrolling="no">You need an iFrame capable browser to view this.</iframe></p>

#. Replace the default URL in the ``src`` attribute
   (``https://studio.edx.org/c4x/edX/DemoX/asset/eulerLineDemo.html``) with the
   URL of the page that contains the exercise or tool. **This URL must start
   with https**. Make sure that you do not delete the quotation marks that
   surround the URL.

#. Change the attributes in the IFrame element to specify any other settings
   that you want. For more information about these settings, see :ref:`IFrame
   Settings`. You can also change the text between the opening and closing
   ``<iframe>`` tags. Learners see this text only when they use a browser that
   does not support IFrames.

#. Select **OK** to close the HTML source code editor and return to the
   :ref:`visual editor<The Visual Editor>`.

#. In the visual editor, replace the default text with your own text.

#. Select **Save**.

.. _IFrame Settings:

======================
IFrame Settings
======================

To specify settings for your IFrame, you add, remove, or change the
attributes inside the opening ``<iframe>`` tag. The ``<iframe>`` tag **must**
contain a ``src`` attribute and a ``title`` attribute. Other attributes are
optional.

You can add these attributes in any order you want.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``src`` (required)
     - Specifies the URL of the page that contains the exercise or tool,
       beginning with https.
   * - ``title`` (required)
     - Describes the content or its purpose in the context of the course.
   * - ``width`` and ``height`` (optional)
     - Specify the width and height of the IFrame, in pixels or as a
       percentage. To specify the value in pixels, enter numerals. To specify a
       percentage, enter numerals followed by a percent sign.

       If you do not specify the width and height, the IFrame uses the
       dimensions that the linked page has set. These dimensions vary by
       website. If you change the width and height of the IFrame, the content
       from the linked page might be resized, or only part of the content may
       appear.

   * - ``marginwidth`` and ``marginheight`` (optional)
     - Specify the size of the space between the edges of the IFrame and your
       exercise or tool, in pixels.
   * - ``frameborder`` (optional)
     - Specifies whether a border appears around your IFrame. If the value is
       0, no border appears. If the value is any positive number, a border
       appears.
   * - ``scrolling`` (optional)
     - For an IFrame that is smaller than the exercise or tool it contains,
       specifies whether a scrollbar appears to help users access all of the
       IFrame's content. For example, if the content in your IFrame is very
       tall, you can set the IFrame's height to a smaller number and add a
       vertical scroll bar for users, as in the first image below.

For example, compare how the different settings in each of the ``<iframe>``
elements below affect the IFrame.

.. code-block:: html

      <p><iframe src="https://studio.edx.org/c4x/edX/DemoX/asset/eulerLineDemo.html" width="442" height="200" marginwidth="20" marginheight="20" frameborder="1" scrolling="yes">You need an iFrame capable browser to view this.</iframe></p>

.. image:: ../../../shared/images/IFrame_3.png
   :alt: IFrame with only top half showing and vertical scroll bar on the side
   :width: 500

.. code-block:: html

      <p><iframe src="https://studio.edx.org/c4x/edX/DemoX/asset/eulerLineDemo.html" width="550" height="250" marginwidth="30" marginheight="60" frameborder="1" scrolling="no">You need an iFrame capable browser to view this.</iframe></p>

.. image:: ../../../shared/images/IFrame_4.png
   :alt:
   :width: 500

For more information about IFrame attributes, see the `IFrame specification
<http://www.w3.org/wiki/HTML/Elements/iframe>`_.
