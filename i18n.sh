#!/bin/bash

# This script purpose is to ease process needed to support i18n
# for the doc. It does that by first generating pot from the
# rst files of a  selected projects using sphinx to generate gettext
# (which outputs the pot files) and then the next step
# is to use sphinx-intl to write to the ./tx/config file, hence
# this script cerates the ./tx/config file. Note: if the file,
# already exists it will be overwritten!.
# This script assumes sphinx-intl is already installed as well,
# It can be installed by `pip install sphinx-intl`
# For more information, about sphinx-intl please visit:
# https://www.sphinx-doc.org/en/master/usage/advanced/intl.html


# Check if this script is running by github, and if it's
# missing the token then exit.
if [ "$CI" = true ] && [ -z "$TX_TOKEN" ]; then
echo 'Running cancelled, missing TX_TOKEN!'
exit 1
fi

IFS= read -r -p "Enter the project name as it appears in Transifex: " PROJECT_NAME

echo "$PROJECT_NAME"

# Root directory
BASE_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
# Config file
TX_CONFIG_FILE=$BASE_DIR/.tx/config

# Success  exit message, wrapped in green color.
EXIT_MESSAGE="\033[0;32mYou should now be able to push the files using tx client \n
Typically this done by 'tx push -s', please note: you should have \n
already installed tx client and configured it such that there is \n
a project called 'open-edx-documentation-project' in the organization \n
and that you already have authenticated with in '~/.transifexrc', \n
for more  information, please visit: \n
https://docs.transifex.com/client/client-configuration.\033[0m"

# Preparing the config file:
rm -rf .tx
mkdir $BASE_DIR/.tx
touch $TX_CONFIG_FILE
echo "[main]" >> $TX_CONFIG_FILE
echo "host = https://www.transifex.com" >> $TX_CONFIG_FILE


# The set of books to run translations for.
# Currently this is only a subset of the books in this repo because we are in the middle of
# assesing which books will remain a part of openedx and which ones are actually specific
# to edx.org
projects=(
    "en_us/open_edx_students"
    "en_us/open_edx_course_authors"
    "en_us/open_edx_release_notes"
    )

# Iterating over each project defined above, to generate the pot the files
# and then mapping the files accordingly in the tx config file
for project in "${projects[@]}"; do
    cd $BASE_DIR/$project
    echo "--> Start generating the pot files for ${project#'en_us/'}"

    # Extract translatable messages into pot files
    make gettext

    # Adding the pot files to tx config file
    echo "--> Start writing tx configuration for the ${project#'en_us/'}"

    cd $BASE_DIR
    sphinx-intl update-txconfig-resources \
    --pot-dir $BASE_DIR/$project/build/locale/ \
    --locale-dir $BASE_DIR/$project/locales/ \
    --transifex-project-name "$PROJECT_NAME"

    python tx_config_fix.py "$project"

done

# Todo: Check for errors and set exit message accordingly

echo -e ${EXIT_MESSAGE}


