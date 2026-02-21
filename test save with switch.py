import json
import csv
leaders_by_country = {
  "us": [
    {
      "id": "Q23",
      "first_name": "George",
      "last_name": "Washington",
      "birth_date": "1732-02-22",
      "death_date": "1799-12-14",
      "place_of_birth": "Westmoreland County",
      "wikipedia_url": "https://en.wikipedia.org/wiki/George_Washington",
      "start_mandate": "1789-04-30",
      "end_mandate": "1797-03-04",
      "Bio": "George Washington (February 22, 1732 – December 14 , 1799) was a Founding Father and the first president of the United States , serving from 1789 to 1797. As commander of the Continental Army , Washington led Patriot forces to victory in the American Revolutionary War against the British Empire . He is commonly known as the Father of the Nation for his role in bringing about American independence ."
    },
    {
      "id": "Q76",
      "first_name": "Barack",
      "last_name": "Obama",
      "birth_date": "1961-08-04",
      "death_date": null,
      "place_of_birth": "Kapiolani Medical Center for Women and Children",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Barack_Obama",
      "start_mandate": "2009-01-20",
      "end_mandate": "2017-01-20",
      "Bio": "Barack Hussein Obama II (born August 4, 1961) is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party , he was the first African American president . Obama previously served as a U.S. senator representing Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004."
    },
    {
      "id": "Q91",
      "first_name": "Abraham",
      "last_name": "Lincoln",
      "birth_date": "1809-02-12",
      "death_date": "1865-04-15",
      "place_of_birth": "Sinking Spring Farm",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Abraham_Lincoln",
      "start_mandate": "1861-03-04",
      "end_mandate": "1865-04-15",
      "Bio": "Abraham Lincoln (February 12, 1809 – April 15, 1865) was the 16th president of the United States , serving from 1861 until his assassination in 1865. He led the United States through the American Civil War , defeating the Confederate States and playing a major role in the abolition of slavery ."
    },
    {
      "id": "Q207",
      "first_name": "George",
      "last_name": "Bush",
      "birth_date": "1946-07-06",
      "death_date": null,
      "place_of_birth": "New Haven",
      "wikipedia_url": "https://en.wikipedia.org/wiki/George_W._Bush",
      "start_mandate": "2001-01-20",
      "end_mandate": "2009-01-20",
      "Bio": "George Walker Bush (born July 6, 1946) is an American politician, businessman, and former U.S. Air Force officer who served as the 43rd president of the United States from 2001 to 2009. A member of the Republican Party and the eldest son of the 41st president, George H. W. Bush , he served as the 46th governor of Texas from 1995 to 2000."
    },
    {
      "id": "Q1124",
      "first_name": "Bill",
      "last_name": "Clinton",
      "birth_date": "1946-08-19",
      "death_date": null,
      "place_of_birth": "Hope",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Bill_Clinton",
      "start_mandate": "1993-01-20",
      "end_mandate": "2001-01-20",
      "Bio": "William Jefferson Clinton ( né Blythe III ; born August 19, 1946) is an American politician and lawyer who served as the 42nd president of the United States from 1993 to 2001. A member of the Democratic Party , he previously served as the attorney general of Arkansas from 1977 to 1979 and as the governor of Arkansas from 1979 to 1981, and again from 1983 to 1992. His centrist \" Third Way \" political philosophy became known as Clintonism , which dominated his presidency and the succeeding decades of Democratic Party history ."
    },
    {
      "id": "Q6279",
      "first_name": "Joe",
      "last_name": "Biden",
      "birth_date": "1942-11-20",
      "death_date": null,
      "place_of_birth": "St. Mary's Hospital",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Joe_Biden",
      "start_mandate": "2021-01-20",
      "end_mandate": null,
      "Bio": "Joseph Robinette Biden Jr. (born November 20, 1942) is an American politician who was the 46th president of the United States from 2021 to 2025. A member of the Democratic Party , he represented Delaware in the United States Senate from 1973 to 2009 and also served as the 47th vice president under President Barack Obama from 2009 to 2017."
    },
    {
      "id": "Q8007",
      "first_name": "Franklin",
      "last_name": "Roosevelt",
      "birth_date": "1882-01-30",
      "death_date": "1945-04-12",
      "place_of_birth": "Hyde Park",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Franklin_D._Roosevelt",
      "start_mandate": "1933-03-04",
      "end_mandate": "1945-04-12",
      "Bio": "Franklin Delano Roosevelt (January 30, 1882 – April 12, 1945), also known as FDR , was the 32nd president of the United States , serving from 1933 until his death in 1945. He is the longest-serving U.S. president and the only one to have served more than two terms. His first two terms were centered on combating the Great Depression , while his third and fourth focused on U.S. involvement in World War II . A member of the Democratic Party , Roosevelt served in the New York State Senate from 1911 to 1913 and as the 44th governor of New York from 1929 to 1932."
    },
    {
      "id": "Q8612",
      "first_name": "Andrew",
      "last_name": "Johnson",
      "birth_date": "1808-12-29",
      "death_date": "1875-07-31",
      "place_of_birth": "Raleigh",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Andrew_Johnson",
      "start_mandate": "1865-04-15",
      "end_mandate": "1869-03-04",
      "Bio": "Andrew Johnson (December 29, 1808 – July 31, 1875) was the 17th president of the United States , serving from 1865 to 1869. The 16th vice president , he assumed the presidency following the assassination of Abraham Lincoln . Johnson was a War Democrat who ran with Lincoln on the National Union Party ticket in the 1864 presidential election , coming to office as the American Civil War concluded. Johnson favored quick restoration of the seceded states to the Union without protection for the newly freed people who were formerly enslaved , as well as pardoning ex-Confederates . This led to conflict with the Republican Party -dominated U.S. Congress , culminating in his impeachment by the House of Representatives in 1868. He was acquitted in the Senate by one vote."
    },
    {
      "id": "Q9582",
      "first_name": "Gerald",
      "last_name": "Ford",
      "birth_date": "1913-07-14",
      "death_date": "2006-12-26",
      "place_of_birth": "Omaha",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Gerald_Ford",
      "start_mandate": "1974-08-09",
      "end_mandate": "1977-01-20",
      "Bio": "Gerald Rudolph Ford Jr. (born Leslie Lynch King Jr. ; July 14, 1913 – December 26, 2006) was the 38th president of the United States , serving from 1974 to 1977. A member of the Republican Party , Ford assumed the presidency after the resignation of Richard Nixon , under whom he had served as the 40th vice president from 1973 to 1974 following the resignation of Spiro Agnew . Prior to that, he served as a member of the U.S. House of Representatives from 1949 to 1973."
    },
    {
      "id": "Q9588",
      "first_name": "Richard",
      "last_name": "Nixon",
      "birth_date": "1913-01-09",
      "death_date": "1994-04-22",
      "place_of_birth": "Yorba Linda",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Richard_Nixon",
      "start_mandate": "1969-01-20",
      "end_mandate": "1974-08-09",
      "Bio": "Richard Milhous Nixon (January 9, 1913 – April 22, 1994) was the 37th president of the United States , serving from 1969 until his resignation in 1974. A member of the Republican Party , he represented California in both houses of the United States Congress before serving as the 36th vice president under President Dwight D. Eisenhower from 1953 to 1961. His presidency saw the reduction of U.S. involvement in the Vietnam War , détente with the Soviet Union and China , the Apollo 11 Moon landing, and the establishment of the Environmental Protection Agency and Occupational Safety and Health Administration . Nixon's second term ended early when he became the only U.S. president to resign from office, as a result of the Watergate scandal ."
    },
    {
      "id": "Q9640",
      "first_name": "Lyndon",
      "last_name": "Johnson",
      "birth_date": "1908-08-27",
      "death_date": "1973-01-22",
      "place_of_birth": "Stonewall",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Lyndon_B._Johnson",
      "start_mandate": "1963-11-22",
      "end_mandate": "1969-01-20",
      "Bio": "Lyndon Baines Johnson ( / ˈ l ɪ n d ə n ˈ b eɪ n z / ; August 27, 1908 – January 22, 1973), also known as LBJ , was the 36th president of the United States , serving from 1963 to 1969. He became president after the assassination of John F. Kennedy , under whom he had served as the 37th vice president from 1961 to 1963. A Southern Democrat , Johnson previously represented Texas in Congress for over 23 years, first as a U.S. representative from 1937 to 1949, and then as a U.S. senator from 1949 to 1961."
    },
    {
      "id": "Q9696",
      "first_name": "John",
      "last_name": "Kennedy",
      "birth_date": "1917-05-29",
      "death_date": "1963-11-22",
      "place_of_birth": "Brookline",
      "wikipedia_url": "https://en.wikipedia.org/wiki/John_F._Kennedy",
      "start_mandate": "1961-01-20",
      "end_mandate": "1963-11-22",
      "Bio": "John Fitzgerald Kennedy (May 29, 1917 – November 22, 1963), also known as JFK , was the 35th president of the United States , serving from 1961 until his assassination in 1963. He was the youngest person elected president at 43 years. Kennedy served at the height of the Cold War , and the majority of his foreign policy concerned relations with the Soviet Union and Cuba . A member of the Democratic Party , Kennedy represented Massachusetts in both houses of the United States Congress before his presidency."
    },
    {
      "id": "Q9916",
      "first_name": "Dwight",
      "last_name": "Eisenhower",
      "birth_date": "1890-10-14",
      "death_date": "1969-03-28",
      "place_of_birth": "Denison",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Dwight_D._Eisenhower",
      "start_mandate": "1953-01-20",
      "end_mandate": "1961-01-20",
      "Bio": "Dwight David \" Ike \" Eisenhower (born David Dwight Eisenhower ; October 14, 1890 – March 28, 1969) was the 34th president of the United States , serving from 1953 to 1961. During World War II , he was Supreme Commander of the Allied Expeditionary Force in Europe and achieved the five-star rank as General of the Army . Eisenhower planned and supervised two of the most consequential military campaigns of World War II : Operation Torch in the North Africa campaign in 1942–1943 and the invasion of Normandy in 1944."
    },
    {
      "id": "Q9960",
      "first_name": "Ronald",
      "last_name": "Reagan",
      "birth_date": "1911-02-06",
      "death_date": "2004-06-05",
      "place_of_birth": "Tampico",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Ronald_Reagan",
      "start_mandate": "1981-01-20",
      "end_mandate": "1989-01-20",
      "Bio": "Ronald Wilson Reagan (February 6, 1911 – June 5, 2004) was an American politician and actor who served as the 40th president of the United States from 1981 to 1989. A member of the Republican Party , he became an important figure in the American conservative movement . The period encompassing his presidency is known as the Reagan era ."
    },
    {
      "id": "Q11613",
      "first_name": "Harry",
      "last_name": "Truman",
      "birth_date": "1884-05-08",
      "death_date": "1972-12-26",
      "place_of_birth": "Lamar",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Harry_S._Truman",
      "start_mandate": "1945-04-12",
      "end_mandate": "1953-01-20",
      "Bio": "Harry S. Truman (May 8, 1884 – December 26, 1972) was the 33rd president of the United States , serving from 1945 to 1953. As the 34th vice president in 1945, he assumed the presidency upon the death of Franklin D. Roosevelt that year. Subsequently, Truman implemented the Marshall Plan in the aftermath of World War II to rebuild the economy of Western Europe, and established both the Truman Doctrine and NATO to contain the expansion of Soviet communism . A member of the Democratic Party , he proposed numerous New Deal coalition liberal domestic reforms, but few were enacted by the conservative coalition that dominated the United States Congress ."
    },
    {
      "id": "Q11806",
      "first_name": "John",
      "last_name": "Adams",
      "birth_date": null,
      "death_date": "1826-07-04",
      "place_of_birth": "Braintree",
      "wikipedia_url": "https://en.wikipedia.org/wiki/John_Adams",
      "start_mandate": "1797-03-04",
      "end_mandate": "1801-03-04",
      "Bio": "John Adams (October 30, 1735 – July 4, 1826) was a Founding Father and the second president of the United States from 1797 to 1801. Before his presidency , he was a leader of the American Revolution that achieved independence from Great Britain . During the latter part of the Revolutionary War and in the early years of the new nation, he served the Continental Congress of the United States as a senior diplomat in Europe. Adams was the first person to hold the office of vice president of the United States , serving from 1789 to 1797. He was a dedicated diarist and regularly corresponded with important contemporaries, including his wife and advisor Abigail Adams and his friend and rival Thomas Jefferson ."
    },
    {
      "id": "Q11812",
      "first_name": "Thomas",
      "last_name": "Jefferson",
      "birth_date": null,
      "death_date": "1826-07-04",
      "place_of_birth": "Shadwell",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Thomas_Jefferson",
      "start_mandate": "1801-03-04",
      "end_mandate": "1809-03-04",
      "Bio": "Thomas Jefferson (April 13 , 1743 – July 4, 1826) was an American Founding Father and the third president of the United States from 1801 to 1809. He was the primary author of the Declaration of Independence . Jefferson was the nation's first U.S. secretary of state under George Washington and then the nation's second vice president under John Adams . Jefferson was a leading proponent of democracy, republicanism , and natural rights , and he produced formative documents and decisions at the state, national, and international levels."
    },
    {
      "id": "Q11813",
      "first_name": "James",
      "last_name": "Madison",
      "birth_date": "1751-03-16",
      "death_date": "1836-06-28",
      "place_of_birth": "Port Conway",
      "wikipedia_url": "https://en.wikipedia.org/wiki/James_Madison",
      "start_mandate": "1809-03-04",
      "end_mandate": "1817-03-04",
      "Bio": "James Madison (March 16, 1751 – June 28, 1836) was an American statesman, diplomat, and Founding Father who served as the fourth president of the United States from 1809 to 1817. Madison was popularly acclaimed as the \" Father of the Constitution \" for his pivotal role in drafting and promoting the Constitution of the United States and the Bill of Rights ."
    },
    {
      "id": "Q11815",
      "first_name": "James",
      "last_name": "Monroe",
      "birth_date": "1758-04-28",
      "death_date": "1831-07-04",
      "place_of_birth": "Monroe Hall",
      "wikipedia_url": "https://en.wikipedia.org/wiki/James_Monroe",
      "start_mandate": "1817-03-04",
      "end_mandate": "1825-03-04",
      "Bio": "James Monroe ( / m ə n ˈ r oʊ / mən- ROH ; April 28, 1758 – July 4, 1831) was an American Founding Father who served as the fifth president of the United States from 1817 to 1825. He was the last Founding Father to serve as president as well as the last president of the Virginia dynasty . Monroe was a member of the Democratic-Republican Party , and his presidency coincided with the Era of Good Feelings , concluding the First Party System era of American politics. He issued the Monroe Doctrine , a policy of limiting European colonialism in the Americas. Monroe previously served as Governor of Virginia , a member of the United States Senate , U.S. ambassador to France and Britain, the seventh secretary of state, and the eighth secretary of war."
    },
    {
      "id": "Q11816",
      "first_name": "John",
      "last_name": "Adams",
      "birth_date": "1767-07-11",
      "death_date": "1848-02-23",
      "place_of_birth": "Braintree",
      "wikipedia_url": "https://en.wikipedia.org/wiki/John_Quincy_Adams",
      "start_mandate": "1825-03-04",
      "end_mandate": "1829-03-04",
      "Bio": "John Quincy Adams ( / ˈ k w ɪ n z i / ⓘ ; July 11, 1767 – February 23, 1848) was the sixth president of the United States , serving from 1825 to 1829. He previously served as the eighth United States secretary of state from 1817 to 1825; minister to Great Britain , Prussia , and Russia ; and senator for Massachusetts . After his presidency, Adams uniquely returned to Congress as a member of the lower house , where he died in 1848. He was the eldest son of John Adams , the second president, and First Lady Abigail Adams . Among his children were Charles Francis Adams Sr. Initially a Federalist like his father, Adams spent his presidency as a member of the Democratic-Republican Party , and later, in the mid-1830s, became affiliated with the Whig Party ."
    },
    {
      "id": "Q11817",
      "first_name": "Andrew",
      "last_name": "Jackson",
      "birth_date": "1767-03-15",
      "death_date": "1845-06-08",
      "place_of_birth": "Waxhaws",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Andrew_Jackson",
      "start_mandate": "1829-03-04",
      "end_mandate": "1837-03-04",
      "Bio": "Andrew Jackson (March 15, 1767 – June 8, 1845) was the seventh president of the United States from 1829 to 1837. He rose to fame as a U.S. Army general and served in both houses of the U.S. Congress . His political philosophy, which dominated his presidency , became the basis for the rise of Jacksonian democracy . His legacy is controversial: he has been praised as an advocate for white working Americans and preserving the union of states , and criticized for his racist policies, particularly towards Native Americans ."
    },
    {
      "id": "Q11820",
      "first_name": "Martin",
      "last_name": "Van Buren",
      "birth_date": "1782-12-05",
      "death_date": "1862-07-24",
      "place_of_birth": "Kinderhook",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Martin_Van_Buren",
      "start_mandate": "1837-03-04",
      "end_mandate": "1841-03-04",
      "Bio": "Martin Van Buren ( / v æ n ˈ b jʊər ən / van BYOO -rən ; Dutch : Maarten van Buren ⓘ ; December 5, 1782 – July 24, 1862) was the eighth president of the United States , serving from 1837 to 1841. A primary founder of the Democratic Party , he held a number of prominent offices. Van Buren served as New York's attorney general and U.S. senator , then briefly as the ninth governor of New York . After joining Andrew Jackson's administration , he served as the tenth United States secretary of state , minister to the United Kingdom , and ultimately, as the eighth vice president from 1833 to 1837, after being elected on Jackson's ticket in 1832 . Van Buren won the presidency in 1836 against divided Whig opponents. He lost re-election in 1840 , and failed to win the Democratic nomination in 1844 . Later in life, Van Buren re-emerged as an elder statesman and an anti-slavery leader who led the Free Soil Party ticket in the 1848 presidential election ."
    },
    {
      "id": "Q11869",
      "first_name": "William",
      "last_name": "Harrison",
      "birth_date": "1773-02-09",
      "death_date": "1841-04-04",
      "place_of_birth": "Charles City County",
      "wikipedia_url": "https://en.wikipedia.org/wiki/William_Henry_Harrison",
      "start_mandate": "1841-03-04",
      "end_mandate": "1841-04-04",
      "Bio": "William Henry Harrison (February 9, 1773 – April 4, 1841) was the ninth president of the United States , serving from March 4 to April 4, 1841, the shortest presidency in U.S. history. He was also the first U.S. president to die in office, causing a brief constitutional crisis , since presidential succession was not then fully defined in the U.S. Constitution . Harrison was the last president born as a British subject in the Thirteen Colonies . He was a member of the Harrison family of Virginia , and a son of Benjamin Harrison V , who was a U.S. Founding Father . His own son John Scott Harrison was the father of Benjamin Harrison , the 23rd U.S. president."
    },
    {
      "id": "Q11881",
      "first_name": "John",
      "last_name": "Tyler",
      "birth_date": "1790-03-29",
      "death_date": "1862-01-18",
      "place_of_birth": "Charles City County",
      "wikipedia_url": "https://en.wikipedia.org/wiki/John_Tyler",
      "start_mandate": "1841-04-04",
      "end_mandate": "1845-03-04",
      "Bio": "John Tyler (March 29, 1790 – January 18, 1862) was the tenth president of the United States , serving from 1841 to 1845, after briefly holding office as the tenth vice president in 1841. He was elected vice president on the 1840 Whig ticket with William Henry Harrison , succeeding to the presidency following Harrison's death 31 days after assuming office as president. Tyler was a stalwart supporter and advocate of states' rights , including regarding slavery , and he adopted nationalistic policies as president only when they did not infringe on the states' powers. His unexpected rise to the presidency posed a threat to the presidential ambitions of Senator Henry Clay and other Whig politicians and left Tyler estranged from both major political parties at the time: the Whigs and the Democrats ."
    },
    {
      "id": "Q11891",
      "first_name": "James",
      "last_name": "Polk",
      "birth_date": "1795-11-02",
      "death_date": "1849-06-15",
      "place_of_birth": "Pineville",
      "wikipedia_url": "https://en.wikipedia.org/wiki/James_K._Polk",
      "start_mandate": "1845-03-04",
      "end_mandate": "1849-03-04",
      "Bio": "James Knox Polk ( / p oʊ k / ; November 2, 1795 – June 15, 1849) was the 11th president of the United States , serving from 1845 to 1849. A protégé of Andrew Jackson and a member of the Democratic Party , he was an advocate of American expansionism and Jacksonian democracy . Polk saw Texas join the Union in his first year in office, one of the precipitating causes that soon led the U.S. into the Mexican–American War . The settlement of that war expanded American territory to the Pacific Ocean. During his term, the dispute over the Oregon Territory with the United Kingdom was resolved as well, creating the present U.S.-Canadian boundary."
    },
    {
      "id": "Q11896",
      "first_name": "Zachary",
      "last_name": "Taylor",
      "birth_date": "1784-11-24",
      "death_date": "1850-07-09",
      "place_of_birth": "Barboursville",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Zachary_Taylor",
      "start_mandate": "1849-03-04",
      "end_mandate": "1850-07-09",
      "Bio": "Zachary Taylor (November 24, 1784 – July 9, 1850) was an American military officer and politician who was the 12th president of the United States , serving from 1849 until his death in 1850. Taylor was a career officer in the United States Army , rising to the rank of major general and becoming a national hero for his victories in the Mexican–American War . As a result, he won election to the White House despite his vague political beliefs. His top priority as president was to preserve the Union. He died 16 months into his term from a stomach disease. Taylor had the third-shortest presidential term in U.S. history."
    },
    {
      "id": "Q12306",
      "first_name": "Millard",
      "last_name": "Fillmore",
      "birth_date": "1800-01-07",
      "death_date": "1874-03-08",
      "place_of_birth": "Summerhill",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Millard_Fillmore",
      "start_mandate": "1850-07-09",
      "end_mandate": "1853-03-04",
      "Bio": "Millard Fillmore (January 7, 1800 – March 8, 1874) was the 13th president of the United States , serving from 1850 to 1853. He was the last president to be a member of the Whig Party while in the White House , and the last to be neither a Democrat nor a Republican . A former member of the U.S. House of Representatives , Fillmore was elected vice president in 1848 , and succeeded to the presidency when Zachary Taylor died in 1850. Fillmore was instrumental in passing the Compromise of 1850 , which led to a brief truce in the battle over the expansion of slavery ."
    },
    {
      "id": "Q12312",
      "first_name": "Franklin",
      "last_name": "Pierce",
      "birth_date": "1804-11-23",
      "death_date": "1869-10-08",
      "place_of_birth": "Hillsborough",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Franklin_Pierce",
      "start_mandate": "1853-03-04",
      "end_mandate": "1857-03-04",
      "Bio": "Franklin Pierce (November 23, 1804 – October 8, 1869) was the 14th president of the United States , serving from 1853 to 1857. A northern Democrat who believed that the abolitionist movement was a fundamental threat to national unity, he alienated anti-slavery groups by signing the Kansas–Nebraska Act and enforcing the Fugitive Slave Act . Conflict between North and South continued after Pierce's presidency , and, following Abraham Lincoln 's victory in the 1860 presidential election , the Southern states seceded , resulting in the American Civil War ."
    },
    {
      "id": "Q12325",
      "first_name": "James",
      "last_name": "Buchanan",
      "birth_date": "1791-04-23",
      "death_date": "1868-06-01",
      "place_of_birth": "Stony Batter",
      "wikipedia_url": "https://en.wikipedia.org/wiki/James_Buchanan",
      "start_mandate": "1857-03-04",
      "end_mandate": "1861-03-04",
      "Bio": "James Buchanan Jr. ( / b j uː ˈ k æ n ə n / ⓘ bew- KAN -ən ; April 23, 1791 – June 1, 1868) was the 15th president of the United States , serving from 1857 to 1861. He also served as the 17th United States secretary of state from 1845 to 1849 and represented Pennsylvania in both houses of the U.S. Congress . Buchanan was an advocate for states' rights , particularly regarding slavery , and minimized the role of the federal government preceding the American Civil War ."
    },
    {
      "id": "Q22686",
      "first_name": "Donald",
      "last_name": "Trump",
      "birth_date": "1946-06-14",
      "death_date": null,
      "place_of_birth": "Jamaica Hospital Medical Center",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Donald_Trump",
      "start_mandate": "2017-01-20",
      "end_mandate": "2021-01-20",
      "Bio": "Donald John Trump (born June 14, 1946) is an American politician, media personality, and businessman who is the 47th president of the United States . A member of the Republican Party , he served as the 45th president from 2017 to 2021."
    },
    {
      "id": "Q23505",
      "first_name": "George",
      "last_name": "Bush",
      "birth_date": "1924-06-12",
      "death_date": "2018-11-30",
      "place_of_birth": "Milton",
      "wikipedia_url": "https://en.wikipedia.org/wiki/George_H._W._Bush",
      "start_mandate": "1989-01-20",
      "end_mandate": "1993-01-20",
      "Bio": "George Herbert Walker Bush (June 12, 1924 – November 30, 2018) was the 41st president of the United States , serving from 1989 to 1993. A member of the Republican Party , he also served as the 43rd vice president under President Ronald Reagan from 1981 to 1989 and previously in various other federal positions ."
    },
    {
      "id": "Q23685",
      "first_name": "Jimmy",
      "last_name": "Carter",
      "birth_date": "1924-10-01",
      "death_date": null,
      "place_of_birth": "Lillian G. Carter Nursing Center",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Jimmy_Carter",
      "start_mandate": "1977-01-20",
      "end_mandate": "1981-01-20",
      "Bio": "James Earl Carter Jr. (October 1, 1924 – December 29, 2024) was an American politician and humanitarian who served as the 39th president of the United States from 1977 to 1981. A member of the Democratic Party , Carter served from 1971 to 1975 as the 76th governor of Georgia and from 1963 to 1967 in the Georgia State Senate . He is the only U.S. president from Georgia , and he lived longer than any other president in U.S. history , reaching age 100 ."
    },
    {
      "id": "Q33866",
      "first_name": "Theodore",
      "last_name": "Roosevelt",
      "birth_date": "1858-10-27",
      "death_date": "1919-01-06",
      "place_of_birth": "Manhattan",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Theodore_Roosevelt",
      "start_mandate": "1901-09-14",
      "end_mandate": "1909-03-04",
      "Bio": "Theodore Roosevelt Jr. (October 27, 1858 – January 6, 1919), also known as Teddy or T. R. , was the 26th president of the United States , serving from 1901 to 1909. Roosevelt previously was involved in New York politics, including serving as the state's 33rd governor for two years. He served as the 25th vice president under President William McKinley for six months in 1901, assuming the presidency after McKinley's assassination . As president, Roosevelt emerged as a leader of the Republican Party and became a driving force for anti-trust and Progressive Era policies."
    },
    {
      "id": "Q34296",
      "first_name": "Woodrow",
      "last_name": "Wilson",
      "birth_date": "1856-12-28",
      "death_date": "1924-02-03",
      "place_of_birth": "Staunton",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Woodrow_Wilson",
      "start_mandate": "1913-03-04",
      "end_mandate": "1921-03-04",
      "Bio": "Thomas Woodrow Wilson (December 28, 1856 – February 3, 1924) was the 28th president of the United States , serving from 1913 to 1921. He was the only Democrat to serve as president during the Progressive Era , when Republicans dominated the presidency and legislative branches . As president, Wilson made significant economic reforms and led the United States through World War I . He was the leading architect of the League of Nations , and his stance on foreign policy came to be known as Wilsonianism ."
    },
    {
      "id": "Q34597",
      "first_name": "James",
      "last_name": "Garfield",
      "birth_date": "1831-11-19",
      "death_date": "1881-09-19",
      "place_of_birth": "Moreland Hills",
      "wikipedia_url": "https://en.wikipedia.org/wiki/James_A._Garfield",
      "start_mandate": "1881-03-04",
      "end_mandate": "1881-09-19",
      "Bio": "James Abram Garfield (November 19, 1831 – September 19, 1881) was the 20th president of the United States , serving from March 1881 until his death in September that year after being shot in July . A preacher, lawyer, and Civil War general, Garfield served nine terms in the United States House of Representatives and is the only sitting member of the House to be elected president. Before he ran for president, the Ohio General Assembly had elected him to the U.S. Senate , a position he declined upon becoming president-elect ."
    },
    {
      "id": "Q34836",
      "first_name": "Ulysses",
      "last_name": "Grant",
      "birth_date": "1822-04-27",
      "death_date": "1885-07-23",
      "place_of_birth": "Point Pleasant",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Ulysses_S._Grant",
      "start_mandate": "1869-03-04",
      "end_mandate": "1877-03-04",
      "Bio": "Ulysses S. Grant (born Hiram Ulysses Grant ; April 27, 1822 – July 23, 1885) was the 18th president of the United States , serving from 1869 to 1877. He previously led the Union Army to victory in the American Civil War in 1865 as commanding general ."
    },
    {
      "id": "Q35041",
      "first_name": "William",
      "last_name": "McKinley",
      "birth_date": "1843-01-29",
      "death_date": "1901-09-14",
      "place_of_birth": "Niles",
      "wikipedia_url": "https://en.wikipedia.org/wiki/William_McKinley",
      "start_mandate": "1897-03-04",
      "end_mandate": "1901-09-14",
      "Bio": "William McKinley (January 29, 1843 – September 14, 1901) was the 25th president of the United States , serving from 1897 until his assassination in 1901. A member of the Republican Party , he led a realignment that made Republicans largely dominant in the industrial states and nationwide for decades. McKinley successfully led the U.S. in the Spanish–American War and oversaw a period of American expansionism , with the annexations of Hawaii , Puerto Rico , Guam , the Philippines , and American Samoa ."
    },
    {
      "id": "Q35171",
      "first_name": "Stephen",
      "last_name": "Cleveland",
      "birth_date": "1837-03-18",
      "death_date": "1908-06-24",
      "place_of_birth": "Caldwell",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Grover_Cleveland",
      "start_mandate": "1893-03-04",
      "end_mandate": "1897-03-04",
      "Bio": "Stephen Grover Cleveland (March 18, 1837 – June 24, 1908) was the 22nd and 24th president of the United States , serving from 1885 to 1889 and from 1893 to 1897. He was the first U.S. president to serve nonconsecutive terms and the first Democrat elected president after the American Civil War ."
    },
    {
      "id": "Q35236",
      "first_name": "Herbert",
      "last_name": "Hoover",
      "birth_date": "1874-08-10",
      "death_date": "1964-10-20",
      "place_of_birth": "West Branch",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Herbert_Hoover",
      "start_mandate": "1929-03-04",
      "end_mandate": "1933-03-04",
      "Bio": "Herbert Clark Hoover (August 10, 1874 – October 20, 1964) was the 31st president of the United States , serving from 1929 to 1933. A wealthy mining engineer before his presidency, Hoover led the wartime Commission for Relief in Belgium and was the director of the U.S. Food Administration , followed by post-war relief of Europe. As a member of the Republican Party , he served as the third United States secretary of commerce from 1921 to 1928 before being elected president in 1928 . His presidency was dominated by the Great Depression , and his policies and methods to combat it were seen as inadequate and overly conservative. Amid his unpopularity, he decisively lost reelection to Franklin D. Roosevelt in 1932 ."
    },
    {
      "id": "Q35286",
      "first_name": "Warren",
      "last_name": "Harding",
      "birth_date": "1865-11-02",
      "death_date": "1923-08-02",
      "place_of_birth": "Blooming Grove",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Warren_G._Harding",
      "start_mandate": "1921-03-04",
      "end_mandate": "1923-08-02",
      "Bio": "Warren Gamaliel Harding (November 2, 1865 – August 2, 1923) was the 29th president of the United States , serving from 1921 until his death in 1923. A member of the Republican Party , he was one of the most popular presidents at the time of his death. After that, a number of scandals were exposed that greatly damaged his reputation."
    },
    {
      "id": "Q35498",
      "first_name": "Chester",
      "last_name": "Arthur",
      "birth_date": "1829-10-05",
      "death_date": "1886-11-18",
      "place_of_birth": "Fairfield",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Chester_A._Arthur",
      "start_mandate": "1881-09-19",
      "end_mandate": "1885-03-04",
      "Bio": "Chester Alan Arthur (October 5, 1829 – November 18, 1886) was the 21st president of the United States , serving from 1881 to 1885. He was a Republican from New York who previously served as the 20th vice president under President James A. Garfield . Assuming the presidency after Garfield's assassination , Arthur's administration saw the largest expansion of the U.S. Navy , the end of the so-called \" spoils system \", and the implementation of harsher restrictions for migrants entering from abroad."
    },
    {
      "id": "Q35648",
      "first_name": "William",
      "last_name": "Taft",
      "birth_date": "1857-09-15",
      "death_date": "1930-03-08",
      "place_of_birth": "Cincinnati",
      "wikipedia_url": "https://en.wikipedia.org/wiki/William_Howard_Taft",
      "start_mandate": "1909-03-04",
      "end_mandate": "1913-03-04",
      "Bio": "William Howard Taft (September 15, 1857 – March 8, 1930) was the 27th president of the United States from 1909 to 1913 and the tenth chief justice of the United States from 1921 to 1930. He is the only person to have held both offices."
    },
    {
      "id": "Q35678",
      "first_name": "Benjamin",
      "last_name": "Harrison",
      "birth_date": "1833-08-20",
      "death_date": "1901-03-13",
      "place_of_birth": "North Bend",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Benjamin_Harrison",
      "start_mandate": "1889-03-04",
      "end_mandate": "1893-03-04",
      "Bio": "Benjamin Harrison (August 20, 1833 – March 13, 1901) was the 23rd president of the United States , serving from 1889 to 1893. He was a member of the Harrison family of Virginia —a grandson of the ninth president, William Henry Harrison , and a great-grandson of Benjamin Harrison V , a Founding Father . A Union army veteran and a Republican, he defeated incumbent Grover Cleveland to win the presidency in 1888."
    },
    {
      "id": "Q35686",
      "first_name": "Rutherford",
      "last_name": "Hayes",
      "birth_date": "1822-10-04",
      "death_date": "1893-01-17",
      "place_of_birth": "Delaware",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Rutherford_B._Hayes",
      "start_mandate": "1877-03-04",
      "end_mandate": "1881-03-04",
      "Bio": "Rutherford Birchard Hayes ( / ˈ r ʌ ð ər f ər d / ⓘ ; October 4, 1822 – January 17, 1893) was the 19th president of the United States , serving from 1877 to 1881. He served as Cincinnati 's city solicitor from 1858 to 1861 and was known as a staunch abolitionist who defended refugee slaves in court proceedings. At the start of the Civil War, Hayes left a fledgling political career to join the Union army. He was wounded five times, most seriously at the Battle of South Mountain in 1862. Hayes earned a reputation for bravery in combat, rising in the ranks to serve as brevet major general. After the war, he was a prominent member of the \" Half-Breed \" faction of the Republican Party . Hayes served in Congress from 1865 to 1867 and was elected governor of Ohio, serving two consecutive terms from 1868 to 1872 and half of a third two-year term from 1876 to 1877 before his swearing-in as president."
    },
    {
      "id": "Q36023",
      "first_name": "John",
      "last_name": "Coolidge",
      "birth_date": "1872-07-04",
      "death_date": "1933-01-05",
      "place_of_birth": "Plymouth Notch",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Calvin_Coolidge",
      "start_mandate": "1923-08-02",
      "end_mandate": "1929-03-04",
      "Bio": "Calvin Coolidge (born John Calvin Coolidge Jr. ; / ˈ k uː l ɪ dʒ / KOOL -ij ; July 4, 1872 – January 5, 1933) was the 30th president of the United States , serving from 1923 to 1929. A Republican lawyer from Massachusetts , he previously served as the 29th vice president from 1921 to 1923, under President Warren G. Harding , and as the 48th governor of Massachusetts from 1919 to 1921. Coolidge gained a reputation as a small-government conservative , with a taciturn personality and dry sense of humor that earned him the nickname \" Silent Cal \"."
    }
  ]
}

#print(leaders_by_country)

# this isn't working, obviously. 

with open("test.csv", "w+", newline="", encoding="utf-8") as f:
    fieldnames = ["id",
                  "first_name",
                  "last_name", 
                  "birth_date", 
                  "death_date",
                  "place_of_birth",
                  "wikipedia_url", 
                  "start_mandate", 
                  "end_mandate", 
                  "Bio"
                  ]
    records = json.load(leaders_by_country)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in records:
        #writer.writerow(row)
        try:
            writer.writerow(row)
        except NameError:
            print("got a null, keep going")
            continue
    



def save_leader_by_country_with_switch(format=json):
    if format == "json":
            with open("leaders.json", "w") as leaders_json:
                json.dump(leaders_by_country, leaders_json, indent=2, ensure_ascii=False)
            with open("leaders.json", "r") as file:
                print(json.load(file))
    else: 
        pass
        