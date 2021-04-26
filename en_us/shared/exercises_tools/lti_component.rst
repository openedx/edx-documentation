.. include:: ../../../links/links.rst

.. _LTI Component:

###############
LTI Component
###############

.. note:: EdX offers full support for this tool.

You can integrate remote learning tools, such as applications and textbooks,
into your course with the learning tools interoperability (LTI) component. The
LTI component supports tools with the `LTI 1.1`_ and `LTI 1.3`_ specifications.
Additionally, the LTI 1.3 tools can use the following LTI Advantage extensions:
`Deep Linking`_ and `Assignments and Grades services`_.

.. contents::
   :local:
   :depth: 2

Before you make tools from an external site available through your course, be
sure to review the tools to ensure that they are accessible to people with
disabilities. For example, in addition to testing the LTI components that you
add to your course, you can ask third party providers to confirm that a tool is
accessible, and, if available, contact your on campus accessibility support
services for additional guidance. For more information, see :ref:`Accessibility
Best Practices for Course Content Development`.

*********************
Overview
*********************

You can use an LTI component in several ways.

* You can add remote LTI tools that display content only, and that do
  not require a learner response. An example is a digital copy of a textbook in
  a format other than PDF.

* You can add remote LTI tools that do require a learner response. A remote
  LTI tool provider grades the responses.

* You can use the LTI component as a placeholder for synchronizing with a
  remote grading system.

For example, the following LTI component integrates a Cerego tool that learners
interact with into the LMS for a course.

.. image:: ../../../shared/images/LTIExample.png
   :alt: A page in the LMS showing the Cerego music player and a question for
    learners to answer about it.

When you add an LTI component to your course, the edX Learning Management
System (LMS) is the LTI tool consumer, and the external tool or content is the
LTI tool provider.

Be sure to review all supplemental materials to ensure that they are accessible
before making them available through your course. For more information, see
:ref:`Accessibility Best Practices for Course Content Development`.

You can also integrate content from a course into a remote learning management
system such as Canvas or Blackboard.

.. only:: Partners

  For more information about how to use Studio as an LTI tool provider, see
  :ref:`partnercoursestaff:Using edX as an LTI Tool Provider`.

.. only:: Open_edX

  For more information about how to use Studio as an LTI tool provider, see
  :ref:`opencoursestaff:Using Open edX as an LTI Tool Provider`.

.. note the slightly different destination links ^. Alison 23 Nov 2015

.. _enable_lti_components:

******************************************
Enabling LTI Components for a Course
******************************************

Before you can add LTI components to your course, you must enable the LTI tool
in Studio.

To enable the LTI tool in Studio, add ``"lti_consumer"`` to the
**Advanced Module List** on the **Advanced Settings** page. For more
information, see :ref:`Enable Additional Exercises and Tools`.

.. note::
  The ``lti_consumer`` module replaces a previous version of the LTI component.
  The name of the module for the previous LTI component is ``lti`` and it may
  appear in the **Advanced Module List** for older courses.

  The ``lti_consumer`` module includes all of the functionality of the previous
  LTI component and it should be used for all new courses. Courses that include
  the previous LTI component will continue to work correctly, even if the
  ``lti`` module is no longer present in the **Advanced Module List**.


.. _Setting up a LTI 1.1 component:

*******************************
Setting up an LTI 1.1 component
*******************************

Some LTI 1.1 tools require users to provide authentication credentials. If the LTI
tool you are including in your course requires authentication, you must add an
LTI passport for that tool to your course configuration.

An LTI passport is a string of text that contains the authentication key and
shared secret for one LTI tool. A passport also contains the LTI ID for the
tool. When you add an LTI component to your course, assign it a matching LTI ID
so that it can use the LTI passport that it requires.

For more information about creating and registering LTI passports, see the
following sections.

.. contents::
   :local:
   :depth: 1

=========================================
Creating an LTI Passport String
=========================================

Each LTI passport includes three component text strings that are separated by
colon characters. The component strings are: the LTI ID, the client key, and
the client secret.

-  The **LTI ID** is a value that you create to refer to the remote LTI tool
   provider. You should create an LTI ID that you can remember easily.

   The LTI ID can contain uppercase and lowercase alphanumeric characters, as
   well as underscore characters (_). It can be any length. For example, you
   can create an LTI ID that is as simple as ``test_lti_id``, or your LTI ID
   can be a string of numbers and letters such as  ``id_21441`` or
   ``book_lti_provider_from_new_york``.

-  The **client key** is a sequence of characters that you obtain from the LTI
   tool provider. The client key is used for authentication and can contain any
   number of characters. For example, your client key might be
   ``b289378-f88d-2929-ctools.school.edu``.

