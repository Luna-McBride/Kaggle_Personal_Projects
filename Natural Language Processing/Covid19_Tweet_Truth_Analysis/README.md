# Covid19_Tweet_Truth_Analysis --Kaggle

![ValidationEx](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Covid19_Tweet_Truth_Analysis/ValidationExample.png)

The dataset: https://www.kaggle.com/elvinagammed/covid19-fake-news-dataset-nlp

The notebook in Kaggle: https://www.kaggle.com/lunamcbride24/covid19-tweet-truth-analysis/notebook

My Kaggle: https://www.kaggle.com/lunamcbride24

This analysis utilized Keras to determine the truth values of a dataset of tweets. The dataset contained 8 files, 3 of which I used. I used the training, validation, and test sets to create my model. I ended up ignoring the file for weights built by an ERNIE model, the files that were excel copies of the used sets, and a file that was another version of the test set with actual truth values. 

I started my analysis by checking for null values, getting labels into a simplified format for the machine, and fixing the tweets to remove unwanted aspects. This included getting rid of emojis, extra HTML elements, punctuation, and common stopwords using the Regular Expression, HTML, and NLTK libraries. Next, I used Keras' tokenization and padding tools to bring the tweets into a format that Keras could read quickly. I then created a neural network to make it learn, running through 3 times in about 30 minutes. I then built a dataframe to compare predictions for the validation set, as well as one for predictions on the test set.

![Model](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Covid19_Tweet_Truth_Analysis/Model.png)

![Validation](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Covid19_Tweet_Truth_Analysis/Validation.png)

The model, in its three epochs, came to an accuracy of 97% with a loss of 0.11. The validation came to an accuracy of 91%, meaning the model had a high recall on top of its accuracy. In the original kaggle, I let the entire dataframe for both the validation and test print for those curious, but below is a snippet to show the format.

![ValidationEx](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Covid19_Tweet_Truth_Analysis/ValidationExample.png)

![TestEx](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Natural%20Language%20Processing/Covid19_Tweet_Truth_Analysis/TestExample.png)

To abide by the machine's labeling conventions, 1 = real, 0 = fake. The validation set shows the true value and the prediction while the test set just shows the prediction. The tweet is printed next to the labels just for context sake.

This is an excellent use of natural language processing for the purpose of truth classification. I must emphasize, however, that telling truth is a lot more complex than the labels given. Some of these tweets have abiguous truth values for the context provided (mostly in cases where it is an issue of if someone actually said something). This model is proof that truth can be pulled in some contexts, but the bigger problem is getting the truth values for the values that are trained on. I assumed all of the truth claims were actually the truth for the sake of this analysis, but it is very possible that any one of these was incorrect. A model like this cannot pull external context from what is being shown to it, so it is necessarily relying on the dataset maker to be honest. This is definitely an interesting project, as it shows how important honesty is in the process.
