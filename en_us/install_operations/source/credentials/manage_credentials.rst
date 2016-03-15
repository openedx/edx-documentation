.. _Manage Credentials:

#####################
Manage Credentials
#####################

When you work with credentials, you must configure a site and a certificate for
at least one course. You can create certificates for individual courses, or for
programs that include more than one course. Each certificate includes at least
one signatory.

.. contents::
   :depth: 1
   :local:

*******************************
Adding a Credentials Site
*******************************

To add a site, you use the edX ``SiteConfiguration`` model that extends
the `Django sites framework`_. With this model, you map domains to a **site**
object, which consists of an ID and a name.

Each site can have only one configuration.

======================
Add a Site
======================

To add a Credentials site, follow these steps. All fields are required.

#. In a browser, go to ``http://localhost:8002/admin`` to open the Django
   administration panel.
#. Under **Core**, select **Site configurations**.
#. On the **Select site configuration to change** page, select **Add site
   configuration**.
#. For a devstack installation, for **Site**, leave the default value of
   ``example.com``.

   For any other installation, for **Site**, use the hostname under which your
   service is running. For example, the hostname may be ``localhost:8002``.

#. For **LMS base url for custom site/microsite**, enter
   ``http://localhost:8000``.
#. For **Path to custom site theme**, enter ``main.scss``.
#. Select **Save**.

======================
Edit a Site
======================

To edit a Credentials site, follow these steps. All fields are required.

#. In a browser, go to ``http://localhost:8002/admin`` to open the Django
   administration panel.
#. Under **Core**, select **Site configurations**.
#. On the **Select site configuration to change** page, select the site that
   you want to change.
#. Make the changes that you want, and then select **Save**.

.. _Credentials Adding a Certificate Template:

********************************************
(Optional) Adding a Certificate Template
********************************************

This configuration adds certificate-specific templates. This configuration is
optional. If you do not add a certificate-specific template, certificates use
the default template.

======================
Add a Template
======================

To add a certificate template, use the ``CertificateTemplate``
model.

#. In a browser, go to ``http://localhost:8002/admin/credentials/`` to open the
   **Credentials administration** page in the Django administration panel.
#. Under **Credentials**, select **Certificate Templates**.
#. On the **Select certificate template to change** page, select **Add
   certificate template**.
#. For **Name**, type the name of the certificate template that you want to
   create. This name must be unique across all certficate templates in your
   course or organization.
#. For **Content**, add the HTML for your template.

    .. code-block:: bash

     SAMPLE CODE

#. Select **Save**.

======================
Edit a Template
======================

To edit a certificate template, use the ``CertificateTemplate``
model.

#. In a browser, go to ``http://localhost:8002/admin/credentials/`` to open the
   **Credentials administration** page in the Django administration panel.
#. Under **Credentials**, select **Certificate Templates**.
#. On the **Select certificate template to change** page, select the template
   that you want to change.
#. Make any changes that you want, and then select **Save**.

==========================================
Upload a Certificate Template to Amazon S3
==========================================

To upload a certificate template to S3, you use the
``CertificateTemplateAsset`` model. The ``CertificateTemplate`` model consumes
the assets that you upload.

To upload a certificate template to S3, follow these steps. All fields are
required.

#. In a browser, go to ``http://localhost:8002/admin/credentials/`` to open the
   **Credentials administration** page in the Django administration panel.
#. Under **Credentials**, select **Certificate template assets**.
#. On the **Select certificate template asset to change** page, select **Add
   certificate template asset**.
#. For **Name**, type the name of the asset that you want to
   create.

   .. Does this name have to be unique across all certficate template assets in
   .. the course or organization?

#. For **Asset file**, select **Choose File**.
#. In the **Choose File** dialog box, browse to your file, and then select
   **Open**.
#. Select **Save**.


*********************************
Adding or Editing a Signatory
*********************************

Every certificate must include at least one signatory. You use the
``Signatory`` model to add or update a signatory.

Each signatory must include an image file of the signatory's signature. The
image file must be a square .png file and must be smaller than 250 KB.

.. _Credentials Add a Signatory:

======================
Add a Signatory
======================

To add a signatory, follow these steps. All fields are required.

