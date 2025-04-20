# 1) write a program to read the text from a given file "poems.txt" and find out whether it contains the word 'twinkle' or not

'''f=open("poems.txt")
content=f.read()
if("twinkle" in content):
    print("the word twinkle is present")
else:
    print("the word twinkle is not present")
f.close()'''

'''2) the game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt'
which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the 
Hi-score.'''

'''import random
def game():
    print("You are playing the game...")
    score=random.randint(1,100)
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score is {score}")
    if(score>hiscore):
        #write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()   '''

# 3) write a program to generate multiplication tables from 2 to 20 and write it to the different files.
'''def generate_table(n):
    table=""
    for i in range(1,11):
       table+=f"{n} x {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generate_table(i)'''

# 4) A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.

'''word="Donkey"
with open("q4.txt","r") as f:
    content=f.read()
    content=content.replace(word,"#####")
with open("q4.txt","w") as f:
    f.write(content) '''
   
# 5) Repeat a program 4 for list of such words to be censored

'''words=["Donkey","horse","for"]
with open("q4.txt","r") as f:
    content=f.read()
for word in words:
        content=content.replace(word,len(word)*"#")
with open("q4.txt","w") as f:
    f.write(content)'''

# 6) Write a program to mine a log file and find out whether it contains 'python' or not

'''word="Python"
with open("log.txt","r") as f:
    content=f.read()
if (word in content):
    print("The word Python is present")
else:
    print("The word Python is not present")'''

# 7) write a program to find out the line number where Python is present from ques 6
'''word="Python"
with open("log.txt","r") as f:
    content=f.readlines()
lineno=1
for line in content:
    if (word in line):
        print(f"The word Python is present in line number {lineno}")
        break
    lineno+=1
else:
    print("The word Python is not present")'''

# 8) write a program to make a copy of a text file "this.txt"

'''with open("this.txt","r") as f:
    content=f.read()
with open("copy_this.txt","w") as f:
    f.write(content)'''

#9) write a program to find out whether a file is identical and matches the content of another file.

'''with open("this.txt","r") as f:
    content=f.read()
with open("copy_this.txt","r") as f:
    content1=f.read()
if (content==content1):
    print("The files are identical")
else:
    print("The files are not identical")'''

# 10) writea program to wipe out the contents of a file
'''with open("wipe.txt","w") as f:
    f.write("") ''' #this is used to wipe out the contents of a file

# 11) write a python program to rename a file to "rename.txt"

'''import os
os.rename("file.txt","rename.txt")'''

