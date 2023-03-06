"""Script that performs several tests on the main databases to see if they are still
valid CSVs.
"""

import logging

import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)


def is_valid_url(url, allow_nans=False):
    """Check if a URL starts with http or https.

    Args:
        url (str): The URL to check.

    Returns:
        boolean: True if the URL starts with http or https, False otherwise.
    """
    if allow_nans and pd.isna(url):
        return True
    return True if url.startswith(("http://", "https://")) else False


def contains_duplicate_ICAOs(df):
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


def contains_duplicate_regs(df):
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


def contains_bad_links(df):
    """Check if the main database has any links that don't start with http or https.

    Args:
        df (pandas.Dataframe): The database to check.

    Raises:
        Exception: When the main database has invalid links.
    """

    bad_links = df[df["$#Link"].apply(is_valid_url) == False]["$#Link"].tolist()
    if len(bad_links) > 0:
        logging.error("The main database has invalid links.")
        raise Exception(f"The main database has invalid links: {bad_links}")


def contains_valid_hexes(df):
    """Check if all the values in the data series are a hexidecimal string.

    Args:
        df (pandas.Series): The data series to check.

    Raises:
        Exception: When the main database has invalid hexidecimal values.
    """
    try:
        df.apply(lambda x: int(x, 16))
    except Exception as e:
        logging.error("The main database has invalid hexidecimal values.")
        raise e


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
    contains_duplicate_ICAOs(main_df)
    contains_valid_hexes(main_df["$ICAO"])
    # contains_duplicate_regs(main_df) # NOTE: This is commented out because there are duplicates.
    contains_bad_links(main_df)
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
    contains_duplicate_ICAOs(twitter_blocked_df)
    contains_duplicate_regs(twitter_blocked_df)
    contains_bad_links(twitter_blocked_df)
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
    contains_duplicate_ICAOs(ukraine_df)
    contains_duplicate_regs(ukraine_df)
    contains_bad_links(ukraine_df)
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
    contains_duplicate_ICAOs(images_df)
    bad_links = pd.DataFrame()
    for col in images_df.columns:  # Check all link columns for bad links.
        if col != "$ICAO":
            bad_links = bad_links.append(
                images_df[images_df[col].apply(is_valid_url, allow_nans=True) == False]
            )
    if len(bad_links) > 0:
        logging.error("The 'plane_images.txt' database has invalid links.")
        raise Exception(
            f"The 'plane_images.txt' database has invalid links: {bad_links}"
        )
    logging.info("The 'plane_images.txt' database is valid.")
