#############################################
Develop the Documentation Translation Process
#############################################


***********
Description
***********

The edx-documentation repo contains important documentation written in English.
Many users have a requirement for the important information found in this
repository to be available in other languages. In order to provide the
documentation in a variety of languages, a process must be designed and agreed
upon to serve the greater open source community.

In this ADR, we will describe:
 #. When the translation process is triggered
 #. How the translation process is triggered
 #. How the translation process works
 #. How the translated documents will be integrated back into the documentation


************************
Answers to the questions
************************

1. When is the translation process triggered?
=============================================

Every six months, a newly named Open edX release is created, which includes the
documentation. When this release is "cut", the translation process should also
be triggered. For example, where the Nutmeg version of the Open edX software is
released, the translation process should also be triggered to translate the
Nutmeg Documentation.

2. How is the translation process triggered?
=============================================

An Admin account must add documents to a Transifex Project in order for them to
be translated. Admin accounts have access to financial information and the
ability to delete Transifex Projects. In order to keep this part of the process
secure, we believe that a human should be involved in this process to assure
that financial information stays in the right hands and so that an accidental
merge will not delete Transifex projects. Currently, a GitHub bot account with
Admin access to Transifex updates the translations for several repositories.
This is the old and insecure way of doing it that neither Transifex nor GitHub
recommend. We are retiring that bot account in preference to this secure and
modern method. We believe that elevated permissions should not be granted to a
bot or an app, and we should instead do a bit of the work manually to ensure
that we receive the results we want. That is not to say that some parts of this
process cannot be automated.

Bringing translatable documentation material into Transifex:
 #. When a new named release is cut, a Github Pull Request should be created
    that tags Github users that are also Transifex Admins. This GitHub PR will
    contain the generated files to be uploaded to Transifex.
 #. To complete the process, the Github User/Transifex Admin will pull the PR
    and locally run a script which uses their own credentials that uploads the
    documents to Transifex.
 #. The user would then merge the PR as a record that the material is on
    Transifex and ready to be translated by the greater open source community.

3. How does the translation process work?
=============================================

Translators use Transifex to translate strings stripped from the documentation.
These strings are kept in a Project in Transifex, where each string belongs to
a uniquely named document, which is related to a document in the documentation.
In Transifex, Projects can be grouped together to share the same "Transifex
Memory". Through this feature, strings from previous releases of the
documentation that are identical to the current release of documentation will
be automatically translated, thus speeding up the time it takes to translate
the entire document. For example, if the Nutmeg release has been completely
translated and is in Transifex Memory, when the Olive release is cut, the
strings will look for identical strings from the Documentation in the Nutmeg
release and automatically populate them.

Upcoming work will automate the process of syncing files between GitHub and
Transifex. Once a preset fraction of the strings are translated, a notice will
be triggered to Transifex Admins that translations are ready. This will create
a new Pull Request with these new translations. A maintainer of the
edx-documentation repo will be asked for a review, and in combination with
Transifex Admins, merged. In addition, this syncing process can be run
regularly after the threshold is reached in order to increase the fraction of
strings translated.

4. How will the translated documents be integrated back into the documentation?
===============================================================================

Translated documents will be kept in a newly created separate repository to
avoid having to recut a named Open edX release everytime translations are added
or updated. During the building process of the documents, it will check for the
existence of these translated documents, and build with them if they exist.
Translations will be available both by locale and by selection as is currently
supported by Sphinx and Read the Docs. So for example, while the default option
for document readers in the US locale will be English, they will also be able
to select other translated documents.


*********
Rationale
*********

This process is guided by the respect for secure measures with financial
information, the desire to keep everything as open source as possible by
keeping PR records, and by the hybrid Human-Computer process involved with
translating documentation.


**********
Next Steps
**********

Not all of the documentation lives in the openedx/edx-documentation repository.
In the future documentation will continue to be distributed amongst a number of
repositories. The process described here will be used as a guide to bring
Translations efficiently and consistently to all Open edX documentation
repositories.


******************
Location in GitHub
******************

The documentation will remain in openedx/edx-documentation. It time permits,
engineering work will be done so that the translations can be located in a new
repository named openedx/documentation-translations. If not, the translations
will be co-located with the original strings as per the pattern in other Open
edX repositories.

Moving the translations to their own repository could be beneficial. Keeping
the translations separate from the code that generates the documentation could
decrease repo clone/pull time. In addition, all translations could be kept in
the same repo, and only the translations needed could be pulled from this repo.
Lastly, when a new release of the documentation is cut, it can be separate from
the translations that may be updating over a longer period of time, but still
connected to a specfic version of the documentation.
