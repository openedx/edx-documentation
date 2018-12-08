.. _Video Components:

#################################
Video Components
#################################

You can add video components to any container in your course (such as
a vertical or sequential). Studio places all video components inside
verticals (which it calls units).

.. contents::
  :local:
  :depth: 1

**********************************************
Create the XML File for a Video Component
**********************************************

To add a video component to your course, add it to the course XML tree as
follows.

.. code-block:: xml

  <video
    youtube="1.00:o2pLltkrhGM"
    url_name="Introduction_Lecture"
    display_name="Introduction Lecture"
    youtube_id_1_0="o2pLltkrhGM">
  </video>

If you prefer to place the video component in its own file, you create an XML
file in the ``video`` directory for each video component in your course.

The name of the XML file must match the value of the @url_name attribute of the
``video`` element in the vertical XML file.

For example, the vertical XML file uses the following format.

.. code-block:: xml

   <vertical display_name="Lesson_1_Unit_1">
      <video url_name="Introduction_Lecture"/>
      . . .
  </vertical>

You create the file ``video/Introduction_Lecture.xml`` to define the video
component.

*************************************
Video Component XML File Elements
*************************************

The root element of the XML file for the HTML component is file is ``video``.

The ``video`` element contains a single ``source`` element.

==============================
``source`` Element
==============================

The ``source`` element contains the following attribute.

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``src``
     - The file path for the video file.


*************************************
``video`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``display_name``
     - Required. The value that is displayed to students as the name of the
       video component. If you do not supply a ``display_name`` value, "video"
       is supplied for you.
   * - ``youtube``
     - The speed and ID pairings for the YouTube video source. The value can
       contain multiple speed:ID pairs, separated by commas.
   * - ``download_track``
     - Whether students can download the video track. ``true`` or ``false``.
   * - ``download_video``
     - Whether students can download the video. ``true`` or ``false``.
   * - ``html5_sources``
     - The file path for the HTML5 version of the video.
   * - ``show_captions``
     - Whether students can view the video captions. ``true`` or ``false``.
   * - ``source``
     - TBD
   * - ``sub``
     - TBD
   * - ``youtube_id_0_75``
     - The YouTube ID for the video that plays at 75% normal speed.
   * - ``youtube_id_1_0``
     - The YouTube ID for the video that plays at 100% normal speed.
   * - ``youtube_id_1_25``
     - The YouTube ID for the video that plays at 125% normal speed.
   * - ``youtube_id_1_5``
     - The YouTube ID for the video that plays at 150% normal speed.


*************************************
Example Video Component XML File
*************************************

The following example shows an XML file for a video component.

.. code-block:: xml

  <video
    youtube="0.75:xGKlr7nT_Zw,1.00:o2pLltkrhGM,1.25:XGsB9bA6rGU,1.50:_HuIF16HdTA"
    url_name="Introduction_Lecture"
    display_name="Introduction Lecture"
    download_video="true"
    html5_sources="[&quot;https://s3.amazonaws.com/edx-course-videos/school/DemoCourseIntroductionVideo.mov&quot;]"
    source=""
    youtube_id_0_75="xGKlr7nT_Zw"
    youtube_id_1_0="o2pLltkrhGM"
    youtube_id_1_25="XGsB9bA6rGU"
    youtube_id_1_5="_HuIF16HdTA">

    <source src="https://s3.amazonaws.com/edx-course-videos/mit-6002x/6002-Tutorial-00010_100.mov"/>
  </video>
