"""A list of interesting planes given by James in
https://github.com/sdr-enthusiasts/plane-alert-db/issues/24. 

It looks like James got this list from the RadarAtlas extension using the CRX viewer
extension.
""" ""

import pandas as pd

intChineseMil = {}
interestingDirtboxes = {}
interestingTelevangelists = {}
interestingPeople = {}
interestingEntertainmentIndustry = {}
interestingCompanies = {}
interestingAthletes = {}
interestingAthleticOrgs = {}
interestingAircraft = {}
interestingRutan = {}
interestingArea51 = {}
intSEC = {}
interestingGovernment = {}
interestingNASA = {}
interestingDrones = {}
interestingNorthKorea = {}
interestingHeadsOfState = {}
interestingMusk = {}
intUkraineMil = {}
intEco = {}
c37s = {}
intRussianMil = {}
russianOligs = {}
interestingWealthiestUkrainians = {}
intAutoRacing = {}
intPutin = {}
int50StatesBillionaires = {}
israeliAirForce = {}
interestingNATO = {}
interestingVolga = {}
interestingPaintJobs = {}
interestingHomeland = {}
interestingUN = {}
intPharma = {}
intTechBillionaires = {}
intFirearms = {}
intOil = {}
intUltimateJetCharter = {}
intVertolSystems = {}
intNuclear = {}
intTopAces = {}
intHurricaneHunters = {}
intTelecom = {}
intFinanciers = {}
intSuadiAirForce = {}

# Create a combined dataframe with the constant name as the category column.
categories = [
    "intChineseMil",
    "interestingDirtboxes",
    "interestingTelevangelists",
    "interestingPeople",
    "interestingEntertainmentIndustry",
    "interestingCompanies",
    "interestingAthletes",
    "interestingAthleticOrgs",
    "interestingAircraft",
    "interestingRutan",
    "interestingArea51",
    "intSEC",
    "interestingGovernment",
    "interestingNASA",
    "interestingDrones",
    "interestingNorthKorea",
    "interestingHeadsOfState",
    "interestingMusk",
    "intUkraineMil",
    "intEco",
    "c37s",
    "intRussianMil",
    "russianOligs",
    "interestingWealthiestUkrainians",
    "intAutoRacing",
    "intPutin",
    "int50StatesBillionaires",
    "israeliAirForce",
    "interestingNATO",
    "interestingVolga",
    "interestingPaintJobs",
    "interestingHomeland",
    "interestingUN",
    "intPharma",
    "intTechBillionaires",
    "intFirearms",
    "intOil",
    "intUltimateJetCharter",
    "intVertolSystems",
    "intNuclear",
    "intTopAces",
    "intHurricaneHunters",
    "intTelecom",
    "intFinanciers",
    "intSuadiAirForce",
]
james_planes_df = pd.DataFrame()
for category in categories:
    james_planes_df = pd.concat(
        [
            james_planes_df,
            pd.DataFrame(
                {
                    "$ICAO": list(eval(category).keys()),
                    "name": list(eval(category).values()),
                    "category": category,
                }
            ),
        ]
    )

# Create a new column with the ICAO in uppercase.
james_planes_df["ICAO"] = james_planes_df["$ICAO"].str.upper()