-  The **client secret** is a sequence of characters that you obtain from the
   LTI tool provider. The client secret is used for authentication and can
   contain any number of characters. For example, your client secret can be
   something as simple as ``secret``, or it might be a string of numbers and
   letters such as ``23746387264`` or ``yt4984yr8``.

To create an LTI passport, combine the LTI ID, client key,
and client secret in the following format (be sure to include the colons).

``{your_lti_id}:{client_key}:{client_secret}``

The following example LTI passports show the format of the
passport string.

``test_lti_id:b289378-f88d-2929-ctools.school.edu:secret``

``id_21441:b289378-f88d-2929-ctools.school.edu:23746387264``

``book_lti_provider_from_new_york:b289378-f88d-2929-ctools.company.com:yt4984yr8``

.. _adding_an_lti_passport:

==================================================
Adding an LTI Passport to the Course Configuration
==================================================

To add an LTI passport for an LTI tool to the configuration for your course, follow these steps.

#. From the Studio **Settings** menu, select **Advanced Settings**.

#. In the **LTI Passports** field, place your cursor between the
   brackets.

#. Enter the LTI passport string surrounded by quotation marks.

   The following example shows an LTI passport string.

   ``"test_lti_id:b289378-f88d-2929-ctools.umich.edu:secret"``

   For more information about creating your key, see :ref:`Setting up a LTI 1.1 component`.

#. If you use more than one LTI provider in your course, separate each LTI
   passport string with commas. Make sure to surround each entry with quotation
   marks. The following example shows multiple LTI passports in the **LTI
   Passports** field.

   .. code-block:: json

      [
        "test_lti_id:b289378-f88d-2929-ctools.umich.edu:secret",
        "id_21441:b289378-f88d-2929-ctools.school.edu:23746387264",
        "book_lti_provider_from_new_york:b289378-f88d-2929-ctools.company.com:yt4984yr8"
      ]

#. Select **Save Changes**.

The page refreshes automatically, reformats your entry in the **LTI Passports**
field, and displays a notification that your changes have been saved.


=========================================
Adding an LTI Component to a Course Unit
=========================================

To add an LTI 1.1 component to a course unit, follow these steps.

#. If the LTI tool requires authentication, register the key and shared secret
   for the LTI tool in the configuration for your course. For more information
   about registering authentication credentials, see
   :ref:`Setting up a LTI 1.1 component`.

#. Edit the unit in which you want to add the remote LTI tool and select
   **Advanced** from the **Add New Component** section. Select **LTI
   Consumer**.

   If the **Advanced** component type is not available, make sure you have
   enabled LTI components. To do this, see :ref:`enable_lti_components`.

#. Select **Edit** in the component that appears.

#. In the **LTI Version** field, select **LTI 1.1/1.2**.

#. Configure the LTI component in the component editor. For more information
   about each setting, see :ref:`LTI Component settings`.

#. Select **Save**.

To test an LTI component, use the **Preview** feature or view the live version
in the LMS. For more information, see :ref:`Testing Your Course Content`.

.. _Setting up a LTI 1.3 component:

*******************************
Setting up an LTI 1.3 component
*******************************

To add an LTI 1.3 component to a course unit, follow these steps.

#. Edit the unit in which you want to add the remote LTI tool and select
   **Advanced** from the **Add New Component** section. Select **LTI
   Consumer**.

   If the **Advanced** component type is not available, make sure you have
   enabled LTI components. To do this, see :ref:`enable_lti_components`.

#. Select **Edit** in the component that appears.

#. In the **LTI Version** field, select **LTI 1.3**.

#. Enter the LTI 1.3 settings provided from your tool. For basic LTI 1.3
   tools, without LTI Advantage, you need to set the following settings:

   * **LTI 1.3 Tool Launch URL** (can also be called redirect url)
   * **LTI 1.3 OIDC URL** (can also be called login url)

   To enable *LTI Advantage* features, such as grades pass back and Deep Linking,
   you also need to set **LTI 1.3 Tool Public Key** with a key provided by the
   LTI tool. The key will look similar to this example:

   .. code-block:: bash

        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApAbQVx8FLXOflwvmV4dE
        merOO/C+syqDG7MniysYzbMm+egZ8Z3Dq0e2YuggZlRSHVtT9TpTu6BrP7GyWrhH
        7nOgCx5Rz+9g/B+KsasZ9x35bPjMeqNAu5aP3b0xgaRtnWec0h0a6T1L2xaQLuPS
        bDTJhABs0d22OYmdlMNN0+fWPmqxxAz8t7DBmjMMAmPLG4tjyEOwKCBlYCx0WELP
        Izg9bYA7MhCpHyD6+kTB51dbOA6lBbrIszCO9PBV4RD96LQWPs3YQ+DTqvPfLeTQ
        Q9XwiOe7yzsG1Ml+dkUODpZbuBk5Z9X486l36WbRWGBDWIWlsNE7M9Nl3eS42oS4
        IQIDAQAB
        -----END PUBLIC KEY-----

   You should paste the key from the tool directly into the configuration field.
   For more information about each setting, see :ref:`LTI Component settings`.

