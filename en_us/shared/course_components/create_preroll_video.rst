.. _Adding a PreRoll Video:

*******************************************
Adding a Pre-Roll Video to Your edX Course
*******************************************

.. note:: Only courses that run on the edx.org website can include a pre-roll
 video. In addition, your organization must work with edX partner support to
 encode and host your video files. For more information, see `Processing Video
 Files`_.

You can create a short video message and configure it to play before the other
videos in your course. For example, a pre-roll video might provide learners
with information about your organization, or about the next course in an
XSeries. One pre-roll video can be included in each course.

.. contents::
  :local:
  :depth: 1

=========================================
How Learners Experience a Pre-Roll Video
=========================================

When a learner selects any video in the course, the defined course pre-roll
video might automatically begin to play before the selected video plays. The
pre-roll video does not play every time a learner plays any of the course
videos. Instead, it plays on an infrequent schedule.

While the pre-roll video plays, the video player includes these additional
options for learners to select.

* **Skip**: The pre-roll video immediately stops playing and the course video
  selected by the learner begins playing.

* **Do not show again**: The learner opts out of viewing the pre-roll video.
  The pre-roll video does not play for that learner again.

The following constraints control delivery of the pre-roll video to learners.

* For each enrolled learner, the pre-roll video plays a maximum of once every
  seven days.

* The pre-roll video plays only in web browsers. It does not play in the edX
  mobile applications.

=========================================
Preparing the Pre-Roll Video
=========================================

To include a pre-roll video in your course, you prepare the video file and its
transcript file or files and upload them to Studio. Because the pre-roll video
is not part of the course that is defined in the course outline, you do not use
a video component to add the pre-roll video to your course.

Guidelines for Creating Pre-Roll Videos
*********************************************

EdX encourages partners to consider these suggestions when deciding on the
content for their pre-roll videos.

* Use the pre-roll video as a way to promote general awareness of your
  organization.

* For a course that has sponsors, use the pre-roll video to acknowledge the
  sponsors.

* Use pre-roll videos to engage learners by making timely announcements related
  to the course.

* Avoid messaging that encourages learners to leave the course website or
  participate in activities that are not related to the course content.

The following guidelines can help ensure that the video that you create reaches
as many learners as possible.

* The optimum length for a pre-roll video is 5 to 10 seconds. The video player
  stops playing longer files after 35 seconds.

* Before you create a pre-roll video, be sure to review :ref:`Creating
  Accessible Media`.

* The video must have at least one accompanying transcript.

* The video must be in .mp4 or .mov format. For more information, see
  `Specifications for Successful Video Files`_ in the *Processing Video Files*
  guide.

Upload the Pre-Roll Video File
*********************************************

After you create the file, you upload it on the Studio **Video Uploads** page.
The file goes through the automated encoding and hosting process, and is given
an identifying video ID. For more information, see `Upload Video Files`_ in
the *Processing Video Files* guide.

Prepare Pre-Roll Video Transcript Files
*****************************************

You must provide at least one transcript file for your pre-roll video. You can
provide additional transcript files in multiple languages.

* If you have transcript files in more than one language, edX recommends that
  you include identifying `ISO 639-1 codes`_ in your transcript file names.

* If you supply transcripts in Chinese, you can use supplemental codes to
  identify the character set used. For a Simplified Chinese transcript, use
  zh_HANS, and for a Traditional Chinese transcript, use zh_HANT.

To prepare transcript files for a pre-roll video, follow these steps.

#. On your local computer or network, locate the .srt transcript file or files
   for the pre-roll video.

   If your transcription service delivers your .srt files to YouTube, you must
   download the files from YouTube and save them locally.

#. Verify that each transcript file has a unique name. If you have transcript
   files in more than one language, be sure to include the ISO 639-1 language
   code as part of the file name. Example file names follow.

   ::

    edx_preroll_en.srt
    edx_preroll_fr.srt
    edx_preroll_ru.srt
    edx_preroll_zh_HANS.srt

Upload Pre-Roll Video Transcript Files
***************************************

To upload transcript files for a pre-roll video into Studio, follow these
steps.

#. Open your course in Studio.

#. Select **Content**, and then **Files & Uploads**.

#. Upload the files. For more information, see :ref:`Add Files to a Course`.

================================================
Configuring a Pre-Roll Video for Your Course
================================================

To configure a pre-roll video and its transcript files for your course, you use
an advanced setting in Studio. Because the pre-roll video is not part of the
course that is defined in the course outline, you do not use a video component
to add the pre-roll video.

