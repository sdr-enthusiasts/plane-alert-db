"""This script creates (derivative) category and images CSV database files from the main
'plane-alert-db.csv' database file. The categories are created based on the 'CMPG'
column, while images are added using the 'plane_images.txt' reference file. It also
creates an extended database file using the 'blacklist.txt' file.
"""

import logging

import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    logging.info("Reading the main csv file...")
    df = pd.read_csv("plane-alert-db.csv")
    logging.info("Main csv file read successfully.")

    logging.info("Reading the images reference file...")
    images_df = pd.read_csv("plane_images.txt")
    logging.info("Images reference file read successfully.")

    logging.info("Creating the category and category images csv files...")
    for category in df["#CMPG"].unique():
        if category != category:  # Skip N/A values.
            continue

        # Create category csv files.
        logging.info(f"Creating the '{category}' category csv file...")
        category_df = df[df["#CMPG"] == category]
        category_df.to_csv(f"plane-alert-{category.lower()}.csv", index=False)

        # Create images csv files.
        logging.info(f"Creating the '{category}' category images csv file...")
        category_images_df = pd.merge(category_df, images_df, how="left", on="$ICAO")
        category_images_df.to_csv(
            f"plane-alert-{category.lower()}-images.csv", index=False
        )
    logging.info("Category and category images csv files created successfully.")

    logging.info("Create extended database csv file...")
    blacklist_df = pd.read_csv("blacklist.txt")
    extended_df = pd.merge(df, blacklist_df, how="outer")
    extended_df.to_csv("plane-alert-db-extended.csv", index=False)
    logging.info("Extended database csv file created successfully.")

    logging.info("Creating the extended database images csv file...")
    extended_images_df = pd.merge(extended_df, images_df, how="left", on="$ICAO")
    extended_images_df.to_csv("plane-alert-db-extended-images.csv", index=False)
    logging.info("Extended database images csv file created successfully.")

    logging.info("Creating the main database images csv file...")
    main_images_df = pd.merge(df, images_df, how="left", on="$ICAO")
    main_images_df.to_csv("plane-alert-db-images.csv", index=False)
    logging.info("Category and images csv files created successfully.")
