.. _Installing an XBlock:

##########################
Installing an XBlock
##########################

The XBlock framework allows developers to expand the Open edX platform by
building different learning experiences and deploying them as XBlocks. Before
course teams can use an XBlock in courses running on an instance of the
Open edX platform, both of the following tasks must be completed.

* A system administrator installs the XBlock in the instance of the Open edX
  platform.

* Course teams enable the XBlock in the specific courses that will use it.

.. Future: link to an XBlock reference that would let people explore what's available and get both the GitHub commit string and the key. - Alison 22 Oct 2015

To install an XBlock, follow these steps.

#. Obtain the GitHub location and commit, or PyPi package name and version,
   for the XBlock.

#. Run ``pip`` along with either the GitHub link to the XBlock or the PyPi
   package name.

   An example of the GitHub link that installs the Oppia XBlock follows.

   .. code-block:: bash

     pip install git+https://github.com/oppia/xblock.git@9f6b95b7eb7dbabb96b77198a3202604f96adf65#egg=oppia-xblock==0.0.0


   An example of the PyPi package name that installs the Peer Instruction
   XBlock follows.

   .. code-block:: bash

     pip install ubcpi-xblock==0.4.4

The course teams that want to include components that use the XBlock can then
enable the XBlock for their courses. To do so, they add the name specified in
the XBlock’s ``setup.py`` file to each course's advanced module list. For more
information, see :ref:`Enable Additional Exercises and Tools`.

.. include:: ../../../links/links.rst
