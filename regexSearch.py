''' Write a program that opens all .txt files in a folder and searches for any line that matches
    a user-supplied regular expression. The result should be printed on the screen.
'''
import os, re
# This portion of the program separates the .txt files from rest of the files
fileExp = re.compile('.*.txt')
listOfile = os.listdir('E:\\')
listOtxt = []
for k in listOfile:
    if fileExp.search(k) != None:
        listOtxt = listOtxt + [k]
# Now that the list of all the text files within disk E has been listed in listOtxt now we begin our quest to search the required regular expression in the file.
# First let's create a full path to all the text files
fullPath = []
for l in listOtxt:
    fullPath = fullPath + [os.path.join('E:\\', l)]
# Now we ask the user to input the regular expression to search in all those text files.
print('Please input the regex(regular expression) to search in the text files.')
what = input()
toFind = re.compile(what)
# Then begins the automation process to find all the regular expression in the text files
for m in fullPath:
    file = open(m, 'r')
    allTexts = file.read()
    patternFound = toFind.findall(allTexts)
    print('In ' + m)
    print(patternFound)
    file.close()
