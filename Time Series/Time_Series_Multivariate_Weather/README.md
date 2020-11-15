# Time_Series_Multivariate_Weather--Kaggle

![TempPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/TempForecast.png)

Dataset Used: https://www.kaggle.com/mastmustu/weather-analysis

The Project in Kaggle: https://www.kaggle.com/lunamcbride24/time-series-multivariate-weather

My Kaggle: https://www.kaggle.com/lunamcbride24

This project tests multivariate weather data from Estes Park to test time series functions like SARIMAX. 

I must acknowledge before anything else that the dataset had many missing days, including several months. These dates were also missing in the source this dataset used. I ended up filling them with the data for the day before the gap. This did not cause any prediction problems that I could see, but I feel the need to mention it since I could not just drop the dates and stitch the known data together. The vast amount of data makes it minimally visible in some visualizations, but it is important to acknowledge these sections.

The process:

![Variables](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/Variables.png)

* I started by cleaning the data, checking for nulls, and removing various unnecessary columns. These included columns like a second Dates column, rainfall (as these fields just built up to a monthly/yearly total instead of giving day by day information), and various min-max variables that I decided were covered better by their averages for this use case. I did keep the minimum and maximum temperatures however, as I wanted to see how Estes temperatures varied. In the end, I was left with the variables shown in the image above.

![MinMax](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/MinMaxTemp.png)

* This was also followed by a graph of the minimum and maximum temperatures on a plot together, as I wanted to see how the temperatures varied. This graph is also the most clear indicator of the data fillin, which is shown in the flat areas. The point it is most clear is early 2011, as that was caused by a gap for the majority of March followed by a gap of April. Even so, the gap is so small and can be averaged overshadowed by other years.

![Causality](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/Causality.png)

* The next thing I had to consider was how independent each variable was, shown in this causality chart. The variables are nearly entirely independent of one another, so models like VAR would not work here. This data is also inherently seasonal, which lead me to choose a SARIMAX model to handle this data.

![DewpointValid](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/DewpointValid.png)

* Once I had chosen the model, I decided to look at and predict Dewpoint and Temperature, starting with dewpoint. For these, I validated the data on a small subset, then had it predict a year worth of data. The above is the validation for the dewpoint, which had a mean absolute error of around 1.5. This model was pretty good at capturing the dewpoint, all things considered.

![DewpointPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/DewpointForecast.png)

* This is the predictions the model gave for the dewpoint. I specifically only showed a year of previous dewpoints to make the predictions more clear. I also compared this forecast to the data for yesterday on the source site. The forecast was a bit off, but this year's 11-13 dewpoint was lower than previous years.

![TempValid](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/TempValid.png)

* As for temperature, the model had similar preformance as the dewpoint. The variance was pretty low, but it was impressive how close it was.

![TempPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Time_Series_Multivariate_Weather/TempForecast.png)

* The predictions also seemed reasonable. The prediction for yesterday only varied by 3 degrees (F). I had to pull it again from the initial source since the data only went until July 31, 2020, but I feel the model did a good job at predicting this variable as well.
