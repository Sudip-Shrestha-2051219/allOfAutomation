''' Regex Version of strip()
   Write a function that takes a string and does the same thing as the strip()
   string method. If no other arguments are passed other than the string to 
   strip, then whitespace characters will be removed from the beginning and 
   end of the string. Otherwise, the characters specified in the second argument
   to the function will be removed from the string.
'''
import re
def stripIt(text, char):
    if char == '':                                  # This is to match and remove the whitespace from the beginning and the end of the text
        pattern = re.compile(r'^\s+|\s+$')
        text = pattern.sub('', text)
        return text
    else:
        loop = 0
        while(loop != len(char)):
            loop = 0
            for v in char:
                matcher = re.compile('^%s+|%s+$' %(v, v))
                if(matcher.findall(text) != []):
                    text = matcher.sub('', text)
                    break
                else:
                    loop = loop + 1
        return text
strFor = input('Enter a string that is to be stripped.')
txtTo = input('Enter the text to strip from the string.')
print(stripIt(strFor, txtTo))
