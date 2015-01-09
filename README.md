contactlistscript.py
=================
###Contact List Script for Python

A simple and very specific python script I wrote. ContactListScript looks at an input text file for Names and Email addresses and builds an output text file using [tab delimited values](https://en.wikipedia.org/wiki/Tab-separated_values) format. It uses 3 columns/fields for data; Firstname, Surname and Email Address.
This was not built for general purpose, and in it's current state may break with large files. It needs tweaking, though I decided to put it up anyway. Please refer to the license before use. 

####Usage Instructions

Again, read and understand the license as you agree to be bound by it's terms upon using this script. ;)

Before you use contactListScript on your data, I recommend doing some small tests first. It's current setup may not suit your needs and may mess everything up or even do unwanted things.
Perhaps test it using an unimportant copy of a small portion of the data you are intending to work with.

####Requirements

In it's current state it has some requirements to run.
 * The input file be named 'input.txt' in the same folder as the script.
 * The output file named 'output.txt' in the same folder as the script.
 
####Changes you need to make in the script
 
If you are using it yourself then you will most likely need to change some things within the script.
Most likely is the 'if' condition looking for "Name" and "Email" as well as the list slice lines for each (i.e. like '[8:-1]').
The first number in the list slice is the characters you want to count over before starting to add the data (like 'Name - " incl spaces).
The second number in the list slice is '-1', I used this to remove a newline character (i.e. '\n') from the data I was working with.

####Possible future tweaks

The addition of line or two to remove duplicate entries.
The addition of more robust and capable handling of data.
A simple user interface to allow more general use of the script.