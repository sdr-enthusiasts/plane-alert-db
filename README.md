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

- PF_ALERTLIST=plane-alert-db.txt,https://raw.githubusercontent.com/Sportsbadger/plane-alert-db/main/plane-alert-db.csv

**Note -- the priority of use is first-to-last, so if you want your local list to be interpreted first, move it to the front of the list**

# Current Content

The list contains **1865** unique aircraft in **40** different categories.

- [plane-alert-db.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-db.csv) - The list of interesting aircraft, with tags,categories and links. (1865)
- [plane-alert-civ.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-civ.csv) - Civilian Registered Aircraft, includes Historic and Distinctive. (391)
- [plane-alert-mil.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-mil.csv) - Military Only. (1100)
- [plane-alert-pol.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-pol.csv) - Police Forces. (28)
- [plane-alert-gov.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/plane-alert-gov.csv) - Governments, Gov Agencies and Dictators. (346)
- [badgers-best.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/badgers-best.csv) - My own personal selections from the main list. (701)
- [community-list.csv](https://github.com/Sportsbadger/plane-alert-db/blob/main/community-list) - Open list to add your suggestions to. These will be moved to the main list in time.


# Description of Categories	   

Think of categories like groups, with similar or related aircraft listed together. This allows you to easily select a subset of the list for your own use. The category names (and tags) come from my rather idiosyncratic sense of humour. If you have better suggestions I'm all ears.

- Aerobatic Teams \- Red Arrows, Blue Angels etc (49)
- Army Air Corp \- UK Army Air Corp. Mainly Helicopters (20)
- As Seen on TV \- Companies and Brands (31)
- Battle of Britiain Memorial Flight \- Historic British aircraft from WW2 (12)
- Big Hello \- Large Helicopters (sic) (38)
- Bizjets \- Fancy pants planes for fancy pants people (18)
- Coastguard \- Coastguard, Customs and Border Patrols (15)
- Da Comrade \- Russian or Soviet Aircraft. I love their design, so they get their own category (18)
- Dictator Alert \- People of potentially questionable morals and values (210)
- Distinctive \- Unique and/or special aircraft e.g The AN-224 Myria, NASA aircraft (33)
- Dogs with Jobs \- Aircraft with specific roles and/or modifications (31)
- Football  \- Actual, Aussie Rules or American. We don't descriminate. (1)
- GAF \- Aircraft of the German Air Force, thank to Rhodan76 (291)
- Governments \- Aircraft registired to Governments (16)
- Historic \- It's older than I am, and most likely has a prop. (14)
- Jesus he Knows me \- Aircraft owned and operated by Religious organisations (3)
- Just Because \- I don't know why I like you, but I do. (6)
- M\*A\*S\*H \- Air Ambulance and Medical Flights
- Military Contractors \- Why do the dirty work when someone else can do it for you ? (41)
- Must be nice \- Billionaires, not millionaires, daaaahling (12)
- Nuclear \- Nuclear Emergency Support Team etc (12)
- Other Air Forces \- Air Force aircraft that are not RAF or USAF (74)
- Other Navies \- Navy Aircraft that are not Royal Navy or United States Navy (16)
- Police Forces \- Your friendly neighbourhood flying (insert local colloquialism here) (4)
- Ptolemy would be proud \- Mapping and Aerial Survey aircraft.  (14)
- Quango \- Nato, United Nations, World Bank etc (18)
- RAF \- Aircraft of the Royal Air Force (118)
- Royal Aircraft \- Aircraft used or owned by the UK Royal Family (8)
- Royal Navy \- Aircraft of the Royal Navy (54)
- Sock Puppet \- Someone Pretending to be something they are not e.g. Covert DOJ Aircraft (86)
- UAV \- It's not natural, I tell 'ya (2)
- UK National Police Air Service \- Your friendly neighbourhood flying bobby (24)
- Under Observation \- Up to something dodgy, maybe (33)
- United States Navy \- United States naval avaitors. Some say they are the best of the best. (39)
- USAF \- Aircraft of the United States Air Force (378)
- Vanity Plate \- Distinctive registrations (12)
- Watch Me Fly \- Flying and Training Schools (31)
- Who needs an Engine ? \- Gliders etc (15)
- You came here in that thing ? \- Microlights, tiny planes and helis..think Yakima Super Breezy (thanks skstrand) (6)
- Zoomies \- Fast jets, fighters. Anything that moves fast. (30)

# To do / Ideas

No 1 - Update USAF aircraft to use Reg/serial number in place of Ident/Callsign

- RAF Typhoon Display Team
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


# Tag Count

Total count of how many times each tag is used in plane-alert-db.csv

- Cargo \- 261
- Absolute Unit \- 233
- Eye In The Sky \- 219
- Dictator Alert \- 214
- Luftwaffe \- 155
- Zoomies \- 135
- Danger Zone \- 133
- Do A Barrel Roll \- 124
- Bizjet \- 110
- Fill Her Up \- 99
- US Dept Of Justice \- 86
- Ho Ho Ho \- 64
- Old Stuff \- 54
- Fighter \- 54
- Chopper \- 53
- Must Be Nice \- 44
- You Aint Seen Me Right \- 43
- Chonky Boy \- 42
- One Ping Only Vasily \- 41
- Thunderbird 2 \- 38
- Skycrane \- 38
- Not A Bus \- 38
- Choppa \- 34
- Hiiiiiigh In The Sky \- 33
- Specialist \- 32
- I Thought You Was A Pilot Not An Astronaut \- 32
- L-Plate \- 31
- Id Get That Seen Too \- 31
- Covert \- 31
- Training Wheels \- 29
- Ooh Get You \- 29
- M*A*S*H \- 29
- U Wot m8 \- 27
- Police Squad \- 27
- I Feel The Need.... \- 27
- Heavy Duty \- 26
- Vive La France \- 25
- Speak Up Sonny \- 25
- Air Ambo \- 25
- Nicolás Maduro \- 23
- Mohammed bin Salman \- 23
- How Does It Fly \- 23
- Whirly Bird \- 22
- You Came Here In That Thing \- 21
- Vladimir Putin \- 21
- Ooh La La \- 20
- Brrrrrrrrrrrrrrr \- 19
- Wrong Turn At Albuquerque \- 18
- Tiger Tokens \- 18
- Already Has Wings \- 18
- Wocka Wocka \- 17
- Vashe Zdorovye \- 17
- To Be Faaaaaaaaaaaaaaaaaaair \- 17
- Target Practice \- 17
- Puppers \- 17
- Tamim bin Hamad Al Thani \- 16
- Pass The Sick Bag \- 16
- Tomahawk \- 15
- Shiny \- 15
- Open Skies \- 15
- Old \- 15
- N.A.T.O \- 15
- Turn And Burn \- 14
- Ou Sont Les Bagages \- 14
- History \- 14
- Sheikh Nawaf al-Ahmad al-Sabah \- 13
- Rashid Al Maktoum \- 13
- VIP \- 12
- Mae West \- 12
- Government \- 12
- All About That Wingspan \- 12
- Measuring Stick \- 11
- Whoosh \- 10
- Hamad bin Isa Al Khalifa \- 10
- Dieselgate \- 10
- Theodolite \- 9
- Sce To Aux \- 9
- Nasa \- 9
- Kassym-Jomart Tokayev \- 9
- Yes Maam \- 8
- Red Carpet \- 8
- Private Airline \- 8
- Khalifa Al Nahyan \- 8
- Ilham Aliyev \- 8
- Foutje Bedankt \- 8
- Ciao \- 8
- Abdelmadjid Tebboune \- 8
- Wichita Lineman \- 7
- Teodoro Obiang Nguema Mbasogo \- 7
- Not so VIP \- 7
- mmm Neutrons \- 7
- Haitham bin Tarik \- 7
- Trundle Wheel \- 6
- I Am Old \- 6
- Callsign Viper \- 6
- Big Bird \- 6
- Where Is The Engine \- 5
- War Bird \- 5
- USMC \- 5
- USAF \- 5
- Loooong Raaaaaange \- 5
- Jump Johnny Jump \- 5
- Ali Bongo Ondimba \- 5
- Top..ish Gun \- 4
- Office In The Sky \- 4
- Not A Car \- 4
- Luck Of The Irish \- 4
- Jesus He Knows Me \- 4
- Is This My Good Side \- 4
- Ere Me Now \- 4
- Billy Murphy \- 4
- Ali Khamenei \- 4
- Air Force Two \- 4
- You Just Lost A Refinery \- 3
- We Make Your Planes Better \- 3
- Vanity Plate \- 3
- Ultralight \- 3
- State Dept \- 3
- Skydive \- 3
- Quarterback \- 3
- Original Nuttah \- 3
- Odd \- 3
- Mohammed bin Rashid Al Maktoum \- 3
- Leaves On The Line \- 3
- Kung Fu Grip \- 3
- Its The End Of The World And I Know It \- 3
- How Much \- 3
- Gurbanguly Berdimuhamedow \- 3
- Got It Where It Counts \- 3
- Flying Rust Bucket \- 3
- Flying Brick \- 3
- Félix Tshisekedi \- 3
- Culture Beat \- 3
- Cool \- 3
- Chappy \- 3
- Alexander Lukashenko \- 3
- Adama Barrow \- 3
- Abdul Hamid Dbeibeh \- 3
- Xi Jinping \- 2
- What Is That Smell \- 2
- Orange Danger \- 2
- Nope \- 2
- Marineflieger \- 2
- Magic Roundabout \- 2
- Idriss Déby \- 2
- Hot Hot Hot Hot \- 2
- Fire \- 2
- Faure Gnassingbé \- 2
- Emmerson Mnangagwa \- 2
- Digger \- 2
- CIA \- 2
- Boris \- 2
- BACN \- 2
- Agostinho Neto \- 2
- Abdullah II bin Al-Hussein \- 2
- You Lost Mate \- 1
- Yorkshire \- 1
- Where Is The Pilot \- 1
- Wheelbarrow \- 1
- Waffles \- 1
- Vomit Comet \- 1
- Uphold The Public Trust \- 1
- UFO \- 1
- UAV \- 1
- Tricycle \- 1
- The Last Of Us \- 1
- Testbed \- 1
- Sovereignty Council \- 1
- Sale Must End Soon \- 1
- Recep Tayyip Erdoğan \- 1
- Perfectly Serviceable Aircraft \- 1
- Paul Biya \- 1
- Obrigado \- 1
- No Fighting This Is The War Room \- 1
- Nice Waether For Ducks \- 1
- Mohammed Al Sharqi \- 1
- Mahamadou Issoufou \- 1
- Little Nellie \- 1
- Kim Jong-un \- 1
- Jumpers For Goalposts \- 1
- Hungarian Air Force \- 1
- Hellenic Air Force \- 1
- General Hafar \- 1
- Freeze \- 1
- Eensy Weensy \- 1
- Czech Air Force \- 1
- Con Air \- 1
- BUFF \- 1
- Bravo November \- 1
- Bashar al-Assad \- 1
- Backpack Tadpole V-Jet \- 1
- Angel of Deliverance \- 1
- Alright Me Baber \- 1
- 150th Special Operations Squadron \- 1



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
