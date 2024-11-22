"""Check whether the interesting planes given by James in 
https://github.com/sdr-enthusiasts/plane-alert-db/issues/24 are already in the main
databases.
"""

import pandas as pd
import logging
from james_planes import james_planes_df

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

if __name__ == "__main__":

    logging.info("Reading 'plane-alert-db' csv file...")
    main_df = pd.read_csv("plane-alert-db.csv")
    logging.info("'plane-alert-db' csv file read successfully.")


    logging.info(
        f"Get new items in 'james-planes' database ({james_planes_df.shape[0]})..."
    )
    new_items = james_planes_df[~james_planes_df["$ICAO"].isin(main_df["$ICAO"])]

    james_planes_df[~james_planes_df["$ICAO"].isin(main_df["$ICAO"])]["$ICAO"].iloc[0]
    if new_items.empty:
        logging.info("No new items found.")
    else:
        logging.info(f"New items found ({new_items.shape[0]}).")
        logging.info(new_items)
        new_items.to_csv("james-planes-new-items.csv", index=False)
