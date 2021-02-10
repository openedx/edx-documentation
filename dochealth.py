"""
Uses the readthedocs API to assess the publishing health of our books.
Results are written in two forms, readble to stdout, and to health.csv.

Setting up authentication:

- Get an API token from https://readthedocs.org/accounts/tokens/

- Then, either:

  1. Define a READTHEDOCS_TOKEN environment variable with the token, or

  2. Edit or create your ~/.netrc file to have an entry like this:

        machine readthedocs.org
            login edx
            password 247cb3fb3fcc8f919a81842ce8160b2c92ee0c86


Running::

    $ python dochealth.py

This will write information to the terminal, and also create a health.csv file
to import into a spreadsheet.

"""

import collections
import csv
import netrc
import os
import requests
import time

CSV_FILE = "health.csv"

class ReadthedocsAuth:
    """Implement readthedocs.org "token: xxxxx" authentication for requests."""
    def __call__(self, req):
        token = os.environ.get("READTHEDOCS_TOKEN")
        if token is None:
            credentials = netrc.netrc().hosts.get("readthedocs.org")
            assert credentials is not None, f"No API token! See the instructions in the {__file__} docstring."
            token = credentials[2]
        req.headers["Authorization"] = f"token {token}"
        return req

def get_data(url):
    while True:
        resp = requests.get(url, auth=ReadthedocsAuth())
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 429:
            # Rate-limited. Simple-minded waiting.
            time.sleep(10)
            continue
        resp.raise_for_status()

def normalize_url(url):
    if url.endswith(".git"):
        url = url[:-4]
    if url.startswith("http:"):
        url = "https:" + url[5:]
    if url.endswith("/"):
        url = url[:-1]
    return url

with open(CSV_FILE, "w") as health_out:
    writer = csv.writer(health_out)
    writer.writerow([
        "repo",
        "title",
        "branch",
        "last_build",
        "succeeded",
        "last_good_build",
    ])

    data = get_data("https://readthedocs.org/api/v3/projects/?limit=100")
    assert data["next"] is None, "Oops, more than 100 projects, have to update the code"
    print(f"{data['count']} projects")

    by_repo = collections.defaultdict(list)
    for proj in data["results"]:
        url = normalize_url(proj["repository"]["url"])
        by_repo[url].append(proj)

    for url, projs in sorted(by_repo.items()):
        show_count = ""
        if len(projs) > 1:
            show_count = f" {len(projs)} projects"
        print(f"repo {url}:{show_count}")
        for proj in projs:
            show_branch = ""
            branch = proj["default_branch"]
            if branch != "master":
                show_branch = f" (branch {branch})"
            print(f"""    "{proj["name"]}"{show_branch}""")
            build_url = proj["_links"]["builds"] + "?limit=100"
            builds = get_data(build_url)["results"]
            build = builds[0]
            show_status = ""
            if not build["success"]:
                show_status = " failed"
            print(f"""        latest build: {build["created"]}{show_status}""")
            if build["success"]:
                last_good = build
            else:
                last_good = next((b for b in builds if b["success"]), None)
                if last_good is None:
                    print("        ** no successful build")
                else:
                    print(f"""        last success: {last_good["created"]}""")
            writer.writerow([
                url,
                proj["name"],
                branch,
                build["created"],
                "success" if build["success"] else "fail",
                last_good["created"] if last_good else "never",
            ])

print(f"Wrote {CSV_FILE}")
