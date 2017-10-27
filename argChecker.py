#!/usr/bin/env python3
import re
__author__ = 'Stef'

class ArgChecker(object):
    #constructor to store program that is initializing the ArgChecker object
    #and the argument names
    def __init__(self, argL, programName):
        self.argList = argL
        self.pName = programName

    #Function to check that parameters have been correctly passed
    def checkArgs(self, passedArgs):
        #List of arguments with the parameter names removed (if encountered)
        retrnArgs = []
        #Counter to store which parameter we are looking at
        counter = 0

        for arg in passedArgs:
            #Parameter names have been passed
            if arg.startswith("--"):
                #Parameter names have been used incorrectly for the calling script
                if (re.search("--[\\w]+[=]", arg)).group() not in self.argList[counter]:
                    self.printError()
                    exit()
                #Remove paramter name so the calling script can use the argument
                argName = re.sub("--[\\w]+[=]","", arg)
                retrnArgs.append(argName)
                counter += 1
                #Parameter names were not used, so nothing to process
            else:
                retrnArgs.append(arg)
                counter += 1

        return retrnArgs

    #Function to alert and instruct the user how to pass arguments and parameter names to
    #the calling script
    def printError(self):
        args = self.argList
        index = 0
        params = []
        #Process the argument list
        for item in args:
            name = re.match("--[\\w]+", item)
            param = name.group()
            param = param.replace("--","")
            item += "<" + param + ">"
            params.append("<" + param + ">")
            args[index] = item
            index += 1

        #Remove vestigial array character/notation from the newly created string
        #Ouput for parameter name notation (--option<option>
        args = str(args)
        args = args.replace("[","")
        args = args.replace("]","")
        args = args.replace("'","")
        args = args.replace(",","")

        #Remove vestigial array character/notation from the newly created string
        #Output for arguments <option>
        argNames = str(params)
        argNames = argNames.replace("[","")
        argNames = argNames.replace("]","")
        argNames = argNames.replace("'","")
        argNames = argNames.replace(",","")

        print("\nPlease pass a file and a search term to the program\n")
        print("python3 " + self.pName + " " + args + '\n' "OR")
        print("python3 " + self.pName + " " + argNames + '\n')
