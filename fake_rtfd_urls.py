import os
import os.path
import re
import sys

import requests


BASE_URL = 'http://edx.readthedocs.io/projects/'
VERSIONS = {
    'master': '/en/latest/',
    'openedx': '/en/open-release-ficus.master/',
}

BOOK_URLS = {
    'course_authors': ('edx-partner-course-staff', 'master'),
    'release_notes': ('edx-release-notes', 'master'),
    'data': ('devdata', 'master'),
    'students': ('edx-guide-for-students', 'master'),
    'open_edx_release_notes': ('open-edx-release-notes', 'master'),
    'open_edx_course_authors': ('open-edx-building-and-running-a-course', 'openedx'),
#    'course_catalog_api_user_guide'
#    'landing_page'
#    'ORA2'
#    'install_operations'
#    'edx_style_guide'
#    'developers'
#    'open_edx_students'
}

def find_pages(root):
    for here, _, filenames in os.walk(root):
        if 'build/html' in here:
            for filename in filenames:
                if filename.endswith(".html"):
                    filepath = os.path.join(here, filename)
                    one_page(filepath)

def one_page(filepath):
    match = re.search(r"en_us/(\w+)/build/html/(.*)$", filepath)
    assert match
    book, page = match.groups()
    book_data = BOOK_URLS.get(book)
    if book_data is not None:
        url, version = book_data
        url = BASE_URL + url + VERSIONS[version] + page

        response = requests.get(url)
        if response.status_code != 200:
            print "URL {!r} returned {}".format(url, response.status_code)
        sys.stdout.write(".")
        sys.stdout.flush()

if __name__ == '__main__':
    find_pages(".")
