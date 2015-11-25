.. _Adding Badge Events:

It is possible to create your own Badges for use within an XBlock or the platform.
In order to use these features, you will first need to :ref:`Enable Badging`.

********
Overview
********

Creating a badging event starts with creating a *Badge Class*. A BadgeClass is a specification 
of the badge you wish to award to students. The actual badge the user receives is known as a 
*Badge Assertion*.

**********************
Creating a Badge Class
**********************

Badge Classes are created and retrieved via the ``get_badge_class`` method on the ``BadgeClass`` model from the ``badges`` 
app. This method takes the following arguments:

* ``slug``: An identifier for this badge. It must be a string which conforms to the specification of a Django 
  `SlugField <https://docs.djangoproject.com/en/1.8/ref/models/fields/#slugfield>`_.
* ``issuing_component``: An identifier for the software that is responsible for the badging event. The convention is to use
    double-underscored namespacing. For instance, a Badge Class dealing with discussions might have an ``issuing_component``
    of ``edx__discussions``. Like ``slug``, this must conform to the specification of a Django
    `SlugField <https://docs.djangoproject.com/en/1.8/ref/models/fields/#slugfield>`_.
* ``display_name``: The human-readable name for the award.
* ``description``: A description of the award.
* ``criteria``: A description of the work that was required to earn this award.
* ``image_file_handle``: A file handle object that points to a PNG image, square, under 250KB.

This function will create the Badge Class if it does not already exist. If the badge class already exists, the existing 
Badge Class will be returned. Badge Classes are uniquely identified by a combination of their `slug`` and 
``issuing_component`` fields. If your code changes the description, but uses the existing ``slug`` and ``issuing_component``
fields, the existing Badge Class will be used for backwards compatibility, rather than creating a new one. It will not
update the existing one with new values.

If you do not wish to create the Badge Class should it not exist, use ``create=False``. This will return ``None`` if the
Badge Class does not already Exist.

****************
Awarding a Badge
****************

Once you have created your badge class with ``BadgeClass.get_badge_class``, you can award it with the ``award`` method.
The ``award`` method accepts the following arguments:

* ``user``: The user to whom the badge shall be awarded.
* ``evidence_url``: An optional argument containing a URL that holds proof that the user earned this award.

**************************
The Badging XBlock Service
**************************

To award badges within an XBlock, you will need to use the XBlock ``badging`` service. This service provides an object with
the ``get_badge_class`` method. Because the ``award`` method on Badge Classes requires a user, you will likely also need the 
XBlock ``user`` service.


.. SlugField_: https://docs.djangoproject.com/en/1.8/ref/models/fields/#slugfield

.. include:: ../../../links/links.rst
