##################################################
Guidelines for Translating the Open edX Platform
##################################################

Open edX uses Transifex, an open source translation platform, to power
the translation of edX software into different languages. All translations
are hosted at `Transifex.com <https://www.transifex.com/>`_, which provides
a web application allowing translators to write, submit, and manage their
translations.

This page explains how to get started with Transifex and provides guidelines
for translators to follow when executing translations. For further discussion,
we welcome you to join the `openedx-translation <https://groups.google.com/forum/#!forum/openedx-translation>`_
mailing list.

For information on the Transifex process, see the following sections.

.. contents::
 :local:
 :depth: 1

******************************
Getting Started with Transifex
******************************

Contributors who want to help translate edx-platform and associated projects
can find edX translation projects on
`Transifex <https://www.transifex.com/organization/open-edx/dashboard>`_.

.. note:: All strings must be both translated **and reviewed** before
  we will publish them on the edx.org website.

You should become a translator only if you feel very confident in both English
and your target language. Open edX is written in English, so all translations
are done from English to another language.

This guide shows images from the Transifex website in English.

* Depending on your browser settings, you might see the site in a different
  language. The button locations are the same.

* The content of the Transifex website is subject to change without notice.

This section contains the following topics.

.. contents::
 :local:
 :depth: 1

Sign up for an Account
=========================

Go to `https://www.transifex.com/signup/ <https://www.transifex.com/signup/>`_
and fill out the form to create a free Transifex account, if you do not have
one already.

Join a Translation Team
==========================

#. After you set up your account, visit the `edx-platform project
   <https://www.transifex.com/projects/p/edx-platform/>`_
   to become a translator for a language.

#. The project page lists languages that have translation projects. If your
   target language is listed, click on the name of the language to go to the
   language's page. An example of choosing the Japanese translation
   project follows.

   .. image:: /images/edx-platform-transifex-project.png
     :alt: The Open edX/edx-platform page on the Transifex website, with the
         Japanese language indicated.

#. After you are on the translation project page for the selected language,
   select **Join team** to become part of the translation team for that
   language.

   .. image:: /images/join-language-team.png
     :alt: The Japanese language page on the Transifex website, with the Join
         team option indicated.

   After you join a translation team, you can begin translating strings
   immediately. For more information, see :ref:`How To Translate With Transifex`.

Join a Review Team
=====================

Optionally, you can request to become a `reviewer
<http://support.transifex.com/customer/portal/articles/1167280>`_ for a
language. Review teams are incredibly important, because all strings must be
both translated **and reviewed** before we will publish them on the edx.org
website.

You should join a review team only if you feel very confident in both your
language and in English. To join a review team, request permission from the
project coordinator(s).

#. On the Transifex edx-platform project page for your selected target
   language, select **Members**.

   .. image:: /images/view-team-members.png
     :alt: The Japanese language page on the Transifex website, with the
         Members option indicated.

   A list of the current members of that translation team appears.

#. Select one of the language coordinators to open the Transifex profile page,
   where you can select **Send message** to send an email message asking for
   reviewer access.

If the coordinator does not respond, try sending a message to another language
coordinator. You can also send a message to one of the edX project maintainers.
The project maintainers appear at the top of the main project page.

If you are willing to become a coordinator for a language, let us know in
your message.


.. _How To Translate With Transifex:

Translating With Transifex
===============================

After you become a member of a translation or review team, you can select any
of the resources in the project to begin translating it. Before you begin, be
sure to review the `Guidelines for Translators`_.

For help documentation on Transifex, see the `Transifex translators
help desk <http://support.transifex.com/customer/portal/topics/414107-translators/articles>`_.

Each language page lists a set of distinct resources to translate.

.. image:: /images/project-resources.png
     :alt: The Japanese language page on the Transifex website, with the
         list of resources to translate indicated.

Focus on translating the non-Studio resources first. That is, please first
translate and review these resources, in this order, before anything else.

  * messages
  * mako
  * django-partial
  * djangojs-partial
  * wiki
  * notifier-django
  * comments-service

Only after the above resources are 100% translated and reviewed, move on to the
Studio resources.

  * mako-studio
  * djangojs-studio
  * django-studio

Requesting a New Language
=========================

If the language you are interested in contributing translations for is not
listed on the Transifex edx-platform project page, select **Request language**
to start a new translation project for your target language.

