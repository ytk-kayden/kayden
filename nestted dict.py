inputStr=input("enter the string - ")
vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
        }
for c in inputStr:
    if c in vowels:
        vowels[c] += 1
print(vowels)

#count the occurrence of each alphabhet  in the string entered by the user
inputstr = input("enter the string - ")
charcount = 0

for c in inputstr:
     if c.isalpha():
          charcount += 1
     else:
         charcount += 1

print(charcount)