Thanks for contributing to the edX release notes!

Release notes are set up as a collection of ReStructured Text (.rst) files.
There is one file for each of several categories:

* Analytics
* Documentation
* LMS
* Mobile
* Open edX
* Studio
* The edx.org website

To add a release notes item, you determine the category for the item,
and then enter the item in the .rst file for that category. The documentation
team then copy edits the file and adds it to the index file for the week's
release notes.

Complete instructions follow.

************************
Add a Release Notes Item
************************

To add a release notes item, follow these steps.

1. Change to the edx-documentation directory.

2. Create a new branch.

3. On your branch, run the following command.

   ./add-upcoming-release-notes-file.sh

4. At the prompt, enter the category that you want, and then press Enter.

   The script returns a message with the name and location of the .rst file
   where you will add your item. If the file does not already exist, the script
   creates the file.

   For example, the file might have the following name.

   /edx-documentation/en_us/release_notes/source/2016/lms/lms_2016-07-25.rst

5. In a text editor, open the file and follow the inline instructions to add
   your note.

6. Save, commit, and push your changes.

7. Open a PR for your branch and resolve any merge conflicts.

   The doc team is tagged automatically when you open your PR and will complete
   any necessary copy editing. The doc team will also add the new files to the
   release notes index.


