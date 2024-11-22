""""script to export current categories"""

import logging
import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Reading the main csv file...")
    df = pd.read_csv("plane-alert-db.csv")

    category_unique_df = (
        df["Category"]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    logging.info(f"Total Categories Count: ({category_unique_df.shape[0]}).")
    logging.info("Creating the plane-alert-categories.csv file.")
    
    category_unique_df.to_csv(
    "plane-alert-categories.csv",
    mode="wb",
    index=False,
    header=True,
    encoding="utf8",
    lineterminator="\n",
    )
    logging.info("File created successfully!")