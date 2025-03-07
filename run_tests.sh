#!/bin/bash

# Each documentation project is in a directory in the en_us folder.
# To generate docs for a project, Go to a project directory and
# run `make HTML` and `make latexpdf`.

# To test a subset of projects you can pass them in as command line
# arguments to this script.  For example:
# `./run_tests.sh en_us/install_operations` would only run tests on
# the install operations project.

# The directory that this script is located in.
BASE_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# FAILED_BUILDS are builds that had either a SPHINX_ERROR
# or a BUILD_ERROR
FAILED_BUILDS=()

# BUILD_ERRORS are errors that resulted in the doc build
# exiting with a non-zero exit status.
BUILD_ERRORS=0

# SPHINX_ERRORS are errors that are reported by Sphinx
# but do not cause the doc build to return a non-zero exit
# status. These are considered a build failure from a CI
# perspective though.
SPHINX_ERRORS=0

# SPHINX_WARNINGS are warning messages generated by Sphinx
# while building the docs.
SPHINX_WARNINGS=0

projects=($@)
if [ ${#projects[@]} -eq 0 ]
then
    projects=(
        "en_us/contribute"
        "en_us/course_authors"
        "en_us/data"
        "en_us/developers"
        "en_us/discovery_api"
        "en_us/edx_style_guide"
        "en_us/enterprise_api"
        "en_us/install_operations"
        "en_us/landing_page"
        "en_us/open_edx_course_authors"
        "en_us/open_edx_release_notes"
        "en_us/edx_students"
        "en_us/students_redirect"
    )
fi

for project in "${projects[@]}"; do
    cd $BASE_DIR/$project
    echo "--> Starting pre-build for $PWD"

    # Generate docs just to get the cross-project references.
    # -j4 uses four parallel workers to build faster.
    # -E Don’t use a saved environment (the structure caching all
    #    cross-references), but rebuild it completely.
    make html SPHINXOPTS="-j4 -E"
done

all_bad_file=$BASE_DIR/test_root/bad.log
echo "Problems:" >$all_bad_file

for project in "${projects[@]}"; do
    cd $BASE_DIR/$project
    echo "--> Starting build for $PWD"
    project_build_status=0

    # Make sure log dir exists
    err_log_dir=$BASE_DIR/test_root/$project
    err_log_file=$err_log_dir/err.log
    mkdir -p $err_log_dir

    # Generate html docs.
    # -j4 uses four parallel workers to build faster.
    # -w writes warnings and errors to the specified file in
    #    addition to stderr.
    # -n runs in nit-picky mode.
    make html SPHINXOPTS="-j4 -n -w $err_log_file"

    if [ $? -gt 0 ]; then
        project_build_status=1
        BUILD_ERRORS=$((BUILD_ERRORS + 1))
    fi

    num_errors=$(egrep -c 'ERROR:|SEVERE:' < $err_log_file)
    num_warnings=$(egrep -c 'WARNING:' < $err_log_file)
    egrep 'ERROR:|SEVERE:|WARNING:' < $err_log_file >>$all_bad_file

    echo SPHINX ERRORS: $num_errors
    echo SPHINX WARNINGS: $num_warnings
    echo

    if [ $num_errors -gt 0 ]; then
        project_build_status=1
        SPHINX_ERRORS=$((SPHINX_ERRORS + num_errors))
    fi

    if [ $num_warnings -gt 0 ]; then
        project_build_status=1
        SPHINX_WARNINGS=$((SPHINX_WARNINGS + num_warnings))
    fi

    if [ $project_build_status -gt 0 ]; then
        FAILED_BUILDS+=($project)
    fi
done

# Report and exit with the correct code
echo '********** All builds done ************'
echo TOTAL SPHINX ERRORS: $SPHINX_ERRORS
echo TOTAL SPHINX WARNINGS: $SPHINX_WARNINGS
echo OTHER BUILD ERRORS: $BUILD_ERRORS

EXIT_STATUS=0
if [ ${#FAILED_BUILDS[@]} -gt 0 ]; then
    echo "There were problems while building the following projects:"
    for project in "${FAILED_BUILDS[@]}"; do
        echo $project
    done
    cat $all_bad_file
    EXIT_STATUS=1
else
    echo "All builds passed."
fi

exit $EXIT_STATUS
