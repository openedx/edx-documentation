.. _Enable Badging:

##################
Enabling Badging
##################

This topic describes how to enable and configure badging in your instance of
Open edX.

.. note:: Before proceeding, make sure you have read :ref:`Guidelines for
   Updating the Open edX Platform`.

.. contents::
   :local:
   :depth: 1

.. _Badges Overview:

*********
Overview
*********

Badges provide a way for learners to share their course achievements. For
courses that have course completion badges enabled, learners receive a badge at
the same time that they receive a course certificate, and have the option of
sharing their badges to a badging site such as Mozilla Backpack. For more
information, see :ref:`Course Completion Badges`.

In addition to badges that are awarded for completing single courses, you can
also issue badges for various cross-course events. For example, you can create
badges to be awarded when any of the following events occur.

* A learner enrolls in a certain number of courses.
* A learner receives a completion certificate for a certain number of courses.
* A learner receives a completion certificate for every course in a specified
  list of courses.

For more information, see :ref:`Course Event Badges`.

By default, Open edX supports Open Badges (http://openbadges.org/), an open
standard originally developed by the Mozilla Foundation. Open Badges provides a
badge generator called Badgr Server, which is used by default in Open edX.

You can use a badge generator other than Badgr Server. For information, see
:ref:`Specify a Badge Generator Other Than Badgr Server`.

For information about creating custom badges, see :ref:`Create New Badges`.

.. _Badging Prerequisites:

***************
Prerequisites
***************

Setting up the badges feature on your instance of Open edX involves performing
the set up and configuration tasks that are described in the topics below.

.. contents::
   :local:
   :depth: 1

.. _Make Sure Certificates are Enabled:

=======================================
Make Sure Certificates Are Enabled
=======================================

Badge generation depends on certificate generation. Badges for course
completion are automatically generated when a course certificate is generated
for a learner. Make sure certificates are enabled on your Open edX instance.
For information, see :ref:`Enable Certificates`.

.. _Specify a Badge Generator:

=========================
Specify a Badge Generator
=========================

By default, Open edX uses Badgr Server as the badge generator. If you do not use
Badgr Server, you can configure a different badge generator.

* To use Badgr Server register an Issuer App at https://badgr.org/app-developers/#issuer-apps
  or :ref:`Install Badgr Server` and :ref:`Specify a Badge Issuer`.

* To use a different badge generator, see :ref:`Specify a Badge Generator
  Other Than Badgr Server`.


.. _Install Badgr Server:

++++++++++++++++++++
Install Badgr Server
++++++++++++++++++++

Badgr Server provides an API for issuing Open Badges. Follow the instructions
at https://github.com/concentricsky/badgr-server to install and run Badgr
Server.

.. important:: You must install Badgr Server at a publicly accessible IP
   address, to allow the Open edX LMS and services such as Mozilla Backpack to
   contact Badgr Server.

If you do not use Badgr Server, you can configure a different badge generator.
See :ref:`Specify a Badge Generator Other Than Badgr Server`.

.. _Specify a Badge Issuer:

+++++++++++++++++++++++++++++++++++++++++++++
Specify a Badge Issuer for Your Organization
+++++++++++++++++++++++++++++++++++++++++++++

.. note:: This step is required only if you use Badgr Server for your badge
   generator.

If you are using Badgr Server, log in to your installation of Badgr
Server and add an issuer of Open Badges for your organization.

For more information about issuing Open Badges, see the `Issuing Badges`_ topic
on the Mozilla wiki.


.. _Specify a Badge Generator Other Than Badgr Server:

+++++++++++++++++++++++++++++++++++++++++++++++++++
Specify a Badge Generator Other Than Badgr Server
+++++++++++++++++++++++++++++++++++++++++++++++++++

By default, Open edX uses Badgr Server as the badge generator. To use Badgr
Server, see :ref:`Install Badgr Server` and :ref:`Specify a Badge Issuer`.

To specify a different badge generator, follow these steps.

.. note:: Because the services and software used for badge generation can differ
   significantly, the steps described in this topic are intended as guidelines
   and not as exact procedures.

#. Add the BadgingBackend object as a subclass to
   ``lms/djangoapps/badges/backends/base.py``.

   A BadgingBackend object must include the ``award`` function

   ``award(badge_class, user_id, evidence_url=None)``

   where

   * ``badge_class`` is the definition of the badge class for which the
     BadgeAssertion is created,

   * ``user_id`` is an ID for the user that the BadgeAssertion is to be created
     for, and

   * ``evidence_url`` is an optional URL for the location where the badge
     evidence can be viewed.

   The ``award`` function is responsible for the server awarding a badge to a
   learner. It is also responsible for all checks leading up to the awarding of
   the badge, including making sure the badge specification does not already
   exist on the target before creating a new badge specification.

   The ``award`` function should either return a BadgeAssertion object or raise
   an exception if the award cannot be given. By default, a base badge
   generation object called ``BadgeBackend`` exists, and contains a dummy
   version of the ``award`` function.

   .. code-block:: python

    class BadgeBackend(object):
        """
        Defines the interface for badge generators.
        """
        __metaclass__ = ABCMeta

        @abstractmethod
        def award(self, badge_class, user, evidence_url=None):
        """
        Create a badge assertion for the user using this badge generator.
        """

#. In the BadgeAssertion object that is generated by the ``award`` function, make
   sure the ``backend`` value is the name of the BadgingBackend subclass.

   .. code-block:: python

    class BadgeAssertion(models.Model):
        """
        Tracks badges on our side of the badge baking transaction
        """
        user = models.ForeignKey(User)
        badge_class = models.ForeignKey(BadgeClass)
        data = JSONField()
        backend = models.CharField(max_length=50)
        image_url = models.URLField()
        assertion_url = models.URLField(

#. In the ``lms.yml`` and ``studio.yml`` files, set the value of
   ``BADGING_BACKEND`` as a dot-separated python path specification to the
   object that you use to create and assign badges.

#. When you have finished modifying your configuration files for the badge
   generator, restart the Studio and Learning Management System processes so
   that the updated environment configurations are loaded.


.. _Enable Badges in Studio and LMS:

*****************************************************************
Enable Badges in Studio and the Learning Management System
*****************************************************************

To enable badges, you modify the ``lms.yml`` and ``studio.yml`` files,
which are located one level above the ``edx-platform`` directory.

#. In the ``lms.yml`` and ``studio.yml`` files, in the FEATURES
   section, set the value of ``ENABLE_OPENBADGES``  to ``True``.

   .. code-block:: none

     # Enable OpenBadge support.
     'ENABLE_OPENBADGES': True,

#. In ``lms.yml``, set the values for the following parameters.

   * ``BADGR_USERNAME``: The username connected to your Issuer App in Badgr.org
     or in your installation of Badgr Server. This will be used to create OAuth2 tokens.

   * ``BADGR_PASSWORD``: The password connected to your Issuer App in Badgr.org
     or in your installation of Badgr Server. This will be used to create OAuth2 tokens.

   * ``BADGR_TOKENS_CACHE_KEY``: The cache key for Badgr API tokens. Once created,
     the tokens will be stored in cache and can be retrieved using this key.

   * ``BADGR_BASE_URL``: A string containing the base URL for Badgr Server.
     If you are running your own installation, the Badgr Server must be installed
     at a publicly accessible IP address. If you have registered an Issuer App
     with Badgr.org, this will be provided for you.

   * ``BADGR_ISSUER_SLUG``: A string that is the slug for the Badgr issuer.
     The slug can be obtained from the URL of the Badgr Server page that
     displays the issuer. For example, in the URL
     ``http://exampleserver.com/issuer/test-issuer``, the issuer slug is
     ``test-issuer``.

     .. code-block:: none

       ############## Badgr OpenBadges generation ##############

       BADGR_USERNAME = "example@example.com"
       BADGR_PASSWORD = "password"
       BADGR_TOKENS_CACHE_KEY = "secret-test-cache-key"
       # Do not add the trailing slash here.
       BADGR_BASE_URL = "http://localhost:8005"
       BADGR_ISSUER_SLUG = "test-issuer"

#. Save the ``lms.yml`` and ``studio.yml`` files.

#. Run database migrations.

#. Restart the Studio and Learning Management System processes so that the
   updated environment configurations are loaded.


.. _Enable Badges For a Course:

*****************************************
Enable Badges Within Each Course
*****************************************

The ability to issue course completion badges is enabled by default for all
courses, but can be turned off or on again using an advanced setting in
Studio. For information, see :ref:`opencoursestaff:Enable Badges in Course` in
*Building and Running an Open edX Course*.

.. note:: The course-level setting to enable badges does not affect badges that
   are issued for completing or enrolling in multiple courses.


.. _Badge Types:

*******************************************
Configure Badges for Your Open edX Instance
*******************************************

You can configure several types of badges to issue to learners in your Open edX
instance.

.. contents::
   :local:
   :depth: 1

In addition, you can use the badging framework to create custom badges. For
information, see :ref:`About Creating New Badges`.

.. _Course Completion Badges:

========================
Course Completion Badges
========================

For courses that have badges enabled, learners receive a course completion
badge at the same time as they receive a course certificate, and have the
option of sharing their badges to a badging site such as Mozilla Backpack.

You can configure a different course completion badge for each course mode that
you support (for example, "professional", "advanced", or "basic"). You can also
specify a different badge image for each of the badges that you configure. For
information, see :ref:`Enable Badges For a Course` and :ref:`Create Course
Completion Badges`.


.. _Course Event Badges:

========================
Course Event Badges
========================

Course event badges are awarded across courses, and can be awarded when any of
the following events occur.

* A learner enrolls in a certain number of courses.
* A learner receives a completion certificate for a certain number of courses.
* A learner receives a completion certificate for every course in a specified
  list of courses.

You can customize these course event badges with your parameters and badge
images. For information, see :ref:`Create Course Event Badges`.


.. _Create Course Completion Badges:

**********************************************************
Create Course Completion Badges for Your Open edX Instance
**********************************************************

.. important:: Default images are supplied in Open edX for course completion
   badges. Be sure to replace these default badge images with your
   organization's own badge images before any badges are issued. When the first
   badge is issued for a given course, badge images are uploaded to Badgr
   Server. All badges issued in future for this course will use this uploaded
   original badge image, even if you subsequently change badge images in the
   Django Administration badge image configuration.

#. Access the Django Administration website for your instance of Open edX. To
   do this, go to ``https://<host name of your Open edX instance>/admin``. For
   example, this might be ``https://YourOrganization.org/admin``.

#. Select **Site Administration** > **Badges** > **Course complete image
   configurations**, and then define a course complete image configuration for
   each course mode on your platform for which you want to issue badges upon
   course completion. Examples of course modes are "professional" or "advanced"
   or "basic".

#. For each course complete badge image configuration, set these parameters.

   * Mode: The course mode for which the badge image should be used.
   * Icon: The badge image to use for the specified course mode.

   .. important:: Be sure to replace the default badge images with your
      organization's own badge images before any badges are issued.

#. Optionally, you can define a badge image that will be used as the default
   badge image for any course modes that do not have an explicitly specified
   badge image.

   To do so, in the course complete image configuration that references the
   image you want to use as a default, select the **Default** checkbox. After
   you save the configuration, this badge image is used for any course
   completion badge configurations that do not have a badge image explicitly
   specified.

   .. note:: You can specify only one default badge image.

#. Save each configuration parameter and exit the Django Administration
   website.


.. _Create Course Event Badges:

*******************************************************
Create Course Event Badges for Your Open edX Instance
*******************************************************

Open edX provides several customizable course event badges that can be awarded
when any of the following events occur.

* A learner enrolls in a certain number of courses.
* A learner receives a completion certificate for a certain number of courses.
* A learner receives a completion certificate for every course in a specified
  list of courses.

Before course event badges can be awarded, you must customize them with your
parameters and badge images. To customize any of the course event badges, follow
these steps.

.. note:: You can also use the badging framework to create custom badges. For
   information, see :ref:`About Creating New Badges`.

#. Access the Django Administration website for your instance of Open edX. To
   do this, go to ``https://<host name of your Open edX instance>/admin``. For
   example, this might be ``https://YourOrganization.org/admin``

#. Select **Site Administration** > **Badges** > **Badge Classes**.

#. Add a badge class for each course event for which you want to issue badges.
   Examples of course events might be enrolling in five courses, or completing
   three required courses.

#. For each badge class, set the following parameters.

   * Slug: A unique identifier that you choose to identify the badge class. This
     identifier can contain only numbers, lowercase letters, underscores, or
     hyphens. The slug, combined with the Issuing Component value, uniquely
     identifies a badge.

   * Issuing Component: Identifies the part of the platform that is issuing the
     badge. This identifier can contain only numbers, lowercase
     letters,underscores, or hyphens. For the three customizable course event
     badges that are included in the Open edX platform, the value for **Issuing
     Component** must be ``openedx__course`` (with two underscores). For
     :ref:`course completion badges<Course Completion Badges>` that are included
     in the Open edX platform, the issuing component value should be empty.

     For new badge types that you create, specify an
     **Issuing Component** value that identifies the software component
     responsible for issuing the badge. For example, if badges are issued by the
     course management component, you might define **Issuing Component** as
     ``platform__course``; if badges are issued based on activity in course
     discussions, you might define **Issuing Component** as
     ``platform__discussions``.

   * Display name: The human readable badge name that is used when badges are
     shown to learners, for example, in the Accomplishments view of learners'
     profiles.

   * Course ID: This value should be blank for course event type badges, as
     they are not associated with a single course.

   * Description: A description of this badge.
   * Criteria: A description of the criteria for awarding this badge.

   * Mode: The course mode for the course associated with this badge, if
     applicable.

   * Image: The badge image to use for this badge. Badge images should be
     square .png files less than 250KB in size.

   An example of a badge class configuration might have the following values.

   * ``slug``: ``enrolled_three``
   * ``issuing_component``: ``openedx__course``
   * ``display_name``: Enroll in Three Courses
   * ``description``: Enrolled in three courses
   * ``criteria``: A learner must enroll in three courses to receive this badge
   * ``image``: triple_enrollment_badge_image.png

#. When you have finished defining the badge class, select **Save**.

#. Next, you create a new course event badge configuration that defines all of
   the course event badges that you want to issue. Select **Site
   Administration** > **Badges** > **Course event badges configurations** >
   **Add course event badges configuration**.

   .. important:: You can create more than one course event badge configuration,
      but you can only mark one configuration as **Enabled**. Only the most
      recently activated course event badge configuration is used.

#. Within the new course event badge configuration, set the following
   parameters.

   * Courses completed: Define badges to be awarded for completing a certain
     number of courses, or completion of specific courses. Define one badge
     per line. On each line, enter the number of courses that must be completed,
     followed by a comma and then the slug of the badge class to associate
     with this badge.

     For example, to configure two badges, one that is awarded when a learner
     completes 3 courses, and another that is awarded when a learner completes
     8 courses, you add two lines to the **Courses completed** field.

     ``3,completed_three``
     ``8,completed_eight``

     where ``completed_three`` and ``completed_eight`` are badge slugs that
     you previously defined in badge classes.

   * Courses enrolled: Define badges to be awarded for enrolling in a certain
     number of courses, or enrolling in specific courses. Define one badge per
     line. On each line, enter the number of courses that must be enrolled in,
     followed by a comma and then the slug of the badge class to associate
     with this badge.

     For example, to configure a badge that is awarded when a learner enrolls in
     5 courses, you add this definition.

     ``5,enrolled_five``

     where ``enrolled_five`` is a badge slug that you previously defined in a
     badge class.

   * Course groups: Define badges to be awarded for completing a list of
     specific courses. Define one badge per line. On each line, enter the slug
     of the badge class, a comma, then the list of course keys.

     For example, to configure a badge that is awarded when a learner completes
     the 3 prerequisite courses in a series, you add this definition.

     ``prereq_computerscience_badge_slug,course1_identifier,course2_identifier,course_3_identifier``

     where ``prereq_computerscience_badge_slug`` is a badge slug that you
     previously defined in a badge class, and ``course1_identifier``,
     ``course2_identifier``, and ``course3_identifier`` are the Course IDs for
     the three courses that must be completed for this badge.

#. When you have finished defining badges in the configuration, select **Save**.

#. To activate this configuration, select **Enabled** at the top of the
   configuration page.

.. important:: You can create more than one course event badge configuration,
   but you can only mark one configuration as **Enabled**. Only the most
   recently activated course event badge configuration is used.


.. _About Creating New Badges:

**********************************************
Creating New Badges for Your Open edX Instance
**********************************************

In addition to using the default customizable badges that are provided with the
Open edX platform, you can design new badges that are generated when a
particular XBlock-related or course-related action occurs.

Before you create new badges, you should understand the following concepts.

* Badge Class - The specification of the badge that is to be awarded.
  Parameters for badge classes are described in Step 4 of the :ref:`Create
  Course Event Badges` topic.

* Slug - This field in the BadgeClass model uniquely identifies the badge
  class.

* Issuing Component - This field in the BadgeClass model identifies the part
  of the software that is issuing the badge. For example, the name of the
  XBlock where the occurrence of some event triggers the awarding of a badge.

  For the customizable :ref:`course event badges<Course Event Badges>` that are
  included with the Open edX platform, the value for ``issuing_component`` must
  be ``openedx__course`` (with two underscores). For :ref:`course completion
  badges<Course Completion Badges>` that are included in the Open edX platform,
  the issuing component value should be empty.

  For new badge types that you create, specify an **Issuing Component** value
  that identifies the software component responsible for issuing the badge. For
  example, if badges are issued by the course management component, you might
  define **Issuing Component** as ``platform__course``; if badges are issued
  based on activity in course discussions, you might define **Issuing
  Component** as ``platform__discussions``.

* The combination of badge slug, issuing component, and optionally, course ID
  uniquely identifies an awarded badge.

* Award method - The ``award`` function on the Badge Class instantiates the
  badge generator and calls the badge generator's ``award`` function, which is
  responsible for awarding a badge to a learner, as well as for performing all
  checks leading up to the awarding of the badge. On the Badge Class, the
  ``award`` function either returns a BadgeAssertion object or raises an
  exception if the award cannot be given.

* Badge Assertion - A specific generated instance of a badge that a
  learner has been awarded. Badge assertions contain data about the learner
  who earned the badge, and the date and time that the badge was awarded.
  Multiple badge assertions can be awarded for a specific BadgeClass,
  including to the same learner. You can get all assertions for a particular
  learner for a specific BadgeClass using the ``get_for_user`` method, using
  ``user`` as an argument.

For instructions for creating new badges, see :ref:`Create New Badges`.


.. _Create New Badges:

============================================
Create New Badges for Your Open edX Instance
============================================

To create new badges for use within your Open edX platform, follow these steps.

#. Create a Badge Class specifying the details of the badge you want to award.
   You can do this using the ``get_badge_class`` method from the ``badges``
   app, or create a badge class in Django Admin. For Django Admin
   instructions, see steps 1-5 in :ref:`Create Course Event Badges`.

   ``BadgeClass.get_badge_class`` creates the requested badge class if one does
   not already exist that has the same combination of ``slug`` and
   ``issuing_component``. Badge classes are uniquely identified by a
   combination of their ``slug`` and ``issuing_component`` fields, and
   optionally also the ``course_id`` field if a badge is associated with an
   individual course.

   If a badge class already exists with the same combination of ``slug`` and
   ``issuing_component`` that is in the request, the existing badge is returned.
   No new badge class is created, and no changes are made to the values of the
   existing badge class.

#. In the XBlock or component where badges are to be awarded based on some
   event occurring, add declarations to the ``badging`` and ``user`` services.

   The following example illustrates creating a badge class and awarding it
   from an XBlock.

   .. code-block:: python

    from xblock import XBlock
    from xblock.fragment import Fragment
    import pkg_resources

    @XBlock.wants('badging')
    @XBlock.wants('user')
    class AwardBlock(XBlock):
    """
    A Block that awards a badge when a learner visits it.
    """
    def award_badge(self, user_service, badge_service):
         user = user_service.get_current_user()
         badge_class = badge_service.get_badge_class(
             slug='general_award', issuing_component='my_org__award_block',
             description="A shiny badge, given to anyone who finds it!",
             criteria="Visit a page with an award block.",
             # This attribute not available in all runtimes,
             # but if we have both of these services, it's a safe bet we're in the LMS.
             course_id=self.runtime.course_id,
             # The path to this file should be somewhere relative to your XBlock's package.
             image_file_handle=pkg_resources.get_resource_stream(__name__, 'badge_images/award.png')
             # Badge image should be a square PNG file less than 250KB in size.
         )
         # Award the badge.
         if not badge_class.get_for_user(user):
             badge_class.award(user)

    def student_view(self, context=None):
        """
        Displayed to the learner when they visit.
        """
        # If the user and badge services are not present, we cannot award the badge.
        # If they are, we are ready to award one.
        user_service = self.runtime.service(self, 'user')
        badge_service = self.runtime.service(self, 'badging')
        if user_service and badge_service:
            self.award_badge(user_service, badge_service)
        return Fragment(u"<div><p>You just earned a badge!</p></div>")

.. _Get Badge Assertions Info:

============================================
Get Information about Badge Assertions
============================================

Depending on the type of badge you have created and are awarding, you might
want to limit the number of times that a learner can receive a badge. You can
find whether a specific learner has already received a particular badge in
either of the following ways.

* Use ``badge_class.assertions_for_user`` with ``user`` as an argument, to
  return a list of all assertions that the specified user has received for the
  badge class.

* Use the Badges API GET method to return a list of assertions for a particular
  username. For example, use ``GET /api/badges/v1/assertions/user/{username}/``.


For more information and additional parameters, see :ref:`Badges API Endpoints`.


.. _Badges API Endpoints:

=============================
Supported Badges API Endpoint
=============================

The Badges API supports the endpoint
``GET /api/badges/v1/assertions/user/{username}/``. You can use the following
query parameters with this endpoint.

.. note:: All of these query parameters are optional.

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Parameters
     - Description
   * - slug
     - If used, filters by the badge class identified by this slug. Unless
       ``issuing component`` is also specified, assumes a null/empty issuing
       component.
   * - issuing component
     - If used, also requires ``slug`` to be specified. Filters by the badge
       class.
   * - courseid
     - If used, returns only badge assertions that were awarded as part of the
       specific course.

For example, to get a list of badge assertions issued for a badge with an
``issuing_component`` value of ``openedx__course`` and a ``slug`` value of
``enroll_in_three_courses``, the query would be

.. code-block:: none

   {openedx domain}/api/badges/v1/assertions/user/?issuing_component=openedx__course&slug=enroll_in_three_courses

where ``<openedx_instance>`` is the site URL for your Open edX instance.

Possible query results are as follows.

*     200 on success, with a list of badge assertions.

*     403 if a user who does not have permission to masquerade as another user
      specifies a username other than their own.

*     404 if the specified user, badge class, or course does not exist.


.. include:: ../../../links/links.rst
