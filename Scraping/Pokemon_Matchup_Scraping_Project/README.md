# Pokemon_Matchup_Scraping_Project--Kaggle

![Types](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Scraping/Pokemon_Matchup_Scraping_Project/TypeFix3.png)

Used Data (The data is also in the PokeTypeMatchupData file in this repository): https://www.kaggle.com/lunamcbride24/pokemon-type-matchup-data

The Analysis Notebook in Kaggle: https://www.kaggle.com/lunamcbride24/pokemon-matchup-scraping-project

My Kaggle: https://www.kaggle.com/lunamcbride24

This project has two key parts, being scraping Serebii.net for Pokemon Type Matchup data and analyzing said data in a Kaggle Kernel for consistency. Please note that Serebii has lax scraping rules in their terms and Robots.txt (screenshot shown below). The only disallowed links are an admin page and crosswords, so I can assume with high certainty that that this site is alright with scraping their Pokemon data.

![Robots](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Scraping/Pokemon_Matchup_Scraping_Project/SerebiiRobots.png)

As for the actual scraping, this process took longer than I initially expected. Of course this is in tandem with having a busy week, but the overall process of working with Selenium and scraping the data took nearly a week. A lot of this was trying to handle edge cases, such as Pokemon with n different forms with different type effectiveness data as well as Pokemon with spaces in their names like Mr. Mime. There is still likely more cases that I can come back to and find later (such as Rotom Wash being Rotom Wash Rotom in the data), but I assume that is the nature of scraping. Also, the HTML for Serebii is pretty complex, creating more difficulty with xpaths. When all was said and done, the dataset contained 576 Pokemon and Pokemon forms, being the entire available Pokedex in Galar (Excluding the Crowned Tundra, which is not out yet and thus not represented in Serebii's most recent dex information). The Pokedex numbers are not currently sequential given the Pokemon not in the Galar dex as well as the different forms, so keep in mind that it would not be an appropriate index in this case.

There is also a test python file that only scrapes the last few Pokemon if you want to see a small version of the outcome. Just be sure to adjust the pathway for the Pandas to_csv function to see its outcome in the CSV.

As for the analysis, I mostly used sums and means to get a more general look at the data. As I was looking at the type effective data for every Pokemon, I thought it would be best to find the types that would have the highest sum/mean of the type matchup multipliers, as a higher number would mean more multipliers being a value of 1 or more, thus doing at least neutral damage per hit and thus being more versitile to whatever would come out, assuming equal probability for each Pokemon. This lead to Flying, Rock, and Fire types popping out as the most generally versitile when it comes to effectiveness, thus having a move of one of these types would be best to handle whatever comes out.

I then looked at both Super Effective and Not Very Effective multipliers specifically in a true false sort of way, having everything but the desired multipliers be set to 0 and the desired multipliers be set to 1. For Super Effective, that was multipliers higher than 1. For not very effective, that was multipliers lower than 1. 1 is neutral damage, so it was not considered in either case. Super Effective lead to a list of Fighting, Fire, and Ice on top, thus meaning those moves would hit for super effective damage most commonly. As for Not Very Effective, Grass, Bug, and Fighting came out on top. This put Fighting on both lists, giving the insight that it could be good or bad situationally, which makes sense since it does not effect Ghost type Pokemon. Grass being on top here does not mean it is necessarily bad, as it hits for super effective damage on water types, the most abundant type of Pokemon. Its inclusion here, however, means that it is less generally applicable to whatever is thrown out, which is the key factor in this case (all conclusions drawn from charts shown below, in the order general, super effective, not very effective).

![General](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Scraping/Pokemon_Matchup_Scraping_Project/General.png)

![Super](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Scraping/Pokemon_Matchup_Scraping_Project/SuperEffective.png)

![Not](https://github.com/Luna-McBride/Kaggle_Personal_Projects/blob/master/Scraping/Pokemon_Matchup_Scraping_Project/NotVeryEffective.png)
