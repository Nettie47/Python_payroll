"""
Program: payroll.py
Chapter 4 example
2/27/2026

Payroll-type application that reads employee data from a text file and calculates then outputs payroll info in tabular format.
"""

import os
import time

# Get the directory where this script is located
fileDir = os.path.dirname(os.path.abspath(__file__))

# User input for just the file name
fileName = input("Please type the name of the payroll file that you wish to process >> ")

# New variable with the directory name and the file name properly joined into one string
filePath = os.path.join(fileDir, fileName)

#WHILE loop which will test if the file exists. If not, it will prompt the user again until a valid filename is provided
while not os.path.isfile(filePath):
	fileName = input(f"Sorry! '{fileName}' does NOT exist!\nPlease enter a VALID payroll file name >> ")
	filePath = os.path.join(fileDir, fileName)

# Process the verified file into a local variable
print("Processing the payroll data...")
time.sleep(2)

dataFile = open(filePath, "r")

# This output section will become the HEADER of our table
print()
print("%-16s%9s%7s%11s" % ("Last Name", "Wage", "Hours", "Earnings"))
print("-" * 50)

# FOR loop that can go through the file line by line, split the data into parts, and calculate the earnings for each employee
for line in dataFile:
	
	# Split the line into parts and assign to variables. Then calculate the earnings for each employee
	dataArray = line.split()
	
	# Extract the lats name form dataArray and store it in a variable called name. 
	name = dataArray[0]
	
	# Extract the wage from dataArray, convert them to floats, and store them in variables called wage. 
	wage = float(dataArray[1])
	
	# Extract the hours from dataArray, convert them to floats, and store them in variables called hours.
	hours = float(dataArray[2])
	
	# Calculate the earnings for each employee and store them in a variable called earnings.
	earnings = wage * hours

	# Output the payroll info for each employee in a tabular format. The name should be left justified, and the wage, hours, and earnings should be right justified with 2 decimal places.

	# This output section will become the BODY of our table
	print("%-16s%9.2f%7.2f%11.2f" % (name, wage, hours, earnings))

input("\nEnd of file. Press the ENTER to quit.")
