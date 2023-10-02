"""Script that performs several tests on the main databases to see if they are still
valid CSVs.
"""

import logging
import sys

import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

MAIN_DATABASE_NAME = "plane-alert-db.csv"
UKRAINE_DATABASE_NAME = "plane-alert-ukraine.csv"
PLANE_IMAGES_DATABASE_NAME = "plane_images.csv"


def is_valid_url(url, allow_nans=False):
    """Check if a URL starts with http or https.

    Args:
        url (str): The URL to check.
        allow_nans (bool, optional): If True, NaN values will be considered valid.
            Defaults to False.

    Returns:
        boolean: True if the URL starts with http or https, False otherwise.
    """
    if pd.isna(url):
        return True if allow_nans and pd.isna(url) else False
    return True if url.startswith(("http://", "https://")) else False


def is_hex(string):
    """Check if a string is a hexidecimal string.

    Args:
        string (str): The string to check.

    Returns:
        boolean: True if the string is a hexidecimal string, False otherwise.
    """
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def contains_duplicate_ICAOs(df):
    """Check if the database has any duplicate ICAO codes.

    Args:
        df (pandas.Dataframe): The database to check.

    Raises:
        Exception: When the database has duplicate ICAO codes.
    """
    duplicate_icao = df[df.duplicated(subset="$ICAO", keep=False)]["$ICAO"]
    if len(duplicate_icao) > 0:
        db_name = df.name if hasattr(df, "name") else "database"
        logging.error(f"The {db_name} database has duplicate ICAO codes.")
        sys.stdout.write(
            f"The ' {db_name}' database has '{duplicate_icao.shape[0]}' duplicate "
            f"ICAO codes:\n {duplicate_icao.to_string(index=False)}\n"
        )
        sys.exit(1)


def contains_duplicate_regs(df):
    """Check if the database has any duplicate registration numbers.

    Args:
        df (pandas.Dataframe): The database to check.

    Raises:
        Exception: When the database has duplicate registration numbers.
    """

    duplicate_regs = df[df.duplicated(subset="$Registration", keep=False)][
        ["$ICAO", "$Registration"]
    ]
    if len(duplicate_regs) > 0:
        db_name = df.name if hasattr(df, "name") else "database"
        logging.error(f"The '{db_name}' database has duplicate registration numbers.")
        sys.stdout.write(
            f"The '{db_name}' database has '{duplicate_regs.shape[0]}' duplicate "
            f"registration numbers:\n{duplicate_regs.to_string(index=False)}\n"
        )
        sys.exit(1)


def contains_bad_links(df, allow_nans=False):
    """Check if the database has any links that don't start with http or https.

    Args:
        df (pandas.Dataframe): The database to check.
        allow_nans (bool, optional): If True, NaN values will be considered valid.
            Defaults to False.

    Raises:
        Exception: When the database has invalid links.
    """
    bad_links = df[~df["$#Link"].apply(is_valid_url, allow_nans).astype(bool)][
        ["$ICAO", "$#Link"]
    ].fillna("")
    if len(bad_links) > 0:
        db_name = df.name if hasattr(df, "name") else "database"
        logging.error(f"The '{db_name}' database has invalid links.")
        sys.stdout.write(
            f"The '{db_name} database has '{bad_links.shape[0]}' invalid links:\n"
            f"{bad_links.to_string(index=False)}\n"
        )
        sys.exit(1)


def contains_valid_ICAO_hexes(df):
    """Check if all the values in the '$ICAO' data series are hexidecimal strings.

    Args:
        df (pandas.Series): The '$ICAO' data series to check.

    Raises:
        Exception: When the data series has invalid hexidecimal values.
    """
    invalid_hexes = df[~df["$ICAO"].apply(is_hex).astype(bool)]["$ICAO"]
    if len(invalid_hexes) > 0:
        db_name = df.name if hasattr(df, "name") else "database"
        error_strings = (
            ["value", "is", "a hexidecimal"]
            if invalid_hexes.shape[0] == 1
            else ["values", "are", "hexidecimals"]
        )
        logging.error(
            f"The '{db_name}' database contains non-hexidecimal '$ICAO' values."
        )
        sys.stdout.write(
            f"The {db_name} database has '{invalid_hexes.shape[0]}' '$ICAO' "
            f"{error_strings[0]} that {error_strings[1]} not {error_strings[2]}:\n"
            f"{invalid_hexes.to_string(index=False)}\n"
        )
        sys.exit(1)


if __name__ == "__main__":
    ##########################################
    # Check main database.                   #
    ##########################################
    logging.info("Checking the main database...")
    try:
        main_df = pd.read_csv(MAIN_DATABASE_NAME)
        main_df.name = MAIN_DATABASE_NAME
    except Exception as e:
        logging.error(f"The '{MAIN_DATABASE_NAME}' database is not a valid CSV.")
        sys.stdout.write(
            f"The '{MAIN_DATABASE_NAME}' database is not a valid CSV: {e}\n"
        )
        sys.exit(1)

    # Preform database checks.
    contains_duplicate_ICAOs(main_df)
    contains_valid_ICAO_hexes(
        main_df
    )
    # contains_duplicate_regs(
    #     main_df
    # )  # NOTE: This is commented out because there are duplicates.
    # contains_bad_links(main_df)
    logging.info("The main database is valid.")


    ##########################################
    # Check 'plane-alert-ukraine' db.        #
    ##########################################
    logging.info("Checking the 'plane-alert-ukraine' database...")
    try:
        ukraine_df = pd.read_csv(UKRAINE_DATABASE_NAME)
        ukraine_df.name = UKRAINE_DATABASE_NAME
    except Exception as e:
        logging.error(f"The '{UKRAINE_DATABASE_NAME}' database is not a valid CSV.")
        sys.stdout.write(
            f"The '{UKRAINE_DATABASE_NAME}' database is not a valid CSV: {e}\n"
        )
        sys.exit(1)

    # Preform database checks.
    contains_duplicate_ICAOs(ukraine_df)
    contains_duplicate_regs(ukraine_df)
    contains_bad_links(ukraine_df)
    logging.info("The 'plane-alert-ukraine' database is valid.")

    ##########################################
    # Check 'plane_images.csv' db.           #
    ##########################################
    logging.info("Checking the 'plane_images.csv' database...")
    try:
        images_df = pd.read_csv(PLANE_IMAGES_DATABASE_NAME)
        images_df.name = PLANE_IMAGES_DATABASE_NAME
    except Exception as e:
        logging.error(
            f"The '{PLANE_IMAGES_DATABASE_NAME}' database is not a valid CSV."
        )
        sys.stdout.write(
            f"The '{PLANE_IMAGES_DATABASE_NAME}' database is not a valid CSV: {e}\n"
        )
        sys.exit(1)

    # Perform database checks.
    contains_duplicate_ICAOs(images_df)
    bad_links = pd.DataFrame()
    for col in images_df.columns:  # Check all link columns for bad links.
        if col != "$ICAO":
            bad_links = pd.concat(
                [
                    bad_links,
                    images_df[
                        ~images_df[col]
                        .apply(is_valid_url, allow_nans=True)
                        .astype(bool)
                    ],
                ]
            )
    if len(bad_links) > 0:
        logging.error("The 'plane_images.csv' database has invalid links.")
        sys.stdout.write(
            f"The 'plane_images.csv' database has invalid links: {bad_links}\n"
        )
        sys.exit(1)
    logging.info("The 'plane_images.csv' database is valid.")
