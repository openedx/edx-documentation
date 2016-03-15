To create and register a new OIDC client, follow these steps.

#. Start the LMS.
#. In your browser, go to ``http://127.0.0.1:8000/admin/oauth2/client/``.
#. Select **Add client**.
#. Leave the **User** field blank.
#. For **Client Name**, enter ``E-Commerce Service``.
#. For **URL**, enter ``http://localhost:8002/``.
#. For **Redirect URL**, enter ``https://localhost:8002/complete/edx-oidc/``.
   This is the OIDC client endpoint.

   The system automatically generates values in the **Client ID** and **Client
   Secret** fields. You use these values when you update the Django settings.

#. For **Client Type**, select **Confidential (Web applications)**.
#. Select **Save**.



