# 
# Name: Julian Lankstead
# Student Number: 101043448
#
# References: Gaddis, T (2015). "Starting Out With Python"

def concat_slices_and_print():
	string = str('hgfdcbjknopqsteruvwamixzlydfghjk')
	print(string[12:15]+string[19:22]+string[24:26])
def if_positive_concat_slices(n1):
	string = str('vuqponwxyzstabcdfgrhjmnolpquvwxikyzeghjm')
	n1 = int(n1)
	if n1 > 0:
		print(string[10:13]+string[18:19]+string[24:25]+string[31:33]+string[35:36])
def return_concat_slices():
	string = str('rqpouvwxysztjklmopanqruvchwxyzedbfgi')
	stanched = string[9:10]+string[11:12]+string[18:20]+string[24:26]+string[30:32]
	return stanched 
def concat_arg_slices_and_return(n1):
	n1 = int(n1)
	string1 = str('mlkjhgnqsuvwpodxziatefghryjklmnq') #must return 'podiatry'
	string2 = str('zyxwvubcdghiseajklmfropquvntwxyzbc') #must return 'seafront'
	string3 = str('lkjhedmopquvstrwxyzafibcdenghjklmo') #must return 'strafing'
	podiatry = string1[12:15]+string1[17:20]+string1[24:26]
	seafront = string2[12:15]+string2[19:22]+string2[26:28]
	strafing = string3[12:15]+string3[19:22]+string3[26:28]
	if n1 < 0: 
		return podiatry
	elif n1 == 0:
		return seafront
	elif n1 > 0: 
		return strafing 
def main():

	print("Test 1 of 7:", concat_slices_and_print())
	print("Test 2 of 7:", if_positive_concat_slices(1))
	print("Test 3 of 7:", if_positive_concat_slices(-1))
	print("Test 4 of 7:", return_concat_slices())
	
	# replace the strings for the next three arguments with those values
	# provided in the generator-specified criteria for your 4th function
	print("Test 5 of 7:", concat_arg_slices_and_return("-1"))
	print("Test 6 of 7:", concat_arg_slices_and_return("0"))
	print("Test 7 of 7:", concat_arg_slices_and_return("1"))

main()
