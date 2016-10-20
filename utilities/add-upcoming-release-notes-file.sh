#!/bin/bash
#
# Create a new RST file to hold a release note for the upcoming release, 
# if it doesn't already exist.
#
# Invoke this script from the command line. It does not matter which 
# directory you invoke it from.
#
#    ./add-upcoming-release-notes-file.sh
#

platform='unknown'
unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
    platform='linux'
elif [[ "$unamestr" == 'Darwin' ]]; then
    platform='darwin'
elif [[ "$unamestr" == 'FreeBSD' ]]; then
    platform='freebsd'
fi

# These are the categories of release notes. If we add a new category,
# for example, certificates, add a label to this list.
NOTE_CATEGORIES="analytics documentation lms mobile openedx studio website"

# Relative path from the utilities directory to the release notes source
RELEASE_NOTES_SOURCE_PATH="../en_us/release_notes/source/"
SCRIPT_DIRECTORY=`dirname ${0}`

# Temporarily change to the script directory, so we can use relative paths.
pushd ${SCRIPT_DIRECTORY}

# Gather some information about file paths, for labeling.
ABSOLUTE_SCRIPT_DIRECTORY="`pwd | sed 's%/utilities%%'`"
ABSOLUTE_RELEASE_NOTES_SOURCE_PATH=`echo ${RELEASE_NOTES_SOURCE_PATH} | sed "s%..%${ABSOLUTE_SCRIPT_DIRECTORY}%"`

# Explain what the script is doing.
echo ""
echo "Hello, writer! This script adds a new RST documentation source file to hold release notes for the upcoming release. It will not overwrite existing files."

# Find out which release notes category the new note fits in.

echo ""
echo "These are the categories for release notes. Choose a category based on the audience who needs the note. If the note you are writing does not fit in any of the categories, contact the edX documentation team (docs@edx.org)."
echo ""

for POSSIBLE_CATEGORY in ${NOTE_CATEGORIES}
do
    echo "    ${POSSIBLE_CATEGORY}"
done

echo ""
echo "Enter the category that you are adding a note to."

read NOTE_CATEGORY

for POSSIBLE_CATEGORY in ${NOTE_CATEGORIES}
do
    if [[ ${NOTE_CATEGORY} == ${POSSIBLE_CATEGORY} ]]
    then
        NOTE_CATEGORY_VALID="true"
    fi
done

if [[ ${NOTE_CATEGORY_VALID} != "true" ]]
then
    echo ""
    echo "${NOTE_CATEGORY} is not a valid category."
    exit 1
fi

# Determine the date of the upcoming Monday.

POSSIBLE_UPCOMING_MONDAY_OFFSET=0

while [[ -z ${UPCOMING_MONDAY_DATE} ]]
do
    
    if [[ $platform == 'linux' || $platform == 'unknown' ]]; then
        POSSIBLE_UPCOMING_MONDAY_DAY_OF_WEEK=`date -d "+${POSSIBLE_UPCOMING_MONDAY_OFFSET} days" +%a`
    else
        POSSIBLE_UPCOMING_MONDAY_DAY_OF_WEEK=`date -v +${POSSIBLE_UPCOMING_MONDAY_OFFSET}d +%a`
    fi
    
    if [[ ${POSSIBLE_UPCOMING_MONDAY_DAY_OF_WEEK} == "Mon" ]]
    then
        # This is where we set the date string format.
        if [[ $platform == 'linux' || $platform == 'unknown' ]]; then
            UPCOMING_MONDAY_DATE=`date -d "+${POSSIBLE_UPCOMING_MONDAY_OFFSET} days" +%Y-%m-%d`
            UPCOMING_MONDAY_YEAR=`date -d "+${POSSIBLE_UPCOMING_MONDAY_OFFSET} days" +%Y`
        else
            UPCOMING_MONDAY_DATE=`date -v +${POSSIBLE_UPCOMING_MONDAY_OFFSET}d +%Y-%m-%d`
            UPCOMING_MONDAY_YEAR=`date -v +${POSSIBLE_UPCOMING_MONDAY_OFFSET}d +%Y`
        fi

    else
        POSSIBLE_UPCOMING_MONDAY_OFFSET=`expr ${POSSIBLE_UPCOMING_MONDAY_OFFSET} + 1`
    fi
done

# Add a new RST file for the upcoming date, in the release note category directory.

NEW_NOTE_FILE_NAME="${UPCOMING_MONDAY_YEAR}/${NOTE_CATEGORY}/${NOTE_CATEGORY}_${UPCOMING_MONDAY_DATE}.rst"

if [[ -e "${RELEASE_NOTES_SOURCE_PATH}/${NEW_NOTE_FILE_NAME}" ]]
then
    echo ""
    echo "The source file for that category already exists. Add your note to:"
    echo ""
    echo "    ${ABSOLUTE_RELEASE_NOTES_SOURCE_PATH}${NEW_NOTE_FILE_NAME}"
    echo ""
else
    echo ""
    echo "Creating the source file for that category. Add your note to:"
    echo ""
    echo "    ${ABSOLUTE_RELEASE_NOTES_SOURCE_PATH}${NEW_NOTE_FILE_NAME}"
    echo ""
    
    # If the year and/or category directory isn't present, create it.
    if [[ ! -e "${RELEASE_NOTES_SOURCE_PATH}${UPCOMING_MONDAY_YEAR}/${NOTE_CATEGORY}" ]]
    then
        mkdir -p ${RELEASE_NOTES_SOURCE_PATH}${UPCOMING_MONDAY_YEAR}/${NOTE_CATEGORY}
    fi
    
    # Define a function that writes comments to the new note source file.
    write_note_comment () {
        echo ".. ${1}" >> ${RELEASE_NOTES_SOURCE_PATH}${NEW_NOTE_FILE_NAME}
    }
    
    # Add a comment to the top of the new RST file.
    
    write_note_comment "Add release notes for the ${NOTE_CATEGORY} audience in RST format here."
    write_note_comment "The edX documentation team will include this file in the index "
    write_note_comment "file for the upcoming release. If you add more than one note, format the"
    write_note_comment "notes as a bulleted list by preceding each note with an asterisk."
    write_note_comment
    write_note_comment "If your release note change is associated with a JIRA item, add the"
    write_note_comment "JIRA ticket number at the end of your item."
    write_note_comment
    write_note_comment "For example:"
    write_note_comment
    write_note_comment "To improve the experience of learners who use screen readers, the"
    write_note_comment "learner dashboard now provides additional, course specific context for"
    write_note_comment "each of the Upgrade to Verified or View XSeries Details options that"
    write_note_comment "appear on this page. (:jira:\`ECOM-4269\`, :jira:\`ECOM-4270\`)"
    write_note_comment

    
fi

popd

exit 0
