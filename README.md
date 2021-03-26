# plane-alert-db
This project consists of a list of 'interesting' aircraft, formatted as a CSV file. The list is designed to work with the excellent https://github.com/kx1t/docker-planefence and takes the form 

- ICAO,Ident,Operator,Type,CMPG,$Tag,#$Tag2,Category

e.g 406C1B,G-CNWL,Cornwall Air Ambulance,Bell MD-900 Explorer,Civ,Air Ambo,Choppa,M\*A\*S\*H 

Add these characters to the column headers to control the behavior of PlaneAlert

- "$" \- Tweet this column as #hashtag
- "#" \- Don't show on the website (it will ignore this for the ICAO field, which is always shown)
- "#$"\- Don't show on the website, but tweet as a #hashtag

in the eample above the #hashtags would be 'Air Ambo' and 'Choppa', and Tag2 will not be shown on the PA website.

\*CMPG = Civilian, Military, Police, Government

# plane-alert-db
To use this list with Planefence, simply configure your planefence.config setup to include the following line:
PF_ALERTLIST=https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-db.txt

If you want to add the list in addition to your local plane-alert-db.txt list, you can do the following. 
PF_ALERTLIST=plane-alert-db.txt,https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-db.txt

**Note -- the priority of use is first-to-last, so if you want your local list to be interpreted first, move it to the front of the list**

# Current Content

The list contains **568** unique aircraft in **32** different categories

- [plane-alert-db.txt](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-db.txt) - The list of interesting aircaft, with tags and categories.
- [community-list.txt](https://github.com/Sportsbadger/plane-alert-db/blob/main/community-list) - Open list to add your suggestions to. These will be moved to the main list in time.  


# Description of Categories	   

Think of categories like groups, with similar or related aircraft listed together. This allows you to easily select a subset of the list for your own use. The category names (and tags) come from my rather idiosyncratic sense of humour. If you have better suggestions I'm all ears.

- Aerobatic Teams \- Red Arrows, Blue Angels etc (21)
- Army Air Corp \- UK Army Air Corp. Mainly Helicopters (5)
- As Seen on TV \- Companies and Brands (22)
- Battle of Britiain Memorial Flight \- Historic British aircraft from WW2 (12)
- Bizjets \- Fancy pants planes for fancy pants people (9)
- Coastguard \- Coastguard Aircraft (6)
- Community \- Suggested by you. Aircraft start here and move other other categories (0)
- Dictator Alert \- People of potentially questionable morals and values (45)
- Distinctive \- Unique and/or special aircraft e.g The AN-224 Myria, NASA aircraft (38)
- Dogs with Jobs \- Aircraft with specific roles and/or modifications (17)
- Governments \- Aircraft registired to Governments (4)
- Historic \- It's older than I am, and most likely has a prop. (0)
- Jesus he Knows me \- Aircraft owned and operated by Religious organisations (1)
- Just Because \- I don't know why I like you, but I do. (8)
- M\*A\*S\*H \- Air Ambulance and Medical Flights
- Military Contractors \- Why do the dirty work when someone else can do it for you ? (39)
- Must be nice \- Billionaires, not millionaires, daaaahling (2)
- Nuclear \- Nuclear Emergency Support Team etc (12)
- Other Air Forces \- Air Force aircarft that are not RAF or USAF (15)
- Other Navies \- Navy Aircraft that are not Royal Navy or United States Navy (1)
- Police Forces \- Your friendly neighbourhood flying (insert local colloquialism here) (3)
- Quango \- Nato, United Nations, World Bank etc (15)
- RAF \- Aircraft of the Royal Air Force (47)
- Royal Aircraft \- Aircraft used or owned by the UK Royal Family (8)
- Royal Navy \- Aircraft of the Royal Navy (1)
- Sock Puppet \- Someone Pretending to be something they are not e.g. Covert DOJ Aircraft (86)
- UK National Police Air Service \- Your friendly neighbourhood flying bobby (24)
- Under Observation \- Up to something dodgy, maybe (30)
- USAF \- Aircraft of the United States Air Force (47)
- Watch me Fly \- Flying and Training Schools (13)
- Who needs an Engine ? \- Gliders etc (2)
- Zoomies \- Fast jets, fighters. Anything that moves fast. (12)


# To do / Ideas

- Add more Military/Research/One-off Aircraft
- National Display Teams (e.g. Red Arrows, Blue Angels)
- Heads of State
- Drones and Spy Aircraft
- 'Covert' aircraft hiding their true purpose/ownership
- Old and Rare
- Aircraft with special history (e.g. Chinook Bravo November)
- Firefighting aircraft
- NASA Aircraft
- Input from non-english speaking countries
- film/tv/famous (Airwolf etc)
- UK Border force

Any other idea's welcome.

# Data Sources

This data has been gathered from far too many sources to mention, but some sites have been *really* useful.

https://www.flightdb.net/index.php

http://www.rotorspot.nl/

http://www.dtvmovements.co.uk/

http://www.ads-b.nl/

https://www.live-military-mode-s.eu/
