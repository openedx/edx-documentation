In Dec 2015 and Jan 2016, edX added several accessibility enhancements to the
video player's controls. This release includes the following updates to the
events that the video player emits. (AC-383, AC-385, and AC-444)

* The button that shows or hides a transcript file on the right of the video
  was relabeled from CC to ``"``. The video player emits the existing
  ``show_transcript``/``edx.video.transcript.shown`` and
  ``hide_transcript``/``edx.video.transcript.hidden`` events when users
  interact with this control.

* A button, labeled CC, was added to show or hide closed captions, which are
  overlaid on the video while it plays. The video player emits new events,
  ``edx.video.closed_captions.shown`` and ``edx.video.closed_captions.hidden``,
  when users interact with this control.

* A menu for selecting a different language for the transcript and closed
  captions was added. The video player emits the existing
  ``video_hide_cc_menu`` and ``video_show_cc_menu`` when users interact with
  this control. In addition, these events now include ``name`` values of
  ``edx.video.language_menu.hidden`` and ``edx.video.language_menu.shown``,
  respectively, and the
  ``video_hide_cc_menu``/``edx.video.language_menu.hidden`` events include a
  new ``event`` member field, ``language``.

For more information, see :ref:`data:video`.

