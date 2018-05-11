# 
# Name: Julian Lankstead
# Student Number: 101043448
#
# References: Gaddis, T (2015). "Starting Out With Python"

#Welcome Statement!!!!
print("Welcome to the Boston Bruins quiz! ")
#The First List
list1 = [['MC', 1, 'What year did were the Boston Bruins founded?'], 
		['MC', 2, 'Who is the GM of the Bruins?'], 
		['MC', 3, 'Who is the captain of the Bruins?'], 
		['MC', 4, 'How many presidents trophies have the Bruins won?'], 
		['MC', 5, 'How many Stanley cups have the bruins won?'], 
		['MC', 6, 'Who is the head coach?'], 
		['MC', 7, 'Who is their starting centre?'], 
		['MC', 8, 'What arena do they play at?'], 
		['MC', 9, 'Who was the famous player who wore number four for the Bruins?'], 
		['MC', 10, 'What number was Cam Neely?'], 
		['TF', 11, 'Black White and Gold are the Bruins colors. True or False?'], 
		['TF', 12, 'NESN is the main broadcaster for the Bruins. True or False?'], 
		['TF', 13, 'The Bruins only have one minor leaugue affiliate. True or False?'], 
		['TF', 14, 'Their main logo is a bear. True or False?'],
		['TF', 15, 'The Bruins are in the Eastern conference. True or False? ']]
#The Second List
list2 = [['a. 1900', 'b. 1890', 'c. 1924', -1, 2], 
		['a. Claude Julien', 'b. Charles Adams', 'c. Don Sweeny', -1, 2], 
		['a. Marchand', 'b. Backes', 'c. Chara', -1, 2], 
		['a. 1', 'b. 2', 'c. 3',-1, 1], 
		['a. 2', 'b. 4', 'c. 6', -1, 2], 
		['a. Don Sweeny', 'b. Claude Julien', 'c. Don Cherry', -1, 1], 
		['a. Spooner', 'b. Marchand', 'c. Bergeron', -1, 2], 
		['a. Scotiabank Place', 'b. TD Garden', 'c. Boston Arena', -1, 2], 
		['a. Boychuk', 'b. Orr', 'c. Sittler', -1, 1], 
		['a. 6', 'b. 7', 'c. 8', -1, 2], 
		[-1, 'True'], 
		[-1, 'True'], 
		[-1, 'False'], 
		[-1, 'False'],
		[-1, 'True']]
while True:		
	mark = 0	
	for i in range(15):
		if list1[i][0] == 'MC':   #For Multiple Choice Questions
			print('Question Number-',list1[i][1],':', list1[i][2], sep='')
			print(list2[i][0], list2[i][1], list2[i][2])
			answer = input('Type your answer here: ')
			if answer == 'a':
				list2[i][3] = 0	
			elif answer == 'b':
				list2[i][3] = 1
			elif answer == 'c':
				list2[i][3] = 2
			if list2[i][3] == list2[i][4]:
				mark += 1
			else:
				mark += 0
			cont = input("Would you like to continue the quiz? ")
			if cont != 'yes': 
				exit()
				
		elif list1[i][0] == 'TF': #For True Or False Questions
			print('Question Number-',list1[i][1],':', list1[i][2], sep='')
			answer = input('Type your answer here: ')
			if i < 14:
				cont = input("Would you like to continue the quiz? ")
				if cont != 'yes': 
					exit()
				if answer == 'true':
					list2[i][0] = 'True'
				elif answer == 'false':
					list2[i][0] = 'False'
				if list2[i][0] == list2[i][1]:
					mark += 1
				else:
					mark += 0
			#So the "Would you like to continue the quiz" phrase doesnt appear	
			if i > 14:
				if answer == 'true':
					list2[i][0] = 'True'
				elif answer == 'false':
					list2[i][0] = 'False'
				if list2[i][0] == list2[i][1]:
					mark += 1
				else:
					mark += 0
	#Mark calculationssss			
	score = (mark / 15) * 100
	print('Your final score is: ', score)
	cont = input("Would you like to take the quiz again? ")
	if cont != 'yes': 
		exit()	
			
				
			
	
		
		

			
				

				
			
	

	
	
		


