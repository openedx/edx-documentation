.. _Accessibility Best Practices for Course Content Development:

############################################################
Accessibility Best Practices for Developing Course Content
############################################################

EdX is dedicated to creating a platform that is not only itself accessible,
but also enables course content creators to create accessible content. If you
encounter platform issues that you believe might affect your ability to
provide accessible course content, please contact us at accessibility@edx.org.
We welcome any comments and questions.

.. note:: If you use authoring tools other than those provided by edX, your
   course content might not be accessible or might not meet our standards for
   accessibility.

.. contents::
   :local:
   :depth: 1


.. _Make Sure Your Course Content is Perceivable:

************************************************
Make Sure Your Course Content is Perceivable
************************************************

The `WCAG 2.0 <http://www.w3.org/TR/WCAG20/#cc1>`_ guidelines are organized
around several principles, one of which is that web content must be
perceivable. Information and user interface components must be presentable to
users in ways they can perceive. Users must be able to perceive the
information being presented; it cannot be invisible to all of their senses.

To produce content that is perceivable by all learners, follow these
guidelines.

=================================================
Include Text Alternatives for Non-Text Content
=================================================

For any non-text content, provide text alternatives so that the content can
be changed into other forms that people need, such as large print, braille,
speech, symbols, or simpler language. 

For non-text tests or exercises that would be invalid if presented in text,
provide text alternatives that at least provide descriptions of the non-text
content. Make sure that all images have useful alternative text that screen
readers and other assistive technologies can read. For more information, see
:ref:`Best Practices for Describing Images`.

=================================================
Provide Alternatives for Time-Based Media
=================================================

For time-based media, including pre-recorded audio or video content, provide
alternative equivalent information, such as captions, audio description or
pre-recorded sign language interpretation. For more information, see
:ref:`Creating Accessible Media`.

=================================================
Make Sure Your Content is Adaptable
=================================================

Design your course content so that it can be presented in different ways
without losing information or structure. If your content includes specific
information, structure, and relationships (such as sequence) that is conveyed
through presentation, make sure the same information, structure, and
relationships can be programmatically determined or are available in text.

Make sure your course content does not rely solely on sensory characteristics
such as shape, size, visual location, orientation, or sound, to be understood
by learners.

======================================================
Make It Easier for Learners to See and Hear Content
======================================================

Make the default presentation as easy to perceive as possible, especially by
making it easier for learners to distinguish foreground information from the
background, in both visual and audio elements.

For visual elements, techniques include making sure the fonts you use are
readable, that there is sufficient contrast between the foreground and
background. Do not use color as the sole means of visually distinguishing an
element or conveying critical information. When images contain text, make sure
that the text has a font size of at least 14 points and has good contrast with
the background.

For audio elements, make sure foreground sounds are sufficiently louder than
background sounds.


.. _Make Sure Your Course Content is Understandable:

************************************************
Make Sure Your Course Content is Understandable
************************************************

Make sure your course content is readable and understandable. EdX courses have
a global and diverse audience, including learners whose native language is not
the language in which you created your course, as well as learners who have a
disability that affects reading, such as dyslexia or a visual impairment.

Learners will be better positioned to access concepts in your content if you
write in clear, straightforward language and the content is well structured.


=========================================
Write Simply and Clearly
=========================================

Avoid jargon. If unfamiliar words or phrases are relevant to the subject,
explain them when they are first used, and include a glossary with your course
materials. When you use an abbreviation or acronym, provide the full phrase
the first time it appears. For example, "World Health Organization (WHO)."

The Center for Plain Language provides detailed resources on writing clearly
and concisely, in language appropriate for your content and target audience.
http://centerforplainlanguage.org/5-steps-to-plain-language/

=========================================
Make Your Course Easy to Navigate
=========================================

One aspect of making your course understandable is making sure that learners
can easily grasp its structure, find content, and determine where they are
within the course.

Name your course sections, subsections, units, components, and discussion
topics in a consistent way, and make sure the names are useful and easy to
skim. Make an element's name descriptive of its content, and put important
keyword information first in the name. These names are used in navigation
menus, page headings, and section headings; they are signposts that help
learners to navigate your course and read course content.

When you create written learning resources, break text into sections using
HTML elements such as headings, paragraphs, and lists. Long blocks of unbroken
text are a barrier to most readers. Segmented content is more inviting and is
easier to navigate and search. See :ref:`Best Practices for HTML Markup` for
guidance on creating accessible HTML.

