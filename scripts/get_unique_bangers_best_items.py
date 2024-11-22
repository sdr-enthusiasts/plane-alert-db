"""Small script used to check if all the items in the 'bangers-best' database are found
in the main databases.
"""

import pandas as pd
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Reading 'plane-alert-db' csv file...")
    main_df = pd.read_csv("plane-alert-db.csv")
    logging.info("'plane-alert-db' csv file read successfully.")

    logging.info("Reading 'badgers-best' csv file...")
    bangers = pd.read_csv("badgers-best.csv")
    logging.info("'badgers-best' csv file read successfully.")

    logging.info("Get new items in 'bangers-best' database...")
    new_items = bangers[~bangers["$ICAO"].isin(main_df["$ICAO"])]
    if new_items.empty:
        logging.info("No new items found.")
    else:
        logging.info("New items found.")
        logging.info(new_items)