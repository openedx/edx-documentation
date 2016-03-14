.. _Verify Service User:

************************************
Verify the Service User Account
************************************

TThe Open edX Credentials service must communicate with other Open edX services, such as the LMS or Platform services. Because certificates are publicly accessible, edX provides a “Credentials service user” account that uses JWT authentication to communicate between the Credentials service and other Open edX services. The Credentials service user makes requests on behalf of the Credentials service to access required APIs and fetch data. The Credentials service user is only available for internal use in Open edX services.

By default, the username for the Credentials service user is credentials_service_user. You can change the username of the Credentials service user in the CREDENTIALS_SERVICE_USER configuration setting. However, the Credentials service assumes that a service user named credentials_service_user is present in all needed services.

The Credentials service user must have the following characteristics.

The service user must have the Admin role.
The service user must have a password that is very difficult to guess so that the account cannot be accessed from web interfaces.
The service user must be available in all of the services that the Credentials service must communicate with if these services do not require real user names.

