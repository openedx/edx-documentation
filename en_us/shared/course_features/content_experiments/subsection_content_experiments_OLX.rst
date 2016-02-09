.. This section is shared in course authors and OLX guides.

.. _Add a Content Experiment in OLX:

****************************************
Add a Content Experiment in OLX
****************************************

You work with multiple XML files to configure a content experiment. This
section steps through the files involved in a content experiment that shows
different content to two different groups of learners.

=====================================================
Define the Content Experiment in the Sequential File
=====================================================

You reference a content experiment in the file for the subsection, or
sequential, in the ``sequential`` directory. For example:

.. code-block:: xml

    ...
    <vertical url_name="name for the unit that contains the A/B test" display_name="A/B Test Unit">
        <split_test url_name="name of A/B test file in the split_test folder"/>
    </vertical>
    .....

The ``<split_test>`` element's ``url_name`` value references the name of the
content experiment file in the ``split_test`` directory.

.. caution::
  You can only define a content experiment in a unit, or vertical, in which different collections of components are associated with different experiment groups.  You cannot define a content experiment at a subsection (sequential) or section (chapter) level and have different units or subsections associated with different groups.


.. _Define the Experiment Content in the Split Test File:

=====================================================
Define the Experiment Content in the Split Test File
=====================================================

After you define the content experiment in the sequential file, you define the
course content you want to test in the file in the ``split_test`` directory.
This is the file referenced in the ``<split_test>`` element in the sequential
file, as shown above.

In the content experiment file, you add elements for the experiment content.
For this example, you add two ``<vertical>`` elements to compare the two
different sets of content.

.. code-block:: xml

    <split_test url_name="AB_Test.xml" display_name="A/B Test" user_partition_id="0"
                group_id_to_child='{"0": "i4x://path-to-course/vertical/group_a",
                                    "1": "i4x://path-to-course/vertical/group_b"}'>
        <vertical url_name="group_a" display_name="Group A">
           <html>Welcome to group A.</html>
           <video url_name="group_a_video"/>
        </vertical>
        <vertical url_name="group_b" display_name="Group B">
            <html>Welcome to group B.</html>
            <problem display_name="Checkboxes">
                <p>A checkboxes problem presents checkbox buttons for learner input.
                   Learners can select more than one option presented.</p>
                <choiceresponse>
                    <checkboxgroup label="Select the answer that matches">
                        <choice correct="true">correct</choice>
                        <choice correct="false">incorrect</choice>
                        <choice correct="true">correct</choice>
                    </checkboxgroup>
                </choiceresponse>
            </problem>
        </vertical>
    </split_test>


In this example:

* The ``user_partition_id`` value references the ID of the experiment defined
  in the ``policy.json`` file.

* The ``group_id_to_child`` value references the IDs of the groups defined in
  the ``policy.json`` file and maps the group IDs to specific content.

  For example,  the value for group ``0``, ``i4x://path-to-
  course/vertical/group_a``, maps to the ``<vertical>`` element with the
  ``url_name`` equal to ``group_a``.  Therefore, learners in group 0 see the
  content in that vertical.

For information about the ``policy.json`` file, see :ref:`Set Up Group
Configuration for OLX Courses`.
