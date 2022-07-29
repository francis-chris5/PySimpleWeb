# PySimpleWeb
Some reference files for the critical parts to run python scripts as cgi scripts on a server to create web apps


<h2>To run a Python script on a server</h2>

<br>

<p>First off on an Apache server, go to the http.conf file and add the following lines to the bottom of the file</p>

<blockquote>
  
  <p>AddHandler cgi-script .py</p>
  
  <p>ScriptInterpreterSource Registry-Strict</p>
  
</blockqoute>

<p>This will redirect standard output from the terminal on the server to the client it is currently connected to, i.e. the Python print(...) method will be sent to the client.</p>

<br>

<br>

<p>Then create a python script and make the FIRST LINE a sh-bang that points to your python interpeter</p>

<blockqoute>
  
  <p>Probably</p>
  
  <p>#!/bin/python3.10</p>
  
</blockqoute>

<p>It is different in the files here as I tested this using a xampp localhost virtual server on a Windows machine</p>

<br>

<br>

<p>To get html pages sent to the client simply read them in as a text file and print them to the client</p>

<p>To make the html pages more dynamic make up a special character you can easily parse out of the text in the file and replace that character with some dynamic data from the script.</p>

<p>To process an html form (make a web application with a nice looking user interface via html and css that is processed by a python script), set the Python script you want to run as the action on a form, and the default installation of the Python language will have a module called "cgi" which you can import and use an instance of the FieldStorage class from to retreieve the data in the form of a python dictionary.</p>

