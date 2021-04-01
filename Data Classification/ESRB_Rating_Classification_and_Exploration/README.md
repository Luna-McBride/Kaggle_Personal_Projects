# ESRB_Rating_Classification_and_Exploration --Kaggle

![predict](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/ESRB_Rating_Classification_and_Exploration/Predictions.png)

The Dataset: https://www.kaggle.com/imohtn/video-games-rating-by-esrb?select=test_esrb.csv

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/esrb-rating-classification-and-exploration

My Kaggle: https://www.kaggle.com/lunamcbride24

This analysis utilized a dataset of video games, as well as their ESRB ratings to predict ratings on a test set with 83% accuracy. These predictions were based on descriptors the ESRB tends to mark on the games nexxt to the rating, such as alcohol use and blood. This dataset has more than 30 of these descriptors, so there is a lot that goes into these predictions. Below are three examples of descriptors, taken from the training dataset.

![blood](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/ESRB_Rating_Classification_and_Exploration/BloodTrain.png)

![sThemes](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/ESRB_Rating_Classification_and_Exploration/SThemesTrain.png)

![alUse](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/ESRB_Rating_Classification_and_Exploration/AlUseTrain.png)

All of these examples simply state the existance of these warnings, with 0 meaning the problem does not exist and 1 meaning the issue does exist. Every single one of these descriptors occur pretty rarely, hence why the "1" bar tends to be much smaller. The blood theme is much more common compared to the others, judging by how the "1" bar is comparatively taller, but that does not say much given how uncommon it still is.

![Accuracy](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/ESRB_Rating_Classification_and_Exploration/Accuracy.png)

![TopFeatures](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/ESRB_Rating_Classification_and_Exploration/TopFeatures.png)

The rating predictions were made using a random forest. The overall accuracy came to about 83%, with stronger accuracies for M and E games. The top features list shows that the key descriptors are having no major descriptors, along with blood, violence, and strong language. These are likely the strongest factors in distinguishing between E (for mild, suggestive, and no descriptors) and M (blood, blood and gore, and strong language) versus the middle tiers.

![predict](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/ESRB_Rating_Classification_and_Exploration/Predictions.png)

This lead to a prediction sheet like this. The whole test set is printed in the original notebook, but a quick runthrough shows that the most common mistakes were the rating predictions being off by one (such as M vs T or T vs ET). This is likely some inconsistency caused by the humans behind the ratings, who weigh different factors differently and may judge games differently based on the time or culture surrounding these judgements. Another important note is that the ET (Everyone 10+) rating was not established until 2005, which might be another issue (especially in the ET vs T rating tier).
