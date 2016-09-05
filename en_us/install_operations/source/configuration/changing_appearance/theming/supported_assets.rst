.. _Supported Themable Assets:

*************************
Supported Themable Assets
*************************

In theory, all core assets in the LMS and Studio can be overriden by themed assets.
In practice, most of the system assumes that core assets are not currently
overridden by themed assets, and you might see unexpected behavior
if you override certain assets.
So far, the list of supported themable assets is limited to the following set.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Component
     - Asset
     - Description

   * - LMS
     - ``images/logo.png``
     - The logo for the LMS. Displayed in the upper left corner of the LMS.

   * - Studio
     - ``images/studio-logo.png``
     - The logo for Studio. Displayed in the upper left corner of Studio.

   * - LMS
     - ``images/profiles/default_30.png``
       ``images/profiles/default_50.png``
       ``images/profiles/default_120.png``
       ``images/profiles/default_500.png``
     - Default profile images for learner profiles.
       The default image displays for learners until they upload their own
       profile images. These images are named based on their sizes:
       30px by 30px, 50px by 50px, 120px by 120px, and 500px by 500px,
       respectively.
