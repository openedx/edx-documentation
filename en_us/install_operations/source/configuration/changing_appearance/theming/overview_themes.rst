.. _Theming Overview:

###################
Themes Overview
###################

After you configure one or more sites for your Open edX installation, including
their domain and platform names, you can set up a theme to use for each site.

To override the files that constitute the default Open edX theme, you create
replacements for one or more of those files, place them in file paths that are
constructed and named in parallel to the default file locations,
configure your Open edX instance to use the files in your theme's directories
instead of the default locations, and then compile the theme.

EdX first looks for files in your theme directories, and uses any file that
matches the exact file path and file name of a default UI file. If matching
files are not found, then Open edX looks in the default location.

For more information about Open edX sites, see :ref:`Configuring Open edX
Sites`.
