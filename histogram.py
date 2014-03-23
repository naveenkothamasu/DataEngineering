#!/usr/bin/env python
import sys;
import numpy as np;
import matplotlib.pyplot as plt

inputFileName = "test_10.txt"
inputFile = open(inputFileName, "r");
likesAndCountsMap = {};
wordList = [];
allLikes = [];

for line in inputFile:
        line = line.lower();
        wordList = line.split(",");
        wordList.remove(wordList[0]);
        for word in wordList:
                if word in likesAndCountsMap:
                        likesAndCountsMap[word] += 1;
                else:
                        likesAndCountsMap[word] = 1;
                        allLikes.append(word);

for entry in likesAndCountsMap:
        print entry+"\t"+str(likesAndCountsMap[entry]);

plt.hist(x=np.arange(0,len(allLikes)), weights=likesAndCountsMap.values());
plt.show();
