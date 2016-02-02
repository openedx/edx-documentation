.. _Student_Info:

##############################
Student Info and Progress Data
##############################

The following sections detail how edX stores stateful data for students
internally. This information can be useful for developers and researchers who
are examining database exports.

.. contents::
  :local:
  :depth: 1

EdX also uses the Django Python Web framework. Tables that are built into the
Django Web framework are documented here only if they are used in
unconventional ways.

.. _Conventions:

***************
Conventions
***************

EdX uses MySQL 5.1 relational database system with InnoDb storage engine.

The following conventions apply to most of the .sql output files. The exception
is the ``courseware_studentmodule`` table, which is created by a different
process than the other edX SQL tables.

* Output files are stored as UTF-8.

* Datetimes are stored as UTC (Coordinated Universal Time), and appear without
  trailing zeros.

* The .sql files are tab separated. Embedded tabs are replaced by the two
  character sequence ``\t``.

* Records are delimited by newlines. Embedded newlines are replaced by the two
  character sequence ``\n``.

* Embedded carriage returns are replaced by the two character sequence ``\r``.

* Backslash characters (``\``) are escaped as ``\\``.

 .. note:: The ``submission`` table for open response assessments stores raw
  text that is JSON encoded. When the last four of these conventions are
  applied to the ``submission.raw_answer`` column, the result is doubly encoded
  values.

Descriptions of the tables and columns that store student data follow, first
in summary form with field types and constraints, and then with a detailed
explanation of each column.

********************
MySQL Terminology
********************

The summary information provided about the SQL table columns uses the
following MySQL schema terminology.

========
Type
========

  The kind of data and the size of the field. When a numeric field has a
  length specified, the length indicates how many digits display but does not
  affect the number of bytes used.

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Value
       - Description
     * - int
       - 4 byte integer.
     * - smallint
       - 2 byte integer, sometimes used for enumerated values.
     * - tinyint
       - 1 byte integer, usually used to indicate a Boolean with 0 = False and
         1 = True.
     * - varchar
       - String, typically short and indexable. The length is the number of
         chars, not bytes, to support multi-byte character sets.
     * - longtext
       - A long block of text, usually not indexed.
     * - date
       - Date
     * - datetime
       - Datetime in UTC, precision in seconds.

========
Null
========

  .. list-table::
     :widths: 25 70
     :header-rows: 1

     * - Value
       - Description
     * - YES
       - NULL values are allowed.
     * - NO
       - NULL values are not allowed.

.. note::
     Django often just places blank strings instead of NULL when it wants to
     indicate a text value is optional. This is more meaningful for numeric
     and date fields.

========
Key
========

  .. list-table::
     :widths: 25 65
     :header-rows: 1

     * - Value
       - Description
     * - PRI
       - Primary key for the table, usually named ``id``, unique.
     * - UNI
       - Unique
     * - MUL
       - Indexed for fast lookup, but the same value can appear multiple
         times. A unique index that allows NULL can also show up as MUL.

.. _User_Data:

****************
User Data
****************

Data for students is gathered during site registration, course
enrollment, and as other activities, such as responding to a particular type of problem or joining a team, take place.

.. contents::
  :local:
  :depth: 1

.. note:: The Teams feature is in limited release. For more information,
   contact your edX partner manager. For Open edX sites, contact your system
   administrator.

.. _auth_user:

==================================
Columns in the ``auth_user`` Table
==================================

The ``auth_user`` table is built into the edX Django Web framework. It holds
generic information necessary for user login and permissions.

A sample of the heading row and a data row in the ``auth_user`` table follows.

.. code-block:: json

    id  username  first_name  last_name  email  password  is_staff  is_active
    is_superuser  last_login  date_joined status  email_key  avatar_typ
    country  show_country  date_of_birth  interesting_tags  ignored_tags
    email_tag_filter_strategy display_tag_filter_strategy
    consecutive_days_visit_count

    9999999    AAAAAAAAA    AAAAAA  AAAAAA 1 1 0 2014-01-01 17:28:27 2012-03-04
    00:57:49   NULL      0 NULL      0 0

The ``auth_user`` table has the following columns.

  +------------------------------+--------------+------+-----+------------------+
  | Column                       | Type         | Null | Key | Comment          |
  +==============================+==============+======+=====+==================+
  | id                           | int(11)      | NO   | PRI |                  |
  +------------------------------+--------------+------+-----+------------------+
  | username                     | varchar(30)  | NO   | UNI |                  |
  +------------------------------+--------------+------+-----+------------------+
  | first_name                   | varchar(30)  | NO   |     | # Never used     |
  +------------------------------+--------------+------+-----+------------------+
  | last_name                    | varchar(30)  | NO   |     | # Never used     |
  +------------------------------+--------------+------+-----+------------------+
  | email                        | varchar(75)  | NO   | UNI |                  |
  +------------------------------+--------------+------+-----+------------------+
  | password                     | varchar(128) | NO   |     |                  |
  +------------------------------+--------------+------+-----+------------------+
  | is_staff                     | tinyint(1)   | NO   |     |                  |
  +------------------------------+--------------+------+-----+------------------+
  | is_active                    | tinyint(1)   | NO   |     |                  |
  +------------------------------+--------------+------+-----+------------------+
  | is_superuser                 | tinyint(1)   | NO   |     |                  |
  +------------------------------+--------------+------+-----+------------------+
  | last_login                   | datetime     | NO   |     |                  |
  +------------------------------+--------------+------+-----+------------------+
  | date_joined                  | datetime     | NO   |     |                  |
  +------------------------------+--------------+------+-----+------------------+
  | status                       | varchar(2)   | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | email_key                    | varchar(32)  | YES  |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | avatar_typ                   | varchar(1)   | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | country                      | varchar(2)   | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | show_country                 | tinyint(1)   | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | date_of_birth                | date         | YES  |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | interesting_tags             | longtext     | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | ignored_tags                 | longtext     | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | email_tag_filter_strategy    | smallint(6)  | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | display_tag_filter_strategy  | smallint(6)  | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+
  | consecutive_days_visit_count | int(11)      | NO   |     | # Obsolete       |
  +------------------------------+--------------+------+-----+------------------+

