.. _Download Data Package:

############################################
Downloading the Data Package from Amazon S3
############################################

.. _Access Amazon S3:

To connect to Amazon S3, you must have your
:ref:`decrypted credentials<Getting_Credentials_Data_Czar>`. You may want
to use a third-party tool that gives you a user interface for managing files
and transferring them from Amazon S3 to your network. Some data czars use
S3 applications like CloudBerry Explorer for Amazon S3, Bucket Explorer, or S3
Browser. As an alternative, you can use the `AWS Command Line Interface`_.
Follow these steps to access your edX data package on Amazon S3.

#. Select and install a third-party tool or interface to manage your S3
   account.

#. Open your decrypted ``credentials.csv`` file. This file contains your AWS
   Access Key and your AWS Secret Key.

#. Open the third-party tool.

#. Enter information to connect to the S3 account.

   For example, you might need to select an option such as **Open Connection**,
   and then supply the service you want to connect to (Amazon S3), your Access
   Key, and your Secret Key. For more information, see the documentation
   provided for the tool that you selected.

#. To access the database data files, specify or select ``s3://course-data``.

   To access the event data files, specify or select ``s3://edx-course-
  data/{org}/``. You must include the identifier for your organization after
   the name of the bucket.

   .. note:: If you are using a third-party tool to connect to Amazon S3, you
    might not be able to navigate directly between ``s3://course-data`` and
    ``s3://edx-course-data/{org}/``. You might need to disconnect from Amazon
    S3 and then reconnect to specify the other destination.

For information about the files found at each of these Amazon S3 destinations,
see :ref:`Package`.

.. include:: ../../../links/links.rst
