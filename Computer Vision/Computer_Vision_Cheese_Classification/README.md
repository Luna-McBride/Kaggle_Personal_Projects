# Computer_Vision_Cheese_Classification--Kaggle

![fine](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/fineCheese.png)

The Dataset: https://www.kaggle.com/mathurinache/french-cheese-detection

The Test Dataset I Made for This: https://www.kaggle.com/lunamcbride24/cheese-test-csv

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/computer-vision-cheese-classification

My Kaggle: https://www.kaggle.com/lunamcbride24

For this project, I took advantage of a French cheese dataset to classify cheese images by their types. This dataset had 139 training images of two cheese types, being Fourme de Montbrison and Fourme D'Ambert. There are also 8 testing images, cropped out of 6 photos. The original dataset did not come with data for the test images, hence the one I made to suppliment it. I got pixel coordinates for cropping using Microsoft Paint and the cheese name by reverse image searching the original photos. 

This image set may be small, but I seem to have gotten a lot of leverage from it. I used keras to build this model, in which I got an accuracy of 99.3% on the training data at Epoch 50. The model was very similar to the Pokemon image classification project, but the main difference is the change in the use of Keras ImageDataGenerator objects. This lead to the test set being predicted with 100% accuracy (shown below). Ignore the lower image quality, as I specifically lowered the quality to make the images easier for Keras to process. 

![pred1](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction1.png)

![pred2](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction2.png)

![pred3](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction3.png)

![pred4](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction4.png)

![pred5](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction5.png)

![pred6](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction6.png)

![pred7](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction7.png)

![pred8](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Computer_Vision_Cheese_Classification/prediction8.png)
