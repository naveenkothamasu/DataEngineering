#!/usr/bin/env python
import sys;
import random;

inputFileName = "likes.csv";
numFiles = 50;
inputFile = open(inputFileName, "r");
inputData = [];
for line in inputFile:
	inputData.append(line)

i = 0;
fileCount = 0;
prev = inputFile;
while(i < len(inputData)):
	if i%1000 == 0:
		prev.close();
		outputFile = open("test_"+str(i/1000)+".txt", "w");
		fileCount += 1;
		prev = outputFile;
	outputFile.write(inputData[i]);
	i+=1;
print "Generated "+str(fileCount)+"s files."