#. Select **Save**.

#. The Studio page will refresh and display LTI configuration required by the
   tool. Copy each of those values and follow the instructions provided by the
   tool to set them up.

   For basic LTI 1.3 launches, the following configuration values are required
   (they are provided by the LTI tool being set up):

   * **Client**
   * **Deployment ID**
   * **Keyset URL**
   * **OIDC Callback URL** (some tools refer to this as launch or redirect urls).

   For LTI Advantage, you'll also need to set **OAuth Token URL** (token/login url)
   in the tool.

.. note:: LTI 1.3 launches only work with published blocks, make sure the block is
          published before doing a launch.

.. _Enabling and using LTI Advantage features:

*****************************************
Enabling and using LTI Advantage features
*****************************************

LTI Advantage is an extension of the LTI 1.3 specification that enables additional
features in LTI components. See `LTI Advantage`_ for more imformation.

Currently, the platform supports the following LTI Advantage extensions:

* `Assignments and Grades services`_
* `Deep Linking`_


.. _Enabling LTI Assignments and Grades services:

============================================
Enabling LTI Assignments and Grades services
============================================

To set up LTI Assignments and Grades (LTI-AGS) services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-AGS functionality.

#. Select **Edit** in the component that appears.

#. Locate the **LTI Assignment and Grades Service** setting.

#. Select the operation mode of the Assignments and Grades services. You can disable
   the LTI-AGS service by selecting **Disabled** or pick one of the operation
   modes available: *declarative* to allow only one grade per problem, or *programmatic*
   to let the tool create many grades. For more information about each mode, read the
   corresponding entry on :ref:`LTI Component settings`.

#. Select **Save**.

.. _Enabling and using LTI Deep Linking:

===================================
Enabling and using LTI Deep Linking
===================================

To set up LTI Deep Linking (LTI-DL) services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-DL functionality.

#. Select **Edit** in the component that appears.

#. Locate the **Deep linking** setting and set it to **True** (enabled).

#. Locate the **LTI Advantage Deep Linking Launch URL** setting.

#. Retrieve the Deep Linking Launch url from the tool you're integrating with. If it's not
   provided, try using the same value as in the **LTI 1.3 Tool Launch URL**.

#. Select **Save**. The Studio page will refresh and show the updated details page.

To use LTI Deep Linking, follow these steps:

#. Ensure that LTI-DL is enabled by following the steps above.

#. Locate the unit and LTI component in Studio.

#. In the LTI component page in Studio, locate the **Deep Linking Launch - Configure tool**
   link and select it.

#. You'll be redirected to the Tool and presented with a page to select the options.

#. Once the configuration is complete, you'll be redirected back to the Studio and the
   Deep Linking setup will be complete.

#. The content you selected in the tool will be presented to your students in the LMS.

.. note:: LTI 1.3 launches only work with published blocks, make sure the block is
          published before doing a Deep Link Launch.

.. _LTI Component settings:

