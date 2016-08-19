.. _Sass Theming:

************
Sass Theming
************

CSS files are treated as assets, and like all assets in Open edX, they can be
replaced with themed versions. However, the Open edX project uses the Sass_
framework for writing and organizing CSS files, and this gives theme authors
more flexibility with how they modify styling on Open edX. Instead of replacing
the CSS files outright, theme authors can override specific `Sass variables`_
to modify parts of the CSS files without replacing all of them.

.. note::

    The `Sass/CSS Styleguide`_, created by the edX UX (user experience) team,
    includes guidance for syntax preferences and suggestions for documenting
    variables.
    You don't have to make your Sass overrides conform to this styleguide,
    but your theme may be easier to maintain if it does.

To override Sass variables, create a ``sass`` directory inside of
the ``static`` directory in your theme. If you are overriding Sass
for the LMS, in a theme named ``my-theme``, the directory structure looks
like the following example.

.. code-block:: text

    my-theme
    └── lms
        └── static
            └── sass

Inside of the ``sass`` directory, you can create Sass files with names that
match the core Sass files in the platform. For example, most of the styling
in the LMS comes from the ``lms/static/sass/lms-main.scss`` Sass file, so to
override styling in that file, you must create a file named ``lms-main.scss``
in your theme's ``sass`` directory.

.. code-block:: text

    my-theme
    └── lms
        └── static
            └── sass
                └── lms-main.scss

Within that file, you must define whatever themable Sass variables you want,
and then import the core Sass file that you wish to override.
Your theme's ``lms-main.scss`` might look like this example.

.. code-block:: css

    // Make the background red
    $header-bg: rgb(250,0,0);

    // Import the core Sass file
    @import 'lms/static/sass/lms-main';

.. note::

    When overriding variables in Sass, your variables must be defined **before**
    you import the core template, otherwise they will not work properly.

Organizing Sass with Partials
-----------------------------

`Sass partials`_ are a widely-used way of organizing Sass
and reducing repetition in your styling.
The Open edX core Sass files use partials extensively, and edX
recommends that you do so, as well. During the Sass compilation
process, Open edX produces multiple different CSS files, including special
versions of these files for languages with right-to-left alphabets. In order
to override Sass variables for all of these CSS files without needing to
repeat your overrides multiple times, edX recommends that you use
Sass partials to define your overrides once, and import those overrides wherever
they are needed.

In the previous example, you overrode the ``$header-bg`` variable in the
``lms-main.scss`` file only. To make these overrides also apply when
Open edX users are using a right-to-left language, make
the same overrides in the ``lms-main-rtl.scss`` file, as well.
To override the ``lms-main-rtl.scss`` file, you add a Sass file with that name
to your ``my-theme`` Sass directory. As a result, your ``my-theme`` directory
now includes the following subdirectories and files.

.. code-block:: text

    my-theme
    └── lms
        └── static
            └── sass
                ├── lms-main.scss
                └── lms-main-rtl.scss

Without using partials, the contents of the ``lms-main-rtl.scss`` file might
look like this example.

.. code-block:: css

    // Make the background red
    $header-bg: rgb(250,0,0);

    // Import the core Sass file
    @import 'lms/static/sass/lms-main-rtl';

But that means you are defining the ``$header-bg`` variable
in two different places.
If you ever want to change the background color again in the theme,
you will need to remember to do it twice.
This becomes much more difficult to keep track of
as the number of Sass overrides in your theme grows.

Instead, move this definition out into a partial. Add another Sass file
to your theme's ``sass`` directory, and name it ``_overrides.scss``. Be sure
that the name starts with an underscore!

.. code-block:: text

    my-theme
    └── lms
        └── static
            └── sass
                ├── _overrides.scss
                ├── lms-main.scss
                └── lms-main-rtl.scss

In this ``_overrides.scss`` file, you can define only the overrides that should
apply to both of the other files, like this example.

.. code-block:: css

    // Make the background red
    $header-bg: rgb(250,0,0);

Now modify both of the other Sass files to import this partial. The contents
of ``lms-main.scss`` should now look like this example.

.. code-block:: css

    // Import our theme overrides
    @import 'overrides';

    // Import the core Sass file
    @import 'lms/static/sass/lms-main';

The contents of ``lms-main-rtl.scss`` should look like this example.

.. code-block:: css

    // Import our theme overrides
    @import 'overrides';

    // Import the core Sass file
    @import 'lms/static/sass/lms-main-rtl';

.. note::
   The Sass partial must be in a name that starts with an underscore:
   ``_overrides.scss``. However, when using ``@import`` in the other Sass
   files in your theme, you should **not** start with an underscore:
   ``@import 'overrides';``.
   For more information, see `the documentation for Sass partials`_.

This way, both files will load the contents of your ``_overrides.scss`` file,
and you only need to modify your overrides in one place.

Adding New Sass Rules
---------------------
In addition to overriding Sass variables in your theme, you can also define new
Sass rules. These rules are added to any other rules defined in the core
Sass files, rather than replacing the existing Sass rules. To add a new Sass
rule, you define it in the themed Sass file, or one of the Sass partials
that your themed Sass file imports. For example, your ``_overrides.scss`` could
contain the following content.

.. code-block:: css

    // Override a Sass variable
    $header-bg: rgb(250,0,0);

    // Define a new Sass rule
    body ul li {
        font-size: 1000px;
    }

You still need to import the core Sass file in your themed
``lms-main.scss`` file; otherwise, your Sass rules will replace all of the
core Sass rules instead of adding to them.

Next Steps
----------
When you have finished creating your theme,
:ref:`activate your theme <Activating a Theme>`.

.. include:: ../../../../links/links.rst
