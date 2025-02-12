.. _styling_drag_and_drop_problems:

##############################
Styling Drag and Drop Problems
##############################

You can customize the appearance of drag and drop problems in your Open edX
site using custom Cascading Style Sheet (CSS) files. The style that you
configure applies to all drag and drop problems in all courses. For more
information about drag and drop problems, see
:ref:`drag_and_drop_problem`.

The following two methods apply CSS styling to drag and drop problems.

* You can apply CSS styles to drag and drop problems by creating a theme for
  your site and updating the Syntactically Awesome Style Sheet (Sass) files
  that produce the CSS files. For more information, see :ref:`Creating a
  Theme`.

* You can apply CSS styles to drag and drop problems by adding a Python
  programming language module that includes a CSS file to your Open edX site.
  For more information, see the instructions in this section.

.. note:: This section provides information about styling the drag and drop
    problem type that was added to the edX platform in 2016. This drag and drop
    problem type replaced an earlier drag and drop problem type. You should use
    the latest drag and drop problem type for all new course problems.

.. note::
    Course teams can also style the background and text colors of the draggable
    items in an individual drag and drop problem, without adding CSS files or
    configuring a Python module. For more information, see
    :ref:`changing_visual_style_of_drag_and_drop_problem`.

To customize the style of drag and drop problems by adding a CSS file in a
Python module, follow these steps.

#. Create a custom CSS style sheet that applies styles to the drag and drop
   problem user interface. You can base your style sheet on the `example CSS
   file for drag and drop problems`_ that is included in the drag and drop
   problem module.

#. Create a Python module that includes your custom CSS style sheet. For
   example, the following Python module files include a CSS style sheet.

    .. code-block:: shell

        ./my_drag_and_drop_style
        ./my_drag_and_drop_style/css
        ./my_drag_and_drop_style/css/my_drag_and_drop_style.css
        ./my_drag_and_drop_style/__init__.py
        ./setup.py

   For more information about creating and installing Python modules, see the
   documentation for the Python programming language.

#. Install your Python module on the LMS server as the ``edxapp`` user.

   .. code-block:: shell

        pip install /path/to/my/module


#. Edit the ``lms.yml`` file for your LMS server. Add the ``drag-and-
   drop-v2`` object to the ``XBLOCK_SETTINGS`` object. Include the content
   shown in the following example.

   .. code-block:: none

           "XBLOCK_SETTINGS":{
                "drag-and-drop-v2": {
                    "theme": {
                        "package": "my_drag_and_drop_style",
                        "locations": ["css/my_drag_and_drop_style.css"]
                    }
                }

   Enter the name of your Python module in the value of the ``package`` object. The value in the example above is ``my_drag_and_drop_style``.

   Enter the path to your CSS style sheet file in the value of the
   ``locations`` object. The value in the example above is
   ``css/my_drag_and_drop_style.css``. The path must be relative to your Python
   module installation directory. You can include more than one path in the
   ``locations`` array, separated by commas.

#. Restart the LMS.

.. include:: ../../../../links/links.rst
