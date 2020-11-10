# Time_Series_Amazon_Stocks--Kaggle

![Predictions](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/AmazonPredictions.png)

Dataset Used: https://www.kaggle.com/salmanfaroz/amazon-stock-price-1997-to-2020

The Project in Kaggle: https://www.kaggle.com/lunamcbride24/time-series-amazon-stocks

My Kaggle: https://www.kaggle.com/lunamcbride24

This project was made to practice time series and ARIMA practices. This is done using a dataset of Amazon stocks from May 15th, 1997 to July 31st, 2020. In the project, I prepared the data, looked for appropriate ARIMA values, validated the model with a 0.9 - 0.1 train test split, and ultimately predicted Amazon stocks.

The Process:

![Original](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/AmazonStock.png)

* The process started with graphing the stocks themselves (shown above). The data is a time series following a business day pattern on the opening price of the stocks. There were a couple missing days, such as holidays, so I made sure those were added and opened with the next day's opening price, as that logically would have been the price they opened with if they opened at all.

![StockSeasonal](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/AmazonSeasonal.png)

* I then followed processes to check if the data was stationary or not. This includes a seasonality report (above). Of course the seasonal graph itself looks like a blob given the long time frame. The important factor is the trend, which is not stationary. With this and ADFuller testing coming to a flat 1.0 significance, it was easy to tell this needed to be made stationary.

![Stationary](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/AmazonStationary.png)

* The obvious next step was to make it stationary, given all the stationary tests. This was done by taking the log of the set and subtracting a shifted version of the log set (following this video: https://www.youtube.com/watch?v=e8Yw4alG16Q). There is a lot of wiggle given the nature of this stock data, but ADFuller showed it was stationary (with a P significance value so far below 0 sometimes Kaggle denotes it in scientific notation with an exponent of -22, while at other times it just says 0).

![StationarySeasonal](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/StationarySeasonal.png)

* This is further exemplified by the trend above, which is relatively flat.

![Fitting](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/ForecastFitting.png)

* Next came the ARIMA model. I used the stationary set to fit the model in order to get a good idea about its forecasting. The above graph shows the predictions on the stationary model with the p, d, and q values I decided on. I made it very light so I could actually see the red forecast under the blue data, but it is still visible. The red forecast follows the stationary model pretty well, just with not as much variance and jumping around.

![Validation](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/ValidationForecast.png)

* With the parameters now firmly decided, I could now validate the model by splitting the data into training and testing sets. I decided on a 0.9 - 0.1 train test split in order to go far enough to capture the large general increase that started in the late 2010's. The test forecast (the green line above) then predicted the general trend of the data. This forecast is a good average line for the data up until 2020, which itself in an anomoly caused by Covid. Ignoring this anomoly, the ARIMA model looks to have predicted the test set very well.

![Predictions2](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Amazon_Stocks/AmazonPredictions.png)

* All that is left is to predict the future with the model. The image above (which is also the header image) looks 1000 stock days into the future to predict Amazon stocks. The predictions, shown in red, shows a generally flatter trend compared to the big jump during Covid. The confidence interval is also very wide to try and catch variance. This prediction seems pretty good given the previous data, but I should emphasize it is a prediction. There could very well be bigger spikes or dips as people try to go back to normal. The increased use and trust in the company could very well go back down once the virus has run its course. I would say this seems fair given trends and looking at the current world, but the post-covid world is a big factor that could sway these numbers. We will just have to see in time. 
