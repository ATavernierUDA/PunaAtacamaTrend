
paths = 'ADS/EarthScience/'
paths1 = 'Scopus/EarthScience/Global/'

path1 =  paths + 'DOIADS.txt'
path2 =  paths1 + 'DOIScopus.txt'

path3 =  paths + 'TitleADS.txt'
path4 =  paths1 + 'TitleScopus.txt'

file1 = open(path1,'r')
file2 = open(path2,'r')
file3 = open(path3,'r')
file4 = open(path4,'r')

text1 = file1.read()
text2 = file2.read()
text3 = file3.read()
text4 = file4.read()

text1 = text1.upper()
text2 = text2.upper()
text3 = text3.upper()
text4 = text4.upper()

list1 = text1.split('\n')
list2 = text2.split('\n')
list3 = text3.split('\n')
list4 = text4.split('\n')

list1 =list1[0:len(list1)-1]
list2 =list2[0:len(list2)-1]
list3 =list3[0:len(list3)-1]
list4 =list4[0:len(list4)-1]


empty = 0
share = 0
doublon = 0

Doublon1 = []
Doublon3 = []

listeshare=[]

for i in range(0,len(list1)) :

	for j in range(0,len(list1)) :

		if (i != j) :

			if ( (list1[i] == list1[j]) and  (list1[i] != '') and (list1[i] not in Doublon1)  ) :

				
				Doublon1.append(list1[i])
				

			if ((list3[i] == list3[j]) and (list3[i] != '') and (list3[i] not in Doublon3)) :

				
				Doublon3.append(list3[i])
				

Doublon1 = list(set(Doublon1))
Doublon3 = list(set(Doublon3))

Doublon11=[]
Doublon33=[]

for i in range(0,len(Doublon1)) :

	for j in range(0,len(list2)) :

		if ((Doublon1[i] == list2[j]) and (list3[i] not in Doublon33)) :

			share =share + 1
			Doublon11.append(list1[i])
			break

for i in range(0,len(Doublon3)) :

	for j in range(0,len(list4)) :

		if ((Doublon3[i] == list4[j]) and (list1[i] not in Doublon11)):

			share =share + 1
			Doublon33.append(list3[i])
			break

Doublon11=[]
Doublon33=[]
doublonreal=0

for i in range(0,len(list1)) :

	flag = 0
	
	if (list1[i] in Doublon1) :

		flag = 1
	
		

	if (list3[i] in Doublon3) :

		flag = flag + 2
		
																																											 

	if ( (list1[i] == '') and (list3[i] == '') ) :

		empty = empty + 1
		
	

	else :

		if (flag == 0):

			for j in range(0,len(list2)) :

				if ( ( (list1[i] == list2[j]) and (list1[i] != '') ) or ( (list3[i] == list4[j]) and (list3[i] != '') ) ) :

					#print(list1[i])
					#print(list2[j])
					#print(list3[i])
					#print(list4[j])
					#print('------------------------------------')
					
					share = share + 1
					listeshare.append(list3[i])
					break
		else :
				
			doublon = doublon + 1

			if ((flag == 1) and (list1[i] not in Doublon11)) :

				doublonreal = doublonreal + 1
				Doublon11.append(list1[i])

			if((flag == 2) and (list3[i] not in Doublon33)) :

				doublonreal = doublonreal + 1
				Doublon33.append(list3[i])

			if((flag == 3) and (list3[i] not in Doublon33) and (list1[i] not in Doublon11)) :

				doublonreal = doublonreal + 1
				Doublon11.append(list1[i])
				Doublon33.append(list3[i])

			if((flag == 3) and (list3[i] in Doublon33) and (list1[i] not in Doublon11)) :

				Doublon11.append(list1[i])

			if((flag == 3) and (list3[i] not in Doublon33) and (list1[i] in Doublon11)) :

				Doublon33.append(list3[i])



path5 = '/home/lica/Documents/PlanetarySciences/ArticleSpaceScience/JournalP_ADS'

file5 = open(path5,'r')
text5 = file5.read()
text5 = text5.upper()
list5 = text5.split('\n')
list5 =list5[0:len(list5)-1]

path6 = '/home/lica/Documents/PlanetarySciences/ArticleSpaceScience/ADSexlude'
file6=open(path6,'w')
'''
for i in range(0,len(list3)) :

	for j in range(0,len(listeshare)) :

		if (list3[i] == listeshare[j]) :

			break

		else :

			if (j==len(listeshare)-1) :

				file6.write(list3[i])
				file6.write('\t')
				file6.write(list5[i])
				file6.write('\n')
						

file6.close()
'''

print(path1 + '  Empty : ' + str(empty) + ' / DoublonReal : ' + str(doublonreal)+ ' / DoublonTotal : ' + str(doublon)+ ' / DoublonDOI : ' + str(len(Doublon1)) + ' / DoublonTitle : ' + str(len(Doublon3)) + ' / Share : ' + str(share) + ' / Total : ' + str(len(list1)) )
print(path2 + ' Total : ' + str(len(list2)) )


