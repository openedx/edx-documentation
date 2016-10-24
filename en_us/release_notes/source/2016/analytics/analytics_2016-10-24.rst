* For Insights, this release adds a **Course Home** link to the navigation bar
  on all course pages.

  The navigation bar before the change:

   .. image:: /Images/before_coursehome.png
    :width: 800
    :alt: An example of the navigation bar on the Enrollment page before the
        change. The bar contains a lens dropdown titled "Enrollment", an active
        link "Activity", an inactive link "Demographics", and an inactive link
        "Geography".

  The navigation bar after the change:

   .. image:: /Images/after_coursehome.png
    :width: 800
    :alt: An example of the navigation bar on the Enrollment page after the
        change. A new link titled "Course Home" at the beginning of the bar is
        highlighted followed by a lens dropdown titled "Enrollment", an active
        link "Activity", an inactive link "Demographics", and an inactive link
        "Geography".


* Two new SQL tables are now included in the data packages that edX prepares
  for partner organizations. These tables, ``student_courseaccessrole``  and
  ``django_comment_client_role_users``, contain data to identify the privilege
  levels, or roles, that individual users have for a course.

  * ``student_courseaccessrole`` lists the users who have a privileged role or
    roles for working in a course.
  *  ``django_comment_client_role_users`` identifies the privilege role for
     working in course discussions for every user enrolled in a course.

  For more information, see :ref:`data:Student_Info` in the *EdX Research
  Guide*. (:jira:`TNL-4154`)

