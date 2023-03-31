.. _Enable Additional Exercises and Tools:

#########################################
Enabling Additional Exercises and Tools
#########################################

Studio includes a default set of core problem types that can be added to any
course, including CAPA problems like text input, single select, and math
expression input. To add these problem types to a course, you select
**Problem** on the unit page.

You can expand the types of content you include in your course by enabling
additional exercises and tools. After you enable an exercise or tool for use
with your course, when you add a component to a unit, that type of content
might be listed as one of the **Advanced**, **Text**, or **Problem** options

******************************************
Enable an Exercise or Tool for Your Course
******************************************

To enable an advanced exercise or tool, follow these steps.

#. In Studio, select **Settings**, and then **Advanced Settings**.

#. Locate the **Advanced Module List** field. This field lists any exercises
   and tools that have been added to your course.

#. If the **Advanced Module List** field is empty, place your cursor between
   the brackets (``[ ]``).

   If the list already contains one or more keys, place your cursor after the
   first bracket (``[``).

#. Enter the key for the exercise or tool that you want to add.

#. Add quotation marks (``" "``) before and after the key.

   If you are adding the key to a list of keys, follow the
   closing quotation mark with a comma character (``,``).

#. Review your entry to verify that the key is accurate and that it is
   surrounded by quotation marks. If there is a list of keys, they must be
   comma separated.

   * In this example, the key for the annotation problem tool is the only value
     in the list.

     ::

       ["annotatable"]

   * In this example, the key for the annotation problem tool is added at
     the beginning of a list of other keys.

     ::

       [
         "annotatable",
         "word_cloud",
         "split_test"
       ]

#. Select **Save Changes**.

   Studio checks the syntax of your entry and reformats your entry to add line
   feeds and indentation. A message lets you know whether your changes were
   saved successfully.



