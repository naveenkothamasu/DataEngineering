#!/usr/bin/env python

import sys;
import random;

inputFileName = "likes.csv";
inputFile = open(inputFileName, "r");
outputFile = open("test_100.txt", "w");
inputData = [];
for line in inputFile:
	inputData.append(line)

i = 0;
while(i<100):
	outputFile.write(inputData[random.randint(0,len(inputData)-1)]);
	i+=1;
outputFile.close();
print "Generated test_100.txt"
