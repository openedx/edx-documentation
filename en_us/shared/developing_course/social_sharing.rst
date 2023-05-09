
################################################
Sharing Course Content on Social Media Platforms
################################################

EdX course video content can now be shared to a select list of Social Media platforms.  At the time of writing, this feature is in limited release, please reach out to your platform operator to include this feature.

.. _Supported Platforms:

************************************************
Supported Platforms
************************************************
Currently, edX supports sharing content to 

* Twitter
* Facebook
* LinkedIn

Other platforms may be added in a future release.


.. _Enabling Content for sharing:

************************************************
Enabling Content for sharing
************************************************

:ref:`The course outline<Developing Your Course Outline>` will have a new selector near the top of the page, labeled "Video Sharing". This control enables you to manage how video content in your course will be shared. Options are:

* Per Video
* All Videos
* No Videos

.. _Sharing Control:

****************************************
Sharing Control
****************************************
The different options in the control will enable you to share all videos in a course, share no videos, or allow control on a per-video basis. The default state for a course is *Per Video*.

.. note:: Setting the control to *All Videos* or *No Videos* will enable or disable sharing for all videos in the course, **regardless of any per-video setting**. Per-video settings **are** preserved and will apply if the course is set to *Per Video* 

Per Video
=========

This is the default state for a course. The default state for a video is unshared. To change the sharing state for a video, click the edit option for the video and navigate to the *Social Sharing* section. This section of the editor will indicate if this video is shared and if the course or the video controls if it is shared or not.

.. note:: Per video share state is persisted even if the course is set to all or no videos. Changing the course to per-video will restore what ever state the video was in beforehand.

All Videos
==========

Setting the course to *All Videos* will enable the social sharing links on all course videos.

No Videos
=========
Setting the course to *No Videos* will disable the social sharing links on all course videos.  Any previously shared video links will no longer work, clicking on one in a social media platform  in this state will return a 404 error.