----
id
----
  Primary key, and the value typically used in URLs that reference the user. A
  user has the same value for ``id`` here as they do in the MongoDB database's
  users collection. Foreign keys referencing ``auth_user.id`` will often be
  named ``user_id``, but are sometimes named ``student_id``.

----------
username
----------
  The unique username for a user in the edX system. It can contain
  alphanumerics and the special characters shown within the brackets:
  [ _ @ + - . ]. The username is the only user-provided information that
  other users can currently see. EdX has never allowed users to change
  usernames, but might do so in the future.

------------
first_name
------------
  Not used; a user's full name is stored in ``auth_userprofile.name`` instead.

-----------
last_name
-----------
  Not used; a user's full name is stored in ``auth_userprofile.name`` instead.

-------
email
-------
  The user's email address, which is the primary mechanism users use to log
  in. This value is optional by default in Django, but is required by edX.
  This value must be unique to each user and is never shown to other users.

----------
password
----------
  A hashed version of the user's password. Depending on when the password was
  last set, this will either be a SHA1 hash or PBKDF2 with SHA256 (Django 1.3
  uses the former and 1.4 the latter).

----------
is_staff
----------
  Most users have a 0 for this field. Set to 1 if the user is a staff member
  of **edX**, with corresponding elevated privileges that cut across courses.
  It does not indicate that the person is a member of the course team for any
  given course.

  Generally, users with this flag set to 1 are either edX partner managers
  responsible for course delivery, or edX developers who need access for
  testing and debugging purposes. Users who have ``is_staff`` = 1 have
  Admin privileges on all courses and can see additional debug
  information on the Instructor Dashboard.

.. note::
     This designation has no bearing on a user's role in the discussion
     forums, and confers no elevated privileges there.

-----------
is_active
-----------
  This value is 1 if the user has clicked on the activation link that was sent
  to them when they created their account, and 0 otherwise.

  Users who have ``is_active`` = 0 generally cannot log into the system.
  However, when users first create an account, they are automatically logged
  in even though they have not yet activated the account. This is to let them
  experience the site immediately without having to check their email. A
  message displays on the dashboard to remind users to check their email and
  activate their accounts when they have time. When they log out, they cannot
  log back in again until activation is complete. However, because edX
  sessions last a long time, it is possible for someone to use the site as a
  student for days without being "active".

  Once ``is_active`` is set to 1, it is *only* set back to 0 if the user is
  banned (which is a very rare, manual operation).

--------------
is_superuser
--------------
  Controls access to django_admin views. Set to 1 (true) only for site admins.
  0 for almost everybody.

  **History**: Only the earliest developers of the system have this set to 1,
  and it is no longer really used in the codebase.

------------
last_login
------------
  A datetime of the user's last login. Should not be used as a proxy for
  activity, since people can use the site all the time and go days between
  logging in and out.

-------------
date_joined
-------------
  Date that the account was created.

.. note::
     This is not the date that the user activated the account.

-------------------
Obsolete columns
-------------------
  All of the following columns were added by an application called Askbot, a
  discussion forum package that is no longer part of the system.

  * status
  * email_key
  * avatar_typ
  * country
  * show_country
  * date_of_birth
  * interesting_tags
  * ignored_tags
  * email_tag_filter_strategy
  * display_tag_filter_strategy
  * consecutive_days_visit_count

  Only users who were part of the prototype 6.002x course run in the Spring of
  2012 have any information in these columns. Even for those users, most of
  this information was never collected. Only the columns with values that are
  automatically generated have any values in them, such as the tag-related
  columns.

  These columns are unrelated to the discussion forums that edX currently
  uses, and will eventually be dropped from this table.

.. _auth_userprofile:

=========================================
Columns in the ``auth_userprofile`` Table
=========================================

The ``auth_userprofile`` table stores user demographic data collected when
students register for a user account. Every row in this table corresponds to
one row in ``auth_user``.

A sample of the heading row and a data row in the ``auth_userprofile`` table
follows.

.. code-block:: json

    id  user_id name  language  location  meta  courseware  gender
    mailing_address year_of_birth level_of_education  goals allow_certificate
    country  city  bio   profile_image_uploaded_at

    9999999  AAAAAAAA  AAAAAAAAA English MIT {"old_emails":
    [["aaaaa@xxxxx.xxx", "2012-11-16T10:28:10.096489"]], "old_names":
    [["BBBBBBBBBBBBB", "I wanted to test out the name-change functionality",
    "2012-10-22T12:23:10.598444"]]} course.xml  NULL  NULL  NULL  NULL  NULL
    1      NULL   Hi! I'm from the US and I've taken 4 edX courses so far. I
    want to learn how to confront problems of wealth inequality. 2015-04-19 16:41:27

The ``auth_userprofile`` table has the following columns.

  +----------------------------+--------------+------+-----+------------------------------------------+
  | Column                     | Type         | Null | Key | Comment                                  |
  +============================+==============+======+=====+==========================================+
  | id                         | int(11)      | NO   | PRI |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | user_id                    | int(11)      | NO   | UNI |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | name                       | varchar(255) | NO   | MUL |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | language                   | varchar(255) | NO   | MUL | # Obsolete                               |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | location                   | varchar(255) | NO   | MUL | # Obsolete                               |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | meta                       | longtext     | NO   |     |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | courseware                 | varchar(255) | NO   |     | # Obsolete                               |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | gender                     | varchar(6)   | YES  | MUL | # Only users signed up after prototype   |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | mailing_address            | longtext     | YES  |     | # Only users signed up after prototype   |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | year_of_birth              | int(11)      | YES  | MUL | # Only users signed up after prototype   |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | level_of_education         | varchar(6)   | YES  | MUL | # Only users signed up after prototype   |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | goals                      | longtext     | YES  |     | # Only users signed up after prototype   |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | allow_certificate          | tinyint(1)   | NO   |     |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | country                    | varchar(2)   | YES  |     |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | city                       | longtext     | YES  |     |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | bio                        | varchar(3000)| YES  |     |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+
  | profile_image_uploaded_at  | datetime     | YES  |     |                                          |
  +----------------------------+--------------+------+-----+------------------------------------------+

