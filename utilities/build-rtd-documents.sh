#!/bin/bash

# This script invokes the REST API that builds edX Read the Docs projects
# for publicly visible documents.
# The script requires the curl HTTP client (installed by default in most
# Linux and Mac OSes) and a connection to the internet. Verify that you
# have curl installed by invoking the "curl --version" command in a
# terminal.

# To run this script, navigate to its directory and make sure the file is executable:

# C1MQH7NLG944:~ peterdesjardins$ chmod a+x build-rtd-documents.sh 
# C1MQH7NLG944:~ peterdesjardins$ ls -l build-rtd-documents.sh
# -rwxr-xr-x  1 peterdesjardins  staff  758 Feb  2 14:12 build-rtd-documents.sh

# Invoke the script from the command line:

# C1MQH7NLG944:~ peterdesjardins$ ./build-rtd-documents.sh


if [ -z ${1} ]
then
   DOC_IDS="edx
            edx-partner-course-staff
            edx-insights
            devdata
            edx-guide-for-students
            edx-installing-configuring-and-running
            open-edx-building-and-running-a-course
            open-edx-learner-guide
            edx-developer-guide
            edx-open-learning-xml
            xblock-tutorial
            edx-release-notes
            course-catalog-api-guide
            "
else
   DOC_IDS=${1}
fi
         
# xblock - Removed this project because it is failing local builds
# edx-platform-api - Removed from list because of its separate repo
# edx-data-analytics-api - Removed from list because of its separate repo

for DOC_ID in ${DOC_IDS}
do

  # Report the document ID
  echo "Building ${DOC_ID}"
  # Invoke the build API for the document ID using curl
  curl -X POST https://readthedocs.org/build/${DOC_ID}
  
done
