import random
print "You must find the treasure"
print ""
print "-------------------------------------------------------------"
print "|(0,0)|(0,1)|(0,2)|(0,3)|(0,4)|(0,5)|(0,6)|(0,7)|(0,8)|(0,9)|"
print "-------------------------------------------------------------"
print "|(1,0)|(1,1)|(1,2)|(1,3)|(1,4)|(1,5)|(1,6)|(1,7)|(1,8)|(1,9)|"
print "-------------------------------------------------------------"
print "|(2,0)|(2,1)|(2,2)|(2,3)|(2,4)|(2,5)|(2,6)|(2,7)|(2,8)|(2,9)|"
print "-------------------------------------------------------------"
print "|(3,0)|(3,1)|(3,2)|(3,3)|(3,4)|(3,5)|(3,6)|(3,7)|(3,8)|(3,9)|"
print "-------------------------------------------------------------"
print "|(4,0)|(4,1)|(4,2)|(4,3)|(4,4)|(4,5)|(4,6)|(4,7)|(4,8)|(4,9)|"
print "-------------------------------------------------------------"
print "|(5,0)|(5,1)|(5,2)|(5,3)|(5,4)|(5,5)|(5,6)|(5,7)|(5,8)|(5,9)|"
print "-------------------------------------------------------------"
print "|(6,0)|(6,1)|(6,2)|(6,3)|(6,4)|(6,5)|(6,6)|(6,7)|(6,8)|(6,9)|"
print "-------------------------------------------------------------"
print "|(7,0)|(7,1)|(7,2)|(7,3)|(7,4)|(7,5)|(7,6)|(7,7)|(7,8)|(7,9)|"
print "-------------------------------------------------------------"
print "|(8,0)|(8,1)|(8,2)|(8,3)|(8,4)|(8,5)|(8,6)|(8,7)|(8,8)|(8,9)|"
print "-------------------------------------------------------------"
print "|(9,0)|(9,1)|(9,2)|(9,3)|(9,4)|(9,5)|(9,6)|(9,7)|(9,8)|(9,9)|"
print "-------------------------------------------------------------"
#Dimiourgia pseudopinaka mesw mias listas 
lista=["Paiktis","Thusauros"]
for i in range(98):
	lista.append("*")
random.shuffle(lista)
#prosdiorismos suntetagmenwn paikti kai thusaurou mesw suntetagmenwn
#to x1 prosdiorozei ti grammi kai to y1 prosdiorizei ti stili tou paikti ston pseudopinaka
#to x2 prosdiorizei ti grammi kai to y2 prosdiorizei ti stili tou thusaurou ston pseudopinaka

for i in range(100):
		if lista[i]=="Paiktis":
			x1=i/10
			y1=i%10
		if lista[i]=="Thusauros":
			x2=i/10
			y2=i%10
print "you are in the position:" 
arx=[x1,y1]
print ','.join(map(str,arx))
print "the treasure is in the position:"
tel=[x2,y2]
print ','.join(map(str,tel))
print "GAME RULES"
print "Use the capital letters W,A,S,D"
print "Press W to move up"
print "Press A to move left"
print "Press S to move down"
print "Press D to move right"
while (x1!=x2 or y1!=y2):
	nea_thesi=[]
	twr_thesi=[]
	#kinisi tou paikti
	move="*"
	print ""
	#Epilogi kinisis
	move=raw_input('Your move is:')	
	if (move!="W" and move!="A" and move!="S" and move!="D"):
		print"Please insert a valid character"
		twr_thesi=[x1,y1]
		print "You are in position:" ,','.join(map(str,twr_thesi))	
	  
	if (move=="W"):
		if  x1!=0:
			x1=x1-1
			#upologismos neas thesis
			nea_thesi=[x1,y1]
			print "You are in position:" ,','.join(map(str,nea_thesi))
		elif x1==0:
			print "You can't move up /Out of map"	
	if (move=="A"):
		if y1!=0:
			y1=y1-1
			nea_thesi=[x1,y1]
			print "You are in position:" ,','.join(map(str,nea_thesi))
		elif y1==0:
			print "You can't move left /Out of map"
	if (move=="S"):
		if x1!=9:
			x1=x1+1
			nea_thesi=[x1,y1]
			print "You are in position:" ,','.join(map(str,nea_thesi))
		elif x1==9:
			print "You can't move down /Out of map"
	if (move=="D"):
		if y1!=9:
			y1=y1+1
			nea_thesi=[x1,y1]
			print "You are in position:" ,','.join(map(str,nea_thesi))
		elif y1==9:
			print "You can't move right /Out of map"
	
	#Ypologismos twn kinisewn mesw tis apostasis tou paikti kai tou thusaurou
	apostasi=abs(x1-x2)+abs(y1-y2)
	if apostasi!=0:
		print ""
		print "There are ",apostasi," moves left"
	print ""
print "You found the treasure! Congratulations "
