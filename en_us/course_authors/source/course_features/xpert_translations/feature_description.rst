.. _Enabling_Xpert_Unit_Summaries:

##############################################
Feature Description: Xpert Course Translations 
##############################################

.. only:: Partners

  Two translation features will be available on the edX platform

   #. **Video transc1ript translations:** Machine generated transcripts produced produced from existing english transcripts, originally provided by content creators.
  
   #. **Unit page translations:** The ability to real-time replace unit page content with translated versions of unit page content.

      a. V1 - Generate Spanish or Arabic translated versions of HTML+Problem blocks.

  Combined, these features support the concept of **Xpert Course Translation** - where on average ~85% of course content is expected to be available in the languages selected for V1 (note, currently ~65% of content is available for translation in beta version.)

  *****************************
  Video transcript translations
  *****************************

  Video transcripts can be generated through a translations UI on the videos page in Studio for a course.

  For more information on how this works see `readthedocs <https://edx.readthedocs.io/projects/edx-partner-course-staff/en/latest/video/prepare_video/obtain_transcript.html>`_.

  .. image:: ../../images/xpert_transcript_settings_link.png
     :alt: Stuio page showing link to Transcript settings

  .. image:: ../../images/xpert_transcript_settings_options.png
     :alt: Studio pane showing links to generate translations in different languages

  If video transcript translations are enabled for a course, users can select from a list of available languages to view the transcript 

  .. image:: ../../images/xpert_transcript_caption_select.png
     :alt: Course video player showing list of generated transcripts

  Once a learner selects a language for their translated transcript, that choice is persistent as the default for the rest of the videos in a course. Users can update their language preference at any time. 

  =========================================
  Video transcript translation limitations:
  ========================================= 

  - Does not currently apply to youtube video transcripts 

  - An existing english transcript is required for translation into other languages 

  **********************
  Unit page translations
  **********************

  Users will be able to select a new icon on the unit page of a course (pictured below):

  .. image:: ../../images/xpert_unit_translations_widget.png
     :alt: Course unit showing Xpert translations widget

  .. image:: ../../images/xpert_unit_translations_language_selector.png
     :alt: Course unit showing Xpert translations language selector

  Once users have selected a language to translate the course into, each new unit page they encounter will have the content translated into the specified language. 

  ==================================
  Unit page translation limitations:
  ==================================

  This feature is currently limited to translating HTML (aka HTML (aka text)) blocks, and Spanish language.  We are anticipating a fast follow to enable the translation of problem blocks and offering Arabic language and offering Arabic language before making this feature widely available.