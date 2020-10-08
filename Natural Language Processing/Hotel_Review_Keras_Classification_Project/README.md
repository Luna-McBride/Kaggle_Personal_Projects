# Hotel_Review_Keras_Classification_Project--Kaggle

![Examples](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Hotel_Review_Keras_Classification_Project/ExampleSentence.png)

Used Data: https://www.kaggle.com/andrewmvd/trip-advisor-hotel-reviews

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/hotel-review-keras-classification-project

My Kaggle: https://www.kaggle.com/lunamcbride24

This project processes hotel review data and classifies their ratings via Keras. This was meant as a response to my Coronavirus Tweet Classification Project, which used Spacy entirely, took an hour to fit, and got an accuracy of 76%. There was not much cleaning that was needed for this dataset, so the comparison is mostly in regard to tokenization and model training. 

I would like to acknowledge some differences before going into the comparison. The Keras uses reviews instead of tweets, which tend to be longer than tweets and have a much larger character limit. The tweet data also had a more even distribution of classifications while the hotel reviews had a heavy bias toward positive reviews, as shown below. This is to emphasize that this fight is not necessarily fair going into the comparison, but these differences show the strengths Keras has.

![Ratings](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Hotel_Review_Keras_Classification_Project/Ratings.png)

The tokenization was very different between Spacy and Keras. Spacy held the tokens as words in their own special format while Keras held the words numerically with the need for padding to normalize the size, which is shown in the image at the top of the readme. While it looks better to me, a human, to see the words as words, I understand that this portion may have been part of the equation to increasing speed.

As for the models themselves, Keras also took an hour to fit the model. However, as acknowledged previously, this data was larger per individial review, which shows how powerful Keras was to shorten this fitting to an hour. The training and testing models are shown below, but the fact the first epoch held a better accuracy than the spacy model got total is pretty nice.

![Training](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Hotel_Review_Keras_Classification_Project/TrainingAccuracy.png)

![Testing](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Hotel_Review_Keras_Classification_Project/TestingAccuracy.png)

As for the overall stats, the below classification report shows how the heavy positive bias played into the classification process. There were no neutral values guessed correctly, which is understandable due to its small size and how shaky defining a text as neutral is, even for a human due to bias. Even so, the Keras model ended up doing really well overall all things considered. This definitely beats out Spacy's model, even without doing crazy hyperparameter tweaking and adding more layers. It appears Keras is the way to go when it comes to NLP modeling in the future.

![Report](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Hotel_Review_Keras_Classification_Project/stats.png)
