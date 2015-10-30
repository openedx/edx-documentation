
.. for reuse, not in TOC, excluded from build list

************************************
Configure the Milestones Application
************************************

#. Set the value of ``MILESTONES_APP`` in the ``lms.env.json`` and
   ``cms.env.json`` files to ``True``.

   .. code-block:: bash

       # Milestones application flag
       'MILESTONES_APP': True,

#. Save the the ``lms.env.json`` and ``cms.env.json`` files.

#. Run database migrations.
