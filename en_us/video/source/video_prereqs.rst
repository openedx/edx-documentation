.. _Video Getting Started:

###########################
Getting Started with Video
###########################

.. _Video Processing Overview:

******************************
Video Processing Overview
******************************

Videos are one of the most important assets of an online course. Making
course videos available to students who are located all over the world, and
who are accessing course content with different devices and Internet
connectivity constraints, can be a complex undertaking.

* For a video to play at locations around the world, it needs to be available
  from more than one host site. 

* For a video to play on different devices, including both desktop computers
  and smart phones, it needs to be available in several different formats.

To help course teams at partner institutions meet the challenge of delivering
high quality video experiences to as many students as possible, edX offers
media hosting services to address alternative playback and download needs.

* The edX media team establishes accounts for you at YouTube and Amazon Web
  Services (AWS).

* To ensure optimal playback quality for the original video files that your
  course teams upload, the edX media uses an automated process to create
  multiple file formats.

After these services are set up for your institution and course, course teams
only need to upload a single file to Studio for each of the videos they want
to include in their course. EdX completes the encoding and hosting process for
your video files.

.. note:: The edX automation process does not include captioning services. 
 Your course teams use your institution's current workflow to generate
 transcripts for your video files. See the section on `creating a video
 transcript`_ in the *Building and Running an edX Course* guide.

===================================
Prerequisite Tasks
===================================

Before your course teams can begin to upload videos in Studio, you work with
the edX media team to make sure that these preparatory tasks are complete.

* :ref:`Identify Video Administrators`

* :ref:`Establish Access to YouTube Account`

* :ref:`Create YouTube Channels`

* :ref:`Add a Channel Manager`

* :ref:`Enable Video Upload in Studio` 

When these tasks are complete, your course teams can upload original video
files in .mp4 or .mov format to Studio. After video files upload successfully,
an automated process starts to create additional file formats and transfer the
files to YouTube and AWS, so that the videos are ready for students to access
and download. The automated process takes 24 hours to complete. Course teams
can track file status on the Studio **Video Uploads** page as the videos
upload to edX and then go through automated processing.

.. important:: The tasks described in this section rely on the use of
 third-party tools and software. Because these tools are subject to change by
 their respective owners, the steps provided here are intended as
 guidelines and not as exact procedures.

.. _Identify Video Administrators:

****************************************
Identify Video Administrators
****************************************

Each partner institution identifies one person, or more often several
people, to be video administrators. The video administrators periodically use
the YouTube Content Management System (CMS) to access the video files that
are hosted by YouTube and the reports that YouTube produces.

Video administrators use the CMS to access your YouTube channels, the
videos associated with those channels, and YouTube’s reporting tools. In
general, the CMS enables an administrator to:

* Manage ownership of files hosted on YouTube.
* :ref:`Create a YouTube channel<Create YouTube Channels>` that is linked to
  your YouTube account for each course.
* :ref:`Grant management access<Add a Channel Manager>` to each YouTube
  channel to members of the corresponding course team.
* Download reports and other analytics that measure views.

Video administrators also work with course teams and the edX media team to
distribute information and resolve questions about video files. 

EdX recommends that organizations identify specific individuals to be the
video administrators for all of your courses. By working with the edX team
over time, the video administrators can develop repeatable and consistent
procedures for managing your video assets.

.. _Establish Access to YouTube Account:

****************************************
Establish Access to YouTube Account 
****************************************

=========================================
Video Administrator Access to the Account 
=========================================

For :ref:`video administrators<Identify Video Administrators>` to use the
YouTube CMS, they must have administrative access to your CMS account. Because
account access is granted to specific email addresses, the edX media team
works with one of your video administrators to set up an email address
specifically for this purpose and give it administrative privileges.

This procedure only needs to be completed once and can be done by one of
the video administrators.

===================================
Establishing Access to the Account 
===================================

#. Create a single Google email, or Gmail, account. The recommended format
   for the account name is your edx.org member identifier followed by
   "-CMSmanager". For example, ``HarvardX-CMSmanager@gmail.com`` or 
   ``MITx-CMSmanager@gmail.com``.

#. Send the email address to the edX media team at ``media@edx.org``.

   On receipt, the media team adds the Gmail address to your YouTube CMS
   account and gives the account administrative privileges. This process
   results in an activation message that is sent to your CMSmanager Gmail
   account. Access to the CMS account is not provided until activation is
   complete.

3. Check the Gmail account for the activation message from YouTube. These
   messages are typically routed to the Gmail "Social" inbox.

#. To activate the account, click the "Visit the sign-up page" link in the
   email message. A browser opens to the YouTube signup page.