**History**: ``bio`` and ``profile_image_uploaded_at`` added 22 April 2015.
``country`` and ``city`` added January 2014. The organization of this table
was different for the students who signed up for the MITx prototype phase in
the spring of 2012, than for those who signed up afterwards. The column
descriptions that follow detail the differences in the demographic data
gathered.

----
id
----
  Primary key, not referenced anywhere else.

---------
user_id
---------
  A foreign key that maps to ``auth_user.id``.

------
name
------
  String for a user's full name. EdX makes no constraints on language or
  breakdown into first/last name. The names are never shown to other students.
  International students usually enter a romanized version of their names, but
  not always. Name changes are permitted, and the previous name is logged in
  the ``meta`` field.

  **History**: A former edX policy required manual approval of name changes to
  guard the integrity of the certificates. Students would submit a name change
  request, and an edX team member would approve or reject the request.

----------
language
----------
  No longer used.

  **History**: User's preferred language, asked during the sign up process for
  the 6.002x prototype course given in the Spring of 2012. Sometimes written
  in those languages. EdX stopped collecting this data after MITx transitioned
  to edX, but never removed the values for the first group of students.

----------
location
----------
  No longer used.

  **History**: User's location, asked during the sign up process for the
  6.002x prototype course given in the Spring of 2012. The request was not
  specific, so people tended to put the city they were in, though some just
  supplied a country and some got as specific as their street address. Again,
  sometimes romanized and sometimes written in their native language. Like
  ``language``, edX stopped collecting this column after MITx transitioned to
  edX, so it is only available for the first batch of students.

------
meta
------
  An optional, freeform text field that stores JSON data. This field allows us
  to associate arbitrary metadata with a user. An example of the JSON that can
  be stored in this field follows, using pretty print for an easier-to-read
  display format.

.. code-block:: json

 {
  "old_names": [
    [
      "Mike Smith",
      "Mike's too informal for a certificate.",
      "2012-11-15T17:28:12.658126"
    ],
    [
      "Michael Smith",
      "I want to add a middle name as well.",
      "2013-02-07T11:15:46.524331"
    ]
  ],
  "old_emails": [
    [
      "mr_mike@email.com",
      "2012-10-18T15:21:41.916389"
    ]
  ],
  "6002x_exit_response": {
    "rating": [
      "6"
    ],
    "teach_ee": [
      "I do not teach EE."
    ],
    "improvement_textbook": [
      "I'd like to get the full PDF."
    ],
    "future_offerings": [
      "true"
    ],
    "university_comparison": [
      "This course was <strong>on the same level<\/strong> as the university class."
    ],
    "improvement_lectures": [
      "More PowerPoint!"
    ],
    "highest_degree": [
      "Bachelor's degree."
    ],
    "future_classes": [
      "true"
    ],
    "future_updates": [
      "true"
    ],
    "favorite_parts": [
      "Releases, bug fixes, and askbot."
    ]
  }
 }

Details about this metadata follow. Please note that the "fields" described
here are found as JSON attributes *inside* a given ``meta`` field, and are
*not* separate database columns of their own.

  ``old_names``

    A list of the previous names this user had, and the timestamps at which
    they submitted a request to change those names. These name change request
    submissions used to require a staff member to approve it before the name
    change took effect. This is no longer the case, though their previous
    names are still recorded.

    Note that the value stored for each entry is the name they had, not the
    name they requested to get changed to. People often changed their names as
    the time for certificate generation approached, to replace nicknames with
    their actual names or correct spelling/punctuation errors.

    The timestamps are UTC, like all datetimes stored in the edX database.

  ``old_emails``

    A list of previous emails this user had, with timestamps of when they
    changed them, in a format similar to `old_names`. There was never an
    approval process for this.

    The timestamps are UTC, like all datetimes stored in the edX database.

  ``6002x_exit_response``

    Answers to a survey that was sent to students after the prototype 6.002x
    course in the Spring of 2012. The questions and number of questions were
    randomly selected to measure how much survey length affected response
    rate. Only students from this course have this field.

------------
courseware
------------
  No longer used.

  **History**: At one point, it was part of a way to do A/B tests, but it has
  not been used for anything meaningful since the conclusion of the prototype
  course in the spring of 2012.

--------
gender
--------
  Collected during student signup from a drop-down list control.

  .. list-table::
       :widths: 10 80
       :header-rows: 1

       * - Value
         - Description
       * - f
         - Female
       * - m
         - Male
       * - o
         - Other/Prefer Not to Say
       * - (blank)
         - User did not specify a gender.
       * - NULL
         - This student signed up before this information was collected.

  **History**: This information began to be collected after the transition
  from MITx to edX; prototype course students have NULL for this field.

-----------------
mailing_address
-----------------
  Collected during student registration from a text field control. A blank
  string for students who elect not to enter anything.

  This column can contain multiple lines, which are separated by '``\r\n``'.

  **History**: This information began to be collected after the transition
  from MITx to edX; prototype course students have NULL for this field.

---------------
year_of_birth
---------------
  Collected during student registration from a drop-down list control. NULL
  for students who decide not to fill this in.

  **History**: This information began to be collected after the transition
  from MITx to edX; prototype course students have NULL for this field.

--------------------
level_of_education
--------------------
  Collected during student registration from a drop-down list control.

  .. list-table::
       :widths: 10 80
       :header-rows: 1

       * - Value
         - Description
       * - p
         - Doctorate.
       * - m
         - Master's or professional degree.
       * - b
         - Bachelor's degree.
       * - a
         - Associate degree.
       * - hs
         - Secondary/high school.
       * - jhs
         - Junior secondary/junior high/middle school.
       * - el
         - Elementary/primary school.
       * - none
         - No Formal Education.
       * - other
         - Other Education.
       * - (blank)
         - User did not specify level of education.
       * - p_se
         - Doctorate in science or engineering (no longer used).
       * - p_oth
         - Doctorate in another field (no longer used).
       * - NULL
         - This student signed up before this information was collected.

  **History**: Data began to be collected in this column after the transition
  from MITx to edX; prototype course students have NULL for this field.

