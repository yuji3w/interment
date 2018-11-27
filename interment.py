import os
import pprint
import gender_guesser.detector as gender
import re
import string

femPre1900 = []
femPost1900 = []
manPre1900 = []
manPost1900 = []

def findBD(inputText):
	bYear = re.findall(r"b\. ([1-3][0-9]{3})", inputText)
	dYear = re.findall(r"d\. ([1-3][0-9]{3})", inputText)
	if not bYear or not dYear:
		return -1, -1
		#for when there's nothing
	bYear = int(bYear[0])
	dYear = int(dYear[0])
	return bYear, dYear

def bigSmallYear(inputText):
	years = re.findall(r"([1-3][0-9]{3})", inputText)
	years = list(map(int, years))
	if not years:
		return -1, -1
	dYear = max(years)
	bYear = min(years)
	if bYear is dYear and len(years) is 1:
		return -1, -1
	return bYear, dYear

def sexAge(inputText):
	splitText = inputText.split()
	#split by spaces
	sanitizedName = splitText[1].translate(str.maketrans('','',string.punctuation))
	#sanitize by removing punctuation

	bYear, dYear = findBD(inputText)
	if bYear is -1 or dYear is -1:
		return

	age = dYear - bYear
	if d.get_gender(sanitizedName) is "mostly_female" or d.get_gender(sanitizedName) is "female":
		if dYear <1900:
			femPre1900.append(age)
		else:
			femPost1900.append(age)
	elif d.get_gender(sanitizedName) is "mostly_male" or d.get_gender(sanitizedName) is "male":
		if dYear <1900:
			manPre1900.append(age)
		else:
			manPost1900.append(age)

d = gender.Detector()
inputText = r"C:\Users\Yujie Wang\Desktop\interment.txt"
inputText = open(inputText,"r")
inputText = inputText.read().splitlines()

for line in inputText:
	sexAge(line)

print("femPre1900")
print(femPre1900)
print("femPost1900")
print(femPost1900)
print("manPre1900")
print(manPre1900)
print("manPost1900")
print(manPost1900)