#!usr/bin/env python

import sys;

inputFileName = "test.txt"
inputFile = open(inputFileName, "r");
likesAndCountsMap = {};
wordList = [];

for line in inputFile:
	line = line.lower();
	wordList = line.split(",");
	wordList.remove(wordList[0]);
	for word in wordList:
		if word in likesAndCountsMap:
			likesAndCountsMap[word] += 1;
		else:
			likesAndCountsMap[word] = 1;

for entry in likesAndCountsMap:
	print entry+"\t"+str(likesAndCountsMap[entry]);
			
		
