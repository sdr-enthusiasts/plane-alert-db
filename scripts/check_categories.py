""""script to flag new/invalid categories"""

import logging
import pandas as pd
import sys

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Reading the main csv file...")
    df = pd.read_csv("plane-alert-db.csv")

    logging.info("Reading the Ukraine csv file...")
    ukraine_df = pd.read_csv("plane-alert-ukraine.csv")

    category_unique_df = (
        pd.concat([df["Category"], ukraine_df["Category"]])
        .drop_duplicates()
        .reset_index(drop=False)
    )
    category_unique_df = category_unique_df.drop('index', axis=1)
    logging.info(f"Total Categories in PR Count: ({category_unique_df.shape[0]}).")

    logging.info("Reading the export category csv file...")
    valid_df = pd.read_csv("plane-alert-categories.csv")

    if not valid_df.equals(category_unique_df):
        logging.info("Invalid category used!")
        merged_df = valid_df.merge(category_unique_df, indicator=True, how='outer')
        changed_df = merged_df[merged_df['_merge'] == 'right_only']
        changed_df = changed_df.drop('_merge', axis=1)
        
        logging.info(
            "New Categories found ({}):\n{}".format(
                changed_df.shape[0],
                changed_df.to_string(header=False, index=False),
            )
        )

        sys.stdout.write(
            f"The files contain invalid or new Categories:\n"
        )
        sys.exit(1)
    logging.info("Categories check good!")