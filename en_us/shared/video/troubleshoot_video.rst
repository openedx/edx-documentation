.. _Troubleshoot Video Problems:

################################
Troubleshooting Video Problems
################################

When you use video, you might experience one of the following problems.

* If you (or your beta testers or learners) encounter an error when you view a
  course video, try one of the following troubleshooting methods.

  * Verify that the viewer's browser is up to date. For example, some older
    versions of the Mozilla Firefox browser did not play .mp4 video files.
    These problems do not occur in more recent browser versions.

    For more information, see `Media formats supported by the HTML audio and
    video elements`_.

  * Verify that file metadata, particularly the MIME type, is correctly set on
    the host site. For example, when edX offered support for Internet Explorer
    10 browsers, videos did not play if the MIME type was not set. The HTTP
    header ``Content-Type`` had to be set to video/mp4 for an .mp4 file.

    As an example of how you might set metadata on a video host site, the
    *Console User Guide* for Amazon Simple Storage Service (S3) provides
    information about `editing object metadata`_.

* If two sets of captions appear when you select **CC** on the video player,
  YouTube and your course might both be providing captions for the video. This
  problem can occur when YouTube is the host service for the video and your
  YouTube account settings for playback are set to always show captions. To
  correct this problem, select **CC** again or change your YouTube account
  settings.


  .. include:: ../../../links/links.rst
