
.. include:: ../../../../links/links.rst

.. _Configuring ORA2 to Prohibit Submission of File Types:

###############################################################
Configuring ORA2 to Prohibit Submission of File Types
###############################################################

Course teams can configure open response assessments so that learners can
upload files along with their text responses. During the peer review stage of
the assessment, one or more other learners downloads the submitted file and
reads the response. 

To protect learners from exposure to files with malicious content, the ORA2
application identifies a set of file types that learners are not permitted to
upload in a "blacklist".

To add or remove file types from the blacklist, follow these steps.

#. In the ORA-2 repository, use an editor to open the `submission_mixin.py`_
   file.

#. Locate the ``FILE_EXT_BLACK_LIST`` parameter in the file. By default, this
   parameter lists the following file types.
   
   ::

     FILE_EXT_BLACK_LIST = [
         'exe', 'msi', 'app', 'dmg', 'com', 'pif', 'application', 'gadget',
         'msp', 'scr', 'hta', 'cpl', 'msc', 'jar', 'bat', 'cmd', 'vb', 'vbs',
         'jse', 'ws', 'wsf', 'wsc', 'wsh', 'scf', 'lnk', 'inf', 'reg', 'ps1',
         'ps1xml', 'ps2', 'ps2xml', 'psc1', 'psc2', 'msh', 'msh1', 'msh2', 'mshxml',
         'msh1xml', 'msh2xml', 'action', 'apk', 'app', 'bin', 'command', 'csh',
         'ins', 'inx', 'ipa', 'isu', 'job', 'mst', 'osx', 'out', 'paf', 'prg',
         'rgs', 'run', 'sct', 'shb', 'shs', 'u3p', 'vbscript', 'vbe', 'workflow',
     ]

#. Add or remove values from this list. 

#. Save your changes to ``submission_mixin.py``.

#. Restart the Studio (CMS) and Learning Management System (LMS) processes so
   that your updates are loaded.

