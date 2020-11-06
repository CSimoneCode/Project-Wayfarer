DROP TABLE IF EXISTS city CASCADE;

CREATE TABLE city (
    id integer NOT NULL,
    name text NOT NULL,
    country text NOT NULL,
    region text NOT NULL,
    language text NOT NULL,
    blurb text NOT NULL
);

INSERT INTO city VALUES(1,"Cairo","Egypt","Northern Africa","Arabic","Cairo is growing fast in popularity, thanks to the region becoming more stable. Oh, and those famous pyramids of course.");
INSERT INTO city VALUES(2,"Athens","Greece","Europe","Greek","Athens is a super base from which to explore the Greek islands and ancient architecture of Europe.");
INSERT INTO city VALUES(3,"Moscow","Russia","Eastern Europe","Russian","Moscow is becoming a popular city to visit, with tourists flocking over for the beautiful squares and churches.");
INSERT INTO city VALUES(4,"Florence","Italy","Europe","Italian","Florence is one of the most beautiful cities in Italy, with culture, amazing food and scenery all rolled into one.");
INSERT INTO city VALUES(5,"Dublin","Ireland","Western Europe","English","Dublin may be small, but it’s also mighty. The Irish capitol packs a lot into its city and is a great place to spend a weekend.");
INSERT INTO city VALUES(6,"Chennai","India","South Asia","Hindi","Chennai on the Bay of Bengal in eastern India, is a hugely busy IT and tech hub and will continue to rise.");
INSERT INTO city VALUES(7,"Orlando","United States","North America","English","Home to Disney World and plenty of sunshine, Orlando is a winner with families and couples alike.");
INSERT INTO city VALUES(8,"Madrid","Spain","Europe","Spanish","Spain’s central capital is known for its rich collection of European art and elegant streets.");
INSERT INTO city VALUES(9,"Jaipur","India","South Asia","Hindi","Jaipur – the ‘Pink City’ – is an exciting mix of classic architecture, bustling street markets and a 16th-century Royal Palace.");
INSERT INTO city VALUES(10,"Venice","Italy","Europe","Italian","Venice is a stunning city of shaded Piazzas, romantic boat trips through the canals and luxurious hotels.");
INSERT INTO city VALUES(11,"Riyadh","Saudi Arabia","Middle East","Arabic","Saudi Arabia’s capital and main financial hub, has distinct landmarks and is becoming an exciting hub.");
INSERT INTO city VALUES(12,"Ho Chi Minh City","Vietnam","Southeast Asia","Vietnamese","Formerly Saigon, this southern Vietnamese city is a metropolis of history and culture.");
INSERT INTO city VALUES(13,"Johannesburg","South Africa","Africa","English","Johannesburg is the largest city in South Africa and one of the 50 largest urban areas in the world.");
INSERT INTO city VALUES(14,"Johor Bahru","Malaysia","Southeast Asia","Malay","With a bridge from the Straits of Johor connecting it to Singapore, this city is a great place to explore Asia from.");
INSERT INTO city VALUES(15,"Berlin","Germany","Europe","German","Germany’s coolest city, Berlin enjoys steady levels of tourism from visitors across the world who want to experience its unique atmosphere.");
INSERT INTO city VALUES(16,"Cancun","Mexico","North America","Spanish","Popular for Spring Break for US students, Cancun is also an ideal honeymoon destination.");
INSERT INTO city VALUES(17,"Vienna","Austria","Europe","German","Vienna is a charming city, where legendary figures such as Mozart, Beethoven and Sigmund Freud all called home.");
INSERT INTO city VALUES(18,"Denpasar","Indonesia","Southeast Asia","Indonesian","This is the largest city of the island of Bali, making it a trendy place for travellers to visit while they explore the Indonesian islands. One of the most visited cities on the planet.");
INSERT INTO city VALUES(19,"Milan","Italy","Europe","Italian","The stylish fashion capital has incredible cathedrals, green city parks and a thriving food and drink scene.");
INSERT INTO city VALUES(20,"Barcelona","Spain","Europe","Spanish","Home to Gaudi’s iconic works of art, a scenic beachfront and cosy tapas bars, it’s no wonder Barcelona appeals to so many.");
INSERT INTO city VALUES(21,"Osaka","Japan","East Asia","Japanese","Come to Osaka for its modern architecture, nightlife and hearty street food.");
INSERT INTO city VALUES(22,"Agra","India","South Asia","Hindi","The closest city to the Taj Mahal, millions of people make the trip to see this majestic wonder every year.");
INSERT INTO city VALUES(23,"Las Vegas","United States","North America","English","The party city shows no sign of slowing down, with casinos, upscale boutiques and luxury hotels all part of its pull.");
INSERT INTO city VALUES(24,"Los Angeles","United States","North America","English","LA is a city for fitness fans,  as well as celebrity hunters – or celeb wannabes – who hope to catch sight of a star.");
INSERT INTO city VALUES(25,"Shanghai","China","Asia","Mandarin","Shanghai, on China’s central coast, is the country’s biggest city and a global financial hub.");
INSERT INTO city VALUES(26,"Pattaya","Thailand","Southeast Asia","Thai","Once a quiet fishing village, Pattaya is now popular for its beaches, cabaret bars and 24-hour clubs.");
INSERT INTO city VALUES(27,"Seoul","South Korea","East Asia","Korean","Seoul is a fun city where you can experience K-Pop, modern skyscrapers, high-tech subways and pop culture. A magic place and one of the most visited cities in the world.");
INSERT INTO city VALUES(28,"Amsterdam","Netherlands","Europe","Dutch","A wonderful city to explore – by bike, tram or foot – Amsterdam is a consistently popular choice.");
INSERT INTO city VALUES(29,"Miami","United States","North America","English","The Miami area offers something for everyone – trendy nightlife, beaches, art galleries and world class food.");
INSERT INTO city VALUES(30,"Mecca","Saudi Arabia","Middle East","Arabic","Islam’s holiest city, (it’s the birthplace of the Prophet Muhammad and the faith itself), only Muslims are allowed to visit, and millions make an annual pilgrimage.");
INSERT INTO city VALUES(31,"Prague","Czech Republic","Europe","Czech","Nicknamed “the City of a Hundred Spires,” Prague is an affordable option for many young travellers.");
INSERT INTO city VALUES(32,"Mumbai","India","South Asia","Hindi","Mumbai is an exciting, busy city with a vibrant nightlife scene and colonial buildings.");
INSERT INTO city VALUES(33,"Guangzhou","China","Asia","Chinese","China’s third biggest city has internationally renowned restaurants, striking buildings and mountain views.");
INSERT INTO city VALUES(34,"Taipei","Taiwan","Asia","Mandarin","Come to Taipei for its busy shopping streets and lively street-food scene.");
INSERT INTO city VALUES(35,"Antalya","Turkey","Eastern Europe","Turkish","A popular Turkish resort city, Antalya continues to be a popular pick for holidaymakers looking to relax in the sun.");
INSERT INTO city VALUES(36,"Rome","Italy","Europe","Italian","Drink incredible wine, see the Vatican and the Colosseum in Italy’s must-visit city.");
INSERT INTO city VALUES(37,"Tokyo","Japan","East Asia","Japanese","Super busy but super exciting, Tokyo offers a look into the future of what every city could be like.");
INSERT INTO city VALUES(38,"Delhi","India","South Asia","Hindi","Made up of New Delhi and Old Delhi, this city never slows down. Enjoy the famous street food markets and buzz.");
INSERT INTO city VALUES(39,"Istanbul","Turkey","Eastern Europe","Turkish","Istanbul is the country’s economic, cultural and historic centre.");
INSERT INTO city VALUES(40,"Phuket","Thailand","Southeast Asia","Thai","The island of Phuket has beautiful beaches, a pretty Old Town and five-star resorts, so it’s easy to see why so many people want to visit.");
INSERT INTO city VALUES(41,"Shenzhen","China","Asia","Mandarin","Shenzhen links Hong Kong to China’s mainland and is a fantastic place to come to for designer shopping.");
INSERT INTO city VALUES(42,"Kuala Lumpur","Malaysia","Southeast Asia","Malay","Home to the famous Petronas Twin Towers, the skyline here at night is unforgettable. One of the worlds most visited cities is well worth a visit.");
INSERT INTO city VALUES(43,"New York City","United States","North America","English","Where to begin with the Big Apple? Each borough offers something different, from trendy Brooklyn to stylish Manhattan.");
INSERT INTO city VALUES(44,"Dubai","United Arab Emirates","Middle East","Arabic","Dubai has burst onto the tourism scene with fancy resorts, outstanding museums and shopping malls and a luxury vibe.");
INSERT INTO city VALUES(45,"Paris","France","Europe","French","The City Of Love will continue to be one of the world’s most loved holiday destinations. Its biggest attractions? The Eiffel Tower and great cuisine.");
INSERT INTO city VALUES(46,"Macau","China","Asia","Mandarin","With the nickname, “Las Vegas of Asia”, Macau is a mega-popular casino city where everything is OTT.");
INSERT INTO city VALUES(47,"Singapore","Singapore","Asia","English","Singapore is home to the world's most instagrammable hotel, an exciting mix of cultures and state-of-the-art restaurants.");
INSERT INTO city VALUES(48,"London","United Kingdom","Europe","English","Big Ben, the London Eye, Buckingham Palace and means London stays front and centre.");
INSERT INTO city VALUES(49,"Bangkok","Thailand","Southeast Asia","Thai","A global hub that’s the gateway to the rest of Asia, Bangkok is famous for its Buddhist shrines, street shopping and local food.");
INSERT INTO city VALUES(50,"Hong Kong","China","Asia","Mandarin","Hong Kong is a major shopping destination, famed for bespoke tailors and Temple Street Night Market.");