-------
goals
-------
  Collected during student registration from a text field control with the
  label "Goals in signing up for edX". A blank string for students who elect
  not to enter anything.

  This column can contain multiple lines, which are separated by '``\r\n``'.

  **History**: This information began to be collected after the transition
  from MITx to edX; prototype course students have NULL for this field.

-------------------
allow_certificate
-------------------
  Set to 1 (true).

  **History**: Prior to 10 Feb 2014, this field was set to 0 (false) if log
  analysis revealed that the student was accessing the edX site from a country
  that the U.S. had embargoed. This restriction is no longer in effect, and on
  10 Feb 2014 this value was changed to 1 for all users.


----------------------
country
----------------------
  Stores a two digit country code based on the selection made by the student
  during registration. Set to an empty string for students who do not select a
  country.

  **History**: Added in Jan 2014, but not implemented until 18 Sep 2014. Null
  for all user profiles created before 18 Sep 2014.

------
city
------
  Not currently used. Set to null for all user profiles.

  **History**: Added in Jan 2014, not yet implemented.

------
bio
------
  Stores one or more paragraphs of biographical information that the learner
  enters. The maximum number of characters is 3000.

  **History**: Added 22 April 2015.


------------------------------
profile_image_uploaded_at
------------------------------
  Stores the date and time when a learner uploaded a profile image.

  **History**: Added 22 April 2015.


.. _student_courseenrollment:

=================================================
Columns in the ``student_courseenrollment`` Table
=================================================

A row in this table represents a student's enrollment for a particular course
run.

.. note:: A row is created for every student who starts the enrollment
  process, even if they never complete site registration by activating the user
  account.

**History**: As of 20 Aug 2013, this table retains the records of students who
unenroll. Records are no longer deleted from this table.

A sample of the heading row and a data row in the ``student_courseenrollment``
table follows.

.. code-block:: sql

    id  user_id course_id created is_active mode

    1135683 9999999 edX/DemoX/Demo_course 2013-03-19 17:20:58 1 honor

The ``student_courseenrollment`` table has the following columns.

+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+===========+==============+======+=====+=========+================+
| id        | int(11)      | NO   | PRI | NULL    | auto_increment |
+-----------+--------------+------+-----+---------+----------------+
| user_id   | int(11)      | NO   | MUL | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
| course_id | varchar(255) | NO   | MUL | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
| created   | datetime     | YES  | MUL | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
| is_active | tinyint(1)   | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
| mode      | varchar(100) | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+

----
id
----
  Primary key.

---------
user_id
---------
  Student's ID in ``auth_user.id``.

-----------
course_id
-----------
  The ID of the course run that the user is enrolling in, in the format
  ``{key type}:{org}+{course}+{run}``. For example,
  ``course-v1:edX+DemoX+Demo_2014``. When you view the course content in your
  browser, the ``course_id`` appears as part of the URL. For example,
  ``http://www.edx.org/courses/course-v1:edX+DemoX+Demo_2014/info``.

  **History**: In October 2014, identifiers for some new courses began to use
  the format shown above. Other new courses, and all courses created prior to
  October 2014, use the format ``{org}/{course}/{run}``,  for example,
  ``MITx/6.002x/2012_Fall``. The URL format for a course with a ``course_id``
  in this format was
  ``https://www.edx.org/courses/MITx/6.002x/2012_Fall/info``.

---------
created
---------
  Stores the date and time that this row was created, in UTC format.

-----------
is_active
-----------
  Boolean indicating whether this enrollment is active. If an enrollment is not
  active, a student is not enrolled in that course. For example, if a student
  decides to unenroll from the course, ``is_active`` is set to 0 (false). The
  student's state in ``courseware_studentmodule`` is untouched, so courseware
  state is not lost if a student unenrolls and then re-enrolls.

  ``is_active`` can also be set to 0 if a student begins the process of
  enrolling in a course by purchasing a verified certificate, but then abandons
  the shopping cart before completing the purchase (and the enrollment).

  **History**: This column was introduced in the 20 Aug 2013 release. Before
  this release, unenrolling a student simply deleted the row in
  ``student_courseenrollment``.

------
mode
------
  String indicating what kind of enrollment this is: audit, honor,
  professional, verified, or blank.

  **History**:

  * All enrollments prior to 20 Aug 2013 are "honor", when the "audit" and
    "verified" values were added.

  * The "professional" value was added for courses on edx.org on 29 Sep 2014.

  * The "audit" value was deprecated on 23 Oct 2014.

  .. _user_api_usercoursetag:

===============================================
Columns in the ``user_api_usercoursetag`` Table
===============================================

This table uses key-value pairs to store metadata about a specific student's
involvement in a specific course. For example, for a course that assigns
students to groups randomly for content experiments, a row in this table
identifies the student's assignment to a partition and group.

**History**: Added 7 Mar 2014.

.. need a sample header and row from a data package when available

The ``user_api_usercoursetag`` table has the following columns.

.. list-table::
     :widths: 15 15 15 15
     :header-rows: 1

     * - Column
       - Type
       - Null
       - Key
     * - user_id
       - int(11)
       - NO
       - PRI
     * - course_id
       - varchar(255)
       - NO
       -
     * - key
       - varchar(255)
       - NO
       -
     * - value
       - textfield
       - NO
       -

.. need type, null, key for each one

---------
user_id
---------
  The student's ID in ``auth_user.id``.

-----------
course_id
-----------
  The course identifier, in the format ``{key type}:{org}+{course}+{run}``. For
  example, ``course-v1:edX+DemoX+Demo_2014``.

  **History**: In October 2014, identifiers for some new courses began to use
  the format shown above. Other new courses, and all courses created prior to
  October 2014, use the format ``{org}/{course}/{run}``,  for example,
  ``MITx/6.002x/2012_Fall``.

----
key
----
  Identifies an attribute of the course.

  For example, for a course that includes modules that are set up to perform
  content experiments, the value in this column identifies a partition, or type
  of experiment. The key for the partition is in the format
  ``xblock.partition_service.partition_ID``, where ID is an integer.

