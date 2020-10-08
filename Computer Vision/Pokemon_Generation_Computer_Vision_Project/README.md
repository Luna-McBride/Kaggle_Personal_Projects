# Pokemon_Generation_Computer_Vision_Project--Kaggle

![BoarderPokemon](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Pokemon_Generation_Computer_Vision_Project/Pokemon.png)

Used Data: https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types?select=pokemon.csv

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/pokemon-generation-computer-vision-project

My Kaggle: https://www.kaggle.com/lunamcbride24

This project takes images of every Pokemon in generations 1-7 and classifies them based on their generation. This was meant as a rebutal to the people who hold the sentiment that all new pokemon are bad.

This was originally meant to use Keras to not only classify, but also show a classification report for the prediction. This, however, failed when I continuously used all available Kaggle RAM, even when the test split was only 0.01 (that comes to about 9 images). Despite this, I can still gain insight from the evaluation accuracy, which came to 85.7% accuracy. This accuracy does not just mean it is predicting new versus old at 85.7% accuracy, but it is predicting the exact generation the Pokemon came from at 85.7% accuracy (that is 7 different choices) by the Pokemon's image alone. This means there is something distinct in the designs of these pokemon for each generation that the generation it came from 85% of the time. This means there is no true credence to the "new" versus "old" argument, but that each generation is individually unique with its Pokemon designs. I hope to try to do this again in the future when I find something that either negates or vastly lowered this memory problem in the predict function to truly see which generations it was better at identifying via a classification report, but at the moment, I would say this is a good find.

I would like to note the peak no matter what I did was 85.7%, so there might be something else notible here to take a look at. With the memory problems, however, I cannot build predictions on a 0.01 test split, let alone a full classification report to try and explore which generation it may be having trouble with.

![Train](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Pokemon_Generation_Computer_Vision_Project/Training.png)

![Train](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Computer%20Vision/Pokemon_Generation_Computer_Vision_Project/Testing.png)