Before you request a new language, please make sure that the language is not
already listed. Keep in mind that variants of a language might exist in the
list of translation projects ("Chinese" versus "Chinese-China") and one of
these variants may meet your needs.

An edX translation team member will respond to your request within a few days.
If the language that you request is approved, you become the coordinator of
the project. You can add additional coordinators, reviewers, and translators as
you wish.

If you request a new language, we ask that you commit to the success of your
language's translation project. Particularly, we expect you to be an active
translator and work to recruit other translators and reviewers so that the
translation project for your target language advances to completion, with all
strings translated and reviewed, so that we can publish your work on the
edx.org website.

**************************
Guidelines for Translators
**************************

Before you begin translation work, please familiarize yourself with the
following guidelines.

.. contents::
 :local:
 :depth: 1


Ask for Clarification
=====================

If you are uncertain of how to translate a string, we strongly encourage you to
reach out to us and ask for clarification. Please join the `openedx-translation
<https://groups.google.com/forum/#!forum/openedx-translation>`_ mailing list
and make a post. Group members can help clarify the context of the string, and
even add a comment to the code to clarify the string, which will help
translators working on other language projects.

Working With HTML
=================

Translating strings for a website like edX is more complicated than simply
translating sentences from one language to another. Sometimes, sentences (or
"strings") will contain `HTML markup tags
<https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction>`_.
It is very important to understand how to deal with HTML markup.

.. important:: Do not alter or translate any HTML markup tags.

You should translate the text that is between the tags. HTML markup tags begin
and end with ``<`` and ``>`` characters.

Spacing is especially important. Adding spaces in an HTML tag (for example,
changing ``</a>`` to ``</ a>``) will break the website.

Examples::

   String: "If you have a general question about {platform_name} please email
   <a href="mailto:{contact_email}">{contact_email}</a>."

   Good translation: "{platform_name}에 대해 일반적인 질문이 있으면
     <a href="mailto:{contact_email}">{contact_email}</a>로 이메일 주십시요."

   Bad translation: "{platform_name}에 대해 일반적인 질문이 있으면
     {contact_email}로 이메일 주십시요."

     Please do not remove the HTML tags.

   Bad translation: "{platform_name}에 대해 일반적인 질문이 있으면
     <a href="흔한:{contact_email}">{contact_email}</a>로 이메일 주십시요."

     Do not translate the HTML tags. Please use the given HTML tags.

   Bad translation: "{platform_name}에 대해 일반적인 질문이 있으면
     <b>{contact_email}</b>로 이메일 주십시요."

     Do not change the HTML tags to something new. Please use the given HTML
     tags.

   Bad translation: "{platform_name}에 대해 일반적인 질문이 있으면
   < a href = " mailto : {contact_email} " > {contact_email} < / a >로 이메일 주십시요."

     Do not add additional spacing to the HTML tags. Please use the given HTML tags.


Working With Placeholders
=========================

Strings in programs sometimes need to have data inserted into them before being
displayed to the user. Data placeholders label the places in the string where
the data will go. Strings can also have markup like HTML included. It is very
important to preserve the placeholders and markup so that the web site will
work properly.

Placeholders come in a few different forms. Often, they are named so that data
will be placed into the proper placeholder. Please familiarize yourself with
all the different forms to make your translation successful.

Summary Of Placeholders
-----------------------

+-------------------------+
| Placeholder Forms       |
+=========================+
| ``{student_name}``      |
+-------------------------+
| ``%(student_name)s``    |
+-------------------------+
| ``<%= student_name %>`` |
+-------------------------+

When dealing with placeholders, you must follow these rules.

* Do not translate the placeholder (for example, changing ``{day}`` to
  ``{día}``).
* Do not alter or remove the punctuation of the placeholder string (for
  example, changing a ``_`` to a ``-``).
* Do not alter the capitalization of the placeholder string (for example,
  changing ``{day}`` to ``{Day}``).
* Do not alter the spacing of the placeholder string (for example, changing
  ``{day}`` to ``{ day }``).

Please continue reading for examples of each type of placeholder form inside a string.

