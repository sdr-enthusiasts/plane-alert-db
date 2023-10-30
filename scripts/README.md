# Readme

This folder contains several scripts used in the GitHub actions:

- `check_james_planes`: A script that can be used to check if the planes mentioned in https://github.com/sdr-enthusiasts/plane-alert-db/issues/24 are already in the main databases.
- `check_main_databases`: A script that is used to check whether the main databases are correctly formatted.
- `create_db_derivatives`: A script that can be used to create the derivative databases based on the `plane-alert-db.csv` and `plane_images.csv` files.
- `get_unique_bangers_best_items`: A script that can be used to check if the `bangers-best.csv` database contains items not found in the main databases.
- `update_readme`: A script that can be used to automate the README.md updates using the mustache template language and the chevron parser.
