from selenium import webdriver #Make it so we can get into chrome
from selenium.webdriver.common.keys import Keys #Get the enter key for searches
from selenium.webdriver.common.by import By #Signify the method to search the html
from selenium.webdriver.support.ui import WebDriverWait #Wait until the page has loaded
from selenium.webdriver.support import expected_conditions as EC #Make sure there is a page presence before trying to use
import time #Allow for waiting a second
import pandas as pd #Open dataframes and hold data
import numpy as np #Use array functions common in pandas as well

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

def checkForm(tabNum, form):
	#Check to see if it can open with this set of values
	try:
		driver.find_element_by_xpath("html/body/div/div/main/div/table[{}]/tbody/tr[{}]".format(tabNum, form))
		return True #Send back that it could be opened
	except:
		return False #Send back that it could not be opened

options = webdriver.ChromeOptions() #Get chrome options

#Ignore some errors
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

PATH = "C:\Program Files (x86)\chromedriver.exe" #Put the path to the chrome driver
driver = webdriver.Chrome(PATH, options = options) #Open the chrome driver

driver.get("https://www.serebii.net/pokedex-swsh/eternatus/") #Go to Serebii

#galar = driver.find_element_by_xpath("html/body/div/div/main/div/table[6]/tbody")
#nameNum = driver.find_element_by_xpath("html/body/div/div/main/div/table/tbody/tr/td/table/tbody/tr/td[2]")
#number, name  = nameNum.text.split()
#print(galar.text.split())
#toAppend = name + " " + galar.text.split()[2] + " " + galar.text.split()[3]
#thisPokemon = [toAppend, number]

#print(len(driver.find_elements_by_xpath("html/body/div/div/main/div/table[6]/tbody/tr")))

isEnd = False
pokeData = []
time.sleep(1) #Take a second to breath and not overwhelm servers

#While we have not yet looked through all the pokemon
while isEnd == False:
	time.sleep(3) #Take a second to breath and not overwhelm servers

	main = WebDriverWait(driver, 10).until( 
		EC.presence_of_element_located((By.XPATH, "html/body/div/div/main/div/table/tbody/tr/td/table/tbody/tr/td[2]"))
	)
		#Get the name and pokedex number from the page
	nameNum = driver.find_element_by_xpath("html/body/div/div/main/div/table/tbody/tr/td/table/tbody/tr/td[2]")

	if checkForm(6, 3) == True:
		tabForm = 6
	else:
		tabForm = 5
		
	elements = len(driver.find_elements_by_xpath(f"html/body/div/div/main/div/table[{tabForm}]/tbody/tr"))

	for form in range(3, elements + 1, 2):
			#Set the regional variant to be added (plus add the region to its name)
		if form > 3:
			toAppend = driver.find_element_by_xpath("html/body/div/div/main/div/table[{}]/tbody/tr[{}]".format(tabForm, form - 1))
			toAppend = " " + toAppend.text.split()[2] + " " + toAppend.text.split()[3]
		else:
			toAppend = ""
		typeMatch = driver.find_element_by_xpath("html/body/div/div/main/div/table[{}]/tbody/tr[{}]".format(tabForm, form))

			#Add the regional variant
		pokeData.append(addPokemon(nameNum, toAppend, typeMatch))

		
	try: 
		time.sleep(1)
		nextPokemon = driver.find_element_by_xpath("html/body/div/div/main/div/table[last()]/tbody/tr/td[2]/table/tbody/tr/td/a")
		driver.execute_script("arguments[0].click();", nextPokemon)
	except:
		isEnd = True

types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
"Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
"Dragon", "Dark", "Steel", "Fairy"]
poke = ["Name", "Number"]
data = poke + types

pokemon = pd.DataFrame(pokeData, columns = data)
pokemon.to_csv(r"C:\Users\Luna.DESKTOP-PEBO18O\Dropbox\DataScience\PokeData-TEST.csv", index = False)
driver.quit()