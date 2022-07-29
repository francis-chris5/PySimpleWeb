#!C:/Users/franc/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type: text/html\n")
"""
For an apache server put this in the httpd.conf file (at the bottom is fine)
    AddHandler cgi-script .py
    ScriptInterpreterSource Registry-Strict

The above lines have to be the first two in every python script
**MAKE SURE your sh-bang points to the python interpreter (this was tested on xampp on a windows 11 machine)
"""

import cgi ## library for working with incoming Common Gateway Interface data

def processForm():
    formData = cgi.FieldStorage()
    print("<p>Whole thing:</p>")
    print("<p> &nbsp;&nbsp;&nbsp;" + str(formData))
    print("<h3>Desired Part: " + formData['stuff'].value + "</h3>")

if __name__=="__main__":
    processForm()
