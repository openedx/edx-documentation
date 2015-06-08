.. _Setting Up Course Certificates:

################################
Setting Up Course Certificates
################################

.. This file is for open edx only. Currently on edx.org there is no ability
.. for course authors to create certificate configurations.

This section describes how to configure certificates for your course in
Studio.

.. contents::
   :local:


.. _Create a Certificate:
  
***************************************
Create a Certificate Configuration
***************************************

You create one certificate configuration per course to serve as the template
for certificates issued for all of the enrollment tracks available for your
course (such as "honor code" or "verified"). Honor code certificates use the
organization logo and signatory information, but do not include signature
images, which are used only for verified certificates.

To create a certificate configuration for your course, follow these steps.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, select **Add a new certificate**.

#. (Optional) Specify an alternative course title to use on the certificate
   instead of the official course title. You might want to use a different
   title on your course certificates if, for example, the official course
   name is too long to fit well on the certificate.

4. Upload your organization's logo image file. Make sure that this is the
   approved official logo for your organization, for consistency with
   certificates that are issued by other courses in your organization.

   .. note:: Images that you upload for certificates can be a maximum of 10MB
      in size and must not exceed the dimensions indicated underneath the
      **Organization Logo** field.

#. Add a signatory for each person associated with the course or organization
   whose name and title you want to appear on the certificate, up to a maximum
   of four signatories. You must specify at least one signatory.

#. (Optional) If you offer verified certificates in your course, upload image
   files showing the signature for each signatory. Signature images are used
   only for verified certificates; honor certificates show only the names and
   titles of signatories, without signatures.

#. When you have finished creating your certificate configuration, select
   **Create**.

   You can :ref:`preview the certificate<Preview a Certificate>` to see how it
   will appear to a learner taking the course in the selected mode.

   Your course certificate is not available for issuing to learners until you
   :ref:`activate the certificate configuration<Activate a Certificate>`.


.. _Edit a Certificate:

********************************
Edit a Certificate Configuration
********************************

You can edit a certificate configuration at any time, including after the
configuration has been activated. However, as a best practice, do not make
changes to certificate configurations in a running course if it is possible
that certificates have already been issued to learners, because different
learners might be awarded certificates with different details for the same
course.

To make changes to a certificate configuration, follow these steps.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, at the top right corner of the certificate
   configuration form, select the **Edit** icon.

#. When you have finished editing the certificate configuration, select
   **Save**.

   After you save your changes, you can :ref:`preview the certificate<Preview
   a Certificate>` to make sure it appears as you want it to. You then need to
   :ref:`activate the certificate configuration<Activate a Certificate>` again
   before certificates can be issued.


.. _Delete a Certificate:

***********************************
Delete a Certificate Configuration
***********************************

You can delete a certificate configuration at any time. However, as a best
practice, do not delete certificate configurations in a running course if it
is possible that certificates have already been issued to learners.

To delete a certificate configuration, follow these steps.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, at the top right corner of the certificate
   configuration form, select the "Delete" icon.

#. In the confirmation dialog, confirm that you want to delete the certificate
   configuration.

.. image:: ../../../shared/building_and_running_chapters/Images/CertificateDeleteIcon.png
   :width: 500
   :alt: Top portion of the certificate form showing the delete icon in the upper right corner


.. _Preview a Certificate:

************************
Preview Certificates
************************

After you have finished editing your certificate configuration, you can
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
     :alt: The Preview button on the Certificates page in Studio

After previewing the certificate, you can :ref:`edit the certificate<Edit a
Certificate>` further or :ref:`activate your certificate configuration<Activate a
Certificate>`.


.. _Activate a Certificate:

************************************
Activate a Certificate Configuration
************************************

When you have verified your certificate configuration and are ready to issue
certificates, you activate the configuration.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, click **Activate**.

   .. image:: ../../../shared/building_and_running_chapters/Images/ActivateCertificate.png
     :width: 350
     :alt: The Activate button on the Certificates page in Studio

The certificate configuration becomes active. When learners in your course
attain a passing grade or otherwise qualify for certificates, they receive
certificates that are based on this active configuration.

You can edit active certificate configurations, but if you make and save any
changes, the configuration becomes inactive. You must activate it again before
certificates can be issued using the configuration.


.. _Deactivate a Certificate:

********************************************
Deactivate a Certificate Configuration
********************************************

In some situations, after having made a certificate configuration active, you
might need to deactivate an active certificate configuration. If there are no
active configurations, certificates are not available for issuing or for
viewing by learners.As a best practice, do not make changes to certificate
configurations in a running course if it is possible that certificates have
already been issued to learners.


#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the Certificates page, click **Deactivate**.

The certificate configuration is no longer active. Certificates cannot be
viewed by or issued to learners.


.. _Manage Certificate Images:

**************************
Manage Certificate Images
**************************

When you add image files to a certificate configuration, such as the
organization logo or signature images, the uploaded files are listed in Studio
on the **Files & Uploads** page.

When you delete a certificate configuration, images that you uploaded for use
with that configuration are also deleted. However, if you edit a certificate
configuration and replace images, the unused image files remain on the **Files
& Uploads** page. You can manually remove unused images. For information, see
:ref:`Delete a File`.


.. _Enable Badges in Course:

*****************************************
Enable or Disable Badges for Your Course
*****************************************

Badges provide a way for learners to share their course achievements. For
courses that have badges enabled, learners receive a badge at the same time as
they receive a course certificate, and have the option of sharing their badges
to a badging site such as Mozilla Backpack.

The Open edX platform supports Open Badges, an open standard developed by the
Mozilla Foundation. For more information about Open Badges, see the 
`Open Badges web site <http://openbadges.org/>`_.

If badging is enabled for your platform, badges are enabled by default for
your course. If you are unsure whether badging is enabled for your platform,
contact your platform administrator.

To stop issuing badges in your course, follow these steps.

#. In Studio, from the **Settings** menu, select **Advanced Settings**.

#. Locate the **Issue Open Badges** policy key. The default value is ``True``.

#. Change the setting to ``False`` and save your changes.

To enable badging for your course if it has previously been disabled, change
the value of the key to ``True``.

