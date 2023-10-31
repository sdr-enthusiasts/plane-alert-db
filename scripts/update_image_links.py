import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

search_text = "https://cdn.jetphotos.com/400/"
replace_text = "https://cdn.jetphotos.com/full/"

logging.info("Reading 'plane_images.csv'.")
with open(r"plane_images.csv", "r") as images:
    data = images.read()
    data = data.replace(search_text, replace_text)

logging.info("Replace '/400/' paths with '/full/'.")
with open(r"plane_images.csv", "w") as images:
    images.write(data)

logging.info("Update image links complete.")
