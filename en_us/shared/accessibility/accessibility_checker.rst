.. _Accessibility Checker:

######################
Accessibility Checker
######################
* This feature allows you to check HTML in the editor for various 
  WCAG and Section 508 accessibility problems.
* The Accessibility Checker focuses on exceeding WCAG "A", "AA", 
  and "AAA" levels.
* The Accessibility Checker enables content authors to check for 
  accessibility problems using an in-editor dialog, complete with 
  a repair feature that corrects the errors on their behalf.

*******************************
Accessibility Checker Use Case
*******************************
When using the Accessibility Checker, begin by looking for the 
accessibility icon . As you enter content into the Rich Content 
Editor, the Accessibility Checker will automatically start looking 
for any potential accessibility issues. Click on the icon to learn 
more.

After clicking it, the Accessibility Checker will open in the 
sidebar menu with details on each issue found. Navigate between 
the items to learn about each issue and apply the fixes (see 
images below). 

.. image:: ../../../shared/images/AccessibilityCheckerWidget.png
  :alt: an image of the accessibility checker icon and menu. The 
   accessibility checker lists various accessibility issues and 
   includes an auto repair capability.
  :width: 600

************************************************
Accessibility Checker Review
************************************************

#. **Adjacent links**: Adjacent links with the same URL should be 
   a single link. This rule verifies link errors where the link text 
   may include spaces and break the link into multiple links.

#. **Headings**: Headings should not contain more than 120 
   characters.

#. **Image alt text**: Images should include an alt attribute 
   describing the image content.

#. **Image alt filename**: Image filenames should not be used as 
   the alt attribute describing the image content. Currently, files 
   uploaded directly to Canvas create a redirect that does not 
   properly verify image filenames.

#. **Image alt length**: Alt attribute text should contain fewer 
   than 120 characters.

#. **Large text contrast**: Text larger than 18pt (or bold 14pt) 
  should display a minimum contrast ratio of 3:1.

#. **Lists**: Lists should be formatted as lists.

#. **Sequential headings**: Heading levels should not be skipped 
   (e.g. H2 to H4). However, the tool does not check if the first 
   header starts with H2 or whether the headings are sequential 
   with the rest of the content in the page. Tables do not begin 
   with H1, which is designated for the page title.

#. **Small text contrast**: Text smaller than 18pt (or bold 14pt) 
   should display a minimum contrast ratio of 4.5:1.

#. **Table captions**: Tables should include a caption describing 
   the contents of the table.

#. **Table header scope**: Table headers should specify scope and 
   the appropriate structure.

#. **Table header**: Tables should include at least one header.

***************************************
Advantage of the Accessibility Checker
***************************************

The Accessibility Checker has the primary advantage of being very 
low effort and having intelligible warnings and solutions for 
content creators, who are most likely not accessibility experts. 
We have a general goal of minimizing instances of asking content 
creators to edit the HTML view of course content in order to make 
it WCAG-compliant, and this helps with that significantly. 

Course content will be more accessible, consistent, and predictable 
because the TINYMCE accessibility checker reviews for the following 
content:

* Heading levels
* Lists
* Contrast ratios on text
* Image alt text
* Tables
* Captions
* Scopes
