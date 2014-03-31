#!/usr/bin/env python

import sys;
from sets import Set;
import time;
import myHeap;
import codecs;
import matplotlib.pyplot as plt;

inputFile = codecs.open("test_100.txt", encoding = "utf-8", mode = "r");
inputMap = {};
likesAndCountsMap = {};
likePairsAndCountsMap = {};
allLikes = [];
likesAndUIDsMap = {};
topLikePairs = []; #heap initialization
topLikePairsMap = {};

start = time.time();
heap_size = 5;
k = 1;
for line in inputFile:
        line = line.lower();
        line = line.replace("\n", "");
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
                                likePairsAndCountsMap[pair] += 1;
                                #presentLikes = likesPairsAndCountsMap[pair];
                                #myHeap.increase_key(topLikePairs, (presentLikes, pair), (presentLikes+1, pair));
                        elif rPair in likePairsAndCountsMap:
                                likePairsAndCountsMap[rPair] += 1;
                                #presentLikes = likesPairsAndCountsMap[rPair];
                                #myHeap.increase_key(topLikePairs, (presentLikes, rPair), (presentLikes+1, rPair));
                        else:
                                likePairsAndCountsMap[pair] = 1;
                                #if k >= heap_size:
                                #       myHeap.pop(topLikePairs);
                                #myHeap.push(topLikePairs, (1, pair));
                        j += 1;
                        #k += 1;
                i += 1;

for entry in likePairsAndCountsMap:
        if k > heap_size:
                if topLikesPairs[0][0] > likePairsAndCountsMap[entry]:
                        continue;
                myHeap.pop(topLikePairs);
        myHeap.push(topLikePairs, (likePairsAndCountsMap[entry], entry));
        k += 1;
print time.time()-start;
print topLikePairs;
'''
print myHeap.pop(topLikePairs);
print myHeap.pop(topLikePairs);
'''
x = [];
y = [];
while len(topLikePairs) !=0 :
        t = myHeap.pop(topLikePairs);
        x.append(t[1]);
        y.append(t[0]);

plt.axes().set_xticks(np.arange(len(x))+0.5);
plt.axes().set_xticklabels(x,rotation=90,ha='left');
plt.ylabel("Count of like pairs")
hist_x = len(y);
plt.bar(np.arange(hist_x),y,width=1.0, color='r');
plt.show();
