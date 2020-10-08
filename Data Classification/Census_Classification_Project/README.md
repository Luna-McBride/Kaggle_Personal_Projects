# Census_Classification_Project--Kaggle

![Education](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Census_Classification_Project/Education.png)

Data Used: https://www.kaggle.com/johnolafenwa/us-census-data

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/census-classification-project

My Kaggle: https://www.kaggle.com/lunamcbride24

This project takes advantage of a US Census dataset to predict whether each person has a income either lower then or higher than 50K a year. The data was very messy with even column names messed up, so I cleaned each column above and beyond just filtering nulls. This included visualizing each column with Matplotlib, dropping redundant columns, and fixing columns to combine terms (For example, I combined the education levels for preschool, 1st-4th grade, 5th-6th grade, etcetera into a non-graduate category).

As for the classification, I initially went into this project expecting to do some regression work. After I did all the work for a logistic regression, I realized that though it has regression in the name, it is more akin to classification. So after I built the logistic regression and realized this, I decided to test it against other classification algorithms to see if I could get a better score. As can also be seen below as well, the logistic regression was one of the strongest contenders out of the classifiers I picked for this use case. It was only beaten by the gradient boosted classifier, which did not beat it by much. It seems all the classifiers had issue with classifying past 85%, which might be because there were so many more less than 50K than there were more than 50K earners. Even so, 85% accuracy is still a B, so it is pretty good. 

![Accuracies](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Classification/Census_Classification_Project/Accuracies.png)
