print "Find out what day it is in a specific date"

def reset():
	imerominia =""
roh="yes"
while roh=="yes":

	imerominia = raw_input("Give the date in mode: dd/mm/yyyy:")
	imerominia = imerominia.split("/")
	mera = int(imerominia[0])
	mera1 = int(imerominia[0])
	if (mera <=0 or mera > 31):
		print "you inserted an invalid day, try again"
		continue
	minas = int(imerominia[1])
	minas1 = int(imerominia[1]) #xrisimopoieitai gia periorismous fevrouariou pio katw
	xronos = int(imerominia[2])
	aiwnas = xronos/100

 



#kwdikoi minwn
#ianouarios:1, fevrouarios:4, martios:4, aprilios:0, maios:2, iounios:5,
# ioulios:0, augoustos:3, septemvrios, oktwvrios:1, noemvrios:4, 
#dekemvrios:6

	if (minas == 04 or minas == 07):
		minas = 0
	elif (minas == 01 or minas == 10):
		minas = 1
	elif (minas == 05):
		minas = 2
	elif (minas == 8):
		minas = 3
	elif (minas == 02 or minas == 03 or minas == 11):
		minas = 4
	elif (minas == 06):
		minas = 5
	elif (minas == 9 or minas == 12):
		minas = 6
	elif (minas <0 or minas > 12):
		print "you inserted an invalid month,try again"
		continue

#kwdikos aiwna


	if (aiwnas==16 or aiwnas==20):
		aiwnas=6
	elif (aiwnas==17 or aiwnas==21):
		aiwnas=4
	elif (aiwnas==18 or aiwnas==22):
		aiwnas=2
	elif (aiwnas==19 or aiwnas==23):
		aiwnas=0
	
	
	kwdxronou = (aiwnas+(xronos%100)+(xronos%100)/4)%7

	mera = (kwdxronou + minas + mera) % 7
	

#gia disekto etos
	check_disekto = int(imerominia[1])
	if (xronos%4 == 0 and (check_disekto == 01 or check_disekto == 02)):
		mera = mera-1
		
#periorismos fevrouariou gia disekto etos
	if (xronos%4 == 0 and check_disekto == 02 and mera1 >29):
		print "you inserted an invalid day, try again"
		continue
		
	
	#periorismos fevrouariou gia mi disekto etos
	if (xronos%4 !=0 and minas1 == 02 and mera1 > 28):
		print "you put an invalid day, try again"
		continue
	
	print "At this date, the day is or was ----->"

	if (mera == 0):
		print "Saturday"
	elif (mera == 1):
		print "Sunday"
	elif (mera == 2):
		print "Monday"
	elif (mera == 3):	
		print "Tuesday"
	elif (mera == 4):
		print "Wednesday"
	elif (mera == 5):
		print "Thursday"
	elif (mera==6 or mera == -1):
		print "Friday"
	 
#epilogi gia na tsekarei alli imerominia
	roh=raw_input("\nDo you want to check another day(yes/no)?:")

	if roh=="yes":
		print "\nYou choose to check another date\n"
		print "Give the next date:"
		reset()

	elif roh=="no":
		print "\nYou choose to stop\n"

	else:
		print "\nYou put an invalid word,so the program will close\n"


	print "*****"*40    


 
	
 
 

	
	



	