When you provide links to external material, use link text that clearly
explains the link destination (for example, "Review the Course Syllabus").
Avoid using constructs such as “Review the Course Syllabus here”, with only
the word "here" serving as link text. For links that point to documents rather
than web pages, include the document type in the link. For example,
"Supplemental Reading for Week 1 (EPUB)").


.. _Best Practices for Describing Images:

************************************************
Use Best Practices for Describing Images
************************************************

When you use images, diagrams, maps, charts, or icons in your course content,
you must provide text alternatives that provide information equivalent to the
visual content, or that identifies the purpose of such non-text content.

The text alternative for an image depends on the image’s context and purpose,
and might not be a simple description of the image’s visual characteristics.
In general, for every graphic, edX recommends that you provide a text
alternative that provides the equivalent information that a sighted learner
would obtain from viewing the graphic. If the image contains words that are
important for understanding the content, include the words in the text
alternative.

Use the following guidelines when you include images in your course.

=========================================
Provide Short Text Descriptions
=========================================

For each meaningful graphic, provide a short text description that describes
the purpose of the image, unless the image conveys a concept or is the only
source for the information it presents, in which case provide a long text
description. Note that you do not need to provide a long description if the
information appears elsewhere on the page. For example, you do not need to
describe a chart if the same data appears as text in a data table.

Place short descriptions in the ``alt`` attribute of the HTML image element.
For more information about adding images, see :ref:`Add an Image to an HTML
Component`. ::

 <img src="image.jpg" alt="Photo of Ponte Vecchio">
 
* For a representative image, such as a photograph of the Ponte Vecchio, a
  short description could be “Photo of Ponte Vecchio.” If the photograph’s
  purpose is to provide detailed information about the location, the long
  description should be more specific: “Photo of Ponte Vecchio showing its
  three stone arches and the Arno River.”

* For a chart, diagram, or illustration, the short description might be
  “Illlustration of Ponte Vecchio.” The long description should include the
  details conveyed visually, such as dimensions and materials used.

* For a map, a short description might be “Map showing location of Ponte
  Vecchio.” If the map is intended to provide directions to the bridge, the
  long description should provide text directions.
 
* For an icon, the short description should be equivalent to the information
  that the icon provides. For example, for a Course Syllabus link containing
  an EPUB icon, the text equivalent for the icon would be “EPUB,” which would
  be read as “Course Syllabus EPUB.”

* For an image that serves primarily as a link to another web page, the short
  description should describe the link’s destination, not the image. For
  example, an image of a question mark that serves as a link to a Help page
  should be described as “help,” not “question mark.”

=========================================
Provide Long Text Descriptions
=========================================

Consider using a caption to display long descriptions so that the information
is available to all learners. In the following example, the image element
includes the short description as the ``alt`` attribute and the paragraph
element includes the long description. ::

 <img src="image.jpg" alt="Photo of Ponte Vecchio">
 <p>Photo of Ponte Vecchio showing its three stone arches and the Arno river</p>
  
Alternatively, provide long descriptions by creating an additional unit or
downloadable file that contains the descriptive text and providing a link to
the unit or file below the image. ::
 
 <img src="image.jpg" alt="Illustration of Ponte Vecchio">
 <p><a href="description.html">Description of Ponte Vecchio Illustration</a></p>

===================================================
Handle Non-Informative Images Appropriately
===================================================

Images that do not provide information, including purely decorative images, do
not need text descriptions. For example, an icon that is followed by link text
that reads “Course Syllabus (EPUB)” does not need alternative text. 

For non-informative images that should be skipped by screen reading software,
include an ``alt`` attribute but leave it with an empty value. ::

   <img src="image.jpg" alt="">

If image elements do not include an ``alt`` attribute at all, depending on the
specific screen reader software, a screen reader might skip the image,
announce the image filename, or, in the case of a linked image, announce the
link URL.


=====================================================
Accessible Images Resources
=====================================================

* A `decision tree <http://www.4syllables.com.au/2010/12/text-alternatives-decision-tree/>`_ for choosing appropriate alternative text for images (Dey Alexander).

* `WebAim <http://webaim.org/techniques/alttext/>`_ provides general guidance
  on the appropriate use of alternative text for images.

