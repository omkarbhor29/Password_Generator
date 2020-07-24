import random

wordlist = []
special_char = ['@','#','$','^','*','!']
with open("wikipedia-pass.txt",'r') as file:
    data = file.readlines()
    
    for line in data:
        word = line.split()
        
    for item in word:
        if len(item)>4:
            wordlist.append(item.capitalize())

word = random.choice(wordlist)
schar = random.choice(special_char)
num = str(random.randint(100,999))

PassWord = word + schar + num

print(PassWord)
        