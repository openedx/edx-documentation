.. _Advanced Settings and Modules:

###############################
Advanced Settings and Modules
###############################

Some course settings, as well as features and tools that you might want to use
in your course, are enabled or configured on the **Advanced Settings** page in
Studio. This section describes advanced settings and modules that you can use.

.. contents:: 
  :local:
  :depth: 1

**************************
Advanced Settings
**************************

Blurb

.. contents:: 
  :local:
  :depth: 1

==================================
Allow Anonymous Discussion Posts
==================================

If the value for this setting is True, learners can create discussion posts
that are anonymous and not attributable to them. Anonymous posts appear as
anonymous to course team members as well as learners.

The default value for this setting is True.


============================================
Allow Anonymous Discussion Posts to Peers
============================================


If the value for this setting is True, learners can create discussion posts
that appear anonymous to other learners. This setting does not make posts
anonymous to course team members.

The default value for this setting is False.


==================================
Allow Public Wiki Access
==================================

If the value for this setting is True, edX users can view your course wiki
even if they are not enrolled in the course. The default value for this setting is
False.

If you are re-running a course and want learners to be able to see wikis from
a previous course run, you should set this setting to True. Learners in the
new run of the course will be able to visit and edit the old wikis as if they
are part of the new course.

Learners must be logged in to edX.org to participate in any public wikis, and
wiki users will be able to see the history and changes made by all learners
(new and old) as usual.




==================================
Certificate Name (Long)
==================================

Do not change this setting.


==================================
Certificate Name (Short)
==================================

Do not change this setting.


=====================================
Certificate Web/HTML View Overrides
=====================================

Do not change this setting.


==================================
Certificates Display Behavior
==================================

This setting controls the timing of when certificate information and current
grades are shown to learners. It should be used for self-paced courses
planning to offer certificate runs multiple times during the course. Possible
values are ``end``, ``early_no_info``, and ``early_with_info``.

The default value for this setting is ``"end"``. 

If the value for this setting is "end", certificate information is displayed to all learners after the course end date.

If the value for this setting is "early_no_info", certificate links and scores
are shown to eligible learners as soon as certificates are generated. Learners
who have not yet achieved a passing grade do not see any certificate
information on their dashboard until the course ends. This setting is
recommended for self-paced courses or courses with multiple certificate runs.

If the value for this setting is "early_with_info", certificate links and scores are shown to all learners as soon as certificates are generated for the first time. 

.. note:: This setting should be used rarely. Learners might be confused if
   they see a score on their dashboard in the middle of a self-paced or long
   format course run, and when they might have time remaining to improve their
   score and achieve a passing grade.


==================================
Cosmetic Course Display Price
==================================

Do not change this setting.


==================================
Course About Page Image
==================================

Do not change this setting.


==================================
Course Advertised Start Date
==================================


Documented in Building and Running Guide: Setting up the Student View > Set the Advertised Start Date.
This setting overrides the displayed start date on the student dashboard. Teams may wish to alter this setting if they know a course will start in a certain month or quarter, but do not have a firm start date yet. Instead of displaying the Course Start Date from Settings>Schedule & Details, a different date can be displayed. The default is “null”. To display a different date, go to Settings>Advanced Settings>Course Advertised Start Date, remove “null” and type in the desired display date:

Now, in the Learner Dashboard, a learner will see this:

==================================
Course Announcement Date
==================================

Do not change this setting.


==================================
Course Display Name
==================================

Documented in Building and Running Guide: Course Data > Sources in Studio of the Basic Course Information
By default, the Course Display name will be populated with the name your edX Program Manager used when creating the Studio instance of your course. If this name needs to change, enter the new name in this field. Changes will be immediate. Note: Changes to the Course Name on the About Page will need to be handled separately. Contact your edX Program Manager for guidance.

==================================
Course Info Sidebar Name
==================================

Changing this setting overrides the default Course Info sidebar name of “Course Handouts”. Some teams use names like “Additional Readings” or “Supplemental Materials”, for example. To change the name, simply remove the existing text and type the new name. 


==================================
Course Is New
==================================

Do not change this setting.

==================================
Course Is Public
==================================

Do not change this setting.

==================================
Course Maximum Student Enrollment
==================================

Use this setting to specify a maximum number of learners who can enroll in the
course. The default value for this setting is null, which means that unlimited
students can enroll. To cap enrollment, enter the maximum number of learners
that can enroll. Learners who attempt to enroll after the limit has been
reached will see a message explaining that enrollment is closed.


==================================
Course Not Graded
==================================

Do not change this setting.


==================================
Course Number Display String
==================================

By default, the Course Number Display String name will be populated with the course number your edX Program Manager used when creating the Studio instance of your course. If this number needs to change, enter the new number in this field. Changes will be immediate. Note: Changes to the Course Number on the About Page will need to be handled separately. Contact your edX Program Manager for guidance.

==================================
Course Organization Display String
==================================

By default, the Course Organization Display String name will be populated with the information your edX Program Manager used when creating the Studio instance of your course. If this name needs to change, enter the new name in this field. Changes will be immediate, but will only affect the display name. Changes will not affect the course URL. Note: Changes to the Course organization name on the About Page will need to be handled separately. Contact your edX Program Manager for guidance.

==================================
Course Survey URL
==================================

Do not change this setting.

==================================
Course Visibility in Catalog
==================================

Do not change this setting.

==================================
Courseware Chrome
==================================

Do not change this setting. Note: If you are using an Xblock, discuss this setting with your Program Manager.


==================================
Days Early for Beta Users
==================================

Use this setting if you’d like to open content early for beta testers. Enter the number of days before each section and subsection release day that beta testers should be able to access the material. Common values here are 10, 30, or 60 days, depending upon your testing schedule. Note: beta testers can only access published content. For more information on beta testing, visit the edx documentation on Beta Testing a Course.


