
.. for reuse, not in TOC, excluded from build list

************************************
Configure the Milestones Application
************************************

#. Set the value of ``MILESTONES_APP`` in the ``lms.yaml`` and
   ``studio.yaml`` files to ``True``.

   .. code-block:: none

       # Milestones application flag
       'MILESTONES_APP': True,

#. Save the ``lms.yaml`` and ``studio.yaml`` files.

#. Run database migrations.
