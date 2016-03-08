from bitarray import bitarray
import hashlib
import urllib
import os
     
class BloomFilter:   
        
	def __init__(self, size, hash_count):
		self.size = size
		self.hash_count = hash_count
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
            
	def add(self, string):
		for seed in xrange(self.hash_count):
			result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
			self.bit_array[result] = 1
                
	def lookup(self, string):
		for seed in xrange(self.hash_count):
			result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
			if self.bit_array[result] == 0:
				return "Nope"
		return "Probably"
     
bf = BloomFilter(500000, 7)
print "place the folder with the text you want to check in the same directory as the programm's"
dictionary="https://gunet2.cs.unipi.gr/modules/document/file.php/TMA111/american-english.txt"
dicthtml = urllib.urlopen(dictionary).read()
file = open("american-english.txt", "w")
file.write(dicthtml)
file.close()
     
lines = open("american-english.txt").read().splitlines()
for line in lines:
	bf.add(line)
text=raw_input("insert the name of the file which contains the text you want to check:")
open_file = open(text+".txt", 'r')
lst=[]
print "The programm is valid for texts without punctuation"
print " "
print "The exact text that was given is the following:"
print " "
for line in open_file:
	print line
	line=line.strip()
	lst.append(line)
print " "
print "-------------------------------------------------------------------------------"
print "The new text that puts into -- the words that don't exist in the dictionary is:"
print "-------------------------------------------------------------------------------"
print " "
for i in range(len(lst)):
	words=lst[i].split()
	lek=[]
	for word in words:
		bf.lookup(word)
		if bf.lookup(word) == "Nope":
			word="--"+word+"--"
		lek.append(word)
		lek.append(" ")
	print ''.join(map(str, lek))
	print " "
os.remove("american-english.txt")
