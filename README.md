# plane-alert-db
This project consists of lists of 'interesting' aircraft, formatted as CSV files. The list is designed to work with the excellent https://github.com/kx1t/docker-planefence and takes the form 

- ICAO,Ident,Operator,Type,CMPG,$Tag,#$Tag2,Category

e.g 406C1B,G-CNWL,Cornwall Air Ambulance,Bell MD-900 Explorer,Civ,Air Ambo,Choppa,M\*A\*S\*H 

Add these characters to the column headers to control the behavior of PlaneAlert

- "$" \- Tweet this column as #hashtag
- "#" \- Don't show on the website (it will ignore this for the ICAO field, which is always shown)
- "#$"\- Don't show on the website, but tweet as a #hashtag

in the eample above the #hashtags would be 'Air Ambo' and 'Choppa', and Tag2 will not be shown on the PA website.

\*CMPG = Civilian, Military, Police, Government

# Planefence
To use this list with Planefence, simply configure your planefence.config setup to include the following line:

- PF_ALERTLIST=https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-db.txt

If you want to add the list in addition to your local plane-alert-db.txt list, you can do the following:

- PF_ALERTLIST=plane-alert-db.txt,https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-db.txt

**Note -- the priority of use is first-to-last, so if you want your local list to be interpreted first, move it to the front of the list**

# Current Content

The list contains **1034** unique aircraft in **34** different categories.

- [plane-alert-db.txt](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-db.txt) - The list of interesting aircaft, with tags and categories.
- [community-list.txt](https://github.com/Sportsbadger/plane-alert-db/blob/main/community-list) - Open list to add your suggestions to. These will be moved to the main list in time.  
- [dictator-alert.txt](https://github.com/Sportsbadger/plane-alert-db/blob/main/dictator-alert.txt) - A seperate list with only Dictators. These aircaft are also included in the main list.


# Description of Categories	   

Think of categories like groups, with similar or related aircraft listed together. This allows you to easily select a subset of the list for your own use. The category names (and tags) come from my rather idiosyncratic sense of humour. If you have better suggestions I'm all ears.

- Aerobatic Teams \- Red Arrows, Blue Angels etc (21)
- Army Air Corp \- UK Army Air Corp. Mainly Helicopters (7)
- As Seen on TV \- Companies and Brands (24)
- Battle of Britiain Memorial Flight \- Historic British aircraft from WW2 (12)
- Bizjets \- Fancy pants planes for fancy pants people (9)
- Coastguard \- Coastguard Aircraft (6)
- Da Comrade \- Russian or Soviet Aircraft. I love their design, so they get their own category (15)
- Dictator Alert \- People of potentially questionable morals and values (207)
- Distinctive \- Unique and/or special aircraft e.g The AN-224 Myria, NASA aircraft (25)
- Dogs with Jobs \- Aircraft with specific roles and/or modifications (17)
- GAF \- Aircraft of the German Air Force, thank to Rhodan76 (289)
- Governments \- Aircraft registired to Governments (4)
- Historic \- It's older than I am, and most likely has a prop. (0)
- Jesus he Knows me \- Aircraft owned and operated by Religious organisations (1)
- Just Because \- I don't know why I like you, but I do. (8)
- M\*A\*S\*H \- Air Ambulance and Medical Flights
- Military Contractors \- Why do the dirty work when someone else can do it for you ? (39)
- Must be nice \- Billionaires, not millionaires, daaaahling (2)
- Nuclear \- Nuclear Emergency Support Team etc (12)
- Other Air Forces \- Air Force aircraft that are not RAF or USAF (18)
- Other Navies \- Navy Aircraft that are not Royal Navy or United States Navy (1)
- Police Forces \- Your friendly neighbourhood flying (insert local colloquialism here) (4)
- Quango \- Nato, United Nations, World Bank etc (15)
- RAF \- Aircraft of the Royal Air Force (47)
- Royal Aircraft \- Aircraft used or owned by the UK Royal Family (8)
- Royal Navy \- Aircraft of the Royal Navy (2)
- Sock Puppet \- Someone Pretending to be something they are not e.g. Covert DOJ Aircraft (86)
- UAV \- It's not natural, I tell 'ya (0)
- UK National Police Air Service \- Your friendly neighbourhood flying bobby (24)
- Under Observation \- Up to something dodgy, maybe (30)
- USAF \- Aircraft of the United States Air Force (52)
- Watch me Fly \- Flying and Training Schools (13)
- Who needs an Engine ? \- Gliders etc (2)
- Zoomies \- Fast jets, fighters. Anything that moves fast. (12)

# To do / Ideas

- RAF Typhoon Display Team
- US Dept of Interior
- US Dept of Energy
- Other US Gov Depts
- Check Saudi Armed Forces Medical Services is complete
- Check Empire Test Pilots School is complete
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
- List of DA42 / DA62 MPP Operators
- Thales UK
- Qinetiq
- Survey / Mappiing Aircarft
- Other sureveillance aircraft types
- 750 Naval Air Squadron (Observers)
- Cal Fire
- Coulson Aviation
- Australian Aircraft called firebird (fire spotter and fighters)
- Erickson air cranes / SH64 (what is the list of names)
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
- Network Rail Helicopter(s)
- Special Convertions e.g. Engine testbeds
- Duxford and other historic flight collections
- Historic Aircraft Flight Trust
- Low volume Airliners / Special Models
- Multinational MRTT Fleet
- Fly Navy Heritage Trust
- Football Teams and other sporting organisations

Any other idea's welcome.

# Data Sources

This data has been gathered from far too many sources to mention, but some sites have been *really* useful.

https://www.flightdb.net/index.php

http://www.rotorspot.nl/

http://www.dtvmovements.co.uk/

http://www.ads-b.nl/

https://www.live-military-mode-s.eu/

https://dictatoralert.org/
