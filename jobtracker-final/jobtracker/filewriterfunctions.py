
# This file handles all file writing and reading functions
from datetime import datetime

#Creates file if none exists
def createFile():
   file = open("JobsAppliedTo.txt", "a")
   file.close()

def addJobEntryToFile(strJobName, strJobTitle, strSkills, strNotes):
	now = datetime.now() # current date and time
	strSkillArray = formatstrSkills(strSkills)
	strNotesArray = formatstrNotes(strNotes)
	File_object = open(r"JobsAppliedTo.txt", "a")
	File_object.write("\n" + strJobTitle + " position at " + strJobName + "\n")
	File_object.write("Date Applied: " + now.strftime("%m/%d/%Y") + "\n")
	File_object.write("Skills Required: \n")
	#65 is the number of characters before a line gets cut in the gui display, so we need to split the input string into substrings of length 65 or below where no word is cut off
	for i in strSkillArray:
		File_object.write("\t" + i + "\n")
	File_object.write("Additional Notes: \n")
	for j in strNotesArray:
		File_object.write("\t" + j + "\n")
	File_object.write("|-----------------------------------------------------------------------|\n")
	File_object.close()

def formatstrSkills(strSkills):
	arrSkills = []
	currentIndex = 0
	strSub = ""
	for i in range(0, len(strSkills)):
		strSub = strSub + strSkills[i]
		currentIndex = currentIndex + 1 
		if (currentIndex == 64):
			toAdd, delimiter, futureSplit = strSub.rpartition(" ")
			arrSkills.append(toAdd)
			strSub = futureSplit
			currentIndex = len(strSub) #whatever we pull off strSub 
	arrSkills.append(strSub)
	return arrSkills

def formatstrNotes(strNotes):
	arrNotes = []
	currentIndex = 0
	strSub = ""
	for i in range(0, len(strNotes)):
		strSub = strSub + strNotes[i]
		currentIndex = currentIndex + 1
		if (currentIndex == 64):
			toAdd, delimiter, futureSplit = strSub.rpartition(" ")
			arrNotes.append(toAdd)
			strSub = futureSplit
			currentIndex = len(strSub) #whatever we pull off strSub 
	arrNotes.append(strSub)
	return arrNotes

#Appends writing to end of file
def writeTofile(str):
	now = datetime.now() # current date and time
	File_object = open(r"JobsAppliedTo.txt", "a")
	File_object.write(str + " -- "+ now.strftime("%m/%d/%Y") + "\n")
	File_object.close()

#edits a line in the file
#@Parameter rowIndex: the row to be edited
#@Parameter strEdit: the edited row to be inserted
def editLine(rowIndex, strEdit):
	File_object = open(r"JobsAppliedTo.txt", "r")
	list_of_lines = File_object.readlines() #get all lines in an array to edit
	list_of_lines[rowIndex] = strEdit + "\n" 
	File_object.close()

def overwriteFileContents(str):
	File_object = open(r"JobsAppliedTo.txt", "w")
	File_object.write(str)
	File_object.close()

#Prints entire contents of file
def printFile():
	File_object = open(r"JobsAppliedTo.txt", "r+")
	#entireFile = File_object.read()
	file = File_object.read()
	File_object.close()
	return file

def deleteRow(rowNum):
	File_object = open(r"JobsAppliedTo.txt", "r")
	list_of_lines = File_object.readlines() #get all lines in an array to edit
	File_object.close()
	del list_of_lines[rowNum-1]
	new_File = open(r"JobsAppliedTo.txt", "w+")
	for line in list_of_lines:
		new_File.write(line)
	new_File.close()

# Finds any line that contains the keyword specified and returns it
def findKeyword(str):
	numFound = 0 #number of keyword instances found
	index = 0 #current line in file
	keywordRows = []
	File_object = open(r"JobsAppliedTo.txt", "r+")
	for line in File_object:
		index += 1
		if str in line:
			numFound = numFound + 1
			keywordRows.append(line)
	#for i in keywordRows:
	#	print(i)
	File_object.close()
	return numFound, keywordRows

# Search file for jobs that contain the keyword specified. 
# Search is not case sensitive
def findJobsWithKeyword(str):
	numFound = 0 #number of jobs with keyword instances found
	keywordFound = 0 #used to determine if the current job listing has the keyword
	keywordRows = []
	currentJobListing = [] #keep a reference of the current job we are looking at
	File_object = open(r"JobsAppliedTo.txt", "r+")
	for line in File_object:
		currentJobListing.append(line)
		if str.lower() in line.lower():
			numFound = numFound + 1
			keywordFound = 1
		if "---------------" in line:
			if keywordFound == 1:
				keywordRows = keywordRows + currentJobListing
				currentJobListing = []
				keywordFound = 0
			else:
				currentJobListing = []

	File_object.close()
	return numFound, keywordRows

# Search file for jobs that contain the keyword specified. 
# Search is case sensitive
def findJobsWithKeywordCaseSensitive(str):
	numFound = 0 #number of jobs with keyword instances found
	keywordFound = 0 #used to determine if the current job listing has the keyword
	keywordRows = []
	currentJobListing = [] #keep a reference of the current job we are looking at
	File_object = open(r"JobsAppliedTo.txt", "r+")
	for line in File_object:
		currentJobListing.append(line)
		if str in line:
			numFound = numFound + 1
			keywordFound = 1
		if "---------------" in line:
			if keywordFound == 1:
				keywordRows = keywordRows + currentJobListing
				currentJobListing = []
				keywordFound = 0
			else:
				currentJobListing = []

	File_object.close()
	return numFound, keywordRows