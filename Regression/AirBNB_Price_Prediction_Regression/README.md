# AirBNB_Price_Prediction_Regression--Kaggle

![Map](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Regression/AirBNB_Price_Prediction_Regression/locationMap.png)

Dataset Used: https://www.kaggle.com/kritikseth/us-airbnb-open-data

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/airbnb-price-prediction-regression/notebook

My Kaggle: https://www.kaggle.com/lunamcbride24

This project attempts to predict prices for AirBNB locations using random forests. This is achieved by not only looking at the overall data, but the accuracies by major area in the dataset. The areas included in the dataset is shown by the map above. Alaska is not shown since Alaska was not included in the dataset. I congregated them by major area (since this data was mixed with counties and cities, which was pretty weird). The count graph and the proportion pie chart are shown below.

![CountGraph](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Regression/AirBNB_Price_Prediction_Regression/locationCount.png)

![ProportionGraph](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Regression/AirBNB_Price_Prediction_Regression/locationProportion.png)

When it came to training the model, I removed the name, hostName, neighborhood, and lastReview field. The name, hostName, and lastReview fields took up too much space when treated as categorical by pandas' to_dummy function. As for the neighborhood variable, the to_dummies function could handle it, but it increased the fit time by nearly an hour on the overall data and only added at most 3% to the accuracy. I had set forests up to work on the overall data, then separately on each major area's data to compare performance. Thus, I was willing to trade that small accuracy boost for not taking hours to run.

![accuracies](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Regression/AirBNB_Price_Prediction_Regression/accuracyByArea.png)

Next, I ran the data through random forests. In all cases, the root mean square error remained above 1. As for accuracy, the overall data got to about 60%, while the accuracy by area stayed anywhere between 40 and 70 percent (shown above). This was likely caused by AirBNB's hosts deciding the price, meaning that deciding factors could not remain consistent. The prices ranged from $1 to $24999, so there was also a large range of prices to try and predict. I made a graph to show the variance to show this, where I subtracted the prediction from the true value and plotted them (shown below). The predictions tended to undershoot it, given by the majority being positive values. The majority of the values were off by a range of -300 < x < 500 (shown by the black horizontal lines).

![variance](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Regression/AirBNB_Price_Prediction_Regression/Variance.png)

The forest ended up deciding that the columns roomType_Entire home/apt, longitude, latitude, id, and monthlyReviews were most important to getting its price accuracy. The least surprising ones were the number of monthly reviews and the room type being the entire house, as people like privacy and the more reviews per month, the more people are staying at the location. The ID was a bit interesting, since it meant the individual house was considered important by the forests. That likely means there is something inherent about the properties themselves that could not be captured here otherwise, such as pictures. The most surprising aspect here was how high the latitude and longitude were here, or rather that the city/major area was not high while these were. I assume this means that the latitude and longitude pick up price data over multiple major areas that are closer together yet more expensive, while the individual area had varied prices within themselves.