#. Do not alter or translate placeholder strings in between curly braces (``{
   }``). Strings inside curly braces are replaced with different strings
   while the code is executing. Changing the content of the curly braces will
   cause code to break.

   The placeholder string inside of the braces will give you clues as to what
   type of data will be presented in the final string. For example,
   ``{student_name}`` is replaced with the name of a student, whereas
   ``{contact_email}`` is replaced with an email address that users can
   use to contact us. This will give you some context when you are translating
   sentences with placeholders.

   Altering the strings includes: changing, removing, or adding punctuation,
   changing the capitalization, or adding or removing given spacing. So if the
   placeholder string looks like ``{placeholder_string}``, you should not
   change it at all, eg ``{Placeholder_String}``, ``{placeholder-string}``, ``{
   placeholder_string }``, ``{placeholder string}``. All of these changes have
   the potential to break the software.

   Examples::

     String: "Welcome back {student_name}!"

     Good translation: "¡Bienvenido {student_name}!"

     Bad translation: "¡Bienvenido {nombre de estudiente}!"
       Do not translate the placeholder string. You must use
       ``{student_name}`` exactly as is.

     Bad translation: "¡Bienvenido {student-name}!"
       Do not alter the placeholder string punctuation. You must use
       ``{student_name}`` exactly as is.

     Bad translation: "¡Bienvenido {Student_Name}!"
       Do not alter the placeholder string capitalization. You must use
       ``{student_name}``  exactly as is.

     Bad translation: "¡Bienvenido { student_name }!"
       Do not add additional spacing inside the {}. You must use
       ``{student_name}`` exactly as is.

   You can rearrange the order of these strings, depending on the requirements
   of the target language.

   For example, in English the name of the month precedes the day (January 23),
   while in Spanish, the day precedes the month (23 de enero).

   Example::

     String: "Today is {month} {day}."

     Good translation: "Hoy es {day} de {month}."


#. Do not alter or translate placeholder strings that begin with a ``%``, then
   have a string inside parenthesis, and then conclude with an 's' or 'd'. You
   must preserve the whole form.

   As in the previous example, you must not add, change, or remove punctuation,
   change capitalization, or add new spacing.

   Examples::

     String: "Welcome back %(student_name)s!"

     Good translation: "¡Bienvenido %(student_name)s!"

     Bad translation: "¡Bienvenido %(nombre de estudiente)s!"
       Do not translate placeholder strings. You must use ``%(student_name)s``
       exactly as is.

     Bad translation: "¡Bienvenido %(student-name)s!"
       Do not alter the placeholder string punctuation. You must use
       ``%(student_name)s ``exactly as is.

     Bad translation: "¡Bienvenido %(Student_Name)s!"
       Do not alter the placeholder string capitalization. You must use
       ``%(student_name)s ``exactly as is.

     Bad translation: "¡Bienvenido %( student_name )s!"
       Do not add additional spacing inside the (). You must use
       ``%(student_name)s`` exactly as is.

     Bad translation: "¡Bienvenido (student_name)!"
       Do not remove the '%' or 's'. You must use ``%(student_name)s`` exactly
       as is.

   You can rearrange the order of these strings, depending on the requirements
   of the target language. For example, in English the name of the month
   precedes the day (January 23), while in Spanish, the day precedes the month
   (23 de enero).

   Example::

     String: "Today is %(month)s %(day)d."

     Good translation: "Hoy es %(day)d de %(month)s."


#. Do not alter or translate placeholder strings that appear within a
   ``<%= %>`` block. Placeholder strings in this format look like this:
   ``<%= student_name %>``.

   As in the previous examples, you must not add, change, or remove
   punctuation, change capitalization, or add in new spacing.

   Examples::

     String: "Welcome back <%= student_name %>!"

     Good translation: "¡Bienvenido <%= student_name %>!"

     Bad translation: "¡Bienvenido <%= nombre de estudiente %>!"
       Do not translate placeholder strings. You must use
       ``<%= student_name %>`` exactly as is.

     Bad translation: "¡Bienvenido <%= student-name %>!" Do not alter the
       placeholder string punctuation from an underscore to a hyphen. You must
       use ``<%= student_name %>`` exactly as is.

     Bad translation: "¡Bienvenido <%= Student_Name %>!"
       Do not alter the placeholder string capitalization. You must use
       ``<%= student_name %>`` exactly as is.

     Bad translation: "¡Bienvenido < % =  student_name % >!"
       Do not add additional spacing inside the <%= %>. You must use
       ``<%= student_name %>`` exactly as is.

     Bad translation: "¡Bienvenido <student_name>!"
       Do not remove or change the ``<%=`` or ``%>``. You must use
       ``<%= student_name %>`` exactly as is.