------
value
------
  The content for the key that is set for a student.

  For example, for a course that includes modules that are set up to perform
  content experiments, this column stores the group ID of the particular group
  the student is assigned to within the partition.

.. _user_id_map:

=====================================
Columns in the ``user_id_map`` Table
=====================================

A row in this table maps a student's real user ID to an anonymous ID generated
to obfuscate the student's identity. This anonymous ID is not course specific.
For more information about course specific user IDs, see the
:ref:`student_anonymoususerid` table.

Course team members can download the anonymized user IDs for the learners in a
course. For more information, see :ref:`partnercoursestaff:Access_anonymized`.

A sample of the heading row and a data row in the ``user_id_map`` table
follows.

.. code-block:: sql

    hash_id id  username

    e9989f2cca1d699d88e14fd43ccb5b5f  9999999 AAAAAAAA

The ``user_id_map`` table has the following columns.

.. list-table::
     :widths: 15 15 15 15
     :header-rows: 1

     * - Column
       - Type
       - Null
       - Key
     * - hashid
       - int(11)
       - NO
       - PRI
     * - id
       - int(11)
       - NO
       -
     * - username
       - varchar(30)
       - NO
       -

----------
hash_id
----------
   The user ID generated to obfuscate the student's identity.

---------
id
---------
  The student's ID in ``auth_user.id``.

-----------
username
-----------
  The student's username in ``auth_user.username``.

.. _student_anonymoususerid:

====================================================
Columns in the ``student_anonymoususerid`` Table
====================================================

This anonymous ID identifies learners in a single run of a specific course. The
course specific anonymized user IDs in this table can be used to identify
learners in SQL tables for :ref:`open response assessment data<ORA2 Data>`. For
more information about the anonymous IDs that identify users across courses,
see the :ref:`user_id_map` table.

Course team members can download the course specific anonymized user IDs for
learners in a course run. For more information, see
:ref:`partnercoursestaff:Access_anonymized`.

**History**: This table was added to the database data file in data packages
beginning with the 13 Dec 2015 export.

A sample of the heading row and a data row in the ``student_anonymoususerid``
table follows.

.. code-block:: sql

    id   user_id   anonymous_user_id  course_id

    999999   111111   d617d135c2bed4974237a0f18991ab8d   WellesleyX/HIST229x/2013_SOND

The ``student_anonymoususerid`` table has the following columns.

.. list-table::
     :widths: 15 15 15 15
     :header-rows: 1

     * - Column
       - Type
       - Null
       - Key
     * - id
       - int(11)
       - NO
       - PRI
     * - user_id
       - int(11)
       - NO
       - MUL
     * - anonymous_user_id
       - varchar(32)
       - NO
       - UNI
     * - course_id
       - varchar(255)
       - NO
       - MUL

---------
id
---------
  A database auto-increment field that uniquely identifies the learner, and
  acts as the primary key.

---------
user_id
---------
  The learner's ID in ``auth_user.id``.

------------------
anonymous_user_id
------------------
  The anonymous ID assigned to the learner.

---------------------
course_id
---------------------

  The course identifier, in the format ``{key type}:{org}+{course}+{run}``. For
  example, ``course-v1:edX+DemoX+Demo_2014``.

.. _student_languageproficiency:

====================================================
Columns in the ``student_languageproficiency`` Table
====================================================

The ``student_languageproficiency`` table stores information about students'
self-reported language preferences. Students can select only one value.

**History**: Added 22 April 2015.

+-----------------+-------------+------+-----+---------+----------------+
| Field           | Type        | Null | Key | Default | Extra          |
+-----------------+-------------+------+-----+---------+----------------+
| id              | int(11)     | NO   | PRI | NULL    | auto_increment |
+-----------------+-------------+------+-----+---------+----------------+
| user_profile_id | int(11)     | NO   | MUL | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+
| code            | varchar(16) | NO   | MUL | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+

---------
id
---------

  A database auto-increment field that uniquely identifies the language. This
  field is not exposed through the API.

----------------
user_profile_id
----------------

  Specifies the ID in the ``authuser_profile`` table that is associated with a
  particular language proficiency.

----
code
----
  The language code. Most codes are ISO 639-1 codes, with the addition of
  codes for simplified and traditional Chinese.


.. _teams_courseteam:

==============================================
Columns in the ``teams_courseteam`` Table
==============================================

This table stores information about the teams in a course.

.. note:: The Teams feature is in limited release. For more information,
   contact your edX partner manager. For Open edX sites, contact your system
   administrator.

**History**: Added September 15 2015

The ``teams_courseteam`` table has the following columns.

.. list-table::
     :widths: 15 15 15 15
     :header-rows: 1

     * - Column
       - Type
       - Null
       - Key
     * - id
       - int(11)
       - NO
       - PRI
     * - team_id
       - varchar(255)
       - NO
       - UNI
     * - name
       - varchar(255)
       - NO
       - UNI
     * - course_id
       - textfield
       - NO
       - MUL
     * - topic_id
       - varchar(255)
       - YES
       - MUL
     * - date_created
       - datetime
       - NO
       - MUL
     * - description
       - varchar(300)
       - NO
       - MUL
     * - country
       - varchar(2)
       - YES
       - MUL
     * - language
       - varchar(16)
       - YES
       - MUL
     * - discussion_topic_id
       - varchar(255)
       - NO
       - MUL
     * - last_activity_at
       - datetime
       - NO
       - MUL
     * - team_size
       - int(11)
       - NO
       - MUL


--------------------
id
--------------------

  The primary key, a database auto-increment field that uniquely identifies
  the team.

---------
team_id
---------

  The unique identifier for this team.

---------------------
name
---------------------

  The display name for this team. A name is required when a team is created.

---------------------
course_id
---------------------

  The course identifier, in the format ``{key type}:{org}+{course}+{run}``. For
  example, ``course-v1:edX+DemoX+Demo_2014``.

  **History**: In October 2014, identifiers for some new courses began to use
  the format shown above. Other new courses, and all courses created prior to
  October 2014, use the format ``{org}/{course}/{run}``,  for example,
  ``MITx/6.002x/2012_Fall``.

