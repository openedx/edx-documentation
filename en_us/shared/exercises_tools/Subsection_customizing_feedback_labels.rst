-----------------------------
Customizing Feedback Labels
-----------------------------

By default, the feedback labels shown to learners are **Correct** and
**Incorrect**. If you do not define feedback labels, learners see these terms
when they submit an answer, as in the following example.

::

  Incorrect: A pumpkin is the fertilized ovary of a squash plant and contains
  seeds classifying it as a fruit.

You can configure the problem to override the default labels. For example, you
can configure a custom label for a specific wrong answer.

::

  Not Quite: Many people mistakenly think a tomato is a vegetable. However,
  because a tomato is the fertilized ovary of a tomato plant and contains seeds
  it is classified as a fruit.

In the :ref:`advanced editor<Advanced Editor>`, you configure custom feedback
labels with the following syntax.

.. code-block:: xml

  <choice correct="true or false">Answer
    <choicehint label="Custom Label">Feedback for learners who select this
    answer.</choicehint>
  </choice>

For example, the feedback for the following answer option is configured to use
a custom label.

.. code-block:: xml

  <choice correct="false">tomato
    <choicehint label="Not Quite">Many people mistakenly think a tomato is a
    vegetable. However, because a tomato is the fertilized ovary of a tomato
    plant and contains seeds, it is a fruit.</choicehint>
  </choice>

.. note::
  The default labels **Correct** and **Incorrect** display in the learner's
  requested language. If you provide custom labels, they display as you define
  them to all learners. They are not translated into different languages.
