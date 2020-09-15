.. _Configure Transcripts:

####################################
Configuring Transcript Behavior
####################################

As a best practice, transcripts should always be provided, so that course
videos meet accessibility requirements. Video transcripts are displayed in the
language selected by the learner in the video player if they are available in
that language. Otherwise, by default video transcripts fall back to an English
language transcript. In cases where no transcript is available, you can
configure Open edX so that the video player does not display the caption and
transcript buttons.

You can configure the default transcript behavior using the
``FALLBACK_TO_ENGLISH_TRANSCRIPTS`` feature flag. By default, this feature
flag is set to ``TRUE``. If you set it to ``FALSE``, then the video transcript
will not fall back to an English language transcript and if no transcript is
available, the caption and transcript buttons are not displayed in the video
player.

***************************************
Configuring the Transcript Feature Flag
***************************************

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

To set the ``FALLBACK_TO_ENGLISH_TRANSCRIPTS`` feature flag, you modify the
``lms.yml`` and ``studio.yaml`` files, which are located one level above 
the ``edx-platform`` directory.

#. In the ``lms.yml`` and ``studio.yaml`` files, in the ``FEATURES``
   dictionary, change the value of ``FALLBACK_TO_ENGLISH_TRANSCRIPTS`` to
   ``FALSE``.

#. Save the ``lms.yml`` and ``studio.yaml`` files.

.. include:: ../../../links/links.rst
