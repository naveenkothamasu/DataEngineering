#!/usr/bin/env python

import sys;
from sets import Set;
import time;

inputFile = open("test_100.txt" ,"r");
inputMap = {};
likesAndCountsMap = {};
likePairsAndCountsMap = {};
allLikes = [];
likesAndUIDsMap = {};
start = time.time();
for line in inputFile:
	line = line.lower();
	wordList = line.split(",");
	uid = wordList[0];
	inputMap[uid] = [];
	wordList.remove(wordList[0]);
	i = 0;
	while(i<len(wordList)):
		j = i+1;
		while(j < len(wordList)):
			pair = wordList[i]+","+wordList[j];
			rPair = wordList[j]+","+wordList[i];
			if pair in likePairsAndCountsMap:
				likePairsAndCountsMap[pair] += 1;
			elif rPair in likePairsAndCountsMap:
				likePairsAndCountsMap[rPair] += 1;
			else:
				likePairsAndCountsMap[pair] = 1;
			
			j += 1;
			
		i += 1;
'''
for entry in likePairsAndCountsMap:
	print entry+"\t"+str(likePairsAndCountsMap[entry]);
'''
print time.time()-start;
