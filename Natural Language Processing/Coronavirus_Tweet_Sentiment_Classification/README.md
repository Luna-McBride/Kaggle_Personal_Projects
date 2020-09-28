# Coronavirus_Tweet_Classification--Kaggle

![Accuracy](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Coronavirus_Tweet_Sentiment_Classification/Accuracy.png)

Dataset Used: https://www.kaggle.com/datatattle/covid-19-nlp-text-classification

My Kaggle: https://www.kaggle.com/lunamcbride24

This project was made following the concepts in the NLP course on Kaggle. It uses Python, Spacy, and Pandas to analyze tweet data, classifying it by how negative or possitive it was. The max accuracy came to 76% at batches of 10 with a loss of 17. This was definitely a good learning experience, but spacy is pretty difficult to find information on when struggling. It is also pretty restrictive when it comes to access to its optimizer and model. I hope to work on another project using the items that seemed more prominent and powerful even when trying to search for spacy (most likely NLTK and Keras), but I will look into them first beforehand. The tweet cleaning from the project, however, will be quite valuable for further tweet analysis in the future.

This project can be segmented into three key portions, being dataframe cleaning, tweet cleaning, and the spacy model. Dataframe cleaning constituted of some basic null checks, as the other items were not as much of a focus in this project. The tweet cleaning included removing @'s, taking some HTML elements, removing links, among other element cleaning. I also removed clean tweets that became empty in the cleaning process, as a blank string tells nothing about the sentiment. The spacy model was the hefty portion, being choosing labels, training and testing the model, and other tweaks to try to work around the pretty restrictive model. I probably could have done some more exploratory analysis, but I decided that would not be the focus.
