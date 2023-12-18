import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

search_text = "https://cdn.jetphotos.com/400/"
replace_text = "https://cdn.jetphotos.com/full/"
jpcount = 0

logging.info("Reading 'plane_images.csv'.")
with open(r"plane_images.csv", "r") as images:
    for line in images:
        jpcount += line.count(search_text)

if jpcount > 0:
    logging.info(f"Occurences of /400/ found: {jpcount}")
    logging.info("Replacing '/400/' paths with '/full/'.")
    with open(r"plane_images.csv", "r") as images:
        data = images.read()
        data = data.replace(search_text, replace_text)

    logging.info("Writing changes...")
    with open(r"plane_images.csv", "w") as images:
        images.write(data)
        logging.info("Update image links complete!")

else:
    logging.info("No image links to update!")