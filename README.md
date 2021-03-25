# plane-alert-db
This project consists of a list of 'interesting' aircraft, formatted as a CSV files. The list is designed to work with the excellent https://github.com/kx1t/docker-planefence and take the form 

- ICAO,Ident,Operator,Type,CMPG,$Tag,#$Tag2,Category

e.g 406C1B,G-CNWL,Cornwall Air Ambulance,Bell MD-900 Explorer,Civ,Air Ambo,Choppa,M\*A\*S\*H 

Add these characters to the column headers to control the behavior of PlaneAlert

- "$" \- Tweet this column as #hashtag
- "#" \- Don't show on the website (it will ignore this for the ICAO field, which is always shown)
- "#$"\- Don't show on the website, but tweet as a #hashtag

in the eample above the #hashtags would be 'Air Ambo' and 'Choppa', and Tag2 will not be shown on the PA website.

# Current Content

- plane-alert-db.txt - The list of interesting aircaft, with tags and categories.
- community-list.txt - Open list to add your suggestions to. These will be moved to the main list in time.  


# Description of Categories	   

Think of categories like groups, with similar or related aircraft listed together. This allows you to easily select a subset of the list for your own use. The category names (and tags) come from my rather idiosyncratic sense of humour. If you have better suggestions I'm all ears.

- Aerobatic Teams \- Red Arrows, Blue Angels etc
- Army Air Corp \- UK Army Air Corp. Mainly Helicopters
- As Seen on TV \- Companies and Brands
- Battle of Britiain Memorial Flight \- Historic British aircraft from WW2
- Bizjets \- Fancy pants planes for fancy pants people
- Coastguard \- Coastguard Aircraft
- Community \- Suggested by you. Aircraft start here and move other other categories
- Dictator Alert \- People of potentially questionable morals and values
- Distinctive \- Unique and/or special aircraft e.g The AN-224 Myria, NASA aircraft
- Dogs with Jobs \- Aircraft with specific roles and/or modifications
- Governments \- Aircraft registired to Governments
- Jesus he Knows me \- Aircraft owned and operated by Religious organisations
- Just Because \- I don't know why I like you, but I do.
- M\*A\*S\*H \- Air Ambulance and Medical Flights
- Military Contractors \- Why do the dirty work when someone else can do it for you ?
- Must be nice \- Billionaires, not millionaires, daaaahling
- Nuclear \- Nuclear Emergency Support Team etc
- Other Air Forces \- Air Force aircarft that are not RAF or USAF
- Other Navies \- Navy Aircraft that are not Royal Navy or United States Navy
- Police Forces \- Your friendly neighbourhood flying <insert local colloquialism here>
- RAF \- Aircraft of the Royal Air Force
- Royal Aircraft \- Aircraft used or owned by the UK Royal Family
- Royal Navy \- Aircraft of the Royal Navy
- Sock Puppet \- Someone Pretending to be something they are not
- Spotted \- Aircraft spotted by my ADSB station. Aircraft start here and move other other categories
- UK National Police Air Service \- Your friendly neighbourhood flying bobby
- Under Observation \- Up to something dodgy, maybe
- USAF \- Aircraft of the United States Air Force
- Watch me Fly \- Flying and Training Schools
- Who needs an Engine ? \- Gliders etc
- Zoomies \- Fast jets, fighters. Anything that moves fast.


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
