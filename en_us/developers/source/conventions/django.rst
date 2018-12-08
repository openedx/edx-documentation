.. _Django Good Practices:

*********************
Django Good Practices
*********************

.. contents::
 :local:
 :depth: 2

=======
Imports
=======

Always import from the root of the project::

    from lms.djangoapps.hologram.models import 3DExam    # GOOD
    from .models import 3DExam                           # GOOD
    from hologram.models import 3DExam                   # BAD!

The second form (relative import) only works correctly if the importing module is itself imported correctly.  As long as there are no instances of the third form, everything should work.  Don't forget that there are other places that mention import paths::

    url(r'^api/3d/', include('lms.djangoapps.hologram.api_urls')),   # GOOD
    url(r'^api/3d/', include('hologram.api_urls')),                  # BAD!

    @patch('lms.djangoapps.hologram.models.Key', new=MockKey)        # GOOD
    @patch('hologram.models.Key', new=MockKey)                       # BAD!

    INSTALLED_APPS = [
        'lms.djangoapps.hologram',    # GOOD
        'hologram',                   # BAD!
    ]