---------------------
topic_id
---------------------

  The unique identifier for the teams topic associated with the team. Topics,
  including an ID for each topic, are defined by course team members in
  **Advanced Settings** in Studio.

---------------------
date_created
---------------------

  The date and time that this team was created, in the format ``YYYY-MM-DD
  HH:MM:SS``.

---------------------
description
---------------------

  The description for the team. A team description is required when a team is
  created.

---------------------
country
---------------------

  An optional field in a team's details. The person who creates a team can
  specify a country that the team's members primarily identify with. Country
  codes are ISO 3166-1 codes.

---------------------
language
---------------------

  An optional field in a team's details. A team can specify a language that
  the team's members primarily communicate using. Most language codes are ISO
  639-1 codes, with the addition of codes for simplified and traditional
  Chinese.

---------------------
discussion_topic_id
---------------------

  The identifier for all discussion topics within this team's discussions.

--------------------
last_activity_at
--------------------

  The date and time that the most recent activity on the team was recorded, in
  the format ``YYYY-MM-DD HH:MM:SS``. The current definition of activity for
  this field includes team creation, and the creation of posts, comments, and
  responses in the team's discussions.


--------------------
team_size
--------------------

  The current count of the number of members in the team.


.. _teams_courseteammembership:

===================================================
Columns in the ``teams_courseteammembership`` Table
===================================================

This table stores information about learners who are members of a team.

.. note:: The Teams feature is in limited release. For more information,
   contact your edX partner manager. For Open edX sites, contact your system
   administrator.

**History**: Added September 15 2015.

The ``teams_courseteammembership`` table has the following columns.

.. list-table::
     :widths: 15 15 15 15
     :header-rows: 1

     * - Column
       - Type
       - Null
       - Key
     * - id
       - int (11)
       - NO
       - PRI
     * - user_id
       - int (11)
       - NO
       - UNI
     * - team_id
       - int (11)
       - NO
       - MUL
     * - date_joined
       - datetime
       - NO
       - MUL
     * - last_activity_at
       - datetime
       - NO
       - MUL

---------------------
id
---------------------

  The primary key, a database auto-increment field that uniquely identifies
  the membership of a user on a team.

---------------------
user_id
---------------------

  The ID of a user who is currently a member of the team, from
  ``auth_user.id``.

---------------------
team_id
---------------------

  The ID of the team, from ``teams_courseteam.id``.

--------------------
date_joined
--------------------

  The timestamp of the time that the user joined the team, in the format
  ``YYYY-MM-DD HH:MM:SS``.

--------------------
last_activity_at
--------------------

  The date/time of the most recent activity performed by this user on this
  team, in the format ``YYYY-MM-DD HH:MM:SS``. The current definition of
  activity for this field is limited to discussions-related actions by this
  user: adding or deleting posts, adding comments or responses, and voting on
  posts. If the user has not yet participated in the team's discussion, the
  ``last_activity_at`` date/time reflects the timestamp when the user joined
  the team.


.. _Courseware_Progress:

************************
Courseware Progress Data
************************

Any piece of content in the courseware can store state and score in the
``courseware_studentmodule`` table. Grades and the user Progress page are
generated by doing a walk of the course contents, searching for graded items,
looking up a student's entries for those items in ``courseware_studentmodule``
via *(course_id, student_id, module_id)*, and then applying the grade weighting
found in the course policy and grading policy files. Course policy files
determine how much weight one problem has relative to another, and grading
policy files determine how much categories of problems are weighted (for
example, HW=50%, Final=25%, etc.).

==================================
About Modules
==================================

Modules can store state, but whether and how they do so varies based on the
implementation for that particular kind of module. When a user loads a page,
the system looks up all the modules that need to be rendered in order to
display it, and then asks the database to look up state for those modules for
that user. If there is no corresponding entry for that user for a given module,
a new row is created and the state is set to an empty JSON object.

.. _courseware_studentmodule:

====================================================================
Columns in the ``courseware_studentmodule`` Table
====================================================================

The ``courseware_studentmodule`` table holds all courseware state for a given
user.

A sample of the heading row and a data row in the ``courseware_studentmodule``
table follows.

.. code-block:: sql

    id  module_type module_id student_id  state grade created modified  max_grade done
    course_id

    33973858  course  i4x://edX/DemoX/course/Demo_course  96452 {"position": 3} NULL
    2013-03-19 17:21:07 2014-01-07 20:18:54 NULL  na  edX/DemoX/Demo_course

Students have a separate row for every piece of content that they access or
that is created to hold state data, making this the largest table in the data
package.

The ``courseware_studentmodule`` table has the following columns.

+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+=============+==============+======+=====+=========+================+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
+-------------+--------------+------+-----+---------+----------------+
| module_type | varchar(32)  | NO   | MUL | problem |                |
+-------------+--------------+------+-----+---------+----------------+
| module_id   | varchar(255) | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| student_id  | int(11)      | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| state       | longtext     | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| grade       | double       | YES  | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| created     | datetime     | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| modified    | datetime     | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| max_grade   | double       | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| done        | varchar(8)   | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
| course_id   | varchar(255) | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+

.. note:: The output in the ``courseware_studentmodule`` table is the result
 of a different process than the other SQL tables in the edX data packages. As
 a result, not all of the data :ref:`conventions<Conventions>` apply to this
 table.

----
id
----
  Primary key. Rarely used though, since most lookups on this table are
  searches on the three tuple of `(course_id, student_id, module_id)`.

