# Wind_Energy_Analysis_and_Prediction--Kaggle

![TTSOPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TenneTTSONullPred.png)

The Dataset: https://www.kaggle.com/jorgesandoval/wind-power-generation

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/wind-energy-analysis-and-prediction

My Kaggle: https://www.kaggle.com/lunamcbride24

This collection of datasets covered wind energy produced by four German wind companies (50Hertz, Amprion, TenneTTSO, and TransnetBW). The data started as 4 separate CSV's, structured with dates as the rows and times on the columns (taken every 15 minutes). To work with this data the way I did, I had to "melt" the data so the rows were the combined date-time fields with a single column for the company. I then had to connect the four datasets into a single one with four columns, one per company. I also had to add rows for dates/times not represented by the dataset, filling them initially with 0 and replacing with null for comparision sake. The above image is an example to show the empty data, plus a prediction covering the dates when null dates were dropped (which shows how empty this dataset actually is). The initial data is below, which were all initially with null values filled with 0. I used this data to create ARIMA models to predict and forecast wind energy production.

![50Hertz](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/50Hertz.png)

![Amprion](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/Amprion.png)

![TTSO](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TenneTTSO.png)

![TransnetBW](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TransnetBW.png)

These are all the initial values in the dataset, taken every 15 minutes. This makes for a total of 67296 rows. Transnet also has a huge spike right around February 2019. Both of these issues are fixed by collecting the dates by day instead of 15 minutes, which has been done as a baseline for all prediction data moving forward, as there was no way to create a single ARIMA model of this size without using all the memory Kaggle allows for. For a frame of reference, 67296 rows becomes 701 rows when only looking at the values (mean of the values, rather) daily.

![50Hertz0Pred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/50Hertz0Pred.png)

![Amprion0Pred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/Amprion0Pred.png)

![TTSO0Pred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TenneTTSO0Pred.png)

![TransnetBW0Pred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TransnetBW0Pred.png)

I next got the P, D, and Q values to build ARIMA models, which were used to see what the models would predict for the data based (filled with 0). This created predictions the followed the data pretty closely, but zig zagged aroud 0 for unknown data.

![50Hertz0Forecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/50Hertz0Forecast.png)

![Amprion0Forecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/Amprion0Forecast.png)

![TTSO0Forecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TenneTTSO0Forecast.png)

![TransnetBW0Forecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TransnetBW0Forecast.png)

This created forecasts that dipped pretty low below 0, since the models had low knowledge on what was going on with the 0 data. It also resulted in lower peaks, as many data points were 0. I was not satisfied with this outcome, so I decided to have the models drop null values instead.

![50HertzNullPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/50HertzNullPred.png)

![AmprionNullPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/AmprionNullPred.png)

![TTSONullPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TenneTTSONullPred.png)

![TransnetBWNullPred](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TransnetBWNullPred.png)

For this prediction, the models predicted an approximate connecting line between data points when the data became empty.

![50HertzNullForecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/50HertzNullForecast.png)

![AmprionNullForecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/AmprionNullForecast.png)

![TTSONullForecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TenneTTSONullForecast.png)

![TransnetBWNullForecast](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Time%20Series/Wind_Energy_Analysis_and_Prediction/TransnetBWNullForecast.png)

This resulted in less negative values and better forecasts in its peaks. It would be better if this data was included in the dataset, of course, but this is definitely a better forecast given the data than if nulls are replaced with 0.