==================================
Default Tab
==================================

Do not change this setting. Note: If you are using an Xblock, discuss this setting with your Program Manager.

==================================
Disable Progress Graph
==================================

Default for this setting is false. If you enter true, students will not be able to see their progress graph. This setting should not be changed without a very good reason for doing so.


==================================
Discussion Blackout Dates
==================================

Find “discussion_blackouts” in the advanced settings in studio. 
Enter in the start and end times you want the discussion forum to be frozen.
You can set multiple freezes 

Format
[["start date/time", "end date/time"],
["start date/time", "end date/time"],
["start date/time", "end date/time"]] 

Example
[["2015-08-09T00:00", "2099-08-09T00:00"]]  

NOTE: You must place all changes within the existing brackets. Correctly-formatted dates have TWO brackets at the beginning and end, as highlighted.
For details, see the documentation about Closing Discussions.



==================================
Discussion Sorting Alphabetical
==================================

Default for this setting is false, which allows discussions to be sorted chronologically,. Setting this to true sorts discussions alphabetically instead.

==================================
Discussion Topic Mapping
==================================

This is a setting that should be used when setting up cohorted discussion topics. Please see the edX documentation on configuring discussion topics for cohorts for detailed instructions.



==================================
Due Date
==================================

Only use this setting if the same due date applies for all problems. Otherwise, use the settings within each problem.



==================================
Due Date Display Format
==================================

The default due date display format is is Mon DD, YYYY. You can override this setting. Enter "%m-%d-%Y" for MM-DD-YYYY, "%d-%m-%Y" for DD-MM-YYYY, "%Y-%m-%d" for YYYY-MM-DD, or "%Y-%d-%m" for YYYY-DD-MM.


==================================
Enable LaTeX Compiler
==================================



==================================
Enable video caching system
==================================




==================================
External Login Domain
==================================




==================================
HTML Textbooks
==================================

Use this setting to add HTML textbooks that appear as separate tabs in the courseware. Enter the name of the tab (usually the name of the book) as well as the URLs and titles of all the chapters in the book.

==================================
Invitation Only
==================================

Default for this setting is false. If true, xx.

==================================
Issue Open Badges
==================================






==================================
LTI Passports
==================================

Learn how to create an LTI Passport in the edX documentation on how to Obtain LTI Information. Once you’ve created the LTI Passports policy key, enter the policy key into this field. Format must be  "id:client_key:client_secret".


==================================
Matlab API key
==================================

Use this setting to add the API key provided by MathWorks for accessing the MATLAB Hosted Service. For more information about extending the platform with MATLAB, see MathWorks MOOC Support.


==================================
Maximum Attempts
==================================

By default, Maximum Attempts is set to null, meaning that students have an unlimited number of attempts for problems. You can change the course-wide settings for maximum attempts here. You can override this course-wide setting for individual problems within the problem settings, however if the course-wide setting is a specific number, you cannot set the Maximum Attempts for individual problems to unlimited. Best practice is to use individual problem settings to set number of attempts rather than using this Advanced setting.

==================================
Mobile Course Available
==================================

Please do not change this setting unless specifically instructed to do so by your Program Manager. The default is false. If true, the course will be available to mobile devices.



==================================
Randomization
==================================

Use this setting to define coursewide randomization behavior for new problems. Specify how often variable values in a problem are randomized when a student loads the problem. Valid values are "always", "onreset", "never", and "per_student". This setting only applies to problems that have randomly generated numeric values.


==================================
Remote Gradebook
==================================

Enter the remote gradebook mapping. Only use this setting when REMOTE_GRADEBOOK_URL has been specified.

==================================
Secret Token String for Annotation
==================================

The textannotation, videoannotation, and imageannotation advanced modules require this string.

==================================
Show Answer
==================================

Use this setting to Specify when the Show Answer button appears for each problem. Valid values are "always", "answered", "attempted", "closed", "finished", "past_due", and "never". Many times, courses with higher stakes assessments use “finished” while courses with lower-stakes or practice-only assessments use “always” or “attempted”.


==================================
Show Calculator
==================================

Default for this setting is false. When true, students can see the calculator in the course. Use this setting for courses that require mathematical calculations.


==================================
Show Chat Widget
==================================

? Shelby: this was from a pilot in a Berkeley course a long time back. I don't think we should recommend other teams use it. Definitely need to see if we can find more info on it.

==================================
Show Reset Button for Problems
==================================

Default for this setting is false. If true, problems in the course default to always displaying a 'Reset' button. You can override this in each problem's settings. All existing problems are affected when this course-wide setting is changed.


==================================
Static Asset Path
==================================

Do not change this setting

==================================
Text Customization
==================================

Enter string customization substitutions for particular locations.

==================================
URL for Annotation Storage
==================================

Enter the location of the annotation storage server. The textannotation, videoannotation, and imageannotation advanced modules require this setting.

==================================
Video Pre-Roll
==================================


==================================
Video Upload Credentials
==================================

Please do not change this setting. Changes to this setting will be completed by the edX Media Team.







**************************
Advanced Modules List
**************************

The **Advanced Modules List** enables advanced components in your course, such
as content experiments, randomized content blocks, annotation problems, and
the Google Drive and Google Calendar tools.

The available advanced module policy keys are as follows.


* Annotation Problems
* Content Experiments
* Content Libraries
* Google Calendar Tool
* Google Drive Files Tool
* LTI Components


==========================
Enable an Advanced Module
==========================

To enable an advanced module in your course, follow these steps.

#. From the **Settings** menu, select **Advanced Settings**.
#. On the **Advanced Settings** page, locate the **Advanced Modules List**.
#. In the **Advanced Modules List** field, add the name of the 