* A more detailed description of HTML5 techniques for providing useful
  alternative text for images from `W3C <http://dev.w3.org/html5/alt-
  techniques/>`_.

* `The DIAGRAM Center <http://www.diagramcenter.org/webinars.html>`_,
  established by the US Department of Education (Office of Special Education
  Programs), provides guidance on ways to make it easier, faster, and more
  cost effective to create and use accessible images.
  

.. _Creating Accessible Course Materials:

************************************************
Creating Accessible Course Materials
************************************************

The source teaching materials for your course might exist in a variety of
formats. For example, your syllabus might be in MS Word, your presentation
slides in MS PowerPoint, and your textbooks in publisher-supplied PDF. It is
important to consider how accessible these supplemental materials are, before
making them available through your course.

Carefully consider the document format you choose for publishing your course
materials, because some formats support accessibility better than others.
Whenever possible, create course materials in HTML format, using the tools
available to you in edX Studio. When you make digital textbooks (ebooks)
available within your course, ask digital book publishers for books in either
`DAISY <https://en.wikipedia.org/wiki/DAISY_Digital_Talking_Book>`_ or `EPUB 3
<https://en.wikipedia.org/wiki/EPUB#Version_3.0.1_.28current_version.29>`_
format, or both. Both of these digital book formats include unparalleled
support for accessibility. However, simply supporting accessibility does not
always mean a document will be accessible. When you source ebooks from third
parties, it helps to ask the right questions about accessibility.

* Can screen readers read the document text?
* Do images in the document include alternative text descriptions?
* Are all tables, charts, and math provided in an accessible format?
* Does all media include text equivalents?
* Does the document have navigational aids, such as a table of contents,
  index, headings, and bookmarks?

Natively accessible formats like those mentioned above might not always be
available options. Other popular document formats included in edX courses
include PDF, Microsoft Word, Excel, or Powerpoint. Many of the same
accessibility techniques and principles that apply to authoring web content
apply to these document formats as well.

* Images must have descriptive text associated with them.
* Documents should be well structured.
* Information should be presented in a logical order.
* Hyperlinks should be meaningful and describe the destination.
* Tables should include properly defined column and row headers.
* Color combinations should be high contrast.

The information that follows provides some practical guidance to publishing
accessible course materials in popular formats.

.. contents::
   :local:
   :depth: 1


=====================================================
Accessible Course Materials Resources
=====================================================

* `The DAISY Consortium <http://www.daisy.org>`_ is a global partnership of
  organizations that supports and helps to develop inclusive publishing
  standards.

* `The EPUB 3 format <http://www.idpf.org/epub/30/spec/epub30-overview.html>`_
  is widely adopted as the format for digital books.

.. _Creating Accessible PDFs:

=====================================================
Creating Accessible PDF Documents
=====================================================

Not all ebooks are available in DAISY or EPUB 3 format. Portable Document
Format (PDF) is another common format for course materials, including
textbooks supplied by publishers. However, converting materials to PDF
documents can create accessibility barriers, particularly for learners with
visual impairments. Such learners rely on the semantic document structure
inherently available in HTML, DAISY, or EPUB 3 to understand and effectively
navigate PDF documents. For more information, see :ref:`HTML Markup
Resources`).

Accessibility issues are very common in PDF files that were scanned from
printed sources or exported from a non-PDF document format. Scanned documents
are simply images of text. To make scanned documents accessible, you must
perform Optical Character Recognition (OCR) on these documents, and proofread
the resulting text for accuracy before embedding it within the PDF file. You
must also add semantic structure and other metadata (headings, links,
alternative content for images, and so on) to the embedded text.

When you export documents to PDF from other formats, it is important to ensure
that the source document contains all the required semantic structure and
metadata before exporting. Unfortunately, some applications do not include
this information when exporting and require the author to add or "tag" the
document manually using PDF editing software. You should carefully consider
whether exporting to PDF is necessary at all.

.. note:: `OpenOffice <https://www.openoffice.org/>`_ and `LibreOffice
   <https://www.libreoffice.org/>`_ will produce the best results when you
   export documents to PDF.


Best Practices for Authoring Accessible PDF Documents
*******************************************************

* Explicitly define the language of the document so that screen readers know
  what language they should use to parse the document.

* Explicitly set the document title. When you export a file to PDF format, the
  document title usually defaults to the file name, not a human readable
  title.

* Verify that all images have alternative content defined or are marked as
  decorative only.

