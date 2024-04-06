#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:49:48 2024

@author: ryleetexter
"""


# reads a file and outputs a new file with numbered lines along with original data
def line_number(inputFile, outputFile):
    lineNum = 0
    lines = ''
    try: 
        pyFile = open(inputFile, "r")
        txtFile = open(outputFile, "w")
        lines = pyFile.readlines()
    
    
        #loops through lines and prints lineNum counter (line numbers) and original data 
        #on the line
        for line in lines:
            lineNum += 1
            line_str = "{}. {}".format(lineNum, line)
            print(line_str, file = txtFile)
            
        pyFile.close()
        txtFile.close()
        
    except Exception:
        print("File does not exist")
    
#reads a file and outputs a list of tuples containing function information
def parse_function(fileName):
    
    file = open(fileName, "r")
    lines = file.readlines()
    line_count = 0
    lineNums = []
    names = []
    arguments = []
    func_content = []
    func_lines = []
    
    #finds which lines are functions, saves their indexes, names, info
    for line in lines:
        line_count+=1
        
        
        if ("def" in line):
            ##found function
            lineNums.append(line_count)
            char_count = 3
            
            #gets index of the end of the function name
            while(True):
                char_count  += 1
                if line[char_count] == "(":
                    break; 
                  
            names.append(line[4:char_count])
            argument_index = char_count + 1
            
            #gets arguments from line and appends them to a list arguments
            while(True):
                char_count+=1
                
                if line[char_count] == ")":
                    arguments.append(line[argument_index: char_count])
                    break
                
    
    #loops through indexes in lineNums for the found functions
    #finds the amount of lines each function has and appends the index at the 
    #end of the function to a list, func_lines
    for num in lineNums:
        counter = num
        
        #loops through the lines until finding the next line outside of the function
        #and appends the index of the nextline to func_lines
        while(True):
            if len(lines) <= counter:
                func_lines.append(counter)
                break;
            #removes empty lines 
            if((lines[counter][0] == " ") and (lines[counter].isspace() == False)): 
                counter += 1
                
            else:
                func_lines.append(counter)
                break;
    
    
    #loops through func lines and uses i to get the range
    for i in range(len(func_lines)):
        func_string = ""
        rang = range(lineNums[i]-1, func_lines[i])
        
        #loops through the function lines and appends function content and 
        #formatting
        for j in rang:
            func_string += lines[j].strip()
            if j < func_lines[i]-1:
                func_string += "/n"
        func_content.append(func_string) 
    
    list_of_tuples = []
    
    #loops through each index and creates a tuple with function info
    for i in range(len(lineNums)):
        tup = (lineNums[i], names[i], arguments[i], func_content[i])
        list_of_tuples.append(tup)
        
    #displays information
    for tup in list_of_tuples:
        print(tup)
  
          
def main():
    line_number("test.py", "output.txt")
    output_file = open("output.txt", "r")
    lines = output_file.readlines()
    
    for line in lines:
        print(line)
        
    output_file.close()
    
    print("Parsed: ")
    parse_function("test.py")

main()