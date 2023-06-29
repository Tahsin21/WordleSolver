import enum
from functools import partial
from itertools import count
import re
from re import X, match

appActive = True
wrongIndexList = []

while appActive:
    guess = input("What word did you guess? ")
    answers = input("Based on your guess, what was the feedback (x = green, y = yellow, z = grey): ")
    guessList = list(guess.lower())
    answersList = list(answers.lower())
    answersIndexList = []
    answersCompareList = [0,0,0,0,0]
    partialCompareList = [0,0,0,0,0]
    partialIndexList = []

    def convert(charList) : #converts a char list into a string
        strng = ''
        for x in charList:
            strng += x
        return strng


    for position,character in enumerate(answersList): #looks through feedback string
        if character == "x" : #if answers green, it adds its index to a new list
            answersIndexList.append(position)
        elif character == "y" : #if answers yellow, it adds its index to a new list
            partialIndexList.append(position)

    for i in range(len(answersIndexList)) :
        answersCompareList[answersIndexList[i]] = guessList[answersIndexList[i]] #create a new list which is used to find words in text file with letters in correct indices

    for i in range(len(partialIndexList)) :
        partialCompareList[partialIndexList[i]] = guessList[partialIndexList[i]] #creates a new list which is used to check if final set of words contains yellow words in the same index

    for position,character in enumerate(answersList) :
        if character == "z" and guessList[position] not in answersCompareList : # if answer is grey and ISN'T already in answers list (mitigate duplicate issues), add to new list
            wrongIndexList.append(guessList[position])

    #regex builder
    partialStr = ""
    for i in  range(len(partialIndexList)) : 
        partialStr += "(?=\w+" + guessList[partialIndexList[i]] + ")"

    partialStr += "^[^"
    for j in range(len(wrongIndexList)) :
        partialStr += wrongIndexList[j]
    partialStr += "]+$"


    with open(r"https://github.com/Tahsin21/WordleSolver/blob/5fca04962014086035754ecc5f1b103910db8623/words.txt", 'r') as finder:
        soluWords = []
        counter = 0
        lines = finder.readlines()

    for i in range(len(lines)):
        tempWord = list(lines[i].rstrip('\n'))
        for ix, (tW, aCL) in enumerate(zip(tempWord,answersCompareList)): ##take list with letters in correct position and compare against words in text file with the same 
            if tW == aCL:
                counter += 1
            if counter == len(answersIndexList) : #every letter from our feedback "x's" must be present in the text file letters
                soluWords.append(convert(tempWord))
                counter = 0
        else :
            counter = 0



    r = re.compile(partialStr)
    filteredList = list(filter(r.match,soluWords)) # use regex on the first set of solutions (green letter positions) and see if any of the words contain yellow letters
    #since yellow can be in any position and list is already filtered down to correct green indexes, we can print this list


    def partialPositionFilter(list1) : #makes sure any yellow letters aren't in the same position in the new list
        for i in range(len(list1)) :
            wordCheck = list(list1[i])
            check = [j for j, (x, y) in enumerate(zip(wordCheck, partialCompareList)) if x == y]
            if bool(check):
                return False
            else :
                return True

    finalSolution = list(filter(partialPositionFilter,filteredList)) #filter solution based on function above

    print(finalSolution)
