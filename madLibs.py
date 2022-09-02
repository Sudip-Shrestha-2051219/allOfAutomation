''' Mad Libs: This is a program that reads in text files and lets the user add their own text anywhere
   the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file
   may look like this:
   The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these
   events.
   The program would find these occurences and prompt the user to replace them.
    ------------------------------------------------------------------------------------------------------
    Enter an adjective:
    silly
    Enter a noun:
    chandelier
    Enter a verb:
    screamed
    Enter a noun:
    pickup truck
    -------------------------------------------------------------------------------------------------------
    The following text file would then be created:
    -------------------------------------------------------------------------------------------------------
    The silly panda walked to the chandelier and then screamed. A nearby pickup truck was
    unaffected by these events.'''
import re
forRead = open('E:\\text.txt', 'r')
forWrite = open('E:\\dupText.txt', 'w')
words = forRead.read().split()                  # splits the text file into lists so that it becomes easy to manipulate
nounSearch = re.compile('^Noun', re.I)
verbSearch = re.compile('^Verb', re.I)
pronounSearch = re.compile('Pronoun', re.I)
adjectiveSearch = re.compile('Adjective', re.I)
adverbSearch = re.compile('Adverb', re.I)
a = 0
for k in words:
    if nounSearch.search(k) != None:
        print('Enter a noun.')
        taker = input()
        words[a] = taker
        a = a + 1
    elif verbSearch.search(k) != None:
        print('Enter a verb.')
        taker = input()
        words[a] = taker
        a = a + 1
    elif adjectiveSearch.search(k) != None:
        print('Enter an adjective.')
        taker = input()
        words[a] = taker
        a = a + 1
    elif pronounSearch.search(k) != None:
        print('Enter a pronoun.')
        taker = input()
        words[a] = taker
        a = a + 1
    elif adverbSearch.search(k) != None:
        print('Enter an adverb.')
        taker = input()
        words[a] = taker
        a = a + 1
    else:
        a = a + 1
words = ' '.join(words)                         # rejoins the splitted file after modifying it.
forWrite.write(words)
forWrite.close()
forRead.close()
