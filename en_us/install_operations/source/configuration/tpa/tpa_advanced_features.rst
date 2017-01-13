.. _Advanced Third Party Authentication Features:

############################################
Advanced Third Party Authentication Features
############################################

The Open edX Third Party Authentication feature offers many advanced
configuration options and integration points that can be used to customize the
sign in experience for learners using specific third party providers. None of
the following features are required for a typical installation, but they may be useful.

**********************
Skip Registration Form
**********************

When you configure an OAuth2 or SAML provider in the Django admin, there is a
boolean **Skip registration form** option for that provider. Normally, when a
new user signs in with an external provider, the information sent to Open edX is
only used to pre-fill the registration form. When **Skip registration form** is
enabled for a provider, the information sent to Open edX is also used to pre-
fill the registration form, but then the form is automatically submitted before
the user has a chance to see it. If the registration succeeds, the user will
immediately be signed in to their newly created account and can start learning
right away. However, if there is any error, such as no email address was
provided automatically (since email addresses are required) or the email
address of the student conflicts with another existing Open edX user account,
then the pre-filled registration form will still be displayed to the student,
along with an error message. The student can then fix the error and submit the
form to complete the registration process.


***********************
Skip Email Verification
***********************

When you configure an OAuth2 or SAML provider in the Django admin, there is a
boolean **Skip email verification** for that provider. Normally, all users are
required to verify their email address by clicking a link in the verification
email that gets automatically sent to the user upon registration. When this
option is selected, Open edX trusts that the email address provided by the
external authentication provider is correct.

If a user registering with a provider that has this option enabled, and the
user's email address matches the email address that was sent to Open edX by the
external provider, the user's email address will be marked as verified, and no
verification email will be required. (However, the email address sent by the
external provider is only used to pre-fill the registration form, and the user
has a chance to edit the email address on the registration form before creating
their account. If they edit their email address so that it no longer matches
the email address sent by the external provider, the user will still be
required to verify their email address as usual.)

.. _Hinted Sign In:

**************
Hinted Sign In
**************

When you link to Open edX, you can create "hinted links" that prompt the user
to sign in using a specific provider. For example, the following link
represents a typical link to an example course.

::

  https://courses.example.com/courses/course-v1:OrganizationX+Course101x+1T2016/courseware/3eddbb5919544c229d34b3175debc6d6/f9900289d2d0474096d20d23a1eeed81/

The following link represents a hinted link to the same course. At the end of
the URL, ``?tpa_hint=oa2-google-oauth2`` has been added.

::

  https://courses.example.com/courses/course-v1:OrganizationX+Course101x+1T2016/courseware/3eddbb5919544c229d34b3175debc6d6/f9900289d2d0474096d20d23a1eeed81/?tpa_hint=oa2-google-oauth2

When users select the typical link, they go to the sign in page. When they
select the hinted link, they receive a "Would you like to sign in using your
Google credentials?" prompt that includes a large button to use Google to sign
in, as well as a small button to use other sign in options.

The intended use case of this feature is for organizations that wish to provide
a link from an on-premise system (or a course in another LMS like Canvas) to a
course in Open edX. In that case, the organizations will want students to sign
in using the organizations' SAML providers. By using hinted links, the sign in
and/or registration process will be simpler for students, as they won't have to
select a sign in provider or enter a password.

To create a hinted link for an OAuth2 provider, append
``?tpa_hint=oa2-providername`` to any Open edX URL, where ``providername`` is
the "Backend Name" value from the "Provider Configuration (OAuth)" section of
the Open edX Django admin.

To create a hinted link for a SAML provider, append ``?tpa_hint=saml-idpslug``
to any Open edX URL, where ``idpslug`` is the "Idp slug" value from the
"Provider Configuration (SAML IdP)" section of the Open edX Django admin.

***************
Auto-enrollment
***************

Open edX has a feature that allows instructors, marketing teams, and others to
create links that automatically enroll students who click the link into a
specific course.

If you send users to ``{LMS base URL}/account/finish_auth`` and include
``course_id``, ``enrollment_action``, and optional ``course_mode`` and
``email_opt_in`` parameters, the system auto-enrolls the user in the
specified course.

For example, the following URL would auto-enroll the user who clicks this link
into the edX Demo course (that course's ID,
``course-v1:edX+DemoX+Demo_Course``, has been url-encoded as the value of the
``course_id`` parameter). If the user is not signed in, they must sign in or
register first, and then they will be auto-enrolled.

::

  https://courses.example.com/account/finish_auth?course_id=course-v1%3AedX%2BDemoX%2BDemo_Course&enrollment_action=enroll&email_opt_in=false

You can include the following parameters.

* ``enrollment_action``: This is required to trigger the auto-enrollment
  behavior. It must be set to either ``enroll`` (for free courses) or
  ``add_to_cart`` (for paid courses). If ``add_to_cart`` is used, the user will
  be directed to the shopping cart page rather than instantly enrolled.

* ``course_id``: This is required. The ID of the course to enroll the user in,
  or add to cart, etc. It must be URL-encoded.

* ``course_mode``: one of ``audit``, ``honor``, ``verified``, etc. Only applies
  if enrollment_action is ``enroll``. If it's not specified, and the course has
  more than one mode, the user will be sent to the "track selection" page where
  they can choose which track/mode to use. If ``honor`` or ``audit`` is
  specified, the user will be instantly enrolled. If any other mode is
  specified, the user will be sent to the payment/verification flow.

* ``email_opt_in``: Can be ``true`` or ``false``. If true, this indicates that
  the user has consented to receiving marketing emails from Open edX and the
  course partner.

This feature can also be combined with :ref:`hinted sign in<Hinted Sign In>`,
if you create a URL such as the following example.

::

  https://courses.example.com/account/finish_auth?course_id=course-v1%3AedX%2BDemoX%2BDemo_Course&enrollment_action=enroll&email_opt_in=false&tpa_hint=oa2-facebook

*******************
Secondary Providers
*******************

When you configure an OAuth2 or SAML provider in the Django admin, there is a
boolean option to mark the provider as a **Secondary** provider. Normally,
third party sign in providers are displayed on the Open edX sign in and
register pages. However, secondary providers are not displayed directly on the
sign in or register pages. Instead, users see a button that says "Use my
institution/campus credentials". Clicking that will bring up a separate menu
that lists all the secondary providers.

The intended use case of this feature is to keep the sign in/register page from
being cluttered with too many buttons.

***************************
SAML Attribute Requirements
***************************

When you integrate Open edX with a SAML provider, you can allow only some users
to sign in based on some criteria. For example, organizations may not want
alumni or guest users to be able to sign in to Open edX using their SAML
provider, even though those users have valid sign in credentials for the
organization.

Users can be filtered based on ``eduPersonEntitlement`` attributes (supported
out of the box), or other attributes (requires custom code). For details on how
this can be set up, refer to `this edx-code mailing list post
<https://groups.google.com/forum/m/#!topic/edx-code/VW-wP1dhTTk>`_.
