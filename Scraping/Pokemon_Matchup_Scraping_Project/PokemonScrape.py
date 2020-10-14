from selenium import webdriver #Make it so we can get into chrome
from selenium.webdriver.common.keys import Keys #Get the enter key for searches
from selenium.webdriver.common.by import By #Signify the method to search the html
from selenium.webdriver.support.ui import WebDriverWait #Wait until the page has loaded
from selenium.webdriver.support import expected_conditions as EC #Make sure there is a page presence before trying to use
import time #Allow for waiting a second
import pandas as pd #Open dataframes and hold data
import numpy as np #Use array functions common in pandas as well

#CheckForm: checks if there are additional forms in the type matchup list
#Input: the numeric values of where to check in the website
#Output: A boolean value, saying if that form is available
def checkForm(tabNum, form):
	#Check to see if it can open with this set of values
	try:
		driver.find_element_by_xpath("html/body/div/div/main/div/table[{}]/tbody/tr[{}]".format(tabNum, form))
		return True #Send back that it could be opened
	except:
		return False #Send back that it could not be opened

#AddPokemon: adds a pokemon and its type matchup data into one list
#Inputs: The pokemon name-number combo, any form name that needs to be attached,
#	and the type matchup list for the pokemon.
#Outputs: the list of the pokemon and its type matchups
def addPokemon(nameNum, toAppend, typeMatch):
	#Define the name and number to be pulled out separately
	#Just split would have worked if Mr. Mime did not exist
	name = ""
	number = ""

	#For each element in the split set
	for element in nameNum.text.split():
		if "#" in element: #If the element contains the number sign
			number = element #Set the number to the number element
		else: #If there is no number sign
			name = name + element #Append the element to make the name

	thisPokemon = [name + toAppend, number] #Create the list with the name and pokedex number
	matches = typeMatch.text.split() #Retrieve type matchup data for each type
	
	#For each matchup in the list of matchups
	for match in matches:
		thisPokemon.append(match) #Append the matchup to the pokemon list

	return thisPokemon #Return the pokemon with its type matchups



options = webdriver.ChromeOptions() #Get chrome options

#Ignore some errors
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

PATH = "C:\Program Files (x86)\chromedriver.exe" #Put the path to the chrome driver
driver = webdriver.Chrome(PATH, options = options) #Open the chrome driver

driver.get("https://serebii.net/") #Go to Serebii

searchBox = driver.find_element_by_name("q") #Find the searchbox element
searchBox.send_keys("bulbasaur") #Type in bulbasaur (The first pokemon in the dex)
searchBox.send_keys(Keys.RETURN) #Search the bulbasaur

try:
	#Wait until the page loads, then look for the first bulbasaur link (This html is pretty deep)
	main = WebDriverWait(driver, 10).until( 
		EC.presence_of_element_located((By.XPATH, "html/body/div/div/main/div/div/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div"))
	)
	
	time.sleep(1) #Wait a second
	main.click() #Click the bulbasaur link
	time.sleep(2) #Wait two seconds for page loading

	#Serebii opens up the result in a new tab, so this needs to swap tabs
	driver.switch_to.window(driver.window_handles[1]);
	
	#Wait until the page loads, and then click Gen 8 as that is the most recent gen
	gen = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.LINK_TEXT, "Gen VIII Dex"))
	)
	
	time.sleep(1) #Wait a second
	gen.click() #Click on the most recent generation tab
	time.sleep(5) #Wait a few more seconds to check loading

finally:
	isEnd = False #Variable to indicate we looked through all the pokemon
	pokeData = [] #The ultimate holder for all pokemon data

	#While we have not yet looked through all the pokemon
	while isEnd == False:
		time.sleep(1) #Wait a second to give the servers a break
		
		#Wait for the page to load fully
		main = WebDriverWait(driver, 10).until( 
			EC.presence_of_element_located((By.XPATH, "html/body/div/div/main/div/table/tbody/tr/td/table/tbody/tr/td[2]"))
		)

		#Get the name and pokedex number from the page
		nameNum = driver.find_element_by_xpath("html/body/div/div/main/div/table/tbody/tr/td/table/tbody/tr/td[2]")

		#Check if the html has the data I want in table 6 
		#It is table 6 for pokemon that have been in multiple generations
		#Table 5 otherwiae
		if checkForm(6, 3) == True:
			tabForm = 6 #Data is in table 6
		else:
			tabForm = 5 #Data is in table 5
		
		#Get the length of the number of elements
		#The elements increment in stages of 2, being form name and type matchup chart
		elements = len(driver.find_elements_by_xpath(f"html/body/div/div/main/div/table[{tabForm}]/tbody/tr"))

		#For each individual form each pokemon has
		for form in range(3, elements + 1, 2):
			#Append the regional variant name if it is not the base row 3
			if form > 3:
				#Set the form name to be appended to the pokemon name
				toAppend = driver.find_element_by_xpath("html/body/div/div/main/div/table[{}]/tbody/tr[{}]".format(tabForm, form - 1))
				toAppend = " " + toAppend.text.split()[2] + " " + toAppend.text.split()[3]
			
			#If we are representing the base form
			else:
				toAppend = "" #Append nothing

			#Get the type matchup data for the pokemon form
			typeMatch = driver.find_element_by_xpath("html/body/div/div/main/div/table[{}]/tbody/tr[{}]".format(tabForm, form))

			#Add the pokemon form to the dataset
			pokeData.append(addPokemon(nameNum, toAppend, typeMatch))

		#Try pressing the next pokemon button
		try: 
			time.sleep(3) #Wait a second to give the servers a break

			#Get the tab for the next pokemon button
			nextPokemon = driver.find_element_by_xpath("html/body/div/div/main/div/table[last()]/tbody/tr/td[2]/table/tbody/tr/td/a")
			
			#Click the button, avoiding the popup ad
			driver.execute_script("arguments[0].click();", nextPokemon)
		
		#If there is not a next pokemon
		except:
			isEnd = True #End the loop
	

	#Give a list of all types to be matched up to
	types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
	"Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
	"Dragon", "Dark", "Steel", "Fairy"]
	poke = ["Name", "Number"] #Give a list of name and number, which are key features
	data = poke + types #Add the name and number to the type matchups

	#Put the type matchup data into a pandas dataframe
	pokemon = pd.DataFrame(pokeData, columns = data)

	#Take the dataframe and send it to a CSV called "PokeTypeMatchupData"
	pokemon.to_csv(r"C:\Users\Luna.DESKTOP-PEBO18O\Dropbox\DataScience\PokeTypeMatchupData.csv", index = False)

	driver.quit() #Quit the driver when all is done.