-------------
module_type
-------------

  .. list-table::
     :widths: 20 70
     :header-rows: 1

     * - Type
       - Description
     * - chapter
       - The top level categories for a course. Each of these is usually
         labeled as a Week in the courseware, but this is just convention.
     * - combinedopenended
       - A module type developed for grading open ended questions via self
         assessment, peer assessment, and machine learning.
     * - conditional
       - Allows you to prevent access to certain parts of the courseware if
         other parts have not been completed first.
     * - course
       - The top level course module of which all course content is descended.
     * - crowdsource_hinter
       - Not currently used.

         **History**: This ``module_type`` was included in
         a single course on a test basis and then deprecated.

     * - lti
       - Learning Tools Interoperability component that adds an external
         learning application to display content, or to display content and
         also require a student response.
     * - peergrading
       - Indicates a problem that is graded by other students. An option for
         grading open ended questions.
     * - poll_question
       - Not currently used.

         **History**: This ``module_type`` was included in
         a single course on a test basis and then deprecated.

     * - problem
       - A problem that the user can submit solutions for. EdX offers many
         different varieties.
     * - problemset
       - A collection of problems and supplementary materials, typically used
         for homeworks and rendered as a horizontal icon bar in the
         courseware. Use is inconsistent, and some courses use a
         ``sequential`` instead.
     * - randomize
       - Identifies a module in which one of several possible defined
         alternatives is randomly selected for display to each student.
     * - selfassessment
       - Self assessment problems. Used in a single course in Fall 2012 as an
         early test of the open ended grading system. Deprecated in favor of
         ``combinedopenended``.
     * - sequential
       - A collection of videos, problems, and other materials, rendered as a
         horizontal icon bar in the courseware.
     * - timelimit
       - Not currently used.

         **History**: This ``module_type`` was included in
         a single course on a test basis and then deprecated.

     * - video
       - A component that makes a video file available for students to play.
     * - videoalpha
       - Not currently used.

         **History**: During the implementation of a
         change to the ``video`` ``module_type``, both ``video`` and
         ``videoalpha`` were stored. The ``videoalpha`` type was then
         deprecated.

     * - videosequence
       - A collection of videos, exercise problems, and other materials,
         rendered as a horizontal icon bar in the courseware.

         **History**: This ``module_type`` is no longer in use, courses now
         use ``sequential`` instead.

     * - word_cloud
       - A specialized problem that produces a graphic from the words that
         students enter.

.. _module_id:

-----------
module_id
-----------
  Unique ID for a distinct piece of content in a course. Each ``module_id`` is
  recorded as a URL with the format ``{key type}:{org}+{course}+{run}@{module
  type}+block@{module name or hash code}``. Having URLs of this form gives
  content a canonical representation even during a transition between back-end
  data stores.

  As an example, this example ``module_id`` contains the following parts.

    ``block-v1:edX+DemoX+Demo_2014+type@problem+block@303034da25524878a2e66fb57c91cf85``

  .. list-table::
     :widths: 15 20 55
     :header-rows: 1

     * - Part
       - Example Value
       - Definition
     * - ``{key type}``
       - ``block-v1``
       - The type of namespace identifier, including the implementation
         version.
     * - ``{org}``
       - ``edX``
       - The organization part of the ID, indicating what organization created
         this piece of content.
     * - ``{course}``
       - ``DemoX``
       - The course that this content was created for.
     * - ``{run}``
       - ``Demo_2014``
       - The term or specific iteration of the course.
     * - ``type@{module type}``
       - ``type@problem``
       - The module type. The same value is stored in the
         ``courseware_studentmodule.module_type`` column.
     * - ``block@{module name or hash code}``
       - ``block@303034da25524878a2e66fb57c91cf85``
       - The name that the content creators supplied for this module. If the
         module does not have a name, the system generates a hash code as its
         identifier.

**History**: In October 2014, identifiers for modules in some new courses began
to use the format shown above. Other new courses, and all courses created prior
to October 2014, use the format ``i4x://{org}/{course}/{module type}/{module
name or hash code}``. For example,
``i4x://MITx/3.091x/problemset/Sample_Problems``. Note that this format does
not include course run information, so the
``courseware_studentmodule.course_id`` column might need to be used as well.

------------
student_id
------------
  A reference to ``auth_user.id``, this is the student that this module state
  row belongs to.

-------
state
-------
  This is a JSON text field where different module types are free to store
  their state however they wish.

  ``course``, ``chapter``, ``problemset``, ``sequential``, ``videosequence``

    The state for all of these container modules is a JSON object
    indicating the user's last known position within this container. This is
    1-indexed, not 0-indexed, mostly because it was released that way and a
    later change would have broken saved navigation state for users.

    Example: ``{"position" : 3}``

    When this user last interacted with this course/chapter/etc., she clicked
    on the third child element. Note that the position is a simple index and
    not a ``module_id``, so if you rearranged the order of the contents, it
    would not be smart enough to accommodate the changes and would point users
    to the wrong place.

    The hierarchy of these containers is
    ``course > chapter > (problemset | sequential | videosequence)``.

  ``combinedopenended``

    The JSON document includes attributes that identify the student's
    ``answer``, a ``rubric_xml`` that includes the complete XML syntax for the
    rubric, the ``score`` earned and the ``max_score``, and the ``grader_id``
    (the ``auth_user.id``) of each student who assessed the answer.

.. is a complete list of all possible attributes needed? 26 Feb 14

  ``conditional``

    Conditionals don't actually store any state, so this value is always an
    empty JSON object (`'{ }'`). These entries can be removed altogether.

  ``problem``

    There are many kinds of problems supported by the system, and they all
    have different state requirements. Note that a single problem can have
    many different response fields. If a problem generates a random circuit
    and asks five questions about it, then all of that is stored in one row in
    ``courseware_studentmodule``.

.. Include the different problem types and info about the state.

  ``selfassessment``

   In the course that used this module type, the JSON document included
   attributes for the ``student_answers``, the ``scores`` earned and
   ``max_score``, and any ``hints`` provided.

-------
grade
-------
  Floating point value indicating the total unweighted grade for this problem
  that the student has scored. Basically how many responses they got right
  within the problem.

  Only ``problem`` and ``selfassessment`` types use this column. All other
  modules set this to NULL. Due to a quirk in how rendering is done, ``grade``
  can also be NULL for a tenth of a second or so the first time that a user
  loads a problem. The initial load triggers two writes, the first of which
  sets the ``grade`` to NULL, and the second of which sets it to 0.

---------
created
---------
  Datetime when this row was created, which is typically when the student
  first accesses this piece of content.

  .. note:: For a module that contains multiple child modules, a row is
   created for each of them when the student first accesses one of them.

