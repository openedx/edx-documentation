.. _IFrame:

##################
Iframe Tool
##################

.. note:: EdX offers provisional support for this tool.

The iframe tool allows you to integrate ungraded exercises and tools from any
Internet site into the body of your course. It places an iframe inside an HTML
component, and then the exercise or tool appears inside the iframe. The iframe
can include your own tools or third-party tools.

.. image:: ../../../shared/images/IFrame_1.png
  :alt: Iframe tool showing a Euler line exercise.
  :width: 500

Before you make content or a tool from an external site available through your
course, be sure to review the content or tool to ensure that it is accessible
to people with disabilities. For example, in addition to testing the iframe
components that you add to your course, you can ask third party providers to
confirm that a tool is accessible, and, if available, contact your on campus
accessibility support services for additional guidance. For more information,
see :ref:`Accessibility Best Practices for Course Content Development`.

Iframes are well-suited for tools that demonstrate a concept, but that are not
graded or used to store student data. If you want to add a graded tool or
exercise, add the tool as a :ref:`custom JavaScript problem<Custom JavaScript>`
or an :ref:`LTI component<LTI Component>`.

For more information about iframes, see the `iframe: The Inline Frame element
<https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe>`_.

****************************
Create an IFrame Tool
****************************

To add an exercise or tool in an iframe, you create an iframe Text component
and add the URL of the page that contains the exercise or tool to the
component. You can also add text and images both before and after the iframe.

.. note:: The URL of the page that contains the exercise or tool must start
 with ``https`` instead of ``http``. If the URL starts with ``http``, work with
 the owner of that page to find out if an ``https`` version is available. Some
 websites do not allow their content to be embedded in iframes.

#. Under **Add New Component**, select **Text**, and then select **IFrame
   Tool**.

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

#. Change the attributes in the iframe element to specify any other settings
   that you want. For more information about these settings, see :ref:`IFrame
   Settings`. You can also change the text between the opening and closing
   ``<iframe>`` tags. Learners see this text only when they use a browser that
   does not support iframes.

#. Select **OK** to close the HTML source code editor and return to the
   :ref:`visual editor<The Visual Editor>`.

#. In the visual editor, replace the default text with your own text.

#. Select **Save**.

.. _IFrame Settings:

======================
Iframe Settings
======================

To specify settings for your iframe, you add, remove, or change the
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
     - Specify the width and height of the iframe, in pixels or as a
       percentage. To specify the value in pixels, enter numerals. To specify a
       percentage, enter numerals followed by a percent sign.

       If you do not specify the width and height, the iframe uses the
       dimensions that the linked page has set. These dimensions vary by
       website. If you change the width and height of the iframe, the content
       from the linked page might be resized, or only part of the content may
       appear.

   * - ``marginwidth`` and ``marginheight`` (optional)
     - Specify the size of the space between the edges of the iframe and your
       exercise or tool, in pixels.
   * - ``frameborder`` (optional)
     - Specifies whether a border appears around your iframe. If the value is
       0, no border appears. If the value is any positive number, a border
       appears.
   * - ``scrolling`` (optional)
     - For an iframe that is smaller than the exercise or tool it contains,
       specifies whether a scrollbar appears to help users access all of the
       iframe's content. For example, if the content in your iframe is very
       tall, you can set the iframe's height to a smaller number and add a
       vertical scroll bar for users, as in the first image below.

For example, compare how the different settings in each of the ``<iframe>``
elements below affect the iframe.

.. code-block:: html

      <p><iframe src="https://studio.edx.org/c4x/edX/DemoX/asset/eulerLineDemo.html" width="442" height="200" marginwidth="20" marginheight="20" frameborder="1" scrolling="yes">You need an iFrame capable browser to view this.</iframe></p>

.. image:: ../../../shared/images/IFrame_3.png
   :alt: Iframe with only the top half showing and a vertical scroll bar on the
    side.
   :width: 500

.. code-block:: html

      <p><iframe src="https://studio.edx.org/c4x/edX/DemoX/asset/eulerLineDemo.html" width="550" height="250" marginwidth="30" marginheight="60" frameborder="1" scrolling="no">You need an iFrame capable browser to view this.</iframe></p>

.. image:: ../../../shared/images/IFrame_4.png
   :alt: Iframe with only the top half showing but no scroll bar available.
   :width: 500

For more information about iframe attributes, see 
`iframe: The Inline Frame element <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe>`_.
