.. _Feature_Description_Xpert_Course_Translations:

##############################################
Feature Description: Xpert Course Translations 
##############################################

.. only:: Partners

  Two translation features will be available on the edX platform

   #. **Video transcript translations:** Machine generated transcripts produced from existing english transcripts, originally provided by content creators.
  
   #. **Unit page translations:** The ability to replace unit page content with translated versions of unit page content in real time.

      a. V1 - Generate Spanish or Arabic translated versions of HTML+Problem blocks.

  Combined, these features support the concept of **Xpert Course Translation**.

  *****************************
  Video transcript translations
  *****************************

  Video transcripts can be generated through a translations UI on the videos page in Studio for a course. An existing english transcript is required for translations of video transcripts. For more information on obtaining an english transcript see `readthedocs <https://edx.readthedocs.io/projects/edx-partner-course-staff/en/latest/video/prepare_video/obtain_transcript.html>`_.

  .. image:: ../../images/xpert_transcript_settings_link.png
     :alt: Studio page showing link to Transcript settings
     :align: center

  |

  .. image:: ../../images/xpert_transcript_settings_options.png
     :alt: Studio pane showing links to generate translations in different languages
     :align: center
     :scale: 70 %

  |

  If video transcript translations are enabled for a course, learners can select from a list of available languages to view the transcript 

  .. image:: ../../images/xpert_transcript_caption_select.png
     :alt: Course video player showing list of generated transcripts
     :align: center

  |

  Once a learner selects a language for their translated transcript, that choice is persisted as the default for the rest of the videos in a course. Learners can update their transcript language at any time using the video player UI.

  =========================================
  Video transcript translation limitations:
  ========================================= 

  - Does not currently apply to youtube video transcripts 

  - An existing English transcript is required for generating transcripts in other languages.

  **********************
  Unit page translations
  **********************

  Users will be able to select an icon on the unit page of a course (pictured below):

  .. image:: ../../images/xpert_unit_translations_widget.png
     :alt: Course unit showing Xpert translations widget
     :align: center

  |

  .. image:: ../../images/xpert_unit_translations_language_selector.png
     :alt: Course unit showing Xpert translations language selector
     :align: center

  |

  Once users have selected a language to translate the course into, each new unit page they encounter will have the content translated into the specified language. 

  ==================================
  Unit page translation limitations:
  ==================================

  - Currently only on platform HTML and Problem Blocks are available for translation.

  - The languages available for translation are currently Spanish and Arabic.