#. In a browser, go to ``http://localhost:8002/admin/`` to open the Django
   administration panel.
#. Under **Credentials**, select **Signatories**.
#. On the **Select signatory to change** page, select **Add signatory**.
#. On the **Add signatory** page, enter the signatory's information in the
   **Name** and **Title** fields.
#. For **Image**, select **Choose File**, browse to the file that you want, and
   then select **Open**.
#. Select **Save**.

======================
Edit a Signatory
======================

#. In a browser, go to ``http://localhost:8002/admin/`` to open the Django
   administration panel.
#. Under **Credentials**, select **Signatories**.
#. On the **Select signatory to change** page, select the signatory that you
   want to change.
#. On the **Change signatory** page, make the changes that you want.
#. Select **Save**.


****************************************
Adding or Editing a Course Certificate
****************************************

This procedure creates a new ``CourseCertificate`` object that is used to award
course certificates to learners. You use the ``CourseCertificate`` model to add
or update a course certificate.

.. note::
 The **Site**, **Course ID**, and **Certificate type** fields for the
 ``CourseCertificate`` model have a **unique together** constraint. In this
 model, the same site, course ID, and certificate type cannot have more than
 one entry.

You must add at least one signatory before you add a course certificate. For
more information, see :ref:`Credentials Add a Signatory`.

===========================
Add a Course Certificate
===========================

#. In a browser, go to ``http://localhost:8002/admin/`` to open the Django
   administration panel.
#. Under **Credentials**, select **Course certificate configurations**.
#. On the **Select course certificate configuration to change** page, select
   **Add course certificate configuration**.
#. For a devstack installation, for **Site**, leave the default value of
   ``example.com``.

   For any other installation, for **Site**, use the hostname under which your
   service is running. For example, the hostname may be ``localhost:8002``.

#. Select the **Is active** check box.
#. For **Signatories**, select the signatories that you want. Hold down the
   Control or Command keys to select multiple signatories.
#. (Optional) For **Template**, select a template that you have added. For more
   information, see :ref:`Credentials Adding a Certificate Template`.
#. (Optional) For **Title**, enter...
#. For **Course id**, enter <part of the URL for your course>.
#. For **Certificate type**, select <where do these options come from?>.
#. Select **Save**.


===========================
Edit a Course Certificate
===========================

#. In a browser, go to ``http://localhost:8002/admin/`` to open the Django
   administration panel.
#. Under **Credentials**, select **Course certificate configurations**.
#. On the **Select course certificate configuration to change** page, select
   the certificate that you want to change.
#. On the **Change course certificate configuration** page, make the changes
   that you want, and then select **Save**.


**************************************************
Adding or Editing a Program Certificate
**************************************************

This configuration creates a new ``ProgramCertificate`` object that is used to
award program certificates to learners.

You use the ``ProgramCertificate`` model to add or update a program
certificate's configuration.

=====================================
Add a Program Certificate
=====================================

#. In a browser, go to ``http://localhost:8002/admin/`` to open the Django
   administration panel.
#. Under **Credentials**, select **Program certificate configurations**.
#. On the **Select course certificate configuration to change** page, select
   **Add program certificate configuration**.
#. For a devstack installation, for **Site**, leave the default value of
   ``example.com``.

   For any other installation, for **Site**, use the hostname under which your
   service is running. For example, the hostname may be ``localhost:8002``.

#. Select the **Is active** check box.
#. For **Signatories**, select the signatories that you want. Hold down the
   Control or Command keys to select multiple signatories.
#. (Optional) For **Template**, select a template that you have added. For more
   information, see :ref:`Credentials Adding a Certificate Template`.
#. (Optional) For **Title**, enter <any value?>.
#. For **Program id**, enter <any value?>.
#. Select **Save**.

=====================================
Edit a Program Certificate
=====================================

#. In a browser, go to ``http://localhost:8002/admin/`` to open the Django
   administration panel.
#. Under **Credentials**, select **Course certificate configurations**.
#. On the **Select program certificate configuration to change** page, select
   the certificate that you want to change.
#. On the **Change program certificate configuration** page, make the changes
   that you want, and then select **Save**.



.. include:: ../../../links/links.rst
