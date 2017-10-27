#!/usr/bin/env python3
import sys
from faaFileParser import *
from argChecker import *
__author__ = 'Stef Streamer'

'''
This program accepts an faa file and parses the file to determine the
following statistics:
Gene count (number of protein sequences)
Minimum Protein length (shortest amino acid sequence encountered)
Maximum Protein length (largest amino acid sequence encountered)
Average Protein length (a list of protein lengths are stored for future stats)
Count of a given term ("hypothetical" is the term for this assignment)
'''

def printHelp():
    message = "\nThis program accepts an faa file and parses the file to determine the\n" \
              "following statistics:\n" \
              "Gene count (number of protein sequences)\n" \
              "Minimum Protein length (shortest amino acid sequence encountered)\n" \
              "Maximum Protein length (largest amino acid sequence encountered)\n" \
              "Average Protein length (a list of protein lengths are stored for future stats)\n" \
              "Count of a given term in the amino acid sequence headers ('hypothetical' is the term for this assignment)" \
              "\n\nProgram usage:\n" \
              "python3 summarize_fasta.py <faaFile> <searchTerm>\nOr \n" \
              "python3 summarize_fasta.py --file=<faaFile> --searchTerm=<searchTerm>\n"

    print(message)
    exit()

'''
Main script
'''
#Check if the user asked for help
if len(sys.argv) > 1:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        printHelp()
        exit()

#Check that a faa file and search term has been passed to the program
argsNames = ["--file=","--searchTerm="]
if len(sys.argv) != 3:
    arguments = ArgChecker(argsNames, "summarize_fasta.py")
    arguments.printError()
    exit()

#Assign command line arguments
filePath = sys.argv[1]
searchTerm = sys.argv[2]

#check arguments and remove paramater names if present
aList = [filePath,searchTerm]
args = ArgChecker(argsNames, "summarize_fasta.py")
arguments = args.checkArgs(aList)
filePath = arguments[0]
searchTerm = arguments[1]

#Initialize the FaaFileParser object
record = FaaFileParser(filePath)
#Parse the file with the search term count argument
record.processFile(searchTerm)
#Print out the statistics
print("\nProccessing file\n")
print("Gene count = " + str(record.geneCount) + '\n')
print("Min protein length = " + str(record.minProtLen) + '\n')
print("Max protein length = " + str(record.maxProtLen) + '\n')
print("Average protein length = " + str(record.calcAvgLen()) + '\n')
print("Count of " + "\'" + searchTerm + "\'" + " = " + str(record.termGeneCount) + '\n')
