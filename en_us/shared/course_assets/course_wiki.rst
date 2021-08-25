.. _Course_Wiki:

########################
Using the Course Wiki
########################

Wikis provide a way for the course team and learners to access, share, and
collaboratively edit information both about, and for, your course.

.. contents::
   :depth: 1
   :local:

***********************
About the Course Wiki
***********************

Courses can optionally configure a wiki application and set it up for appropriate use in your course.
If you have specific expectations for how the wiki should be
used, communicate these expectations to your learners and staff. You can
:ref:`seed the wiki<Seeding the Wiki>` with specific content and provide a
skeleton structure and some exemplars. At the beginning of the course, explain
how you want the course wiki to be used, and provide clear instructions and
guidelines for its use.

Common uses for the course wiki might include the following activities.

* Sharing answers to course FAQs and collecting new FAQs.
* Sharing editable course information, such as download and installation
  instructions for software required for the course
* Providing shared access to learner-created resources, perhaps as part of a
  collaborative exercise.
* Sharing errata for the course.
* Collecting suggestions for future runs of the course.

As learners and course team members create and edit wiki articles, they
contribute to a repository of information about your course that can be
immediately useful to other learners, or useful for you and your course team as
you develop other courses or future runs of the same course.

The wiki for each course is a "child" wiki of the edX-wide wiki. From within
any course wiki, select the top level **Wiki** link in the breadcrumb trail
at the top of the page to visit the edX-wide wiki.

.. Some courses have linked wikis, which can be useful for course re-runs or for course series. You link a wiki with another course's wiki by...?

.. _Wikis Overview:

********************************
Managing the Course Wiki
********************************

Keep these points in mind as you design the wiki for your course.

* Be clear about the purpose for the wiki or for different parts of the wiki.
  For example, are some parts of the wiki only for disseminating information?
  If that is the case, then make sure that only your course team has write
  access for those articles.

* Decide whether some parts of the wiki are intended for learner collaboration
  or learner input. Make sure that learners are able to create and edit wiki
  articles in those sections, and use text to clearly indicate to learners that
  these pages can be edited.

* Think about the different tasks that will be performed by people in different
  roles. Typically you want your course team to have some privileges that
  learners do not have. For example, course team members can delete wiki
  articles, but learners cannot.

Members of the course team can perform these tasks to manage the wiki.

* :ref:`Show or Hide the Wiki<Showing or Hiding the Wiki>`
* :ref:`Control Wiki Access<Controlling Wiki Access>`
* :ref:`Seed the Wiki<Seeding the Wiki>`
* :ref:`Lock a Wiki Article<Locking a Wiki Article>`
* :ref:`Delete a Wiki Article<Deleting a Wiki Article>`
* :ref:`Purge a Wiki Article<Purging a Wiki Article>`
* :ref:`Restore a Deleted Wiki Article<Restoring a Deleted Wiki Article>`

All users, including learners, can perform the following tasks, depending on
the permissions that you set for an article.

* :ref:`Add a Wiki Article<Adding a Wiki Article>`
* :ref:`Edit a Wiki Article<Editing a Wiki Article>`
* :ref:`Manage Versions of a Wiki Article<Managing Versions of a Wiki Article>`
* :ref:`Search for Wiki Articles<Searching for Wiki Articles>`

.. _Showing or Hiding the Wiki:

********************************
Showing or Hiding the Wiki
********************************

To disable or enable the Wiki application, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Click the gear icon on the **Wiki** card shown on this page.
#. From the **Configure wiki** modal, select the toggle to enable or disable the **wiki**.
#. Select **Apply** to save your configuration changes.

When you hide the wiki in your course, any existing articles remain in the edX- wide wiki,
but the Wiki page is removed from your course pages.

.. In XML authoring, remove the `{"type": "wiki"}` entry in your `/policies/TERM/policy.json` file.

.. _Controlling Wiki Access:

********************************
Controlling Access to the Wiki
********************************

You can control access to the wiki in various ways: by changing access to the
wiki as a whole, by changing the read/write permissions settings of articles
within the wiki, or by locking articles.

To change access to the course wiki, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Click the gear icon on the **Wiki** card shown on this page.
#. From the **Configure wiki** modal, check or uncheck the toggle of the **Enable public wiki access** setting.
#. Select **Apply** to save your configuration changes.


The **Enable public wiki access** wiki setting is disabled by default, meaning that only course team members
and enrolled learners can see the course wiki. If you enable this setting, then any registered edX user
can access the course wiki, even if they are not enrolled in your course. However, public users would have
to explicitly navigate to your wiki via the edX-wide wiki structure, or a link that has been provided to them.

