"""A script to create a transifex project when an open-release occur"""
import sys
import requests

OPENEDX_ORG_ID = "open-edx"
TRANSIFEX_API = "https://rest.api.transifex.com"
REPO_URL = "https://github.com/openedx/edx-platform"


def check_arguments_health():
    """
    Check the correctness of the expected arguments such as:
    sys.argv[0]: Is not checked for and is suppose to be this file/script name.
    sys.argv[1]: Is the open-release name, and is expected to start with
    'open-release' and end with .1
    sys.argv[2]: Is the transifex token, and only checked that is not an empty
    string. If it's wrong, invalid, or expired...etc. It would be indicated by
    other function handle_request_error().
    len(sys.argv): If the there was less or more than 3 arguments, it will
    fail.
    And accordingly it would return:
    returns True: If all good it will return True.
    sys.exit('error message'): Whenever any of the checks above fails.
    """
    if len(sys.argv) < 3:
        sys.exit(
            "Too few arguments, we need release name followed by TX token"
        )
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments!")
    else:
        tx_token = sys.argv[2]
        release_name = sys.argv[1]
        if tx_token == "":  # Check that Transifex token is not null
            sys.exit("Transifex token is empty. Job aborted")
        if not (
            release_name.startswith("open-release")
            and release_name.endswith(".1")
        ):
            sys.exit(
                """Aborted because: it's either not an open-release or not the
                first version of an open-release"""
            )
        return True


def convert_release_to_project_slug():
    """
    This is a simple function that takes release name in this format
    'open-release/tictactoe.1' and return as 'openedx-documentation-tictactoe'.
    This is important to do because transifex doesn't support '/' for projects
    slug which has to be unique as well.
    Return project slug: a project slug for the release.
    """
    release_name = sys.argv[1].split("/")[1].split(".")[0]
    return f"openedx-documentation-{release_name}"


def handle_request_error(response, context):
    """
    A helper function for handeling failed requests while trying to request
    something form transifex API. It handels the cases according to the API
    documentation:
    401: It occurs when the token is invalid
    403: It occur when the token is valid, but not with sufficient permission
    *: It would just print the status code and response body
    """
    code = response.status_code
    if code == 401:
        sys.exit(
            f"Unauthorized or invalid token! while trying to {context}.\n"
            f"More details: {response.text}"
        )
    elif code == 403:
        sys.exit(
            f"TX token doesn't have the right permission for {context}.\n"
            f"More details: {response.text}"
        )
    else:
        sys.exit(
            f"Request for {context} returned with {code}.\n"
            f"Detailed response: {response.text}"
        )


def is_project_exist():
    """
    This function given a release name, it will (or try) to get info about the
    project as if it was already created. And if transifex returns 404, then
    this means the project doesn't exist.
    Return False: if a project for release doesn't exist in Transifex.
    Exit 1: If status code is 200, i.e. (the project already exists).
    Otherwise it will forward the request to the helper function
    handle_request_error().
    """
    headers = {
        "Accept": "application/vnd.api+json",
        "Authorization": f"Bearer {sys.argv[2]}",
    }
    url = (f"{TRANSIFEX_API}/projects/o:{OPENEDX_ORG_ID}:p:"
           f"{convert_release_to_project_slug()}"
           )
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return False
    if response.status_code == 200:
        sys.exit(
            f"Project with slug {convert_release_to_project_slug()}, already"
            f"exist. Job aborted!."
        )
    else:
        return handle_request_error(response, context="getting a project detail")


def create_transifex_project():
    """
    It tries to create a new transifex project, with configuration which can be
    altered, e.g. passing a new arg that indicate weather the project should
    machine translation, machine memory...etc.
    If the function succeed, (i.e. request to create project returned 200), it
    will exit the script with 0 code, and printing the url of the project.
    Otherwise it will forward the request to the helper function
    handle_request_error().
    """
    payload = {
        "data": {
            "attributes": {
                "machine_translation_fillup": False,
                "translation_memory_fillup": True,
                "name": convert_release_to_project_slug().replace('-', ' ')
                .title(),
                "private": False,
                "slug": convert_release_to_project_slug(),
                "repository_url": REPO_URL,
            },
            "relationships": {
                "organization": {
                    "data": {
                        "id": f"o:{OPENEDX_ORG_ID}",
                        "type": "organizations",
                    }},
                "source_language": {
                    "data": {
                        "id": "l:en_US",
                        "type": "languages"}},
            },
            "type": "projects",
        }}
    headers = {
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json",
        "Authorization": f"Bearer {sys.argv[2]}",
    }
    url = f"{TRANSIFEX_API}/projects"
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(
            f"A transifex project for {sys.argv[1]}, has been successfully"
            f"created! \n"
            f"You can access the project at: https://www.transifex.com/"
            f"{OPENEDX_ORG_ID}/{convert_release_to_project_slug()} \n"
            f"Happy Translations!")
        sys.exit(0)
    else:
        handle_request_error(response, f"Creating a project for {sys.argv[1]}")


if __name__ == "__main__":
    if check_arguments_health() and not is_project_exist():
        create_transifex_project()
