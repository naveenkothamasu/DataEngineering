#!/usr/bin/env python

import sys;
from sets import Set;

inputFile = open("test_25.txt" ,"r");
inputMap = {};
likesAndCountsMap = {};
likePairsAndCountsMap = {};
allLikes = [];
likesAndUIDsMap = {};

for line in inputFile:
	line = line.lower();
	wordList = line.split(",");
	uid = wordList[0];
	inputMap[uid] = [];
	wordList.remove(wordList[0]);
	for word in wordList:
		inputMap[uid].append(word);
		if word in likesAndUIDsMap:
			likesAndUIDsMap[word].append(uid);
		else:
			likesAndUIDsMap[word] = [uid];

		if word in likesAndCountsMap:
			likesAndCountsMap[word] += 1;
		else:
			likesAndCountsMap[word] = 1;
			allLikes.append(word);
i = 0;
while(i < len(allLikes)):
	j = i+1;
	while(j < len(allLikes)):
		like1 = allLikes[i];
		like2 = allLikes[j];

		word = like1+","+like2;
		#likePairsAndCountsMap[word] = len(Set(likesAndUIDsMap[like1]).intersection(Set(likesAndUIDsMap[like2])));
		likePairsAndCountsMap[word] = 0;
		for entry in likesAndUIDsMap[like1]:
			if entry in likesAndUIDsMap[like2]:
				likePairsAndCountsMap[word] += 1;
				print word+"\t"+str(likePairsAndCountsMap[word]);
		j += 1;
	i += 1;

print likePairsAndCountsMap;
