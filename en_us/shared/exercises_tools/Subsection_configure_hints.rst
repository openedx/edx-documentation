====================================
Configure Hints in the Simple Editor
====================================

In the simple editor, you configure hints with the following syntax.

::

  ||Hint 1||
  ||Hint 2||
  ||Hint n||

.. note:: 
  You can configure any number of hints. The learner views one hint at a time
  and views the next one by selecting **Hint** again.

For example, the following problem has two hints.

::

  ||A fruit is the fertilized ovary from a flower.||
  ||A fruit contains seeds of the plant.||

======================================
Configure Hints in the Advanced Editor
======================================

In the advanced editor, you configure each hint in the ``<hint>`` element
within the ``<demandhint>`` element.

.. code-block:: xml

  <demandhint>
    <hint>Hint 1</hint>
    <hint>Hint 2</hint>
    <hint>Hint 3</hint>
  </demandhint>

For example, the following XML shows two hints.

.. code-block:: xml

  <demandhint>
    <hint>A fruit is the fertilized ovary from a flower.</hint>
    <hint>A fruit contains seeds of the plant.</hint>
  </demandhint>