To modify viewing or editing permissions for specific groups of users by
article, see :ref:`Setting Permissions for Wiki Articles`.

To lock an article and prevent further editing, see :ref:`Locking
a Wiki Article`.

.. _Setting Permissions for Wiki Articles:

***************************************
Setting Permissions for Wiki Articles
***************************************

To prevent certain groups of users from being able to add or edit articles, you
need to modify the read/write permissions for articles. For example, as a
member of the course team, you likely want to prevent learners from creating
wiki articles at the top level, so you should remove write access to course-
level wiki articles for most users. (Top-level wiki articles are children of
the edX-wide wiki, and cannot be found within the course wiki).

To modify the permissions for wiki articles, follow these steps.

#. View the live version of your course.
#. Select **Wiki**.
#. Navigate to the article whose permissions you are modifying, and then select
   **Settings**.
#. In the **Permissions** section of the **Settings** page, select or clear the
   checkboxes for read or write access for **Group** or **Other**.
#. At the bottom of the page, select the **Save changes** button for the
   **Permissions** section.

Note that there are two different **Save changes** buttons, one near the top of
the page for the **Notifications** section, and one at the bottom of the page
for the **Permissions** section. If you are modifying permissions, make sure
you select the **Save changes** button at the bottom of the page for your
changes to be saved.

===============================
Groups Used in Wiki Permissions
===============================

Each course has the following groups.

    * Beta Testers (by default there are no beta testers until you add them)
    * Admins (by default, the course author is always in this group)
    * Staff (these are course team members)

You add users to these groups in the LMS by selecting **Instructor** and then
**Membership**.

The permissions for the **Others** group apply to users who are not in the
three course groups, including learners.

.. If permissions are unchanged from the default wiki, students can create articles at the course level (children of the edX-wide wiki). This is easy to do accidentally due to the prominence of the Add article button for the top level.

.. _Seeding the Wiki:

********************************
Seeding the Wiki
********************************

To ensure that learners get the most out of your course wiki, design the wiki
space before the course starts by seeding the course wiki with articles that
give it the desired structure.

For example, you could create wiki articles to mirror the course outline. At
the top level, you could provide a course outline, FAQs, and links to the main
articles for each section. In the child articles for each section, you could
provide information specific to the units and components in that section, and a
page for learners to share their feedback and experiences.

.. include:: ../../../shared/course_assets/wiki_tasks.rst

.. _Locking a Wiki Article:

********************************
Locking a Wiki Article
********************************

Locking a wiki article prevents further changes from being made to it. To lock
a wiki article either after you create it, or after you make specific edits,
follow these steps.

.. If you only lock an article without modifying the read/write permissions,
.. other users can still create wiki articles at the top level. They also appear
.. still to have an Edit button at the top level, but they get Permission Denied
.. when they click Edit.

#. View the live version of your course.
#. Select **Wiki**.
#. Navigate to the article you want to lock, and then select **Settings**.
#. In the **Permissions** section of the **Settings** page, select the **Lock
   article** checkbox.
#. At the bottom of the page, select the **Save changes** button for the
   **Permissions** section.

.. _Deleting a Wiki Article:

********************************
Deleting a Wiki Article
********************************

Only course team members can delete articles. In addition, you can only delete
an article if you have permissions to edit that article. If you have the
required permissions, you see a **Delete article** button at the bottom of the
**Edit** page.

To delete an article, follow these steps.

#. View the live version of your course.
#. Select **Wiki**.
#. Navigate to the article you want to delete, and then select **Edit**.
#. Select **Delete article**.
#. On the deletion confirmation page, select **Yes, I am sure**.
#. Optionally, also select the **Purge** checkbox. For details, see
   :ref:`Purging a Wiki Article`.
#. Select **Delete article** to confirm the deletion.


.. _Purging a Wiki Article:

========================
Purging a Wiki Article
========================

When you delete and purge an article, it is completely removed from the wiki,
with no option to undo the deletion. Select this option only if you are sure
you will not want to restore the content.

To purge an article as you delete it, select the **Purge** checkbox on the
deletion confirmation page.


.. _Restoring a Deleted Wiki Article:

=================================
Restoring a Deleted Wiki Article
=================================

Articles that have been deleted but not purged can be restored. A link to the
article remains visible at the level at which it was created.

To restore a deleted article, select the link to the article and select
**Restore**.
