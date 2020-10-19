# R_Ramen_Data_Exploration--Kaggle

![Bottom Brands](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/bottomBrands.png)

The Dataset: https://www.kaggle.com/residentmario/ramen-ratings

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/r-ramen-data-exploration

My Kaggle: https://www.kaggle.com/lunamcbride24

The purpose of this project was to practice working with R. I only used it very lightly before now, so I thought it would be a good idea to do some exploratory analysis with it.

I looked through the ramen's rating, packaging style, country data, brands and their product counts, and compared brands based on their ratings. The following is a description of each graph just in case you do not want to look through my R code. Every description is above their corresponding images with exception to the header image's description, being just below:

* The graph at the top of the page is the brands with only a single product, of which there are 119 (with one on the end to show that number 120 has two products). I made it look rainbow so that it would not look like a blob, so it instead looks like a cool gradient, hence why I put it at the top of the page. 

* The next graph is the top five brands in terms of product numbers. There is a clear jump between Nissin and other companies, but that is likely due to its holding of other brands.

![Top Brands](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/Brands.png)

* This graph shows the distribution of ratings, including ones marked -1 if they were not rated. There is more higher ratings than lower ratings, so there is a slight skew. This does not factor into what I want to consider, however, so the skew does not change my analysis.

![Ratings](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/ratings.png)

* This graph shows the packaging styles of the different products. This ranges from the usual pack and cup to the strange canned ramen, which shows how there is more than just the typical styles.

![Styles](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/Styles.png)

* The next portion is a set of graphs, looking at the countrty markets for the ramen. One considers the top five countries in terms of ramen products while the other considers all the different countries. It does not list every country on the graph, but the wide range of countries that are included shows that the ramen industry is not purely condensed into Asia.

![Top Markets](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/topMarket.png)

![All Markets](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/Markets.png)

* The final set gives the mean of the product ratings to give a star rating to each brand. The first graph includes the top 20 brands by rating. This graph only includes 5 star ratings, however, as it is so much easier to maintain a 5 star rating if the company only has a product or two. That is where the second graph comes in, as this graph only considers brands with more than 20 products. The top 5 biggest brands by product number are also within this graph, but a few smaller local companies beat them out in ratings. 

![Top20](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/top20.png)

![Top20 Count20](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/R_Ramen_Data_Exploration/top20count20.png)
