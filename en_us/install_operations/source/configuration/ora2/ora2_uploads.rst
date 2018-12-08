.. include:: ../../../../links/links.rst

.. _Configuring ORA2 to Upload Files to Alternative Storage Systems:

###############################################################
Configuring ORA2 to Upload Files to Alternative Storage Systems
###############################################################

By default, the Open Response Assessment (ORA2) application stores files that
learners upload in an Amazon S3 bucket.

You can configure ORA2 to store files in an alternate system. To have learners'
files stored in a system other than Amazon S3, follow these steps.

#. In the ORA-2 repository, implement the ``BaseBackend`` class defined in the
   `base.py`_ file.

   For example, the `S3.py`_ file in the same directory is an implementation of
   ``BaseBackend`` for Amazon S3. You must implement the equivalent class for
   the storage system you intend to use.

#. Configure ORA2 to use your alternative storage system by modifying the value
   of ``backend_setting`` in `init file`_ to point to your implementation of
   ``BaseBackend``.

#. Add code to instantiate the new implementation to the ``get_backend()``
   function in the ``init.py`` file.

#. Configure ORA2 to use the alternative storage system by modifying the value
   of ``ORA2_FILEUPLOAD_BACKEND`` in the Django settings to point to your
   implementation of ``BaseBackend``.
