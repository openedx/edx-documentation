
.. for reuse, not in TOC, excluded from build list

************************************
Configure the Milestones Application
************************************

#. Set the value of ``MILESTONES_APP`` in the ``lms.yml`` and
   ``studio.yml`` files to ``True``.

   .. code-block:: none

       # Milestones application flag
       'MILESTONES_APP': True,

#. Save the ``lms.yml`` and ``studio.yml`` files.

#. Run database migrations.
