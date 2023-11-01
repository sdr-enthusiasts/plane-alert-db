"""This script creates (derivative) category and images CSV database files from the main
'plane-alert-db.csv' database file. The categories are created based on the 'CMPG'
column, while images are added using the 'plane_images.csv' reference file. It also
creates the 'plane-alert-ukraine-images.csv' database file.
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
    images_df = pd.read_csv("plane_images.csv")
    logging.info("Images reference file read successfully.")

    logging.info("Creating the category and category images CSV files...")
    for category in df["#CMPG"].unique():
        if category != category:  # Skip N/A values.
            continue

        # Create category CSV files.
        logging.info(f"Creating the '{category}' category CSV file...")
        category_df = df[df["#CMPG"] == category]
        category_df.to_csv(
            f"plane-alert-{category.lower()}.csv",
            index=False,
            mode="wb",
            encoding="utf8",
            lineterminator="\n",
        )

        # Create images CSV files.
        logging.info(f"Creating the '{category}' category images CSV file...")
        category_images_df = pd.merge(category_df, images_df, how="left", on="$ICAO")
        category_images_df.to_csv(
            f"plane-alert-{category.lower()}-images.csv",
            index=False,
            mode="wb",
            encoding="utf8",
            lineterminator="\n",
        )
    logging.info("Category and category images CSV files created successfully.")

    logging.info("Creating the ukraine database images CSV file...")
    ukraine_df = pd.read_csv("plane-alert-ukraine.csv")
    ukraine_df_images = pd.merge(ukraine_df, images_df, how="left", on="$ICAO")
    ukraine_df_images.to_csv(
        "plane-alert-ukraine-images.csv",
        index=False,
        mode="wb",
        encoding="utf8",
        lineterminator="\n",
    )
    logging.info("Ukraine database images CSV file created successfully.")

    logging.info("Creating the main database images csv file...")
    main_images_df = pd.merge(df, images_df, how="left", on="$ICAO")
    main_images_df["#CMPG"] = main_images_df["#CMPG"].fillna("#N/A")
    main_images_df.to_csv(
        "plane-alert-db-images.csv",
        index=False,
        mode="wb",
        encoding="utf8",
        lineterminator="\n",
    )
    logging.info("Category and images CSV files created successfully.")

    logging.info(
        "Check for new ICAOs in DB files and add them to the images reference file..."
    )
    plane_alert_df = (
        pd.concat([df["$ICAO"], ukraine_df["$ICAO"]])
        .drop_duplicates()
        .reset_index(drop=True)
    )
    logging.info(f"ICAOs retrieved from DB files: ({plane_alert_df.shape[0]}).")
    logging.info(f"ICAOs retrieved from 'plane_images.csv ({images_df.shape[0]}).")
    new_ICAOs_df = plane_alert_df[~plane_alert_df.isin(images_df["$ICAO"])]
    if new_ICAOs_df.shape[0] > 0:
        logging.info(
            "New ICAOs found ({}):\n{}".format(
                new_ICAOs_df.shape[0],
                new_ICAOs_df.head(5).to_string(header=False, index=False),
            )
        )
        logging.info("Appending new ICAOs in 'plane_images.csv' file...")
        plane_images_df = pd.merge(
            images_df,
            new_ICAOs_df,
            how="outer",
            on="$ICAO",
        )
        plane_images_df.to_csv(
            "plane_images.csv",
            mode="wb",
            index=False,
            header=True,
            encoding="utf8",
            lineterminator="\n",
        )
        logging.info("New ICAOs successfully saved in 'plane_images.csv' file.")
    else:
        logging.info("No new ICAOs. Nothing to do.")

    logging.info(
        "Check for removed ICAOs in DB files and remove them to the images reference file..."
    )

    if images_df.shape[0] > plane_alert_df.shape[0]:
        logging.info(
            "Extra ICAOs found ({})".format(
                images_df.shape[0] - plane_alert_df.shape[0]
            )
        )

        extra_icao_df = pd.merge(
            images_df, plane_alert_df, on="$ICAO", how="left", indicator=True
        )

        extra_icao_df = extra_icao_df.loc[
            extra_icao_df["_merge"] == "left_only"
        ].index.tolist()
        for item in extra_icao_df:
            if "plane_images_df" in locals():
                plane_images_df = plane_images_df.drop(item)
                plane_images_df.to_csv(
                    "plane_images.csv",
                    mode="wb",
                    index=False,
                    header=True,
                    encoding="utf8",
                    lineterminator="\n",
                )
            else:
                images_df = images_df.drop(item)
                images_df.to_csv(
                    "plane_images.csv",
                    mode="wb",
                    index=False,
                    header=True,
                    encoding="utf8",
                    lineterminator="\n",
                )
        logging.info("Extra ICAOs successfully removed from 'plane_images.csv'")

    else:
        logging.info("No extra ICAOs. Nothing to do.")
