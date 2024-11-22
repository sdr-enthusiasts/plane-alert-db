"""Checks whether the PR includes invalid derivative files.
"""

import logging
import os

import requests
from git import Git

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

CHANGED_FILES = os.environ["CHANGED_FILES"]
MAIN_DB_FILES = [
    "plane-alert-db.csv",
    "plane-alert-pia.csv",
    "plane_images.csv",
]
OUTPUT_FILE = os.getenv("GITHUB_OUTPUT")

if __name__ == "__main__":
    logging.info("Getting the PR files...")
    requests_session = requests.Session()
    pr_files = CHANGED_FILES.split(",")
    logging.info("PR files retrieved successfully.")

    logging.info("Getting changed files...")
    g = Git(".")
    g.ls_files()
    changed_files = g.ls_files("-dmo").splitlines()
    changed_files = [
        changed_file
        for changed_file in changed_files
        if changed_file.endswith(".csv")
        and changed_file not in MAIN_DB_FILES
        and changed_file in pr_files
    ]
    logging.info("Changed files retrieved successfully.")

    logging.info("Setting result as github action output...")
    if changed_files:
        logging.info("Invalid derivative files found.")
        logging.info(f"Invalid derivative files: {changed_files}")
        with open(OUTPUT_FILE, "a") as fh:
            print(
                "derivatives_changed={}".format(str(len(["test"]) >= 1).lower()),
                file=fh,
            )
    else:
        logging.info("No invalid derivative files found.")
        with open(OUTPUT_FILE, "a") as fh:
            print("derivatives_changed=false", file=fh)