* Verify that the PDF file is "tagged". Make sure the semantic structure from
  the source document has been correctly imported to the PDF file.

* Verify that a logical reading order is defined. This is especially important
  for documents that have atypical page layouts or structure.

* If your document includes tables, verify that table headers for rows and
  columns are properly defined.
  
.. note::  When you export Microsoft Office documents as PDF, use the **Save
   as PDF** option. Make sure the **Document Structure Tags for
   Accessibility** option is selected (consult your software documentation for
   more details). PDFs generated from Windows versions of MS Office might be
   more accessible than those generated from Mac OS versions of MS Office.  If
   you are using Mac OS, we highly recommend exporting from OpenOffice or
   LibreOffice.

.. note:: When you export from OpenOffice or LibreOffice, use the **Export as
   PDF** option. Make sure the **Tagged PDF** option is selected.


Evaluating PDF Files for Accessibility
***************************************

EdX highly recommends using the tools available in Adobe Acrobat Pro
("Accessibility Checker") to evaluate your PDF files for accessibility. Adobe
Acrobat Pro also includes a tool ("Make Accessible") for fixing most common
accessibility issues.


Accessible PDF Resources
*******************************************************

* Microsoft provides detailed `guidance on generating accessible PDFs from
  Microsoft Office applications 
  <http://office.microsoft.com/en-gb/word-help/create-accessible-pdfs-HA102478227.aspx>`_, 
  including Word, Excel, and PowerPoint.

* Adobe provides documentation on how to `create and verify PDF accessibility <https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html>`_.

* `Adobe Accessibility <http://www.adobe.com/accessibility.html>`_ (Adobe) is a comprehensive 
  collection of resources on PDF authoring and repair, using Adobe’s products.

* `PDF Accessibility <http://webaim.org/techniques/acrobat/>`_ (WebAIM) provides a 
  detailed and illustrated guide on creating accessible PDFs . 

* The National Center of Disability and Access to Education has a collection
  of one-page `“cheat sheets” on accessible document authoring <http://ncdae.org/resources/cheatsheets/>`_.

* The Accessible Digital Office Document (ADOD) Project provides guidance on
  `creating accessible Office documents <http://adod.idrc.ocad.ca/>`_. 


=====================================================
Creating Accessible Word Documents
=====================================================

Many of the same accessibility techniques and principles that apply to
authoring web content also apply to creating Word documents.

* Images must have `descriptive text associated <https://support.office.com/en-us/article/Creating-accessible-Word-documents-D9BF3683-87AC-47EA-B91A-78DCACB3C66D#__toc275414986>`_ with them.

* Documents should be `well structured <https://support.office.com/en-us/article/Creating-accessible-Word-documents-D9BF3683-87AC-47EA-B91A-78DCACB3C66D#__toc275414990>`_.

* Hyperlinks should be `meaningful <https://support.office.com/en-us/article/Creating-accessible-Word-documents-D9BF3683-87AC-47EA-B91A-78DCACB3C66D#__toc275414991>`_ and describe the destination.

* Tables should include `properly defined column and row headers <https://support.office.com/en-us/article/Creating-accessible-Word-documents-D9BF3683-87AC-47EA-B91A-78DCACB3C66D#__toc271197283>`_.

* Color combinations should be high contrast.

* Verify the accessibility of your document using `Microsoft's Accessibility Checker <https://support.office.com/en-us/article/Check-for-accessibility-issues-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f?ui=en-US&rs=en-US&ad=US>`_.

In addition, follow these guidelines when you format Word documents.

* Keep formatting simple. Use headings, paragraphs, lists, images, and
  captions. Use tables for tabular data. Do not add unnecessary indents,
  rules, columns, blank lines, or typographic variation.

* Use standardized styles for formatting your text, such as Normal, Heading 1,
  and Heading 2, rather than manually formatting text using text styles and
  indents. Formatting text for its semantic meaning and not for its visual
  appearance allows users of assistive technology to consume and navigate
  documents effectively and efficiently.


Accessible Microsoft Word Resources
*************************************

* Microsoft guide to `creating accessible Word documents <https://support.office.com/en-us/article/Creating-accessible-Word-documents-D9BF3683-87AC-47EA-B91A-78DCACB3C66D>`_.

* Microsoft tool that allows you to `check Word documents for accessibility issues <https://support.office.com/en-us/article/Check-for-accessibility-issues-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f?ui=en-US&rs=en-US&ad=US>`_.


