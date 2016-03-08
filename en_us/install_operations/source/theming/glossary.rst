.. _Theming Glossary:

****************
Theming Glossary
****************

* A **theme** is a collection of templates and assets that override the
  look and feel of an Open edX installation. It consists of a directory
  containing those templates and assets in a specific hierarchy.
* A **core template** is a template that exists in one of the Open edX
  codebases. For example, the HTML files in the ``lms/templates`` directory
  of the ``edx-platform`` repository are core templates.
* A **core asset** is an image, CSS file, or JavaScript file that exists
  in one of the Open edX codebases. For example, the image files in the
  ``lms/static/images`` directory of the ``edx-platform`` repository are
  core assets.
* A **themed template** is a template that exists in a theme. Typically,
  themed templates are organized and named in a way that parallels a core
  template, so that the themed template will override the core template.
  For example, a themed template named
  ``my-theme-directory/lms/templates/header.html`` will override a core
  template named ``lms/templates/header.html`` in the ``edx-platform``
  repository.
* A **themed asset** is an image, CSS file, or JavaScript file that exists
  in a theme. Typically, themed assets are organized and named in a way that
  parallels a core asset, so that the themed asset will override the core
  template. For example, a themed asset named
  ``my-theme-directory/lms/static/images/logo.png`` will override a core
  asset named ``lms/static/images/logo.png`` in the ``edx-platform`` repository.
