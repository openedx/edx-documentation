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
  and smartphones, it needs to be available in several different formats.

To help course teams at partner institutions meet the challenge of delivering
high quality video experiences to as many students as possible, edX offers
media hosting services to address alternative playback and download needs.

* The edX media team establishes accounts for you at YouTube and Amazon Web
  Services (AWS).

* To ensure optimal playback quality for the original video files that your
  course teams upload, the edX media team uses an automated process to create
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
YouTube CMS. This approach helps ensure that staffing changes do not interrupt
your access to the YouTube account. Video administrators can also :ref:`add
channel managers<Add a Channel Manager>`, who have limited administrative
access to specific channels in your account.

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

===============================
Creating YouTube Channels
===============================

.. note:: This procedure only needs to be completed once per course, but it 
 must be complete before the course team begins to add videos to the course in
 Studio.

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
   includes the channel that you just created.

#. Contact the edX media team at ``media@edx.org``. After you create the
   channel for a course, the media team can enable the video upload feature
   for that course in Studio.

Optionally, give management access to the channel to members of the
corresponding course team.

.. _Add a Channel Manager:

===============================
Adding a Channel Manager
===============================

Video administrators can grant management access to each YouTube channel to
members of the corresponding course team. Management access allows team
members to perform limited administrative tasks, such as revising YouTube
titles or changing a video's thumbnail. To provide these permissions, a video
administrator obtains the email addresses of one or more course team members
and invites them to manage the channel.

.. note:: Video administrators use YouTube, but not the YouTube CMS, to add
 channel managers.

#. In your browser, use the CMSmanager email address to sign in to YouTube at
   https://www.youtube.com. A list of the channels in your account appears.

#. Select a channel. The page refreshes to display options and information
   about the channel.

#. In your browser, update the URL to https://www.youtube.com/account. The
   account information page opens.

#. Click **Add or remove managers**. A list of the current channel managers
   appears.

#. Click **Add managers**. A popup opens.

#. Supply the email address of a course team member and click **Invite**. An
   activation message is sent to the email address.

#. Advise the course team member to expect and respond to the email message
   to activate the channel manager account. Activation must be complete for
   management access to be granted. 

   See steps 4-5 for :ref:`establishing access to a YouTube account<Establish
   Access to YouTube Account>`.

Course team members who complete the activation process are channel managers.
When they log in to YouTube at https://www.youtube.com using the email address
that has channel manager privileges, they can manage course content.


.. _creating a video transcript: http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_video.html#step-2-create-or-obtain-a-video-transcript