=====================================================
Creating Accessible Excel Documents
=====================================================

Many of the same accessibility techniques and principles that apply to
authoring data tables in HTML also apply to creating Excel spreadsheets.

* Images must have `descriptive text associated <https://support.office.com/en-us/article/Creating-accessible-Excel-workbooks-6CC05FC5-1314-48B5-8EB3-683E49B3E593#__toc271205010>`_ with them.

* Column and row headings should be `programmatically identified <https://support.office.com/en-us/article/Creating-accessible-Excel-workbooks-6CC05FC5-1314-48B5-8EB3-683E49B3E593#__toc271205011>`_. 

* Hyperlinks should be `meaningful <https://support.office.com/en-us/article/Creating-accessible-Excel-workbooks-6CC05FC5-1314-48B5-8EB3-683E49B3E593#__toc271197281>`_ and describe the destination.

* Use a unique and informative title for each worksheet tab.

* Do not use blank cells for formatting.

* Color combinations should be high contrast.

* Verify the accessibility of your workbook using `Microsoft's Accessibility Checker <https://support.office.com/en-us/article/Check-for-accessibility-issues-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f?ui=en-US&rs=en-US&ad=US>`_.


Accessible Microsoft Excel Resources
*******************************************************

* Microsoft guide to `creating accessible Excel workbooks <https://support.office.com/en-us/article/Creating-accessible-Excel-workbooks-6CC05FC5-1314-48B5-8EB3-683E49B3E593>`_.

* Microsoft tool that allows you to `check Excel workbooks for accessibility issues <https://support.office.com/en-us/article/Check-for-accessibility-issues-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f?ui=en-US&rs=en-US&ad=US>`_.


=====================================================
Creating Accessible Powerpoint Documents
=====================================================

Many of the same accessibility techniques and principles that apply to
authoring web content also apply to creating Powerpoint presentations.

* Images must have `descriptive text associated with them <https://support.office.com/en-us/article/Creating-accessible-PowerPoint-presentations-6F7772B2-2F33-4BD2-8CA7-DAE3B2B3EF25#__toc286131977>`_.

* Column and row headings should be `programmatically identified <https://support.office.com/en-us/article/Creating-accessible-PowerPoint-presentations-6F7772B2-2F33-4BD2-8CA7-DAE3B2B3EF25#__toc286131978>`_. 

* Hyperlinks should be `meaningful <https://support.office.com/en-us/article/Creating-accessible-PowerPoint-presentations-6F7772B2-2F33-4BD2-8CA7-DAE3B2B3EF25#__toc286131980>`_ and describe the destination.

* Use a unique and informative title for each slide.

* Ensure that information is `presented in a logical order <https://support.office.com/en-us/article/Creating-accessible-PowerPoint-presentations-6F7772B2-2F33-4BD2-8CA7-DAE3B2B3EF25#__toc286131984>`_

* Color combinations should be high contrast.

* Verify the accessibility of your presentation using `Microsoft's Accessibility Checker <https://support.office.com/en-us/article/Check-for-accessibility-issues-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f?ui=en-US&rs=en-US&ad=US>`_.

To make your content accessible and comprehensible to learners who use screen
reading software, start in Outline view and include all of your content as
text. After completing the outline, add design elements and images, and use
the picture formatting options in MS Powerpoint to include detailed text
descriptions of images that convey useful information to learners who cannot
view the images. Use the **Home > Drawing > Arrange > Selection Pane** option
to view the reading order of objects on each slide. If the reading order is
not logical, change the order of the objects.


Accessible Powerpoint Resources
*******************************************************

* Microsoft guide to `creating accessible PowerPoint presentations <https://support.office.com/en-us/article/Creating-accessible-PowerPoint-presentations-6F7772B2-2F33-4BD2-8CA7-DAE3B2B3EF25>`_.

* WebAIM's `PowerPoint Accessibility <http://webaim.org/techniques/powerpoint/>`_.

* Microsoft tool that allows you to `check Powerpoint documents for accessibility issues <https://support.office.com/en-us/article/Check-for-accessibility-issues-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f?ui=en-US&rs=en-US&ad=US>`_.


.. _Best Practices for Math Content:

************************************************
Use Best Practices for Mathematical Content
************************************************

Math in online courses can be challenging to deliver in a way that is
accessible to people with vision impairments.

