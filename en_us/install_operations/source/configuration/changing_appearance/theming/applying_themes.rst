.. _applying_themes:

#######################
Applying Themes
#######################

You apply themes to the sites that you have configured in your Open edX
installation. If your installation does not have more than one site, you apply
a theme to the default site. For more information about Open edX sites, see
:ref:`Configuring Open edX Sites`.

************************
Apply a Theme to a Site
************************

To apply a theme to an Open edX site, do the following.

#. Make sure that you have enabled theming for your Open edX installation and
   that you have configured a themes directory. For more information, see
   :ref:`enable_theming`.

#. Make sure you have created a theme and that you know the identifier of the
   theme. The identifier of a theme is the name of the directory for that
   theme, within the themes directory. For more information, see :ref:`Creating
   a Theme`.

#. Log into the Django admin site for your Open edX site.

#. Select **Site themes** to open the
   ``http://{hostname}/admin/theming/sitetheme`` page.

#. Select **Add site theme**.

#. From the **Site** menu, select the site you want to apply a theme to.

#. In the **Theme dir name** field, enter the identifier of the theme, which is
   the name of the theme directory within the themes directory for your Open
   edX installation.