**********************
LTI Component Settings
**********************

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Setting
     - Description

   * - Display Name
     - Specifies the name of the component. This name appears as a heading
       above the problem. Unique, descriptive display names help you
       identify problems quickly and accurately for analysis.

   * - LTI Application Information
     - The description of the remote LTI application. If the application
       requires a username or email address, use this field to inform learners
       that their information will be forwarded to the external application.

   * - LTI Version
     - Used to select the LTI version used in for the current LTI component.

   * - LTI ID (LTI 1.1 only)
     - Specifies the LTI ID for the remote LTI tool provider. This value must
       match the LTI ID that you entered as part of the LTI passport string for
       the LTI tool. For more information about LTI passports, see :ref:`LTI
       Information`.

   * - LTI URL (LTI 1.1 only)
     - Specifies the URL of the remote LTI tool that this component launches.

   * - LTI 1.3 Tool Launch URL (LTI 1.3 only)
     - Specifies the URL of the remote LTI tool that this component launches.
       This is sometimes called *Redirect URL* in some tools.

   * - LTI 1.3 OIDC URL (LTI 1.3 only)
     - Specifies the URL of the login URL for the remote LTI tool for the
       authentication flow. This can also be called *Login URL* on some tools.

   * - LTI 1.3 Tool Public Key (LTI 1.3 only)
     - The LTI 1.3 Tool's public key. This is a string that starts with
       '-----BEGIN PUBLIC KEY-----' and is required so that the LMS can check if
       the messages and launch requests received have the signature from the tool.
       This is not required when doing LTI 1.3 Launches without LTI Advantage.

   * - Deep linking (LTI 1.3 only)
     - Toggle to enable or disable LTI Advantage Deep Linking. Select **True** if
       the tool supports this feature and you want to use it in this component.

   * - LTI Advantage Deep Linking Launch URL (LTI 1.3 only)
     - Specifies the URL of the remote LTI tool that this component uses to perform
       deep linking launches. If not specified by the tool, use the same URL as
       in **LTI 1.3 Tool Launch URL**.

   * - LTI Assignment and Grades Service (LTI 1.3 only)
     - Toggle to enable LTI Advantage Assignment and Grades services and set the
       grading model.

       Options are:

       * **Disabled** - LTI AGS service will be disabled. Use this for tools that
         don't send any grades back to the platform.

       * **Allow tools to submit grades only (declarative) (Default)** - the platform
         will enable LTI AGS and prepare a single grade container for problems to
         send grades back to. Use this for simple LTI problems.

       * **Allow tools to manage and submit grade (programmatic)** - The tool will have
         full control over the grading process, enabling it to create and edit one or
         more grade containers and manage the learner scores that will be reported
          to the LMS.

   * - Custom Parameters
     - Sends additional parameters that are required by the remote LTI tool.
       The parameters that you send depend on the specific LTI tool you are
       using.

       Supply a key and value for each custom parameter. The key is an
       identifier for the parameter. Use the following format.

       ``{key}={value}``

       For example, an LTI tool that displays an e-book might accept a ``page``
       parameter to control which page the e-book opens to by default. The
       following example sends a ``page`` parameter to an LTI tool.

       ::

          ["page=144"]

   * - LTI Launch Target
     - Controls the way that the course page will open and display the remote
       LTI tool.

       Options are:

       * **Inline** - the LTI tool will appear directly in the course page.

       * **Modal** - the LTI tool will appear in a separate display window in
         front of the course page. The modal display window prevents learners
         from interacting with the course page until they dismiss the LTI tool.

       * **New Window** - the LTI tool will appear in a new web browser window.
         Depending on the configuration of the web browser, it may appear in a
         new tab or in a separate browser window. Learners can interact with
         both the course page and the LTI tool.

   * - Button Text
     - Enter a custom label for the button that opens the external LTI tool.

   * - Inline Height
     - Specifies the on-screen height of the LTI tool in pixels.

       This setting is only applied if the **LTI Launch Target** is set to
       **Inline**.

   * - Modal Height
     - Specifies the on-screen height of the LTI content window as a percentage
       of the visible web browser window height. Enter the percentage in whole numbers.

       This setting is only applied if the **LTI Launch Target** control is set
       to **Modal**.

   * - Modal Width
     - Specifies the on-screen width of the LTI content window as a percentage
       of the web browser window width. Enter the percentage in whole numbers.

       This setting is only applied if the **LTI Launch Target** control is set
       to **Modal**.

   * - Scored
     - Indicates whether the LTI component receives a numerical score from the
       remote LTI tool provider. By default, this value is set to **False**.

   * - Weight
     - Specifies the number of points possible for a problem. By default, if a
       remote LTI tool provider grades the problem, the problem is worth one
       point, and a learner's score can be any value between zero and one.

       This setting is only applied if **Scored** is set to **True**.

       For more information about problem weights and computing point scores,
       see :ref:`Problem Weight`.

   * - Hide External Tool
     - Controls whether the LTI component will display the remote LTI tool on
       the course page.

       Set the value to **True** to prevent the course page from displaying the
       remote LTI tool. For example, you might use an LTI component to
       synchronize with a remote grading system. In that situation, the LTI
       component should not appear on the course page.

       Set the value to **False** to display the remote LTI tool and allow
       learners to interact with it.

   * - Accept grades past deadline
     - Specifies whether third party systems are allowed to post grades after
       the deadline. By default, this value is set to **True**.

   * - Request user's email
     - Sends the learner's email address to the remote LTI tool.

       An LTI component will only send learners' email addresses if the **LTI
       Launch Target** control is set to **New Window**. When the new window
       launches, the learners are warned that if they continue, their email
       address will be shared with the LTI provider.


       By default, this setting is not available in Studio.

       .. only:: Partners

         To make this setting available, contact your edX partner manager.

       .. only:: Open_edX

         To make this setting available, a system administrator must enable the
         setting in the Django administration console.

   * - Request user's username
     - Sends the learner's username to the remote LTI tool. This is the
       username that the learner used to register for the course.

       An LTI component will only send learners' usernames if the **LTI Launch
       Target** control is set to **New Window**. When the new window
       launches, the learners are warned that if they continue, their username
       will be shared with the LTI provider.

       By default, this setting is not available in Studio.

       .. only:: Partners

         To make this setting available, contact your edX partner manager.

       .. only:: Open_edX

         To make this setting available in Studio, a system administrator must
         enable the setting in the Django administration console.
