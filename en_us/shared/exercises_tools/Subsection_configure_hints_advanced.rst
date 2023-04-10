
In the advanced editor, you add the ``<demandhint>`` element immediately before
the closing ``</problem>`` tag, and then configure each hint using the
``<hint>`` element.

.. code-block:: xml

  <problem>
  .
  .
  .
  <demandhint>
    <hint>Hint 1</hint>
    <hint>Hint 2</hint>
    <hint>Hint 3</hint>
  </demandhint>
  </problem>

For example, the following OLX for a single select problem shows two hints.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
    .
    .
    .
    </multiplechoiceresponse>
    <demandhint>
      <hint>A fruit is the fertilized ovary from a flower.</hint>
      <hint>A fruit contains seeds of the plant.</hint>
    </demandhint>
  </problem>
