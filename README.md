# Python Challenge

This repository contains two projects: 'PyBank' and 'PyPoll'.

### PyBank 
In this project, a Python script is created to analyze the financial records of a company having financial dataset called budget_data.csv.
budget_data.csv file consists of two columns: "Date" and "Profit/Losses". 
The script analyzes the records to calculate each of the following values:
* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period.

The script prints the analysis to the terminal and exports an analysis folder containing output.txt file with the results.

### PyPoll 

This project is about helping a small, rural town modernize its vote counting process. A python script is created to analyze the votes and do some calculations based on the data given by the file 'election_data.csv'. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The script calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

The script prints the analysis to the terminal and exports an analysis folder containing output.txt file with the results.


## Setup

* Before running the scripts, in your terminal/command promt do this:
    
   "conda activate PythonData" 

  to activate PythonData virtual enviroment (assuming that all my clasmates have this enviroment with the same name)
* As both of the scripts contain relative paths, it is important to run the scripts in a correct directory.
  That said, before running the script cd to the directory which contains 'main.py' file.

##  Structure of folders
Both projects PyBank and PyPoll contain 'main.py' file, 'Resources' folder and 'analysis' folder at the same level. 
* 'Resources' folders contain input csv data files, 
* 'analysis' folders contain the logfile called 'output.txt'. 
#### Directory tree
. PyBank ---> main.py, Resources( ---> budget_data.csv), analysis( ---> output.txt)

. PyPoll ---> main.py, Resources( ---> election_data.csv), analysis( ---> output.txt)



### References
This project is a part of UC Berkeley "Data Analysis and Visualisation" Boot Camp education services.


In projects' descriptions, some paragraphs are copy/pasted from 'Module 3 Challenge' of UC Berkeley Data Analytics and Visualisation Bootcamp course. 

 Script author - Nazeli Mnatsakanyan 
 
 Mar-19-2023


