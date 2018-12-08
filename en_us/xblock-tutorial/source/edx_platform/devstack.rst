.. _Deploy Your XBlock in Devstack:

###############################
Deploy Your XBlock in Devstack
###############################

This section provides instructions for deploying your XBlock in Devstack.

.. contents::
 :local:
 :depth: 1

For more information about Devstack, see the :ref:`installation:Installing,
Configuring, and Running the Open edX Platform`.

*******************
Prerequisites
*******************

Before proceeding with the steps to deploy your XBlock, ensure the following
requirements are met.

* Devstack is running. For instructions, see the :ref:`installation:Running
  the Open edX Developer Stack`.

* Ensure you have the XBlock directory in a location you can access from the
  Devstack Vagrant instance.

*******************
Install the XBlock
*******************

#. Use SSH to access the Devstack Vagrant instance.
      
   .. code-block:: bash

      $ vagrant ssh

#. Install the XBlock.
   
   .. code-block:: bash

      vagrant@precise64:~$ sudo -u edxapp /edx/bin/pip.edxapp install /path/to/your/block 

**************************************
Enable the XBlock in the edX Platform
**************************************

#. In the file ``edx-platform/lms/envs/common.py``, ensure the following lines
   are not commented out::

     from xmodule.x_module import prefer_xmodules
     XBLOCK_SELECT_FUNCTION = prefer_xmodules
     .. first line not there. obsolete?

#. In the file ``edx-platform/cms/envs/common.py``, ensure the following lines
   are not commented out::

     from xmodule.x_module import prefer_xmodules
     XBLOCK_SELECT_FUNCTION = prefer_xmodules 

#. In ``edx-platform/cms/envs/common.py``, change the
   ``'ALLOW_ALL_ADVANCED_COMPONENTS'`` value to ``True``.::

     'ALLOW_ALL_ADVANCED_COMPONENTS': True, 

************************
Start the LMS and Studio
************************

#. Start the LMS server.
      
   .. code-block:: bash

      edxapp@precise64:~$ paver devstack lms

#. Start the Studio server.
      
   .. code-block:: bash

      edxapp@precise64:~$ paver devstack studio

********************************
Enable the XBlock in Your Course
********************************

You must enable the XBlock in each course in which you intend to use it.

#.  Log in to Studio.

#.  Open the course.
    
#. From the **Settings** menu, select **Advanced Settings**.

#. In the **Advanced Module List** field, place your cursor between the braces,
   and then type the exact name of the XBlock. 

   .. note::
     The name you enter must match exactly the name specified in your XBlock's
     ``setup.py`` file.

   If you see other values in the **Advanced Module List** field, add a comma
   after the closing quotation mark for the last value, and then type the name
   of your XBlock.   

#. At the bottom of the page, select **Save Changes**.

****************************************
Add an Instance of the XBlock to a Unit
****************************************

You can add instances of the XBlock in any unit in the course.

On the unit page, under **Add New Component**, select **Advanced**. 

Your XBlock is listed as one of the types you can add.

.. add image

Select the name of your XBlock to add an instance to the unit.

.. add image

You can then edit the properties of the instance as needed by selecting the
**Edit** button.

.. add image

For more information about working with components in Studio, see
:ref:`opencoursestaff:Developing Course Components` in the *Building and
Running an Open edX* guide.

.. include:: ../../../links/links.rst
