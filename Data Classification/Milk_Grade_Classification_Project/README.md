# Milk_Grade_Classification_Project--Kaggle

![grades](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/Grade.png)

The Dataset: https://www.kaggle.com/prudhvignv/milk-grading

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/milk-grade-classification-project

My Kaggle: https://www.kaggle.com/lunamcbride24

This project takes a list of characteristics to distinguish milk between good, moderate, and bad with classification models. These models were able to classify with near 100% accuracy. This takes into account the milk's pH, Temperature (please note this is spelled wrong in the data), Colour, Fat Content, Turbidity (fogginess), Odor, and Taste to distinguish between a bad, moderate, and good milk. The good/moderate/bad itself is shown above. There are more more bad milks than good or moderate. The grades are not too different proportionally, so the classification model did not have many issues.

The Characteristics:

![range](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/Ranges.png)

* Ranged Values: These are the ones that have more specific values, like temperatures. These ranges show that bad milks have wider ranges of pH and Temperature, signifying these are likely important in distinguishing between good/moderate and bad milks. The Good and Moderate tend to have similar ranges, so it is fair to assume there are other characteristics more important in deciding a good and moderate. These will need to be looked at separately.

![fat](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/Fat.png)

![odor](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/Odor.png)

![taste](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/Taste.png)

![turbidity](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/Turbidity.png)

* The rest of these values are boolean, meaning they have a simple 0 for bad and 1 for good. They are all pretty even between good and bad, so the model is important in saying which ones are more substantial.

The Models:

I used two random forest models for this data. One is to look at the overall data, while the other is to look at the good/moderate split specifically. Those two appear pretty similar on the surface, so this second model is vital to labeling this distinction. Each model has a listed accuracy, classification report, and a list of the characteristics in order of importance.

![allgrades](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/AllChara.png)

* This is the model for the overall dataset. The pH, Temperature, and Odor were seen as most important to seeing a bad milk. The pH and Temperature were expected given the ranges above, but adding in the odor was a very important factor in my opinion. The lowest were taste and color, which is not surprising since if those went wrong, everything else has necessarily gone wrong.

![goodvmod](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Milk_Grade_Classification_Project/GoodvMod.png)

* This is the Good vs Moderate model. This was made by simply removing bad milk from the dataset. The lack of bad data made this one not operate at 100%, but it was very close. The most important variables were fat content and odor, which tells me these are the most important aspects when classifying a good milk versus a moderate milk. The least important were temperature and taste, which also makes sense. The temperature barrier was already surpassed when classifying bad milk. The taste, once again, goes wrong when everything else goes wrong, so it is a relatively poor indicator of quality.
