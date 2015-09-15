.. _LTI Component:

###############
LTI Component
###############

You can integrate remote learning tools, such as applications and textbooks,
into your course with the learning tools interoperability (LTI) component. The
LTI component is based on the `IMS Global Learning Tools Interoperability™ 
<http://www.imsglobal.org/LTI/v1p1p1/ltiIMGv1p1p1.html>`_ version 1.1.1
specifications.

You can use an LTI component in several ways.

* You can add remote LTI content that displays to learners only, and that does
  not require a learner response. An example is a digital copy of a textbook in
  a format other than PDF.

* You can add remote LTI tools that do require a learner response. A remote
  LTI tool provider grades the responses.

* You can use the LTI component as a placeholder for synchronizing with a
  remote grading system.

For example, the following LTI component integrates a Cerego tool that learners
interact with into the LMS for a course.

.. image:: ../../../shared/building_and_running_chapters/Images/LTIExample.png
   :alt: A page in the LMS showing the Cerego music player and a question for
    learners to answer about it.

When you add an LTI component to your course, the edX Learning Management
System (LMS) is the LTI tool consumer, and the external tool or content is the
LTI tool provider. 

Be sure to review all supplemental materials to assure that they are accessible
before making them available through your course. For more information, see
:ref:`Accessibility Best Practices for Course Content Development`.


.. Alison Make this link V available when you add new LTI section to open source - Alison 14 Sept 15

.. You can also integrate content from an edX course into a remote learning management system such as Canvas or Blackboard. For more information about how to use Studio as an LTI tool provider, see :ref:`TBD`.

.. _LTI Information:

************************
Obtain LTI Information
************************

Before you create an LTI component to integrate content from a remote tool
provider into a unit of your course, you need the following information.

-  If the LTI component requires a learner response that will be graded, the
   **launch URL** is required. You obtain the launch URL from the LTI tool
   provider. The launch URL is the URL that Studio sends to the remote LTI tool
   provider so that the tool provider can send back learners' grades.

- The **LTI Passports** policy key. This policy key has three parts: an LTI ID,
  a client key, and a client secret.

  -  The **LTI ID** is a value that you create to refer to the remote LTI
     tool provider. You should create an LTI ID that you can remember easily.

     The LTI ID can contain uppercase and lowercase alphanumeric characters, as
     well as underscore characters (_). It can be any length. For example, you
     can create an LTI ID that is as simple as ``test_lti_id``, or your LTI ID
     can be a string of numbers and letters such as  ``id_21441`` or
     ``book_lti_provider_from_new_york``.

  -  The **client key** is a sequence of characters that you obtain from the
     LTI tool provider. The client key is used for authentication and can
     contain any number of characters. For example, your client key might be
     ``b289378-f88d-2929-ctools.school.edu``.

  -  The **client secret** is a sequence of characters that you obtain from the
     LTI tool provider. The client secret is used for authentication and can
     contain any number of characters. For example, your client secret can be
     something as simple as ``secret``, or it might be a string of numbers and
     letters such as ``23746387264`` or ``yt4984yr8``.

  To create the **LTI Passports** policy key, combine the LTI ID, client key,
  and client secret in the following format (be sure to include the colons).

  ``{your_lti_id}:{client_key}:{client_secret}``

  An **LTI Passports** policy key can resemble any of the following examples.

  ``test_lti_id:b289378-f88d-2929-ctools.school.edu:secret``
  
  ``id_21441:b289378-f88d-2929-ctools.school.edu:23746387264``

  ``book_lti_provider_from_new_york:b289378-f88d-2929-ctools.company.com:yt4984yr8``

************************
Create an LTI Component
************************

To add an LTI component to your course, you complete all of these steps.

.. contents::
   :local:
   :depth: 1

======================================================
Step 1. Add LTI to the Advanced Module List Policy Key
======================================================

#. From the Studio **Settings** menu, select **Advanced Settings**.

#. In the **Advanced Module List** field, place your cursor between the
   brackets.

#. Enter ``"lti"``. Be sure to include the quotation marks, but not the period.
   The text in the **Advanced Module List** field should resemble the
   following.

   ``["lti"]``

   If the **Advanced Module List** field already contains text, place your
   cursor directly after the closing quotation mark for the final item, and
   then enter a comma followed by ``"lti"`` (again, make sure that you include
   the quotation marks).

   ``["word_cloud","lti"]``

4. At the bottom of the page, select **Save Changes**.

The page refreshes automatically and reformats your entry in the **Advanced
Module List** field. At the top of the page, a message notifies you that your
changes have been saved.

