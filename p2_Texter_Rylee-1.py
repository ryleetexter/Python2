# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:29:47 2024

@author: rylee
"""

#part a: returns tuples with distinct integers, where a^2 + b^2 = c^2 + d^2
#and 1<=a,b,c,d<=10

groups = [(a,b,c,d) for a in range(1,11) for b in range (1,11) for c in range (1,11) for 
          d in range(1,11) if((a**2+b**2 == c**2 + d**2) and (((a!= b and a!=c) and (a!=d and b!= c))and (b!= d and c!= d)))]

print("part a: ")
print(groups)
print()


#part b: returns a list of tuples containing the lowercase string of 
#stringList along with lengths that are less than 5 characters
stringList = ['one', 'SEvEN','Three', 'twO', 'ten' ]
lengths = [(string.lower(), len(string)) for string in stringList if len(string) < 5]

print("part b: ")
print(lengths)
print()


#part c: returns a list of formatted names
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']

names_formatted = [''.join([name.split()[0], name.split()[1][0] + '.', name.split()[2]])
          for name in names]

print("part c")
print(names_formatted)
print()

#part d: returns a list of tuples of anagrams between the two lists
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]


anagrams = [(x,y) for x in lst1 for y in lst2 if sorted(x.lower()) == sorted(y.lower())]
print("part d")
print(anagrams)
print()

#part e: maps each string to its length
s = ['one', 'two', 'three']

string_lengths = {string: len(string) for string in s}
print("part e: ")
print(string_lengths)
print()

#returns disctionary with index of vowel as key and vowel as value
text = "Hello world"

vowelIndexes = {i:text[i] for i in range(len(text)) if text[i] in ['a','e','i','o','u']}
print("part f")
print(vowelIndexes)
print()





