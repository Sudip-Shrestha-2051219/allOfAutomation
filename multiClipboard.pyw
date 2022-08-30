''' This is an automation program in python. It functions as a multi clipboard that can copy multiple texts in clipboard which are handled by different keywords.
    Program is to be run from command prompt as it won't show any output. All the inputs and outputs are to be dealt by the clipboard itself.
    i.e. The syntax for running the program in terminal is:            py.exe multiclipboard.pyw save keyName   ---> saves the texts of clipboard with the keyword keyName.
                                                                                             py.exe multiclipboard.pyw list         ------------> returns a list of all the keyword contained in shelveFile
                                                                                             py.exe multiclipboard.pyw keyName -----------> copies the contents of keyName from shelveFile into clipboard
                                                                                             py.exe multiclipboard.pyw delete keyName ---> deletes the keyword keyName from the shelveFile.
'''
import pyperclip, shelve, sys
go = shelve.open('shelveFile')                                                  # shelve file is simply a file that saves file in a dictionary format. It is more secure than a simple text file and the data is saved in binary format.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        go[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower() == 'delete':
        del go[sys.argv[2]]                                                         # since the file is saved in dictionary format thus delete command is identical to deleting a dictionary item.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(go.keys())))
    elif sys.argv[1] in go:
        pyperclip.copy(go[sys.argv[1]])
go.close()
'''Note: 1) You can skip the py.exe command if you add a path for py.exe to the directory in which this program is stored.
           2) In case you entered a wrong parameter or a wrong keyword then in most cases the previous value of the clipboard is unchanged and you'll simpy get that as a result.
'''
