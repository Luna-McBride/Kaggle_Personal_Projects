# BigQuery_US_Name_Exploration--Kaggle

![me](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/BigQuery/BigQuery_US_Name_Exploration/Me.png)

The Dataset: https://www.kaggle.com/datagov/usa-names

The Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/bigquery-us-name-exploration

My Kaggle: https://www.kaggle.com/lunamcbride24

This project was made to explore the government's name dataset via BigQuery. I ran through various queries, including the most popular names by state, the most popular/unpopular names by gender, and I even looked for my own name. I then went on to put these into datasets and use Matplotlib to plot several of them.

The Plots:

![male210](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/BigQuery/BigQuery_US_Name_Exploration/MaleDistribution210.png)

* I should first emphasize the proportionality of the names is relative to the size considered. This is a graph of 210 male names (with the names removed so they do not look like a black blob). The front runners are pretty obvious, but take up a small chunk given the total 210 names in this graph. When I talk about names being proportionate, keep in mind I mean those of the specified graph and not compared to a monstrosity like this.

![male10](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/BigQuery/BigQuery_US_Name_Exploration/MaleDistribution10.png)

* These are the top 10 male names overall since 1910. They are pretty proportionate to one another with a fairly even spread between the biggest names.

![female10](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/BigQuery/BigQuery_US_Name_Exploration/FemaleDistribution.png)

* These are the top 10 female names since 1910. The names are pretty even with exception to Mary, which takes up a pretty large chunk. I was initially fooled by the overall popular names list since so many male names popped up before a single female name (being Mary) and assumed male names were just unoriginal and had a small spread. The name Mary proved that wrong, as the female names did indeed have a larger spread. Mary just took up the most female name space proportionally.

![malestate](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/BigQuery/BigQuery_US_Name_Exploration/MaleStateDistribution.png)

* The top name by state proved to have another fairly even spread for males, specifically between the names James, John, Robert, and Michael. Of course there was a bit of a skew toward James and John, but it was relatively small.

![femalestate](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/BigQuery/BigQuery_US_Name_Exploration/FemaleStateDistribution.png)

* The top female names by state, on the other hand, was essentially just Mary. Nevada and California tried to throw their Jennifer card into play, but Mary dominated with every other state having it as their top name since 1910. Look at all those Marys.