Do not create images of equations instead of including text equations. Math
images cannot be modified by people who need a larger or high contrast
display, and cannot be read by screen reader software.

EdX uses `MathJax <https://www.mathjax.org>`_ to render math content in a format
that is clear, readable, and accessible to people who use screen readers.
MathJax works together with math notation such as LaTeX and MathML to render
mathematical equations as text instead of images. EdX recommends that you use
MathJax to display your math content.

======================================================
Accessible Mathematical Content Resources
======================================================

* The `DO-IT project <http://www.washington.edu/doit/are-there-guidelines-creating-accessible-math?465=>`_ from the University of Washington provides guidance on creating accessible math content.

* `AccessSTEM <http://www.washington.edu/doit/programs/accessstem/overview>`_
  provides guidance on creating accessible science, technology, engineering
  and math educational content.
  
* `MathJax <http://www.mathjax.org>`_ provides guidance on creating accessible
  pages with their display engine.

* The `Design Science News blog <http://news.dessci.com/accessible-math>`_
  shares information about making math accessible.


.. _Best Practices for Custom Content Types:

************************************************
Use Best Practices for Custom Content Types
************************************************

Using different content types in your courses can significantly add to the
learning experience for your students. This section covers how to design
several custom content types so that your course content is accessible all
learners.

.. contents::
   :local:


.. _Information Graphics:

=============================================================
Information Graphics (Charts, Diagrams, Illustrations)
=============================================================

Graphics are helpful for communicating concepts and information, but they can
present challenges for people with visual impairments. For example, a chart
that requires color perception or a diagram with tiny labels and annotations
will likely be difficult to comprehend for learners with color blindness or
low vision. All images present a barrier to learners who are blind.

EdX recommends that you follow these best practices for making information
graphics accessible to visually impaired students.

* Avoid using only color to distinguish important features of an image. For
  example, on a line graph, use a different symbol or line style as well as
  color to distinguish the data elements.

* Whenever possible, use an image format that supports scaling, such as .svg,
  so that learners can employ zooming or view the image larger. Consider
  providing a high resolution version of complex graphics that have small but
  essential details.

* For every graphic, provide a text alternative that provides the equivalent
  information that a sighted learner would obtain from viewing the graphic.
  For charts and graphs, a text alternative could be a table displaying the
  same data. See :ref:`Best Practices for Describing Images` for details about
  providing useful text alternatives for images.


.. _Simulations and Interactive Modules:

======================================================
Simulations and Interactive Modules
======================================================

Simulations, including animated or gamified content, can enhance the learning
experience. In particular, they benefit learners who might have difficulty
acquiring knowledge from reading and processing textual content alone.
However, simulations can also present some groups of learners with
difficulties. To minimize barriers to learning, consider the intended learning
outcome of the simulation. Is your goal to reinforce understanding that can
also come from textual content or a video lecture, or is it to convey new
knowledge that other course resources cannot cover? Providing alternative
resources will help mitigate the impact of any barriers.

Although you can design simulations to avoid many accessibility barriers, some
barriers, particularly in simulations supplied by third parties, might be
difficult or impossible to address for technical or pedagogic reasons.
Understanding the nature of these barriers can help you provide workarounds
for learners who are affected.  Keep in mind that attempted workarounds for
simulations supplied by third parties might require the supplier’s consent if
copyrighted material is involved.

Consider the following questions when creating simulations, keeping in mind
that as the course instructor, you enjoy considerable freedom in selecting
course objectives and outcomes. Additionally, if the visual components of a
simulation are so central to your course design, providing alternate text
description and other accommodations might not be practical or feasible.

* Does the simulation require vision to understand? If so, provide text
  describing the concepts that the simulation conveys.

* Is a computer mouse necessary to operate the simulation? If so, provide text
  describing the concepts that the simulation conveys.

* Does the simulation include flashing or flickering content that could
  trigger seizures?

  If so, and if this content is critical to the nature of the
  simulation, take these steps.
 
  * Do not make using the simulation a requirement for a graded assessment
    activity.

  * Provide a warning that the simulation contains flickering or flashing content.


.. _Online Exercises and Assessments:

======================================================
Online Exercises and Assessments
======================================================

For each activity or assessment that you design, consider any difficulties
that learners with disabilities might have in completing it, and consider
using multiple assessment options. Focus on activities that can be completed
and submitted by all learners.

