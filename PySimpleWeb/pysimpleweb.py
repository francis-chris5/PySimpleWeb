#!C:/Users/franc/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type: text/html\n")
"""
For an apache server put this in the httpd.conf file (at the bottom is fine)
    AddHandler cgi-script .py
    ScriptInterpreterSource Registry-Strict

The above lines have to be the first two in every python script
**MAKE SURE your sh-bang points to the python interpreter (this was tested on xampp on a windows 11 machine)
"""



pageData = {"message": "Hello Python Web App World"}

def html(file):
    with open(file, "r") as htmlFile:
        for line in htmlFile:
            if "<$" in line:
                start = line.index("<$")
                end = line.index("$>")
                content = line[start+2:end].strip()
                newLine = line[0:start] + pageData[content] + line[end+2:]
                print(newLine)
            else:
                print(line)




if __name__=="__main__":
    html("testPage.html")
