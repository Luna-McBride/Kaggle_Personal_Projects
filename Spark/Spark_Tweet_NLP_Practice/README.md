# Spark_Tweet_NLP_Practice--Kaggle

![SparkData](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Spark/Spark_Tweet_NLP_Practice/SparkData.png)

Data Used: https://www.kaggle.com/kazanova/sentiment140

Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/spark-tweet-nlp-practice

My Kaggle: https://www.kaggle.com/lunamcbride24

This project was used to work with PySpark in order to look through its libraries and understand its functions. This was originally meant to be a full tweet sentiment analysis, but Kaggle could not handle Spark, even for a random forest. The use case for Spark is pretty specific, so I understand a single "cluster" that is not equipped to handle its strengths would not do the best in the MLLIB functions. While this does work fine as a use case for Spark and its basic functionalities, I hope to find a different platform later on to try and levarage its strengths.

The contents of the project are pretty simple yet key functions required to use Spark. Downloading Spark, pulling in a CSV, null checks and cleaning, tweet cleaning, among other tasks. There is also a pipeline to handle tokenization, make vectors, and send to the random forest model. I have left that in and functions like the fit function to show the process, but, of course, Kaggle memory and computing constraints could not handle these functions, especially on this fairly large dataset. 