Some students take longer to read information and input responses, such as
students with visual or mobility impairments and students who need time to
comprehend the information. If an exercise has a time limit, consider whether
the allowed time is enough for all learners to respond. Advance planning might
help to reduce the number of students requesting time extensions.

Some online exercise question types, such as the following examples, might be
difficult for students who have vision or mobility impairments.

* Exercises requiring fine hand-eye coordination, such as image mapped input
  or drag and drop exercises, might present difficulties to students who have
  limited mobility. Consider alternatives that do not require fine motor
  skills, unless, of course, such skills are necessary for effective
  participation in the course. For example, instead of a drag and drop
  exercise for mapping atoms to compounds, provide a checkbox or multiple
  choice exercise.

* Highly visual stimuli, such as word clouds, might not be accessible to
  students who have visual impairments. Provide a text alternative that
  conveys the same information, such as an ordered list of words in the word
  cloud.

.. _Third Party Content:

======================================================
Third-Party Content
======================================================

If you include links to third-party content in your course, be mindful of the
accessibility of such resources. EdX recommends that you test any links prior
to sharing them with learners.

You can use the eReader tool or :ref:`Add Files to a Course` to incorporate
third-party textbooks and other publications in PDF format into your course.
You can also incorporate such materials into your course in HTML format. See
:ref:`Creating Accessible PDFs` for guidance on working with third-party
supplied PDFs, and :ref:`Best Practices for HTML Markup` for guidance on
creating accessible HTML.


.. _Accessible Custom Content Resources:

======================================================
Accessible Custom Content Resources
======================================================

* `Effective Practices for Description of Science Content within Digital Talking Books <http://ncam.wgbh.org/experience_learn/educational_media/stemdx>`_, from the National Center for Accessible Media, provides best practices for describing graphs, charts, diagrams, and illustrations.

* `AccessSTEM <http://www.washington.edu/doit/programs/accessstem/overview>`_
  provides guidance on creating accessible science, technology, engineering
  and math educational content.

* The National Center on Educational Outcomes (NCEO) provides `Principles and Characteristics of Inclusive Assessment and Accountability Systems <http://www.cehd.umn.edu/nceo/onlinepubs/Synthesis40.html>`_.
  

.. _Creating Accessible Media:

************************************************
Create Accessible Media
************************************************

Media-based course materials help to convey concepts and can bring course
information to life. We require all videos in edX courses to include
interactive transcripts that can be read by screen reader software. This
built-in universal design mechanism enhances your course’s accessibility. When
you create your course, you need to factor in time and resources for creating
these transcripts.


=====================================================
Audio Transcripts
=====================================================

Audio transcripts are essential for presenting the readable equivalent of
audio content to learners who cannot hear. They can also be helpful for
learners whose native languages are languages other than English. Synchronized
transcripts allow learners who cannot hear to follow along with the video and
navigate to a specific section of the video by selecting some location within
the transcript text. In addition, all learners can use transcripts of media-
based learning materials for study and review.

A transcript starts with the text version of a video’s spoken content. If you
created your video using a script, you have a great start on creating the
transcript. Just review the recorded video and update the script as needed.
Otherwise, you will need to transcribe the video yourself or engage someone to
do it. There are many companies that will create timed video transcripts
(transcripts that synchronize the text with the video using time codes) for a
fee.

The edX platform supports the use of transcripts in .srt format. When you
integrate a video file into the platform, you should also upload the .srt file
of the timed transcript for such video. See :ref:`Working with Video
Components` for details on how to add timed transcripts.


=====================================================
Descriptions in Video
=====================================================

When you create video segments, consider how you will convey information to
learners who cannot see what is happening in a video. Even if you have audio
transcripts that can be read by screen readers, actions that are only visible
on screen without any audible equivalent are not accessible to learners who
have visual impairments.

For many topics, you can fully cover concepts in the spoken presentation. If
it is practical to do so, you should audibly describe visual events as they
happen in the video. For example, if you are illustrating dropping a coin and
a feather together from a height, you should consider narrating your actions
as you perform them.


=====================================================
Downloadable Transcripts
=====================================================

For both audio and video transcripts, consider including a text file that
students can download and review using tools such as word processing, screen
reader, or literacy software. The downloadable transcript should be text only,
without time codes.


=====================================================
Accessible Media Resources
=====================================================

