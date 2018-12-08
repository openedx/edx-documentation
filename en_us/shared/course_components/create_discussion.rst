.. _Working with Discussion Components:

###################################
Working with Discussion Components
###################################

This section describes how to work with discussion components in Studio.

.. contents::
 :local:
 :depth: 1

*******************
Overview
*******************

You can add discussion components to a unit to pose questions about other
components, such as videos or text, in the unit. A discussion component gives
learners a chance to respond to and interact with each other about a specific
subject.

Discussion topics that you create by adding discussion components in your
course are known as content-specific discussion topics.

For more information about discussions, see these topics.

* :ref:`Discussions`
* :ref:`Guidance for Discussion Moderators`
* :ref:`Set up Discussions in Cohorted Courses`

.. _Create a Discussion Component:

*****************************
Create a Discussion Component
*****************************

.. note:: EdX recommends that you add an HTML component before each discussion
   component to introduce the topic that you want learners to discuss. The
   discussion component itself does not contain any text and can be easy for
   learners to overlook.

#. Under **Add New Component**, select **Discussion**.

   .. warning:: You should always use these steps to create a discussion
     component. Do not create discussion components by using the **Duplicate**
     button in Studio. Duplicated discussion components result in
     discussion topics containing the same conversations, even if users post in
     different discussions.

#. In the discussion component that appears, select **Edit**.

   .. image:: ../../../shared/images/Disc_Create_Edit.png
    :alt: An image of the discussion component with the Edit button circled.
    :width: 600

#. Follow the guidelines in the editor to fill in the **Category**, the
   **Display Name**, and the **Subcategory** fields.

   .. image:: ../../../shared/images/DiscussionComponentEditor.png
    :alt: An image of the discussion component editor with a category of
     "Getting Graded" and a subcategory of "Answering More Than Once".
    :width: 600

   The value in the **Display Name** field identifies the discussion in the
   course content. The default display name for new discussion components is
   "Discussion".  Changing the default to a unique, descriptive display name
   can help you and your learners identify different topics quickly and
   accurately. If you delete the default display name and do not enter your own
   identifying name, the platform supplies "discussion" for you.

   The values in the **Category** and **Subcategory** fields
   are visible to learners in the list of discussion topics on the
   **Discussion** page.

   .. note:: Each **Category**/**Subcategory** pair for the discussion topics
      in your course must be unique.

   .. image:: ../../../shared/images/Discussion_category_subcategory.png
    :alt: A list of discussions with the "Answering More Than Once" topic
     indented under "Getting Graded".
    :width: 400

#. Select **Save**.

.. note:: On the **Discussion** page, you cannot see category and subcategory
   names of discussion components that you created until after the course has
   started and the unit is released. For more details about when discussion
   topics are visible, see :ref:`Visibility of Discussion Topics`.

.. _A Students View of the Discussion:

**********************************
A Learner's View of the Discussion
**********************************

When you add a content-specific discussion topic to a unit, learners see only
the **Show Discussion** and **New Post** options. EdX recommends that you add
an HTML component before each discussion component to introduce the topic that
you want learners to discuss.

In the following example, the discussion component follows video and HTML
components.

.. image:: ../../../shared/images/DiscussionComponent_LMS.png
  :alt: A video component followed by a descriptive HTML component and then a
      discussion component.
  :width: 600

Learners must select **Show Discussion** to expand the discussion space and
read the contributions, or select **New Post** to post their own contributions.

On the **Discussion** page, learners can find the category and subcategory of
the discussion in the discussion thread list.

.. image:: ../../../shared/images/Discussion_category_subcategory.png
 :alt: The Discussion page from a learner's point of view.
 :width: 400
