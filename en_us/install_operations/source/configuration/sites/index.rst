.. _Configuring Open edX Sites:

#############################
Configuring Open edX Sites
#############################

By default, an Open edX installation has one site for users to interact with.
You can configure multiple sites within your Open edX installation. A site
presents Open edX courses and content in an individual way. If you set up
multiple sites, you can configure them independently of each other. For
example, you can assign a different theme to each site and specify which
courses are available on each site.

You host each site on a separate domain or subdomain from your Open edX
installation. You configure the domain name for a site in the Django admin site
when you create it. For example, you might configure one site
with the domain name ``university.edu`` and another site with the domain
name ``advancedplacement.edu``. Or you might configure one site with the domain
name ``arts.myuniversity.edu`` and another site with the domain name
``sciences.myuniversity.edu``.


.. toctree::
   :maxdepth: 1

   create_site
   configure_site

For more information about themes, see :ref:`Theming Open edX`.

