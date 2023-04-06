.. _MathJax in Studio:

##############################
MathJax for Mathematics
##############################

To produce clear and professional-looking symbols and equations in web browser,
edX uses `MathJax <https://www.mathjax.org/>`_. MathJax automatically formats
the mathematical symbols and equations that you enter in Text and problem
components using LaTeX notation into beautiful math.

This topic provides some pointers to get you started. Many resources for
learning and using MathJax are available online, including the official
`MathJax Documentation`_ . A tutorial is available on the `Mathematics meta`_
stack exchange. Additional documentation, with a testing tool, is available on
the `Tree of Math`_ site.

A MathJax equation can appear with other text in the paragraph (inline format)
or on its own dedicated line (display format).

For inline equations, you can do either of the following.

* Surround your MathJax expression with backslash and parentheses characters.

    ``\( equation \)``

* Surround your MathJax expression with ``[mathjaxinline]`` tags. Note that
  these tags use brackets (``[ ]``).

    ``[mathjaxinline] equation [/mathjaxinline]``

For display equations, you can do either of the following.

* Surround your MathJax expression with backslash and bracket characters.

    ``\[ equation \]``

* Surround your MathJax expression with ``[mathjax]`` tags. Note that these
  tags use brackets(``[ ]``)

    ``[mathjax] equation [/mathjax]``

*************************************
Adding MathJax to Text Components
*************************************

In the Text component editor, you can use MathJax in both visual view and
HTML view.

.. image:: ../../../shared/images/MathJax_HTML.png
 :alt: A composite image of four views of the same text and MathJax markup. The
   Text component editor visual view and HTML view are shown at the top, with
   the rendered text and equation on the Studio unit page and in the LMS below.

*****************************************
Adding MathJax to Problem Components
*****************************************

In the problem component editor, you can use MathJax in either the simple
editor or advanced editor.

In the example that follows, note that the Einstein equation in the explanation
is enclosed in backslashes and parentheses, so it appears inline with the text.
The Navier-Stokes equation is enclosed in backslashes and brackets, so it
appears on its own line (display).

.. image:: ../../../shared/images/MathJax_Problem.png
 :alt: A composite image of four views of the same single select problem. The
     simple editor Markdown and advanced editor OLX are shown at the top, with
     the rendered problem on the Studio unit page and in the LMS below.

.. _MathJax Documentation: http://docs.mathjax.org/en/latest/index.html
.. _Mathematics meta: http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
.. _Tree of Math: http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm
