# plane-alert-db

**NOTE - The main file format has changed from .txt to .csv - the old file will remain available (without updates) until 2021/05/01, at which point it will be deleted. Please update any links to the .txt file immediately**

This project consists of lists of 'interesting' aircraft, formatted as CSV files. The list is designed to work with the excellent https://github.com/kx1t/docker-planefence and takes the form 

- ICAO,Ident,Operator,Type,CMPG,$Tag,#$Tag2,Category,#$Link

e.g 406C1B,G-CNWL,Cornwall Air Ambulance,Bell MD-900 Explorer,Civ,Air Ambo,Choppa,M\*A\*S\*H,https://cornwallairambulancetrust.org/

Add these characters to the column headers to control the behavior of PlaneAlert

- "$" \- Tweet this column as #hashtag
- "#" \- Don't show on the website (it will ignore this for the ICAO field, which is always shown)
- "#$"\- Don't show on the website, tweet as a #hashtag

in the example above the #hashtags would be 'Air Ambo' and 'Choppa', and Tag2 will not be shown on the PA website.

\*CMPG = Civilian, Military, Police, Government

# Planefence
To use this list with Planefence, simply configure your planefence.config setup to include the following line:

- PF_ALERTLIST=https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-db.csv

If you want to add the list in addition to your local plane-alert-db.txt list, you can do the following:

- PF_ALERTLIST=plane-alert-db.txt,https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-gov.csv,https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-pol.csv

**Note -- the priority of use is first-to-last, so if you want your local list to be interpreted first, move it to the front of the list**

# Current Content

The list contains **2341** unique aircraft in **42** different categories.

- [plane-alert-db.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-db.csv) - The list of interesting aircraft, with tags,categories and links. (2341)
- [plane-alert-civ.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-civ.csv) - Civilian Registered Aircraft, includes Historic and Distinctive. (652)
- [plane-alert-mil.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-mil.csv) - Military Only. (1264)
- [plane-alert-pol.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-pol.csv) - Police Forces. (48)
- [plane-alert-gov.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-gov.csv) - Governments, Gov Agencies and Dictators. (377)
- [badgers-best.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/badgers-best.csv) - My own personal selections from the main list. (792)
- [community-list.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/community-list.csv) - Open list to add your suggestions to. These will be moved to the main list in time.

This [Dashboard](https://datastudio.google.com/reporting/eb19ab53-b622-4946-b34a-9667232c136d/page/4taCC) contain details of the main list and the most recent additions.

# Description of Categories

Think of categories like groups, with similar or related aircraft listed together. This allows you to easily select a subset of the list for your own use. The category names (and tags) come from my rather idiosyncratic sense of humour. If you have better suggestions I'm all ears.

- Aerobatic Teams \- Red Arrows, Blue Angels etc (52)
- Army Air Corp \- UK Army Air Corp. Mainly Helicopters (20)
- As Seen on TV \- Companies and Brands (37)
- Battle of Britiain Memorial Flight \- Historic British aircraft from WW2 (12)
- Big Hello \- Large Helicopters (sic) (38)
- Bizjets \- Fancy pants planes for fancy pants people (20)
- Coastguard \- Coastguard, Customs and Border Patrols (19)
- Da Comrade \- Russian or Soviet Aircraft. I love their design, so they get their own category (82)
- Dictator Alert \- People of potentially questionable morals and values (218)
- Distinctive \- Unique and/or special aircraft e.g The AN-224 Myria, NASA aircraft (75)
- Dogs with Jobs \- Aircraft with specific roles and/or modifications (47)
- Football  \- Actual, Aussie Rules or American. We don't descriminate. (1)
- GAF \- Aircraft of the German Air Force, thank to Rhodan76 (291)
- Governments \- Aircraft registired to Governments (25)
- Historic \- It's older than I am, and most likely has a prop. (68)
- I For One Welcome our new Overlords \- Clippy et al. (24)
- Jesus he Knows me \- Aircraft owned and operated by Religious organisations (8)
- Just Because \- I don't know why I like you, but I do. (7)
- M\*A\*S\*H \- Air Ambulance and Medical Flights
- Military Contractors \- Why do the dirty work when someone else can do it for you ? (55)
- Must be nice \- Billionaires, not millionaires, daaaahling (12)
- Nuclear \- Nuclear Emergency Support Team etc (12)
- Other Air Forces \- Air Force aircraft that are not RAF or USAF (179)
- Other Navies \- Navy Aircraft that are not Royal Navy or United States Navy (16)
- Police Forces \- Your friendly neighbourhood flying (insert local colloquialism here) (23)
- Ptolemy would be proud \- Mapping and Aerial Survey aircraft.  (16)
- Quango \- Nato, United Nations, World Bank etc (18)
- RAF \- Aircraft of the Royal Air Force (120)
- Royal Aircraft \- Aircraft used or owned by the UK Royal Family (8)
- Royal Navy \- Aircraft of the Royal Navy (57)
- Sock Puppet \- Someone Pretending to be something they are not e.g. Covert DOJ Aircraft (87)
- UAV \- It's not natural, I tell 'ya (10)
- UK National Police Air Service \- Your friendly neighbourhood flying bobby (24)
- Under Observation \- Up to something dodgy, maybe (33)
- United States Navy \- United States naval avaitors. Some say they are the best of the best. (44)
- USAF \- Aircraft of the United States Air Force (417)
- Vanity Plate \- Distinctive registrations (20)
- Watch Me Fly \- Flying and Training Schools (31)
- Who needs an Engine ? \- Gliders etc (25)
- You came here in that thing ? \- Microlights, tiny planes and helis..think Yakima Super Breezy (thanks skstrand) (13)
- Zoomies \- Fast jets, fighters. Anything that moves fast. (31)

# To do / Ideas

No 1 - Update USAF aircraft to use Reg/serial number in place of Ident/Callsign

- RAF Typhoon Display Team
- Breitling Jet Team (not complete)
- US Dept of Interior
- US Dept of Energy
- Other US Gov Depts
- Firefighting Aircraft / Companies
- Police Scotland Air Support Unit (NI Equivalent)
- B737 with Gravel Kits - Nolinor, Air Inuit, Canada North, Chron Aviation
- Defense Helicopter Flying School
- Identify more Aircraft owned by Religious organisations
- Acrobat Ltd (Uk Gov Sock puppet ?)
- UK Ministry of Defence
- UK Border Force
- Shuttleworth Collection
- Other Warbirds
- List of DA42 MPP / DA62 MPP Operators
- Thales UK
- Survey / Mapping Aircarft
- Other surveillance aircraft types
- 750 Naval Air Squadron (Observers)
- Cal Fire
- Coulson Aviation
- Australian Aircraft called firebird (fire spotter and fighters)
- S-64 Skycrane - list only partially completed (what is the list of names)
- Japanese Flying Boats Shin Maywa US-2/US 1 (US2 are 9901 through 9907 - mode s ?)
- Private Adversary Squadrons
- Operators of old Jets/Fighters (e.g. Hawker Huner Aviation)
- Callspan Corp In-Flight Simulators
- GAMA Avaiation (ex RAF spy planes)
- Flying Hospitals (eye Hospital ?)
- UK Coast Guard
- Other Coast Guards (e.g. USCG)
- Air Ambulances (Wikipedia List)
- Big Russian Helis
- Kamov KA32's
- Babcock MCS Spain (and any other countries)
- Lewis Hamilton Jet(s)
- Open Skies Flights
- Eurpoean Union
- Scienctific / Weather planes
- Flight Precision Ltd (and Similar)
- United Nations
- World Bank etc
- Red Cross / MSF
- Special Convertions e.g. Engine testbeds
- Duxford and other historic flight collections
- Historic Aircraft Flight Trust
- Low volume Airliners / Special Models
- Football Teams and other sporting organisations
- Beechcraft RC-12 Guardrail
- Meteorological research flights
- A10 Thunderbolt II
- Film and Televison Companies
- News Choppers
- RCAF Snowbirds
- RAAF Roulettes
- Helicopter Transport Services
- Arena Aviation
- Slagboom & Peeters nv (Aerial Surveys)
- Air Affairs Australia
- ADAC Germany
- Denmar Technical Services (Stealth radar testing)
- IAS Medical (Air Evac)
- Aviation Services Australia
- Historic Army Aircraft Flight
- Odd C130 Hercules - EC130H, EC130E, EC130J, MC130H, WC130J
- Gunships (Spooky, Central American DC3's)
- AeroRescue
- Air-Glaciers
- Alci Avaiation
- Basler BT-67 Operators
- Baltic Bees Display Team
- Bundesamt für Landestopografie
- Bundesamt für Zivilluftfahrt BAZL
- Bundespolizei
- GFD.de
- Royal Flying Doctors Service
- Top Aces Inc.
- Russian FSB
- Aircraft and companies in this article - https://www.cjr.org/watchdog/how-buzzfeed-news-revealed-hidden-spy-planes-in-us-airspace.php
- Chapparral Air Group
- Acorn Growth Companies
- Aircraft owned/Operated by Sultan/State of Brunei (esp his very plush 747)
- Aircraft - Lake Renegade
- Special Hurons - MC-12W, MC-12S, RC-12H, RC-12N
- Edgley Optika
- <strike>Network Rail Helicopter(s)</strike>
- <strike>Multinational MRTT Fleet</strike>
- <strike>Fly Navy Heritage Trust</strike>
- <strike>Check Saudi Armed Forces Medical Services is complete</strike>
- <strike>Aircraft operated by Comlux</strike>
- <strike>Icelandic Coastguard</strike>
- <strike>The Flying Bulls</strike>
- <strike>Check Empire Test Pilots School is complete</strike>
- <strike>Qinetiq</strike>

Any other idea's welcome.

# Data Sources

This data has been gathered from far too many sources to mention, but some sites have been *really* useful.

https://whatisflying.com/en/database/aircraft-types

https://github.com/jbroutier/whatisflying-db

https://www.flightdb.net/index.php

http://www.rotorspot.nl/

http://www.dtvmovements.co.uk/

http://www.ads-b.nl/

https://www.live-military-mode-s.eu/

https://dictatoralert.org/ 
