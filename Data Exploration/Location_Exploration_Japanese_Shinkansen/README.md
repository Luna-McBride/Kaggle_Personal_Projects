# Location_Exploration_Japanese_Shinkansen--Kaggle

![all](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Location_Exploration_Japanese_Shinkansen/AllStation.png)

The Dataset: https://www.kaggle.com/japandata509/shinkansen-stations-in-japan

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/location-exploration-japanese-shinkansen

My Kaggle: https://www.kaggle.com/lunamcbride24

This is a small exploration of Shinkansen (bullet train) station data. This dataset did not come with coordinates, so I used the Nominatim geolocator to get the coordinates and Matplotlib Basemap to draw the map. This was not perfect, given it had various issues such as equating Asa, Japan with Asha, Russia. The overall set of stations is shown above. Below are two additional maps for some further exploration.

![bycompany](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Location_Exploration_Japanese_Shinkansen/ByCompany.png)

* This shows the stations by company/location. The Blue is Kyushu, the light blue covers between Kyushu and Osaka, the red covers between Osaka and Tokyo, the green covers Honshu north of Tokyo, and the black covers the connection to Hokkaido. There seem to be some Nominatim problems shown here, given a few blue Kyushu dots near Tokyo, but the whole appears to be a good representation of the stations. There are very few Hokkaido stations just to get into Hokkaido, which itself is very loosely connected itself compared to the very tightly connected Tokyo. The green stations cover a whole lot more area than the other areas, given the other ones are meant to connect major centers like Osaka to Kitakyushu and Kitakyushu to Kagoshima. The green, on the other hand, acts as a stronger train to connect harder to reach communities where regular trains are more difficult.

![NewvsOld](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Location_Exploration_Japanese_Shinkansen/NewvsOld.png)

* This one shows stations built before 2000 in black and stations built after in red. There are occasional additional stops on the main older lines, but the majority of newer stations were meant to connect previously unconnected communities. The whole Kyushu line, as well as a connection to Kanazawa and another one up through Aomori to Hokkaido, are entirely new. This tells me they focused on the main big city connections and smaller mountain Honshu communities before trying to connect the other two largest islands. I have to emphasize that this is at least partially out of convenience at that point, given Japan's scattered local airports in places like Sapporo and Kagoshima. The key population centers historically in Japan have been about level with Tokyo (Tokyo, Osaka/Kyoto, Hiroshima, Kitakyushu, etc), so it would make sense that they would wait to build that strong bullet train infrastructure to other areas until that key area was covered.
