
For YouTube videos, the ``pause_video`` event was not emitted before the
``stop_video`` event when a video ended. This issue is resolved. Both events
are now correctly emitted when a video ends. (TNL-2167) For details, see the
:ref:`data:video` section in the *EdX Research Guide*.
