"""Script that performs several counts to update the README
"""

import logging
import sys

import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Reading the main csv file...")
    df = pd.read_csv("plane-alert-db.csv")
    logging.info("Main csv file read successfully.")

    logging.info("Reading the Ukraine csv file...")
    ukraine_df = pd.read_csv("plane-alert-ukraine.csv")

    logging.info("Reading the PIA csv file...")
    pia_df = pd.read_csv("plane-alert-pia.csv")

    logging.info("Reading the images reference file...")
    images_df = pd.read_csv("plane_images.csv")   

    plane_count_df = (
        pd.concat([df["$ICAO"], ukraine_df["$ICAO"]])
        .drop_duplicates()
        .reset_index(drop=True)
    )

    category_unique_df = (
        pd.concat([df["Category"], ukraine_df["Category"]])
        .drop_duplicates()
        .reset_index(drop=True)
    )

    category_df = (
        pd.concat([df["Category"], ukraine_df["Category"]])
        .reset_index(drop=False)
    )

import chevron 

with open('readme.mustache', 'r') as template:
    with open('README.md', 'w') as output:
        output.write(chevron.render(template, 
            {
                'planes': plane_count_df.shape[0],
                'categories': category_unique_df.shape[0],
                'plane_alert_db': df.shape[0],
                'plane_alert_pia': pia_df.shape[0],
                'plane_alert_ukraine': ukraine_df.shape[0],
                'plane_alert_images': images_df.dropna(subset=['#ImageLink'],inplace=False).shape[0],
                'civ_count': df[df["#CMPG"] == 'Civ'].shape[0],
                'mil_count': df[df["#CMPG"] == 'Mil'].shape[0],
                'pol_count': df[df["#CMPG"] == 'Pol'].shape[0],
                'gov_count': df[df["#CMPG"] == 'Gov'].shape[0],
                'aerobatic_count': category_df[category_df["Category"] == 'Aerobatic Teams'].shape[0],
                'air_corp_count': category_df[category_df["Category"] == 'Army Air Corp'].shape[0],
                'seen_on_tv_count': category_df[category_df["Category"] == 'As Seen on TV'].shape[0],
                'football_count': category_df[category_df["Category"] == 'Football'].shape[0],
                'britian_memorial_count': category_df[category_df["Category"] == 'Battle of Britain Memorial Flight'].shape[0],
                'big_hello_count': category_df[category_df["Category"] == 'Big Hello'].shape[0],
                'bizjets_count': category_df[category_df["Category"] == 'Bizjets'].shape[0],
                'climate_crisis_count': category_df[category_df["Category"] == 'Climate Crisis'].shape[0],
                'governments_count': category_df[category_df["Category"] == 'Governments'].shape[0],
                'coastguard_count': category_df[category_df["Category"] == 'Coastguard'].shape[0],
                'da_comrade_count': category_df[category_df["Category"] == 'Da Comrade'].shape[0],
                'dictator_count': category_df[category_df["Category"] == 'Dictator Alert'].shape[0],
                'distinctive_count': category_df[category_df["Category"] == 'Distinctive'].shape[0],
                'dogs_jobs_count': category_df[category_df["Category"] == 'Dogs with Jobs'].shape[0],
                'celeb_count': category_df[category_df["Category"] == "Don't you know who I am?"].shape[0],
                'flying_doctors_count': category_df[category_df["Category"] == 'Flying Doctors'].shape[0],
                'gaf_count': category_df[category_df["Category"] == 'GAF'].shape[0],
                'gas_bags_count': category_df[category_df["Category"] == 'Gas Bags'].shape[0],
                'gunship_count': category_df[category_df["Category"] == 'Gunship'].shape[0],
                'hired_gun_count': category_df[category_df["Category"] == 'Hired Gun'].shape[0],
                'historic_count': category_df[category_df["Category"] == 'Historic'].shape[0],
                'religious_count': category_df[category_df["Category"] == 'Jesus he Knows me'].shape[0],
                'joe_cool_count': category_df[category_df["Category"] == 'Joe Cool'].shape[0],
                'jump_johnny_count': category_df[category_df["Category"] == 'Jump Johnny Jump'].shape[0],
                'mash_count': category_df[category_df["Category"] == 'M*A*S*H'].shape[0],
                'nuclear_count': category_df[category_df["Category"] == 'Nuclear'].shape[0],
                'other_air_count': category_df[category_df["Category"] == 'Other Air Forces'].shape[0],
                'toy_soldiers_count': category_df[category_df["Category"] == 'Toy Soldiers'].shape[0],
                'other_navies_count': category_df[category_df["Category"] == 'Other Navies'].shape[0],
                'oxcart_count': category_df[category_df["Category"] == 'Oxcart'].shape[0],
                'psa_count': category_df[category_df["Category"] == 'Perfectly Serviceable Aircraft'].shape[0],
                'pia_count': category_df[category_df["Category"] == 'PIA'].shape[0],
                'police_forces_count': category_df[category_df["Category"] == 'Police Forces'].shape[0],
                'ptolemy_count': category_df[category_df["Category"] == 'Ptolemy would be proud'].shape[0],
                'quango_count': category_df[category_df["Category"] == 'Quango'].shape[0],
                'oligarch_count': category_df[category_df["Category"] == 'Oligarch'].shape[0],
                'radiohead_count': category_df[category_df["Category"] == 'Radiohead'].shape[0],
                'raf_count': category_df[category_df["Category"] == 'RAF'].shape[0],
                'royal_aircraft_count': category_df[category_df["Category"] == 'Royal Aircraft'].shape[0],
                'royal_navy_count': category_df[category_df["Category"] == 'Royal Navy Fleet Air Arm'].shape[0],
                'aerial_firefighter_count': category_df[category_df["Category"] == 'Aerial Firefighter'].shape[0],
                'special_forces_count': category_df[category_df["Category"] == 'Special Forces'].shape[0],
                'uav_count': category_df[category_df["Category"] == 'UAV'].shape[0],
                'uk_police_count': category_df[category_df["Category"] == 'UK National Police Air Service'].shape[0],
                'us_marines_count': category_df[category_df["Category"] == 'United States Marine Corps'].shape[0],
                'us_navy_count': category_df[category_df["Category"] == 'United States Navy'].shape[0],
                'usaf_count': category_df[category_df["Category"] == 'USAF'].shape[0],
                'vanity_plate_count': category_df[category_df["Category"] == 'Vanity Plate'].shape[0],
                'watch_fly_count': category_df[category_df["Category"] == 'Watch Me Fly'].shape[0],
                'that_thing_count': category_df[category_df["Category"] == "You came here in that thing?"].shape[0],
                'zoomies_count': category_df[category_df["Category"] == 'Zoomies'].shape[0],
                'ukraine_count': category_df[category_df["Category"] == 'Ukraine'].shape[0]
            }
        )
    )
