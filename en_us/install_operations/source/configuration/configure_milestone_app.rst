∂
.. for reuse, not in TOC, excluded from build list

************************************
Configure the Milestones Application
************************************

#. Set the value of ``MILESTONES_APP`` in the ``/cms/envs/common.py`` and
   ``/lms/envs/common.py`` files to ``True``.
   
   .. code-block:: bash

       # Milestones application flag
       'MILESTONES_APP': True,

#. Save the ``/cms/envs/common.py`` and ``/lms/envs/common.py`` files.

#. Run database migrations.