You can identify only one file as the pre-roll video at a time, but you can
replace the file with a new one, or delete the file, at any time.

Identify the Pre-Roll Video and Its Transcripts
************************************************

You identify the pre-roll video for your course in Studio. To make finding and
entering the information that you need on different pages in Studio easier, edX
recommends that you use several browser windows.

To identify the pre-roll video for your course, follow these steps.

#. Open three browser windows, and open your course in Studio in each one.

#. In one of the browser windows, select **Content**, and then **Video
   Uploads**. On this page, locate the video ID of the pre-roll video file.

#. In another window, select **Content**, and then **Files & Uploads**. On
   this page, verify that each transcript file has a Studio URL.

#. In the last browser window, select **Settings**, and then **Advanced
   Settings**. On this page you configure the course pre-roll video.

#. Scroll down to the **Video Pre-roll** policy key.

#. Between the braces in this field, enter ``"video_id":`` and then a space,
   followed by the ID value in quotation marks from the **Video Uploads**
   page.

   ::

     {"video_id": "83cef264-d6f5-4cf2-ad9d-0178ab8c92cd"}

#. After the closing quotation mark, add a comma and a space.

   ::

     {"video_id": "83cef264-d6f5-4cf2-ad9d-0178ab8c92cd", }

#. After the comma and the space, enter ``"transcripts": {}``.

#. Inside the pair of braces for the transcripts, you enter a value pair to
   identify the language of the transcript file and then its file name from
   the **Files & Uploads** page.

   .. note:: You identify the language of each transcript file with an
    ISO 639-1 code or with zh_HANS or zh_HANT. If your transcript file names do
    not already include a language code, you will need a reference such as this
    list of `ISO 639-1 codes`_.

   ::

     {"video_id": "83cef264-d6f5-4cf2-ad9d-0178ab8c92cd", "transcripts": {"en": "edx_preroll_en.srt"}}

   You add the language code in quotation marks, followed by a colon and a
   space, and then add the file name in quotation marks. To identify
   transcript files in Chinese, you can include ``"zh_HANS"`` for Simplified
   Chinese or ``"zh_HANT"`` for Traditional Chinese. Note that you enter only
   the file name for each transcript, and not its complete Studio URL.

#. If you have other transcript files, you add them in comma separated pairs
    after your first ``"language": "URL"`` pair.

    ::

      {"video_id": "83cef264-d6f5-4cf2-ad9d-0178ab8c92cd", "transcripts": {"en": "edx_preroll_en.srt", "zh_HANS": "edx_preroll_zh_HANS.srt", "zh_HANT": "edx_preroll_zh_HANT.srt"}}


#. Select **Save Changes**. Studio resequences and reformats your entry.
    Scroll back to **Video Pre-roll** to verify that your entry was saved as
    you expect. Entries that do not contain all of the required punctuation
    characters revert to the previous value when you save, and no warning is
    presented.

    ::

      {
          "transcripts": {
              "en": "edx_preroll_en.srt",
              "zh_HANS": "edx_preroll_zh_HANS.srt",
              "zh_HANT": "edx_preroll_zh_HANT.srt"
          },
          "video_id": "83cef264-d6f5-4cf2-ad9d-0178ab8c92cd"
      }

Replace the Pre-Roll Video and Its Transcripts
***********************************************

You can change the pre-roll video for your course at any time.

.. Note:: The replacement pre-roll video is not shown to learners who have
 already selected the **Do not show again** option.

To replace the pre-roll video for your course, follow these steps.

#. Add the new pre-roll video file to your course on the **Video Uploads**
   page.

#. Add the transcript files for the pre-roll video on the **Files & Uploads**
   page.

#. On the **Advanced Settings** page, edit the **Video Pre-roll** policy key.

#. Replace the previous video ID with the ID for the new pre-roll video file.

#. Replace the previous transcript file names with the new names. If needed, be
   sure to update the language codes for the transcripts.

#. Select **Save Changes**.


Remove the Pre-Roll Video
****************************

To remove the pre-roll file from your course, follow these steps.

#. On the **Advanced Settings** page, delete the contents of the **Video
   Pre-roll** field.

#. Enter a pair of braces in the field.

   ::

    {}

#. Select **Save Changes**.


.. _Processing Video Files: http://processing-video-files.readthedocs.org/en/latest/
.. _Specifications for Successful Video Files: http://processing-video-files.readthedocs.org/en/latest/video_uploads.html#specifications-for-successful-video-files
.. _Upload Video Files: http://processing-video-files.readthedocs.org/en/latest/video_uploads.html#upload-video-files
.. _ISO 639-1 codes: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