==========================================
Step 2. Register the External LTI Provider
==========================================

To register the remote LTI tool provider, you add the **LTI Passports** policy
key to the course's advanced settings.

#. From the Studio **Settings** menu, select **Advanced Settings**.

#. In the **LTI Passports** field, place your cursor between the
   brackets.

#. Enter your **LTI Passports** policy key surrounded by quotation marks.

   For example, the text in the **LTI Passports** field can resemble the
   following.

   ``"test_lti_id:b289378-f88d-2929-ctools.umich.edu:secret"``

   For more information about creating your key, see :ref:`LTI Information`.

#. To integrate tools from more than one LTI provider into your
   course, separate the policy key for each **LTI Passports** policy key with a
   comma. Make sure to surround each entry with quotation marks.

   .. code-block:: xml

      [
          "test_lti_id:b289378-f88d-2929-ctools.umich.edu:secret",
          "id_21441:b289378-f88d-2929-ctools.school.edu:23746387264",
          "book_lti_provider_from_new_york:b289378-f88d-2929-ctools.company.com:yt4984yr8"
      ] 

4. At the bottom of the page, select **Save Changes**.

The page refreshes automatically and reformats your entry in the **LTI
Passports** field. At the top of the page, you see a notification that your
changes have been saved.

==========================================
Step 3. Add the LTI Component to a Unit
==========================================

#. In the unit where you want to add the remote learning tool, from the **Add
   New Component** section select **Advanced**, and then select **LTI**.

#. In the component that appears, select **Edit**.

#. In the component editor, specify the settings that you want. For more
   information about each setting, see :ref:`LTI Component Settings`.

#. Select **Save**.
   
To test an LTI component, you use the Preview feature or view the live version
in the LMS. For more information, see :ref:`Testing Your Course Content`.

.. _LTI Component settings:

**********************
LTI Component Settings
**********************

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Setting
     - Description
   * - Accept grades past deadline
     - Specifies whether third party systems are allowed to post grades past
       the deadline. By default, this value is set to True.
   * - Button Text     
     - Enter a custom label for the button that launches the external LTI
       application.           
   * - Custom Parameters
     - Enables you to add one or more custom parameters. For example, if you
       add an e-book, you can set a custom parameter that opens the e-book to
       a specific page. You could also use a custom parameter to set the
       background color of the LTI component.

       Every custom parameter has a key and a value. You must add the key and
       value in the following format.

       {key}={value}

       An example custom parameter follows.

       ::

          bgcolor=red
          page=144

       To add a custom parameter, select **Add**.

   * - Display Name               
     - Specifies the name of the component. This name appears as a heading
       above the problem and as a tooltip in the learning sequence at the top
       of the **Courseware** page. Unique, descriptive display names help you
       identify problems quickly and accurately for analysis.
   * - Hide External Tool
     - Indicates whether you want to launch a remote tool or use this component
       as a placeholder for synchronizing with a remote grading system.

       If you set the value to True, Studio hides the **Launch** button and any
       IFrames for this component. By default, this value is set to False.

   * - LTI Application Information     
     - The description of the external application. If the application requires
       a username or email address, use this field to inform learners that
       their information will be forwarded to the external application.
   * - LTI ID     
     - Specifies the LTI ID for the remote LTI tool provider. This value must
       be the same LTI ID that you entered as part of the **LTI Passports**
       policy key on the **Advanced Settings** page.
   * - LTI URL 
     - Specifies the URL of the remote tool that this component launches. This
       setting is applicable when **Hide External Tool** is set to False.      
   * - Open in New Page
     - Specifies whether the component opens in a new page. If you set this
       value to True, when the learner selects this component the LTI content
       opens in a new window. If you set this value to False, the LTI content
       opens in an IFrame in the current page. This setting is applicable when
       **Hide External Tool** is set to False.
   * - Request user's email     
     - If **Open in New Page** is set to True, you can also request user
       information. Set this value to True to request the learner's email
       address.
   * - Request user's username     
     - If **Open in New Page** is set to True, you can also request user
       information. Set this value to True to request the learner's username.
   * - Scored     
     - Indicates whether the LTI component receives a numerical score from the
       remote LTI tool provider. By default, this value is set to False.       
   * - Weight
     - Specifies the number of points possible for a problem. By default, if
       a remote LTI tool provider grades the problem, the problem is worth 1
       point, and a learner's score can be any value between 0 and 1. This
       setting is applicable when **Scored** is set to True.

       For more information about problem weights and computing point scores,
       see :ref:`Problem Weight`.
