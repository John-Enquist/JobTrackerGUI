
# This program writes user input to a text file
from filewriterfunctions import *

commands = ['WRITE: Allows the user to write to a file',
			'PRINT FILE: Allows the user to print full file contents',
			'FIND: Find and print all rows that contain the keyword specified',
			'END: Terminates the program']

def main():
    startingInput()

#the starting point of this function, takes user input to perform functions on text file
def startingInput():
	createFile()
	action = input('What would you like to do? type HELP if you are unsure!  ')
	if (action == 'WRITE'):
		writeTofile(getTextToInput())
	elif action == 'PRINT FILE':
		printFile()
	elif action == 'FIND':
		findKeywords()
	elif action == 'HELP':
		printCommands()
	elif action == 'END':
		return
	else:
		print('that command is not valid, please try again\n')
		printCommands()
	startingInput()

#finds all instances of a keyword in file and returns them as a list
def findKeywords():
	rowNum = 0
	keyword = input('type a keyword or phrase you would like to find: ')
	numFound, allRows = findJobsWithKeyword(keyword) #findKeyword(keyword)
	print('\nThe keyword ' + '"' +  keyword + '"' + ' was found ' + str(numFound) + ' times.\n' )
	for i in allRows:
		rowNum = rowNum + 1
		print(str(rowNum) + ": " + i)	
	modifyFile()

def searchFile(keyword, searchType):
	if (searchType == "Case-Sensitive"):
		numFound, allRows = findJobsWithKeywordCaseSensitive(keyword)
	elif (searchType == "Search by Line"):
		numFound, allRows = findKeyword(keyword)
	else:
		numFound, allRows = findJobsWithKeyword(keyword) # findKeyword(keyword)
	results = '\nThe keyword ' + '"' +  keyword + '"' + ' was found ' + str(numFound) + ' times.\n'
	for i in allRows:
		results = results + i	
	return results

def addEntryToFile(input):
	writeTofile(input)

def modifyFile():
	modType = input("Would you like to modify or remove any of the above lines? (type YES or NO) \n")
	if (modType == "YES"):
		changeType = input("What type of changes would you like to make?\n Type EDIT if you would like to edit the row \n Type REMOVE if you would like to delete it\n")
		rowNumber = input("Okay, what row would you like to " + changeType + "?\n")

		if (changeType == "REMOVE"):
			deleteRow(int(rowNumber)) #remove line from file
		elif (changeType == "EDIT"):
			print("this doesnt work yet")
	
#prints all available commands for this function
def printCommands():
	print("\nValid Commands Include:")
	for i in commands:
		print(i)
	print()

def getCommandsToPrint():
	commandText = "\nValid Commands Include:"
	for i in commands:
		commandText = commandText + "\n" + i
	return commandText

def printFileContents():
	return printFile()

def overwritefile(str):
	overwriteFileContents(str)

def addEntry(strJobName, strJobTitle, strSkills, strNotes):
	addJobEntryToFile(strJobName, strJobTitle, strSkills, strNotes)

def getTextToInput():
	text = input('Write anything below \n ')
	return text

if __name__ == "__main__":
    main()
