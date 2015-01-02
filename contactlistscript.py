#opens file to read
input_file = open('input.txt', 'r')
#puts each line into a variable
input_lines = input_file.readlines()
#closes the file (we don't need it open any more, we have the data in a variable)
input_file.close()


#open the file to append new data to
output_append = open('output.txt', 'a+')

#make a list to put the details in
output_list = []

#loop over the file to get the data we want
for line in input_lines:
  if "Name - " in line: #change the condition to suit the data you're looking for
    print "Adding: ", line #output for debugging
    #the code below adds the line into the empty list to make a new line for appending later
    output_list.append(line[7:-1]) # adjust this list-slice as necessary depending on the format of the inputted file

    #for firstname and lastname columns
    if " " in output_list[0]:
        output_list[0] = output_list[0].replace(' ', '\t') #this seperates firstname from last name
    else:
        output_list.append('\t') #this adds a blank column (no second name)
        
    output_list.append('\t') # used to create column in tab delimited text file format

  if "Email - " in line: #change the condition to suit the data you're looking for
    print "Adding: ", line #output for debugging
    output_list.append(line[8:-1]) #adjust slice as necessary to grab data from the line of text
    print(leads_list) #output for debugging
    output_append.writelines(output_list) #writes the new data to a line
    output_append.write('\n') # writes a newline character. Used to create a new line for data in the tab delimited text file.
    output_list = []
  
# close the open output file
output_append.close()