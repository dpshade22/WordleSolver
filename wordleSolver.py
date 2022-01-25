from unittest import skip
import numpy as np
import csv
import streamlit as st
import time

with open("dictionary.csv") as file_name:
    file_read = csv.reader(file_name)

    dictionaryLong = list(file_read)

dictionary = []

for i in range(len(dictionaryLong)):
    dictionaryLong[i] = dictionaryLong[i][0]

    if len(dictionaryLong[i]) == 5:
        dictionary.append(dictionaryLong[i])

# print(dictionary)

# Array form [0, 'a', idx]


class Word:
    def __init__(self, correct, incorrect, wrongPlace):
        self.correct = correct
        self.incorrect = incorrect
        self.wrongPlace = wrongPlace
        self.allCorrect = []
        self.allIncorrect = []
        self.allWrongPlace = []

    def printCorrect(self):
        result = ""
        for i in range(len(self.correct)):
            result += str(self.correct[i])
        return result

    def printIncorrect(self):
        result = ""
        for i in range(len(self.incorrect)):
            result += str(self.incorrect[i])
        return result

    def printWrongPlace(self):
        result = ""
        for i in range(len(self.wrongPlace)):
            result += str(self.wrongPlace[i])
        return result


def confirmWordCorrect(testWord, listOfCorrect):
    for i in range(len(listOfCorrect)):
        if listOfCorrect[i][0] != testWord[listOfCorrect[i][1]]:
            return False
        else:
            continue
    return True


def letterNotIn(testWord, listOfIncorrect):
    for i in range(len(listOfIncorrect)):
        if listOfIncorrect[i][0] not in testWord:
            continue
        else:
            return False
    return True


def letterIsIn(testWord, listOfWrongPlace):
    for i in range(len(listOfWrongPlace)):
        if listOfWrongPlace[i][0] not in testWord:
            return False
        if listOfWrongPlace[i][0] in testWord:
            print(listOfWrongPlace[i])
            if listOfWrongPlace[i][0] == testWord[listOfWrongPlace[i][1]]:
                return False
        else:
            continue
    return True


# Add the word when the letter is in the word, but not in a specific place


def solveWordle(array1=[], array2=[], array3=[], array4=[], array5=[]):

    allInput = [array1, array2, array3, array4, array5]

    wordle = Word([], [], [])

    for i in range(len(allInput)):
        for j in range(5):
            if allInput[i] == []:
                continue

            if (allInput[i][j][0] == 0 and allInput[i][j][1] in wordle.allCorrect) or (
                allInput[i][j][0] == 0 and allInput[i][j][1] in wordle.allWrongPlace
            ):
                pass

            elif allInput[i][j][0] == 0:
                wordle.incorrect.append([allInput[i][j][1], j])
                wordle.allIncorrect.append(allInput[i][j][1])

            if allInput[i][j][0] == 1:
                wordle.correct.append([allInput[i][j][1], j])
                wordle.allCorrect.append(allInput[i][j][1])

            if allInput[i][j][0] == 2:
                wordle.wrongPlace.append([allInput[i][j][1], j])
                wordle.allWrongPlace.append(allInput[i][j][1])

    # print(
    #     f"""
    # Correct: {wordle.printCorrect()}
    # Incorrect: {wordle.printIncorrect()}
    # Wrong Place: {wordle.printWrongPlace()}
    # """
    # )

    return wordle


def findWordWith(wordObject):
    wordsWith = []

    for i in range(len(dictionary)):

        if not letterNotIn(dictionary[i], wordObject.incorrect):
            continue

        if not letterIsIn(dictionary[i], wordObject.wrongPlace):
            continue

        if confirmWordCorrect(dictionary[i], wordObject.correct):
            wordsWith.append(dictionary[i])

    return wordsWith


# Given a list such as [['w', 0],['o', 1],['r', 2],['t', 4]]


st.title("Wordle Solver")

col1, col2 = st.columns(2)

init = False

if st.button("Clear Entries"):
    init = True
    init = False


with st.expander("1 Word Guessed"):
    st.header("Word Guessed + Correctness")
    guess1 = st.text_input("Guess 1", disabled=init)
    correctness1 = st.text_input("Correctness 1", disabled=init)

with st.expander("2 Word Guessed"):
    st.header("Word Guessed + Correctness")
    guess2 = st.text_input("Guess 2", disabled=init)
    correctness2 = st.text_input("Correctness 2", disabled=init)

with st.expander("3 Word Guessed"):
    st.header("Word Guessed + Correctness")
    guess3 = st.text_input("Guess 3", disabled=init)
    correctness3 = st.text_input("Correctness 3", disabled=init)

with st.expander("4 Word Guessed"):
    st.header("Word Guessed + Correctness")
    guess4 = st.text_input("Guess 4", disabled=init)
    correctness4 = st.text_input("Correctness 4", disabled=init)

with st.expander("5 Word Guessed"):
    st.header("Word Guessed + Correctness")
    guess5 = st.text_input("Guess 5", disabled=init)
    correctness5 = st.text_input("Correctness 5", disabled=init)

if len(guess1) == 5 and len(correctness1) == 5:
    firstGuess = [
        [int(correctness1[0]), guess1[0].lower()],
        [int(correctness1[1]), guess1[1]],
        [int(correctness1[2]), guess1[2]],
        [int(correctness1[3]), guess1[3]],
        [int(correctness1[4]), guess1[4]],
    ]
else:
    firstGuess = []

if len(guess2) == 5 and len(correctness2) == 5:
    secondGuess = [
        [int(correctness2[0]), guess2[0].lower()],
        [int(correctness2[1]), guess2[1]],
        [int(correctness2[2]), guess2[2]],
        [int(correctness2[3]), guess2[3]],
        [int(correctness2[4]), guess2[4]],
    ]
else:
    secondGuess = []

if len(guess3) == 5 and len(correctness3) == 5:
    thirdGuess = [
        [int(correctness3[0]), guess3[0].lower()],
        [int(correctness3[1]), guess3[1]],
        [int(correctness3[2]), guess3[2]],
        [int(correctness3[3]), guess3[3]],
        [int(correctness3[4]), guess3[4]],
    ]
else:
    thirdGuess = []

if len(guess4) == 5 and len(correctness4) == 5:
    fourthGuess = [
        [int(correctness4[0]), guess4[0].lower()],
        [int(correctness4[1]), guess4[1]],
        [int(correctness4[2]), guess4[2]],
        [int(correctness4[3]), guess4[3]],
        [int(correctness4[4]), guess4[4]],
    ]
else:
    fourthGuess = []

if len(guess5) == 5 and len(correctness5) == 5:
    fifthGuess = [
        [int(correctness5[0]), guess5[0].lower()],
        [int(correctness5[1]), guess5[1]],
        [int(correctness5[2]), guess5[2]],
        [int(correctness5[3]), guess5[3]],
        [int(correctness5[4]), guess5[4]],
    ]

else:
    fifthGuess = []


if st.button("Enter Guess"):
    for i in findWordWith(
        solveWordle(firstGuess, secondGuess, thirdGuess, fourthGuess, fifthGuess)
    ):
        st.text(i)
