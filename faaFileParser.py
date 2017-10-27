#!/usr/bin/env python3
__author__ = 'Stef Streamer'
import re

'''
This class parses a faa file that is passes to the processFile function

'''
class FaaFileParser(object):
    #Constructor to store values in .faa file search
    def __init__(self, filePath):
        self.file = filePath
        self.fileIn = open(filePath)    #faa file input by the user
        self.geneCount = 0              #variable to store the number of genes that are encountered
        self.minProtLen = 0             #stores the min aa sequence length encountered
        self.maxProtLen = 0             #stores the max aa sequence length encountered
        self.protList = []              #List to store all aa sequence lengths for future length stats
        self.termGeneCount = 0          #variable to count the number of search ("hypothetical") terms encountered
        self.currentAaSeq = ""          #variable to hold the current amino acid sequence

    def processFile(self, searchTerm):
        #variable to determine if we have passed all opening file line and are into aa sequences
        inProtSeq = False

        for line in self.fileIn:
            line = line.strip('\r') #strip unix and windows newlines
            line = line.strip('\n')
            #check if a amino acid sequence (gene) is encountered
            if line.startswith('>'):
                if inProtSeq != False:
                    #process previous amino acid sequence data
                    self.calculateProtStats()
                #Passed the file description
                inProtSeq = True
                self.geneCount += 1
                #check if search term occurs in the header sequence
                if re.search(searchTerm, line):
                    self.termGeneCount += 1
            #Add the amino acid sequence line to the current sequence (if we have passed the opening line)
            else:
                if inProtSeq == True:
                    self.currentAaSeq += line

        self.fileIn.close()


    #This function calculates the amino acid sequence statistics
    def calculateProtStats(self):
        #append aa sequence length to the protList List
        aaLen = len(self.currentAaSeq)
        self.protList.append(aaLen)

        #check if we have encountered a max amino acid length
        if aaLen > self.maxProtLen:
            self.maxProtLen = aaLen

        #check if we have encountered a min amino acid length or the first one
        if aaLen < self.minProtLen or self.minProtLen == 0:
            self.minProtLen = aaLen

        #reset current amino acid sequence
        self.currentAaSeq = ""

    #This function calculates the average amino acid sequence from the
    #Protein length list
    def calcAvgLen(self):
        sum = 0
        size = len(self.protList)

        for item in self.protList:
            sum += item
        #round the length to the nearest whole number
        return int(round((sum/size),1))


    def searchAccession(self, accs):

        hit = ""
        found = False

        for line in self.fileIn:

            #We have encountered a new amino acid sequence
            if line.startswith(">") and found == False:
                info = line.split('|')
                for item in info:
                    if item == accs:
                        hit += line
                        found = True
                        break

            #We are currently in our amino acid sequence of interest
            elif not line.startswith(">") and found == True:
                hit += line

            #We have passed our amino acid sequence of interest
            elif line.startswith(">") and found == True:
                found = False
                return hit

        #We have reached the end of the file without finding the accession
        if hit == "":
            hit = "Sorry, accession number " + accs + " was not found in the file: " + self.file

        return hit



