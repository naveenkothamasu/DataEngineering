#!/usr/bin/env python
import sys;

def parent(i):
	if i == 0:
		return -1;
	else:
		return (i-1)/2;
def left(i):
	return 2*i+1;
def right(i):
	return 2*i+2;

def push(heap, item):
	heap.append(item);
	i = len(heap)-1;
	while parent(i) != -1 and heap[i][0] < heap[parent(i)][0]:

		temp = heap[i];
		heap[i] = heap[parent(i)];
		heap[parent(i)] = temp;
		i = parent(i);
def pop(heap):
	min = heap.pop(0);
	if len(heap) != 0:
		last = heap.pop(len(heap)-1);
		heap.insert(0, last);
		heapify(heap, 0);
	return min;
	
def heapify(heap, i):
	l = left(i);
	r = right(i);
	lowest = i;
	if l < len(heap) and heap[l][0] < heap[i][0]:
		lowest = l;
	if r < len(heap) and heap[r][0] < heap[lowest][0]:
		lowest = r;
	if lowest != i:
		temp = heap[lowest];
		heap[lowest] = heap[i];
		heap[i] = temp;
		heapify(heap, lowest);

def increase_key(heap, old, new):
	i = heap.index(old);
	heap[i] =  new;
	heapify(heap, i);
'''
heap = [];
a = [12,2,15,19,20,5,3,1];

for item in a:
	push(heap, item);
for item in a:
	pop(heap);

for item in a:
	push(heap, item);

i = len(heap)/2;
while i >= 0:
	heapify(heap, i);
	i -= 1;

increase_key(heap, 1, 6)
while len(heap) != 0:
	print pop(heap);
'''
