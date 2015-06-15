
For YouTube videos, the ``pause-video`` event was not emitted before the
``stop-video`` event when a video ended. This issue is resolved. Both events
are now correctly emitted when a video ends. (TNL-2167) For details, see the
`Video Interaction Events <http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#video>`_ section in the *EdX
Research Guide*.
