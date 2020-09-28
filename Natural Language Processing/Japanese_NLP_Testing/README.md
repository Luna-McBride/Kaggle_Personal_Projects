# Japanese_NLP_Testing--Kaggle

![Japanese Data](https://github.com/Luna-McBride/Japanese_NLP_Testing--Kaggle/blob/master/JapaneseProcessing.png)

Data Used: https://www.kaggle.com/daiearth22/ml-tweet

My Kaggle: https://www.kaggle.com/lunamcbride24

This project was done to test processing Japanese. I had processed tweets in the previous project and I thought of the idea after noticing this dataset while looking for more data to test with. The tweets themselves are pretty basic machine learning tweets, with common terms like programming and ability. The processing the Japanese, however, was the interesting part.

Getting the Japanese functionality to work was the first hard part. I tried getting the NLTK Japanese at first, but that just was not working. I ended up getting Spacy to work for Japanese processing, but it requred re-downloading the ja-core-media-large (the processor) to be redownloaded with each reload. Kaggle did not like to remember its existence otherwise.

Next came actual processing, which had to be reworked from my previous in order to fit Japanese. Functions like split() considered Japanese one large block (likely because there are no spaces), so I had to tokenize the text then get the word from the token to actually put it into a clean tweet column. Most Japanese punctuation is considered entirely different compared to the English counterparts, so those had to be added individually to the punctuation set to remove. 

I also noticed after processing that the Japanese stopwords list let slide words like けど and って, which I would consider stopwords due to their lack of independent meaning. けど, for example, can mean but or can be at the end of a phrase to imply another part of the sentence without outright saying it, both of which do not necessarily add context to a sentence for machine understanding in my opinion.

The final biggest issue I noticed was when trying to visualize some of the common words with matplotlib. Matplotlib does not recognize the Japanese characters, instead opting to replace each one with a little box (pictured below). This means when working with Japanese, exploratory graphs are not going to be as helpful. Instead, printing as python dictionaries for stuff like counts seems to be the best course of action, while numeric data and other typical use cases for matplotlib (like model accuracy and losses in machine learning) is fine to continue using it.

![Box Graph](https://github.com/Luna-McBride/Japanese_NLP_Testing--Kaggle/blob/master/JapaneseProcessingGraph.png)