Accessible Digital Media Guidelines provides detailed advice on creating
online video and audio with accessibility in mind.
http://ncam.wgbh.org/invent_build/web_multimedia/accessible-digital-media-guide


.. _Best Practices for HTML Markup:

************************************************
Use Best Practices for HTML Markup
************************************************
 
HTML is the best format for creating accessible content. It is well supported
and adaptable across browsers and devices. Also, the information in HTML
markup helps assistive technologies, such as screen reader software, to
provide information and functionality to people with vision impairments.

Most of the problem type templates in edX Studio conform to our recommended
best practices in terms of good HTML markup. You can manually add appropriate
HTML tagging even if it does not exist in the component template. Depending on
the type of component you are adding to your course in edX Studio, the raw
HTML data is available either automatically or by selecting the “Advanced
Editor” or “HTML” views.

Keep the following guidelines in mind when you create HTML content.

* Use HTML tags to describe your content’s meaning rather than its appearance.
  For example, you should tag a title with the appropriate heading level (for
  example ``<h2>``) rather than making the heading simply appear like a heading
  by using visual elements such as bold text and a larger font size. Format
  list items as a list rather than using bullets and indents, so that they are
  related in the code. Using HTML to describe your content's meaning is
  valuable for learners who screen readers, which, for example, can read
  through all headings of a specific level or announce the number of items in
  a list.

* Use HTML heading levels in sequential order to represent the structure of a
  document. Well-structured headings help learners and screen reader users to
  navigate a page and find what they are looking for.

* Use HTML list elements to group related items and make content easier to
  skim and read. HTML offers three kinds of lists.

  *  Unordered lists, where the order of items is not important. Each item is
     marked with a bullet.

  *  Ordered lists, where the order of items is important. Each item is listed
     with a number.

  *  Definition lists, where each item is represented using term and
     description pairs (like a dictionary).

* Use table elements to format information that works best in a grid format,
  and include descriptive row and column headings. Tag row and column headers
  with the ``<th>`` element so screen readers can effectively describe the
  content in the table.


.. _HTML Markup Resources:

====================================================
HTML Markup Resources
====================================================

* `Creating Semantic Structure <http://webaim.org/techniques/semanticstructure/>`_ provides guidance on reflecting the semantic structure of a web page in the underlying markup (WebAIM).
 
* `Creating Accessible Tables <http://webaim.org/techniques/tables/data>`_
  provides specific guidance on creating data tables with the appropriate
  semantic structure so that screen readers can correctly present the
  information (WebAIM).
  

.. _Universal Design for Learning:

************************************************
Apply Universal Design for Learning
************************************************

Universal Design for Learning focuses on delivering courses in a format so
that as many of your learners as possible can successfully interact with the
learning resources and activities you provide them, without compromising on
pedagogic rigor and quality.

The principles of Universal Design for Learning can be summarized by the
following points.

#. Present information and content in various ways. 
#. Provide more than one way for students to express what they know.
#. Stimulate interest and motivation for learning.

Course teams can apply these principles in course design by following several
guidelines.

* Design resources and activities that can be accessed by learners in
  a variety of ways. For example, if there is a text component, provide the
  ability to enlarge the font size or change the text color. For images and
  diagrams, always provide an equivalent text description. For video, include
  text captions or a transcript as well as an audio track.

* Provide multiple ways for learners to engage with information and
  demonstrate their knowledge. This is particularly important to keep in mind
  as you design activities and assessments.
 
* Identify activities that require specific sensory or physical capability and
  for which it might be difficult or impossible to accommodate the
  accessibility needs of learners. For example, an activity that requires
  learners to identify objects by color might cause difficulties for learners
  with visual impairments. In these cases, consider whether there is a
  pedagogical justification for the activity being designed in that way. If
  there is a justification, communicate these requirements to prospective
  learners in the course description and establish a plan for responding to
  learners who encounter barriers. If there is no justification for the
  requirements, edX recommends that you redesign the learning activities to be
  more flexible and broadly accessible.
 
=======================================
Universal Design for Learning Resources
=======================================

* `Delivering Accessible Digital Learning (JISC Techdis) <http://www.jisctechdis.ac.uk/techdis/resources/accessiblecontent>`_ provides a useful overview of an inclusive approach to course design.

* `The National Center on Universal Design for Learning <http://www.udlcenter.org/implementation/postsecondary>`_ provides a helpful overview on Universal Design for Learning.
  

