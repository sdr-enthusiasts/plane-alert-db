"""This script retrieves the plane images in the 'plane-alert-db-images.csv' database 
and 'planepix.txt' file. It stores these images in a new 'plane_images.csv' reference 
file to use later to create the 'images' CSV database files.

This script can be removed if we know that the new GitHub action results are correct.
"""
import logging

import numpy as np
import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Retrieve images from the 'plane-alert-db-images.csv' file...")
    plane_alert_db_images = pd.read_csv("plane-alert-db-images.csv")
    plane_alert_db_images = plane_alert_db_images[
        ["$ICAO", "#ImageLink", "#ImageLink2", "#ImageLink3"]
    ]
    logging.info(f"Images retrieved ({plane_alert_db_images.shape[0]}).")

    logging.info("Retrieve images from the 'planepix.txt' file...")
    planepix_df = pd.read_csv("planepix.txt")
    planepix_df.columns = ["$ICAO", "#ImageLink4"]
    logging.info(f"Images retrieved ({planepix_df.shape[0]}).")

    logging.info(
        "Merge images from the 'plane-alert-db-images.csv' and 'planepix.txt' files..."
    )
    plane_alert_db_images = pd.merge(
        plane_alert_db_images, planepix_df, how="outer", on="$ICAO"
    )
    plane_alert_db_images = plane_alert_db_images.replace(
        "", np.nan
    )  # Replace empty strings with NaN.
    logging.info(f"Images merged ({plane_alert_db_images.shape[0]}).")

    logging.info("Remove duplicates from the merged images...")
    plane_alert_db_images["#ImageLink4"] = plane_alert_db_images.apply(
        lambda row: row["#ImageLink4"]
        if row["#ImageLink4"]
        not in [row["#ImageLink"], row["#ImageLink2"], row["#ImageLink3"]]
        else np.nan,
        axis=1,
    )
    logging.info(f"Images without duplicates ({plane_alert_db_images.shape[0]}).")

    logging.info("Make sure that the image urls have the correct format...")
    plane_alert_db_images[
        ["#ImageLink", "#ImageLink2", "#ImageLink3", "#ImageLink4"]
    ] = plane_alert_db_images[
        ["#ImageLink", "#ImageLink2", "#ImageLink3", "#ImageLink4"]
    ].apply(
        lambda row: row.apply(
            lambda x: x
            if (isinstance(x, float) and np.isnan(x)) or x.startswith("https://")
            else (
                x.replace("http://", "https://")
                if x.startswith("http://")
                else "https://" + x
            )
        ),
        axis=1,
    )
    logging.info(f"Images with correct format ({plane_alert_db_images.shape[0]}).")

    # Print new images.
    logging.info("Check if there were new images in the 'planepix.txt' file...")
    new_image_links = plane_alert_db_images[
        ~plane_alert_db_images["#ImageLink4"].isnull()
    ][["$ICAO", "#ImageLink4"]]
    logging.info(
        "New images found ({}):\n {}".format(
            new_image_links.shape[0], new_image_links.head().to_string(index=False)
        )
    )

    logging.info("Removing empty left image columns...")
    columns = plane_alert_db_images.columns
    plane_alert_db_images = plane_alert_db_images.apply(
        lambda x: pd.Series(x.dropna().values), axis=1
    )
    logging.info("Empty left image columns removed.")

    logging.info("Adding extra 'ImageLink' column if needed...")
    if columns.shape[0] > plane_alert_db_images.columns.shape[0]:
        logging.info("No extra 'ImageLink' column needed to be added.")
    else:
        logging.info("Extra '#ImageLink4' column added.")
    plane_alert_db_images.columns = columns[: plane_alert_db_images.columns.shape[0]]

    logging.info("Saving found images in 'plane_images.csv' file...")
    plane_alert_db_images.to_csv("plane_images.csv", index=False)
    logging.info("Images successfully saved in 'plane_images.csv' file.")
