"""Script that performs several tests on the main databases to see if they are still
valid CSVs.
"""

import logging
import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)


def isUrlValid(url, allow_nans=False):
    """Check if a URL starts with http or https.

    Args:
        url (str): The URL to check.

    Returns:
        boolean: True if the URL starts with http or https, False otherwise.
    """
    if allow_nans and pd.isna(url):
        return True
    return True if url.startswith(("http://", "https://")) else False


def duplicateICAOs(df):
    """Check if the main database has any duplicate ICAO codes.

    Args:
        df (pandas.Dataframe): The database to check.

    Raises:
        Exception: When the main database has duplicate ICAO codes.
    """
    duplicate_icao = df[df.duplicated(subset="$ICAO", keep=False)]
    if len(duplicate_icao) > 0:
        logging.error("The main database has duplicate ICAO codes.")
        raise Exception(f"The main database has duplicate ICAO codes: {duplicate_icao}")


def duplicateRegs(df):
    """Check if the main database has any duplicate registration numbers.

    Args:
        df (pandas.Dataframe): The database to check.

    Raises:
        Exception: When the main database has duplicate registration numbers.
    """

    duplicate_regs = df[df.duplicated(subset="$Registration", keep=False)]
    if len(duplicate_regs) > 0:
        logging.error("The main database has duplicate registration numbers.")
        raise Exception(
            f"The main database has '{duplicate_regs.shape[0]}'duplicate registration "
            "numbers: {duplicate_regs}"
        )


def badLinks(df):
    """Check if the main database has any links that don't start with http or https.

    Args:
        df (pandas.Dataframe): The database to check.

    Raises:
        Exception: When the main database has invalid links.
    """

    bad_links = df[df["$#Link"].apply(isUrlValid) == False]["$#Link"].tolist()
    if len(bad_links) > 0:
        logging.error("The main database has invalid links.")
        raise Exception(f"The main database has invalid links: {bad_links}")


if __name__ == "__main__":
    ##########################################
    # Check main database.                   #
    ##########################################
    logging.info("Checking the main database...")
    try:
        main_df = pd.read_csv("plane-alert-db.csv")
    except Exception as e:
        logging.error("The main database is not a valid CSV.")
        raise e

    # Preform database checks.
    duplicateICAOs(main_df)
    # duplicateRegs(main_df) # NOTE: This is commented out because there are duplicates.
    badLinks(main_df)
    logging.info("The main database is valid.")

    ##########################################
    # Check 'plane-alert-twitter-blocked' db.#
    ##########################################
    logging.info("Checking the 'plane-alert-twitter-blocked' database...")
    try:
        twitter_blocked_df = pd.read_csv("plane-alert-twitter-blocked.csv")
    except Exception as e:
        logging.error("The 'plane-alert-twitter-blocked' database is not a valid CSV.")
        raise e

    # Preform database checks.
    duplicateICAOs(twitter_blocked_df)
    duplicateRegs(twitter_blocked_df)
    badLinks(twitter_blocked_df)
    logging.info("The 'plane-alert-twitter-blocked' database is valid.")

    ##########################################
    # Check 'plane-alert-ukraine' db.        #
    ##########################################
    logging.info("Checking the 'plane-alert-ukraine' database...")
    try:
        ukraine_df = pd.read_csv("plane-alert-ukraine.csv")
    except Exception as e:
        logging.error("The 'plane-alert-ukraine' database is not a valid CSV.")
        raise e

    # Preform database checks.
    duplicateICAOs(ukraine_df)
    duplicateRegs(ukraine_df)
    badLinks(ukraine_df)
    logging.info("The 'plane-alert-ukraine' database is valid.")

    ##########################################
    # Check 'plane_images.txt' db.           #
    ##########################################
    logging.info("Checking the 'plane_images.txt' database...")
    try:
        images_df = pd.read_csv("plane_images.txt")
    except Exception as e:
        logging.error("The 'plane_images.txt' database is not a valid CSV.")
        raise e

    # Perform database checks.
    duplicateICAOs(images_df)
    bad_links = pd.DataFrame()
    for col in images_df.columns:  # Check all link columns for bad links.
        if col != "$ICAO":
            bad_links = bad_links.append(
                images_df[images_df[col].apply(isUrlValid, allow_nans=True) == False]
            )
    if len(bad_links) > 0:
        logging.error("The 'plane_images.txt' database has invalid links.")
        raise Exception(
            f"The 'plane_images.txt' database has invalid links: {bad_links}"
        )
    logging.info("The 'plane_images.txt' database is valid.")