#. Click **Use existing Google account**. You can now access the CMS account.

All of your video administrators use the same Gmail account to log in to the
YouTube CMS. This approach helps ensure that staffing changes do not
interrupt your access to the YouTube account. Video administrators can also
create channel managers, who have limited administrative access to specific
channels in your account.

.. _Create YouTube Channels:

****************************************
Create YouTube Channels
****************************************

===============================
About YouTube Channels
===============================

For each course that your institution offers, a video administrator creates a
YouTube "channel" to store that course's video files. A channel is,
essentially, a folder or directory that stores the video files that play on
YouTube. Organizing your video files into channels by course simplifies file
delivery and management. YouTube also collects analytics for each channel that
you create. CMS Analytics offers reports and data that can help you evaluate
channel and video performance, including views, subscribers, watch time, and
more.

.. note:: The following procedure only needs to be completed once per 
 course, but it must be complete before the course team begins to add videos
 to the course in Studio.

===============================
Creating YouTube Channels
===============================

#. In your browser, access YouTube by going to https://cms.youtube.com.

#. Use your CMSmanager Gmail address for video administrators to log in to
   the CMS account. The email address that you log in with is the owner of
   any channels that you create.

#. In the navigation bar at left, click **CHANNELS**. A list of your channels
   appears.

#. Above the list of channels click **Create New**. A popup window opens.

#. Leave the checkboxes under **Permissions** unselected, and then click
   **Continue**. (You can change the channel's permission settings at any
   time.) The popup window presents fields for information about the channel.

#. Provide a channel name that clearly and uniquely identifies the course.
   Example channel names include Water201x and Foundations of Chinese
   Thought.

#. For the category, select **Company, Institution, or Organization**.

#. Agree to the terms and then click **Done**. The list of channels now
   includes the channel that you just set up.

You can now notify the edX media team that the channel has been created. You
can also give management access to the channel to members of the
corresponding course team.

.. _Add a Channel Manager:

************************************
Add a Channel Manager
************************************

===============================
About Channel Managers
===============================

Video administrators can give members of course teams management access to a
channel in a process that is similar to :ref:`establishing access to the
YouTube account<Establish Access to YouTube Account>`. To do so, they obtain
the email addresses of one or more of the course team members and then invite
them to manage the channel.

After a course team uploads video files to Studio, an automated process begins
to complete these tasks.

* Create video files in additional formats for optimal web and mobile
  delivery.

* Upload files to the designated course YouTube channel.

* Upload files to Amazon Web Services (AWS).

This process also gives each file a unique identifying name. Often, course
teams prefer to rename these files, which requires a video administrator to
change each file name in the YouTube CMS.

Multiple members of each course team can manage a YouTube channel without
sharing an email address and password. Channel managers can rename or
otherwise change files only in the channels that they can access. To manage a
YouTube channel, your email address must be given management access.

===============================
Adding a Channel Manager
===============================

#. In your browser, access the YouTube CMS by going to
   https://cms.youtube.com/.

#. Sign in to the YouTube CMS account that contains the channel. This is
   likely to be your CMSmanager Gmail address for video administrators.

#. In the navigation bar at left, click **CHANNELS**. A list of your
   channels appears.

#. Click the name of the channel. The page refreshes in your browser.  

#. At top right, click the channel image. A window displays information about
   the account, including the email address that you used to log in.

   .. image:: Images/YouTube_channel_icon.png
    :alt: Icon representing the YouTube channel found at top right of the
       Channels page
   
6. Click the **YouTube settings** icon. A page with account settings opens in
   your browser.

#. On the account information page, click **Add or remove managers**. A
   list of the current channel managers appears.

#. Click **Add managers**. A popup opens.

#. Supply the email address of a course team member.

#. Verify that the **Manager** option appears at lower left.

#. Click **Invite**. An activation message is sent to the email address.

#. Advise the course team member to expect and respond to the email message
   so that the account is activated. Activation must be complete for
   management access to be granted. See steps 4-5 for :ref:`establishing
   access to a YouTube account<Establish Access to YouTube Account>`.

Course team members who complete the activation process are channel managers.
When they log in to the YouTube CMS at https://cms.youtube.com with the email
address that has channel manager privileges, they can manage course content.

.. _Enable Video Upload in Studio:

*******************************
Enable Video Upload in Studio
*******************************

The last task that video administrators complete before a course team can
begin to upload videos is to work with the edX media team to enable the video
upload feature in Studio. Contact the edX media team at ``media@edx.org`` to
coordinate completion of this final preparatory step.


.. _creating a video transcript: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#step-2-create-or-obtain-a-video-transcript
