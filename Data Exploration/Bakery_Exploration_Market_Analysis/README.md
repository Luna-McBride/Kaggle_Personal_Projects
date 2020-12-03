# Bakery_Exploration_Market_Analysis--Kaggle

![Seasonality](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/MonthlySales.png)

The Dataset: https://www.kaggle.com/mittalvasu95/the-bread-basket

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/bakery-exploration-market-analysis

My Kaggle: https://www.kaggle.com/lunamcbride24

This project was meant to explore the Bread Basket dataset. I looked through the number of sales per season, popular times for the bakery, which months are most popular, and found a list of items frequently bought together via the Apriori Algorithm.

The Exploration:

![Weekday](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/WeekdaySales.png)

* This bakery appears to be more popular on the weekends, but by a relatively small amount. This could mean it likely has a large customerbase that are slower and sit down, but the small difference between the days means there is also likely a subset that goes here for breakfast going to work/school.

![Seasonality](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/MonthlySales.png)

* This graph (which is both here and as the header image) shows that this bakery is particularly popular during the colder months, with particularly more sales in March and November. These months are when the weather starts warming up/ starts cooling down respectively, so I assume the nostalgia factor in regard to the cold weather and warm bread/coffee is at play.

![Time](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/PopularTimes.png)

![Time Variance](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/TimeVariance.png)

* The next set of graphs is the number of transactions occurring at certain times. The first one shows the data as a bar graph, and is thus makes the 10-2 peak time more apparent. It can be stated that the day of the week does cause variance from what was stated in the weekday section, but the variance is not enough to justify the strong peaks being during typical working hours. I could not find the actual restaurant when looking it up, but I am going to say it is likely fairly close to a college since it would make sense for college students to go to such an environment betweeen classes, which would account for the weekday traffic. 

* As for the variance graph, this shows the amount of orders done at a certain time across the whole dataset. I thought this was interesting to show, as it is neat to show how many orders were placed at the same time across many days. I imagine it like those blurry people when time speeds up in media, just with 70 people (plus or minus) standing and swaying slightly off from one while purchasing their items, segmented only by the date on the calendar.

![Items](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/PopularItems.png)

* This graph shows the most purchased items in the dataset. The top items are hot drinks and warm pastry-like items for the most part, which is likely why there is a whole lot more traffic in the colder months. Coffee is in first, beating out the second place contestant, bread, by a large margin. This gives more credence to both the "coffee on the way to work" and the "college student between classes" ideas I brought up previously given their connection to coffee. 

![Winter](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/PopularWinter.png)

![Summer](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/PopularSummer.png)

* I also compared the items sold in both the colder months and the warmer ones. This ended up with two nearly identical graphs, which gives additional credence to my statement about warm drinks and pastries bringing in traffic for the winter. They could possibly get more summer customers with a bit of a menu change with cooler items, but I cannot tell them how to run their business.

![Connections](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Bakery_Exploration_Market_Analysis/Connections.png)

* After the overall exploration, I used the Apriori algorithm to determine which items were sold most together with at least a 50% confidence level. Every single one has a connection to coffee, with the majority being a pastry or similar object. The highest was toast and coffee, which sounds like the most going-to-work type breakfast to ever exist. Other options included Juice and Hot Chocolate, which sound like cases where there were more than one people on the transaction (unless there is a large amount of people drinking juice with their coffee, which frankly sounds gross to me). 
