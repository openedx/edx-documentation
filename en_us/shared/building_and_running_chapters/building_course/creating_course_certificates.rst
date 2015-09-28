.. _Setting Up Course Certificates:

################################
Setting Up Course Certificates
################################

.. This file is now for partners and open edx, with differences in conditions

This section describes how to configure certificates for your course in
Studio.

.. contents::
   :local:
   :depth: 1

.. _Overview:
  
***********
Overview
***********

Using Studio, you create certificates that learners can earn in your
course. 

.. Course start date not published for partners at this time, pending review.

.. only:: Open_edX

    ***********************************
    Certificates and Course Start Dates
    ***********************************

    If your course is configured to issue certificates, you cannot start the
    course until the required certificates are :ref:`activated<Activate a
    Certificate>`.

    For information on starting the course, see :ref:`Determine Start and End
    Dates`.

**********************
Certificate Design
**********************

.. only:: Open_edX

  The design of certificates for your course, including your institution's
  logo, are configured on your instance of Open edX. For more information, see
  `Configuring Certificates`_ in *Installing, Configuring, and Running the
  Open edX Platform*.

.. only:: Partners

  The design of certificates for your course, including your institution's
  logo, are configured on edx.org by edX.  Contact your Partner Manager for
  more information.


*******************
Enable Certificates
*******************

Before you can create certificates, you must enable certificates for your
course.

#. From the **Settings** menu, select **Advanced Settings**.

#. In the **Certificate Web/HTML View Enabled** field, enter ``true``.

#. At the bottom of the page, select **Save Changes**.


*********************
Create a Certificate
*********************

You create one certificate for each course mode, or track. For example, if your
course has an "honor code" track and a "verified track", you must create two
certificates. 

To create a certificate for your course, follow these steps.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, select **Add your first certificate** or **Add a
   new certificate**.

#. Optionally, specify an alternative course title to use on the certificate
   instead of the official course title. You might want to use a different
   title on your course certificates if, for example, the official course
   name is too long to fit well on the certificate.

#. Add a signatory for each person associated with the course or organization
   whose name and title you want to appear on the certificate, up to a maximum
   of four signatories. You must specify at least one signatory.

.. only:: Partners

   5. For verified certificates, you must upload an image file showing the
      signature of each signatory.

      The image file must be a transparent .PNG file, 450px by 150px.

.. only:: Open_edX

   5. Optionally, upload an image file showing the signature of each signatory.
      
      The image file must be a transparent .PNG file, 450px by 150px.
      

6. When you have finished creating your certificate, select **Create**.

   You can :ref:`preview the certificate<Preview a Certificate>` to see how it
   will appear to a learner taking the course in the selected mode.

   Your course certificate is not available for issuing to learners until it is
   :ref:`activated<Activate a Certificate>`.


.. _Edit a Certificate:

********************
Edit a Certificate
********************

You can edit a certificate before it is activated. 

.. only:: Open_edX

  After a certificate is activated, only a course team member with the Admin
  role can edit the certificate. As a best practice, the administrator should
  `deactivate <Deactivate a Certificate>`_ the certificate before making edits.

.. only:: Partners

  Contact your edX Partner Manager if you need to edit an activated
  certificate.

.. caution:: 
  As a best practice, do not make changes to certificates in a running course
  if it is possible that certificates have already been issued to learners,
  because different learners might be awarded certificates with different
  details for the same course.

To edit a certificate, follow these steps.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, at the top right corner of the certificate
   form, select the **Edit** icon.

#. When you have finished editing the certificate, select
   **Save**.

   After you save your changes, you can :ref:`preview the certificate<Preview
   a Certificate>` to make sure it appears as you want it to. You then need to
   :ref:`activate the certificate configuration<Activate a Certificate>`
   before certificates can be issued.


.. _Delete a Certificate:

***********************************
Delete a Certificate
***********************************

You can delete a certificate that is not activated. 

.. caution:: 
  Do not delete a certificate after the course has started. A learner who has
  already earned a certificate will no longer be able to access it.

To delete a certificate, follow these steps.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, at the top right corner of the certificate
   form, select the "Delete" icon.

#. In the confirmation dialog, confirm that you want to delete the certificate.