----------
modified
----------
  Datetime when this row was last updated. Set to be equal to ``created`` at
  first. A change in ``modified`` implies that there was a state change,
  usually in response to a user action like saving or submitting a problem, or
  clicking on a navigational element that records its state. However it can
  also be triggered if the module writes multiple times on its first load,
  like problems do (see note in ``grade``).

-----------
max_grade
-----------
  Floating point value indicating the total possible unweighted grade for this
  problem, or basically the number of responses that are in this problem.
  Though in practice it's the same for every entry with the same
  ``module_id``, it is technically possible for it to be anything.

  Another way in which ``max_grade`` can differ between entries with the same
  ``module_id`` is if the problem was modified after the ``max_grade`` was
  written and the user never went back to the problem after it was updated.
  This might happen if a member of the course team puts out a problem with
  five parts, realizes that the last part doesn't make sense, and decides to
  remove it. People who saw and answered it when it had five parts and never
  came back to it after the changes had been made will have a ``max_grade`` of
  5, while people who saw it later will have a ``max_grade`` of 4.

  Only graded module types use this column, with ``problem`` being the primary
  example. All other modules set this to NULL.

------
done
------
  Not used. The value ``na`` appears in every row.

-----------
course_id
-----------
  The course that this row applies to, in the format ``{key
  type}:{org}+{course}+{run}``. For example, ``course-v1:edX+DemoX+Demo_2014``.

  Because the same course content (content with the same ``module_id``) can be
  used in different courses, student state is tracked separately for each
  course.

  **History**: In October 2014, identifiers for some new courses began to use
  the format shown above. Other new courses, and all courses created prior to
  October 2014, use the format ``{org}/{course}/{run}``,  for example,
  ``MITx/6.002x/2012_Fall``.

.. _Certificates:

******************
Certificate Data
******************

.. _certificates_generatedcertificate:

==========================================================
Columns in the ``certificates_generatedcertificate`` Table
==========================================================

The ``certificates_generatedcertificate`` table tracks the state of
certificates and final grades for a course. The table is populated when a
script is run to grade all of the students who are enrolled in the course at
that time and issue certificates. The certificate process can be rerun and
this table is updated appropriately.

A sample of the heading row and two data rows in the
``certificates_generatedcertificate`` table follows.

.. code-block:: sql

 id  user_id  download_url  grade  course_id  key  distinction  status  verify_uuid
 download_uuid  name  created_date  modified_date error_reason  mode

 26  9999999
 https://s3.amazonaws.com/verify.edx.org/downloads/9_hash_1/Certificate.pdf
 0.84  BerkeleyX/CS169.1x/2012_Fall  f_hash_a   0   downloadable  2_hash_f
 9_hash_1  AAAAAA  2012-11-10  00:12:11  2012-11-10  00:12:13   honor

 27  9999999        0.0  BerkeleyX/CS169.1x/2012_Fall    0  notpassing  AAAAAA
 2012-11-10  00:12:11  2012-11-26  19:06:19  honor

The ``certificates_generatedcertificate`` table has the following columns.

+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+===============+==============+======+=====+=========+================+
| id            | int(11)      | NO   | PRI | NULL    | auto_increment |
+---------------+--------------+------+-----+---------+----------------+
| user_id       | int(11)      | NO   | MUL | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| download_url  | varchar(128) | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| grade         | varchar(5)   | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| course_id     | varchar(255) | NO   | MUL | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| key           | varchar(32)  | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| distinction   | tinyint(1)   | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| status        | varchar(32)  | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| verify_uuid   | varchar(32)  | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| download_uuid | varchar(32)  | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| name          | varchar(255) | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| created_date  | datetime     | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| modified_date | datetime     | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| error_reason  | varchar(512) | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
| mode          | varchar(32)  | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

---------
id
---------
  The primary key.

----------------------
user_id, course_id
----------------------
  The table is indexed by user and course.

--------------
download_url
--------------
  The ``download_url`` contains the full URL to the certificate.

-------
grade
-------
  The grade computed the last time certificate generation ran. If the
  courseware, student state, or grading policy change, the value in this
  column can be different than the grade shown on a student's Progress page.

---------
key
---------
  Used internally only. A random string that is used to match server requests
  to responses sent to the LMS.

-----------------
distinction
-----------------
  Not used.

  **History**: This was used for letters of distinction for 188.1x, but is not
  being used for any current courses.

--------
status
--------
  The status can be one of these states.

  .. list-table::
       :widths: 15 80
       :header-rows: 1

       * - Value
         - Description
       * - deleted
         - The certificate has been deleted.
       * - deleting
         - A request has been made to delete a certificate.
       * - downloadable
         - The student passed the course and a certificate is available for
           download.
       * - error
         - An error ocurred during certificate generation.
       * - generating
         - A request has been made to generate a certificate but it has not
           yet been generated.
       * - notpassing
         - The student's grade is not a passing grade.
       * - regenerating
         - A request has been made to regenerate a certificate but it has not
           yet been generated.
       * - restricted
         - No longer used. **History**: Specified when
           ``userprofile.allow_certificate`` was set to false: to indicate
           that the student was on the restricted embargo list.
       * - unavailable
         - No entry, typically because the student has not yet been graded for
           certificate generation.

  After a course has been graded and certificates have been issued, status is
  one of these values.

  * downloadable
  * notpassing

-------------
verify_uuid
-------------
  A hash code that verifies the validity of a certificate. Included on the
  certificate itself as part of a URL.

-------------
download_uuid
-------------
  A hash code that identifies this student's certificate. Included as part of
  the ``download_url``.

------
name
------
  This column records the name of the student that was set at the time the
  student was graded and the certificate was generated.

---------------
created_date
---------------
  Date this row in the database was created.

---------------
modified_date
---------------
  Date this row in the database was modified.

---------------
error_reason
---------------
  Used internally only. Logs messages that are used for debugging if the
  certificate generation process fails.

---------------
mode
---------------
  Contains the value found in the ``enrollment.mode`` field for a student and
  course at the time the certificate was generated: blank, audit, honor, or
  verified. This value is not updated if the student's ``enrollment.mode``
  changes after certificates are generated.
