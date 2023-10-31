import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

search_text = "https://cdn.jetphotos.com/400/"
replace_text = "https://cdn.jetphotos.com/full/"

files = [
    "plane_images.csv",
    "plane-alert-civ-images.csv",
    "plane-alert-db-images.csv",
    "plane-alert-gov-images.csv",
    "plane-alert-mil-images.csv",
    "plane-alert-pol-images.csv",
    "plane-alert-ukraine-images.csv"
]

for item in files:
    logging.info(f"Reading the '{item}' file.")
    with open(f"{item}", "r") as images:
        data = images.read()
        data = data.replace(search_text, replace_text)

    logging.info("Replace '/400/' paths with '/full/'.")
    with open(f"{item}", "w") as images:
        images.write(data)

    logging.info(f"Update '{item}' complete.")
