from ex13_1 import *
from collections import Counter
# I have downloaded _Pride and Prejudice_ from Gutenberg website and modified header with '#'

def count_number(l):
	c = Counter(l)
	print(c) #each word occurence
	#print(c.most_common(20)) #ex13_3

if __name__ == '__main__':
	#print(list(read_file('PrideandPrejudice.txt'))) #check
	l = list(read_file('PrideandPrejudice.txt'))
	count_number(l)
	print("Total number of unique different words is: ", len(set(l)))
	print("Total number of words is:", len(l))