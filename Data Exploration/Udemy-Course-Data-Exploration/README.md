# Udemy_Course_Data_Exploration--Kaggle

![cloud](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/CourseCloud.png)

The Dataset: https://www.kaggle.com/jilkothari/finance-accounting-courses-udemy-13k-course

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/udemy-course-data-exploraton

My Kaggle: https://www.kaggle.com/lunamcbride24

This project explores a dataset of Udemy Financial Courses and their stats (subscriber count, price, etc). I also compared various stats to the ratings and price. Prices are in USD after being converted from Indian Rupees at the current conversion rate of rupee * 0.014 = usd.

The Analysis:

![cloud](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/CourseCloud.png)

* After cleaning and null checking, I started by building a word cloud to see the most common words in the titles (both above and as the header image). This is a financial dataset, so words like business and trading being big make sense. This is also a learning platform, so having level words (beginner, advanced) and words relating to courses also makes sense. The interesting part came in words like Amazon and Bitcoin, showing that this dataset also includes items for personal financial decisions, data analysis, and perhaps even some dev-ops (given Amazon Web Services).

![lecrate](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/LecturevsRating.png)

* Next I compared rating to various other variables, starting with lecture number. I had assumed the lecture number would assume a heaftier course, and thus a higher rating. This was true after going above 200 lectures, but the trend is pretty loose even after that point (the higher rating being above 3 stars after 200 lectures).

![test](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/TestvsRating.png)

* Given the connection with rating and lecture number, I assumed providing higher amounts of practice tests would give a similar result. This ended up being true, but in an even looser connection than the lecture number. This tells me that overall content amount is at play in giving a higher rating, but does not directly describe the quality of the course.

![priceRate](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/PricevsRating.png)

* I followed that up by comparing the rating with the price. The rating was a bit higher generally with a higher price,  but not by a significant margin. I would say the price is not necessarily an indicator of quality in this case like it would be in most other instances.

![reviews](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/ReviewsvsRating.png)

![subcount](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/SubCountvsRating.png)

* The last metrics I looked at versus reviews were what I would call the Popularity Metrics, being review count and subscriber count respectively. These are the indicators of interaction, so it would make sense that they would point to a good course. This ended up being correct, given that both of these created a centralized ray of ratings between 4 and 5 for review counts above 5000 and subscriber counts above 50000. This tells me that if I want to look for a good Udemy course, the best indicator would be review and subscriber counts either around or above those values.

![lecprice](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/LecturevsPrice.png)

* After all these rating metrics, I decided to compare lecture count and price to see if course bulk contributed to price. The answer was, surprisingly, not really. All of the different price points appear to have similar lecture numbers. This gives adds more evidence to the idea that the price does not indicate the quality that I brought up above.

![top](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Data%20Exploration/Udemy-Course-Data-Exploration/TopCourses.png)

* All of this analysis come to one final question: which courses are the best? I decided to answer this by taking the review count given its high correlation with rating (I could have used subscriber count instead, but both of these come to a similar conclusion) as well as the rating to pick the best courses in the dataset. To do this, I removed all courses with fewer than 20000 reviews and a rating below 4.5. This left me with a list of 13 courses that I could say are likely the best (some of which shown above). The full list of courses were:

The Complete SQL Bootcamp 2020, Tableau 2020 A-Z, PMP Exam Prep Seminar, The Complete Financial Analyst Course 2020, Microsoft Power BI - A Complete Introduction, Beginner to Pro in Excel, Become a Product Manager, Microsoft Power BI - Up & Running With Power BI, Leadership: Practical Leadership Skills, The Complete Foundation Stock Trading Course, SQL - MySQL for Data Analytics and Business, The Ultimate Hands-On Hadoop, and Blockchain and Bitcoin Fundamentals.

These can be split into three categories, being tools for data analysis, leadership, and courses for personal financial gain. A lot of these make sense in a business environment, but I was a bit surprised by the Hadoop and Bitcoin entries. I expected Hadoop to be a bit more data science oriented than direct financial analysis, but I guess it makes sense. The Bitcoin entry, along with the stock market entry, were a lot more surprising to me because of the idea of those being a personal means of gaining money. I was going into this dataset thinking these courses would represent a professional trying to learn some missing skills, so these personal financial options were a bit surprising to me.
