#!/usr/bin/env python3
import sys
from faaFileParser import *
from argChecker import *
__author__ = 'Stef'

def printHelp():
    message = "\nThis program accepts an faa file and parses the file for the user\n" \
              "specifed accession number. If the accession number is found in the header sequence,\n" \
              "the program outputs the header sequence and the amino acid sequence.\n" \
              "If no faa file is passed to the program, 'e_coli_k12_dh10b.faa' will be parsed by default.\n" \
              "\nProgram usage:\n" \
              "python3 lookup_sequence.py\n" \
              "python3 lookup_sequence.py <fileName>\n" \
              "python3 lookup_sequence.py --file=<fileName>\n"

    print(message)
    exit()


def promptUser():
    userInput = input("\nPlease enter an accession to search: ")
    return userInput


'''
Main script
'''
if len(sys.argv) > 1:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        printHelp()
        exit()

#Promt the user for a accession number
accession = promptUser()

#If not file is passed to the program use the default file
if len(sys.argv) == 1:
    filePath = "e_coli_k12_dh10b.faa"

#A file has been passed, so process the argument for parameter names ("--file=")
if len(sys.argv) >= 2:
    filePath = sys.argv[1]
    argsNames = ["--file="]
    args = ArgChecker(argsNames, "lookup_sequence.py")
    aList = [filePath]
    arguments = args.checkArgs(aList)
    filePath = arguments[0]

#Create a faa file parser object
accessFinder = FaaFileParser(filePath)
#Call searchAccession function to search for user specified accession number
hit = accessFinder.searchAccession(accession)
#Print the result
print('\n'+hit)