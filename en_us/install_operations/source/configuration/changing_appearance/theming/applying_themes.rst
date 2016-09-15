.. _applying_themes:

#######################
Applying Themes
#######################

You apply themes to the sites that you have configured in your Open edX
installation. If your installation does not have more than one site, you apply
a theme to the default site.

.. For more information about Open edX sites, see :ref:`Configuring Open edX Sites`.

************************
Apply a Theme to a Site
************************

To apply a theme to an Open edX site, follow these steps.

#. Make sure that you have enabled theming for your Open edX installation and
   that you have configured an installation-wide themes directory. For more
   information, see :ref:`enable_theming`.

#. Make sure that you have created a theme and that you know the identifier of
   the theme. The identifier of a theme is the name of the directory for that
   theme, within your installation-wide themes directory. For more information,
   see :ref:`Creating a Theme`.

#. Sign in to the Django administration console for your base URL. For example,
   ``http://{your_URL}/admin``.

#. Select **Site themes** to open the
   ``http://{hostname}/admin/theming/sitetheme`` page.

#. Select **Add site theme**.

#. From the **Site** menu, select the site you want to apply a theme to.

#. In the **Theme dir name** field, enter the identifier of the theme.

.. #. Is there a Save action? - Alison
