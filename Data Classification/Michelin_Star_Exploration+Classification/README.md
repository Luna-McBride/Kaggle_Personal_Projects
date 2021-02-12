# Michelin_Star_Exploration+Classification--Kaggle

![all](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Michelin_Star_Exploration%2BClassification/Locations.png)

The Dataset: https://www.kaggle.com/jackywang529/michelin-restaurants

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/michelin-star-exploration-classification

My Kaggle: https://www.kaggle.com/lunamcbride24

For this project, I analyzed a dataset of Michelin Star Restaurants. This dataset specifically discluded Belgium, France, Germany, Italy, Japan, Luxembourg, Netherlands, Portugal, China, Spain, and Switzerland, so the key areas with many Michelin Star restaurants in the dataset are the UK and Scandanavia. The above image shows the overall locations for the dataset, while below is the dataset by star count (blue for 1, red for 2, and gold for 3).

![starCount](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Michelin_Star_Exploration%2BClassification/LocationsStars.png)

The dataset has very few 3 and 2 star restaurants. In fact, the ones that do exist are surprisingly spread out. The UK and Scandanavia may have the most present in the dataset, the ones that do exist appear to be 1 star. I do have two more images zooming into Europe and the UK/Scandanavia specifically (below), which makes this even more apparent.

![europe](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Michelin_Star_Exploration%2BClassification/LocationsEurope.png)

![uK](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Michelin_Star_Exploration%2BClassification/LocationsUK.png)

The key locations for 3 star restaurants are London and the various capital cities. This shows how few there actually are in the dataset, which means the classifier will most likely have difficulty working with its small numbers. The huge amount of restaurants in the UK is also especially interesting, as why would it be included with so many while countries like Luxembourg are specifically excluded, likely for their huge amounts?

![for](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Michelin_Star_Exploration%2BClassification/LocationsForest.png)

Next I decided to classify the restaurants to see if it could classify them by star count. As shown above, it could only pick up on one star restaurants. That lead to a 75%+ accuracy, but that is only because the amount of one star restaurants is that much higher than two or three star ones. That is to be expected from such an elite club, but I assume the difference would not be as stark if the dataset did not specifically eliminate the top countries.
