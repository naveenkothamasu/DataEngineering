#!/usr/bin/env python

import sys;
from sets import Set;
import time;
import heapq;

inputFile = open("test.txt" ,"r");
inputMap = {};
likesAndCountsMap = {};
likePairsAndCountsMap = {};
allLikes = [];
likesAndUIDsMap = {};
topLikePairs = []; #heap initialization

start = time.time();
for line in inputFile:
	line = line.lower();
	messageList = line.split(",");
	uid = messageList[0];
	inputMap[uid] = [];
	messageList.remove(messageList[0]);
	i = 0;
	while(i<len(messageList)):
		j = i+1;
		while(j < len(messageList)):
			pair = messageList[i]+","+ messageList[j];
			rPair = messageList[j]+","+ messageList[i];
			if pair in likePairsAndCountsMap:
				#likePairsAndCountsMap[pair] += 1;
				heapq._siftup(topLikePairs, (likesPairsAndCountsMap[pair], pair));
			elif rPair in likePairsAndCountsMap:
				#likePairsAndCountsMap[rPair] += 1;
				heapq._siftup(topLikePairs, (likesPairsAndCountsMap[rpair], rPair));
			else:
				#likePairsAndCountsMap[pair] = 1;
				heapq.heappush(topLikePairs, (1, pair));
			j += 1;
			
		i += 1;

for entry in likePairsAndCountsMap:
	if(likePairsAndCountsMap[entry] >= 2):
		print entry+"\t"+str(likePairsAndCountsMap[entry]);

print time.time()-start;
print heapq.heappop(topLikePairs);
print heapq.heappop(topLikePairs);
