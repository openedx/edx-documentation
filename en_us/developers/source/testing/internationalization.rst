********************
Internationalization
********************

Any new text that is added should be internationalized and translated.

Testing translations with dummy translations
============================================

Any text you add to the platform should be internationalized. To generate translations for
your new strings, run the following command.

    ``paver i18n_dummy``

This command generates dummy translations for each language supported in the platform and
puts the dummy strings in the appropriate language files. You can preview the dummy languages
on your local machine and also in your sandbox, if and when you create one.

Please make sure these dummy language files created are not included in your commits!
