.. _Problems:

#################################
Problems
#################################

The format for edX problems is based on the `LON-CAPA XML format`_, although
the two are not quite compatible. In the edX variant, problems are composed of
the following types of tags.

* ``inputtypes`` are similar to XBlocks. They define ways for users to enter
  input into the problem.
* ``responsetypes`` are graders. They define how inputs are mapped to grades.
* ``hinters`` are used to provide feedback to problems.
* Standard HTML tags are used for formatting.

OLX is designed to allow mixing and matching of ``inputtypes``,
``responsetypes``, and ``hinters``. For example, a numerical grader could match
7+-0.1%. Ideally, you could use this grader with any ``inputtype`` that returns
numbers as its output, including a text box, equation input, slider, or
multiple choice question. In practice, this does not always work. For example,
in the example described above, a multiple choice question would not give an
output in a format a numerical grader could handle.

In addition, in many cases, there is a 1:1 mapping between graders and inputs.
For some types of inputs (especially discipline-specific specialized ones),
only one grader is needed.

The most general grader is ``customresponse``. This grader uses Python code to
evaluate the input. By design, this ought to work with any inputtype, although
there are bugs mixing this with a small number of the newer inputtypes.

Like LON-CAPA, OLX allows embedding of code to generate parameterized problems.
Unlike LON-CAPA, edX supports Python (and not Perl). Otherwise, the syntax for
parameterizing problems is approximately identical.

.. toctree::
   :maxdepth: 2

   create_problem
   checkbox
   chemical_equation
   circuit_schematic_builder
   custom_javascript
   custom_python
   drag_and_drop
   dropdown
   gene_explorer
   image_mapped_input
   math_expression_input
   mathjax
   molecule_editor
   mult_choice_num_input
   multiple_choice
   numerical_input
   poll_question
   problem_in_latex
   problem_with_hint
   protein_builder
   survey
   symbolic_response
   text_input


.. include:: ../../../links/links.rst
