import os 


keyword = "will"

li = []
for _,_, i in os.walk('./captions') :
	li = i 

# print (li)


for k in range(len(li)) :
	try : 

		# print (li[k])
		file1 = open("./captions/"+li[k],"r+") 
		x = file1.read()

		if keyword in x :
			print ("Yes @", li[k])
		else : 
			pass
	except :
		pass
	# print (x)
