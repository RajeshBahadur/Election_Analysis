# Written Anallysis of the Election Audit

	# Overview of the Election Audit

	The purpose of this election audit analysis is to use python to manipulate voting data stored in csv file and write the elction results in the text file.
	The election analysis using python was quite challenging as students have to implements conecpts learned in the text book to the practice, the most challenging
	part was creating "for" loop and "if" satement within the "forloop". Since this is the first time using Python language, fixing indentation error took lots of time
	to fix. At the end, with numorous debugging and taking help form experts, I could able to understand and run coding to get the desired output.

	The objective of the analysis is to determine which county has maximum voters turnout followed by determining winner of the elction who received maximun votes. 
	
	# Election-Audit Results
	The election audit result based on voters turnout against each count reveals that, total voter turnout is 369,711 from all three counties. The total number of voters
	turout from Denver county is 306,055 which is 83% of the total voters turnout. Therefore, the maximum voters turnout is Denver county. The result of the output as printed in the
	county_Analysis.txt file  is as follows.

	Election results based on county
		Election Results
	-------------------------
	Total Votes: 369,711
	-------------------------

	County Votes:
	Jefferson: 10.5% (38,855) 
	Denver: 82.8% (306,055) 
	Arapahoe: 6.7% (24,801) 
	-------------------------
	Winner: Denver
	Winning Vote Count: 306,055
	Winning Percentage: 82.8%
	-------------------------
	
	Similarly, analysing results of the election based on candidates reveals that, out of the total votes counted ( 36,711) Diana DeGerre received 73.8% of the total votes, followed by 
	Charles Casper Stockham who has received 23% of the total votes and the least number of votes received by Raymon Anthony which is 3.1%. Therefore, the winning candidates is 
	Diana DeGette. The output of the winning candidate as reflected in the VS Code is produced below.


	Election results based on candidates
	-------------------------
	Charles Casper Stockham: 23.0% (85,213)
	Diana DeGette: 73.8% (272,892)
	Raymon Anthony Doane: 3.1% (11,606)
	-------------------------
	Winner: 
	Winning Vote Count: 306,055
	Winning Percentage: 82.8%
-------------------------


	# Election-Audit Summary
	Based on the above analysis, the codes written to count the winning voters count by county and by provice in this file can be easily replicated to do the analysis of similar
	csv files for other counties with a very large data set. This code can be used as template and by just changing the source file name, we can derive result of the election without
	any error.