.. image:: ../../../shared/building_and_running_chapters/Images/CertificateDeleteIcon.png
   :width: 500
   :alt: Top portion of the certificate form showing the delete icon in the upper right corner.


.. _Preview a Certificate:

************************
Preview Certificates
************************

After you have finished editing your certificate, you can
preview a certificate for verification purposes. You select from the available
course modes (such as "honor code" or "verified") to see how a certificate
will appear to a learner taking the course in the selected mode.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, select the course mode of the certificate you
   want to preview, then click **Preview Certificate**.

   You see the web view for the certificate, as a learner in the selected
   course mode would see it.

   .. image:: ../../../shared/building_and_running_chapters/Images/PreviewCertificate.png
     :width: 350
     :alt: The Preview button on the Certificates page in Studio.

After previewing the certificate, you can :ref:`edit the certificate<Edit a
Certificate>` further or :ref:`activate your certificate configuration<Activate
a Certificate>`.


.. _Activate a Certificate:

***********************
Activate a Certificate
***********************

.. only:: Partners

  When you have verified your certificates, contact your edX Partner Manager to
  activate your certificates.

.. only:: Open_edX

  When you have verified your certificate, a course team member with the Admin
  role must activate the certificate.

  .. note:: Course team members without the Admin role cannot activate a
     certificate.

  The course team administrator must complete the following steps.

  #. In Studio, from the **Settings** menu, select **Certificates**.

  #. On the Certificates page, select **Activate**.

     .. image:: ../../../shared/building_and_running_chapters/Images/ActivateCertificate.png
       :width: 350
       :alt: The Activate button on the Certificates page in Studio.

After certificates are activated, learners in your course who attain a passing
grade or otherwise qualify receive certificates.


.. _Deactivate a Certificate:

********************************************
Deactivate a Certificate
********************************************

In some situations, after having made a certificate active, you
might need to deactivate the certificate to make changes. 

As a best practice, do not make changes to certificates in a running course if
it is possible that certificates have already been issued to learners.

.. only:: Partners

  Contact your edX Partner Manager if you need to modify an activated
  certificate.

.. only:: Open_edX

  A course team member with the Admin role must deactivate the certificate.

  .. note:: Course team members without the Admin role cannot deactivate a
     certificate.

  The course team administrator must complete the following steps.

  #. In Studio, from the **Settings** menu, select **Certificates**.

  #. On the Certificates page, select **Deactivate**.

The certificate is no longer active and the course team can edit it. No new
certificates can be issued to learners while it is deactivated. Learners who
have already been issued certificates can continue to access them.


.. _Manage Certificate Images:

**************************
Manage Certificate Images
**************************

When you add signatory image files to a certificate, the uploaded files are
listed in Studio on the **Files & Uploads** page.

When you delete a certificate, images that you uploaded for use with that
certificate are also deleted. However, if you edit a certificate and replace
images, the unused image files remain on the **Files & Uploads** page. You can
manually remove unused images. For information, see
:ref:`Delete a File`.


.. only:: Open_edX

  .. _Enable Badges in Course:

  *****************************************
  Enable or Disable Badges for Your Course
  *****************************************

  Badges provide a way for learners to share their course achievements. For
  courses that have badges enabled, learners receive a badge at the same time
  as they receive a course certificate, and have the option of sharing their
  badges to a badging site such as Mozilla Backpack.

  The Open edX platform supports Open Badges, an open standard developed by the
  Mozilla Foundation. For more information about Open Badges, see the 
  `Open Badges web site <http://openbadges.org/>`_.

  If badging is enabled for your platform, badges are enabled by default for
  your course. If you are unsure whether badging is enabled for your platform,
  contact your platform administrator.

  To stop issuing badges in your course, follow these steps.

  #. In Studio, from the **Settings** menu, select **Advanced Settings**.

  #. Locate the **Issue Open Badges** policy key. The default value is
     ``True``.

  #. Change the setting to ``False`` and save your changes.

  To enable badging for your course if it has previously been disabled, change
  the value of the key to ``True``.


.. _Configuring Certificates: http://edx.readthedocs.org/projects/edx-installing-configuring-and-running/en/latest/configuration/enable_certificates.html
