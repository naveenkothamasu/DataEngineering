#!/usr/bin/env python
import sys;
import numpy as np;
import matplotlib.pyplot as plt

inputFileName = "test_3.txt"
inputFile = open(inputFileName, "r");
likesAndCountsMap = {};
wordList = [];
allLikes = [];
x= [];
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
'''
for entry in likesAndCountsMap:
        print entry+"\t"+str(likesAndCountsMap[entry]);

print likesAndCountsMap.values()

print np.arange(0,len(allLikes));
print likesAndCountsMap.values();
'''
'''

l = np.arange(0,len(allLikes));
hist = np.histogram([1,2,1],bins=[0,1,2,3]);
print hist;
print np.histogram(likesAndCountsMap.values(), bins=np.arange(0,len(allLikes)));
'''

plt.axes().set_xticks(np.arange(len(allLikes))+0.5);
plt.axes().set_xticklabels(unicode(likesAndCountsMap.keys()));

hist_x = len(likesAndCountsMap.values());
plt.bar(np.arange(hist_x),likesAndCountsMap.values(),width=1.0, color='r');
plt.show();

