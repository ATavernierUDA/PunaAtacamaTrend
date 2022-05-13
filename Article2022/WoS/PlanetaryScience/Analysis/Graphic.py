
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt

path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(34).txt'

country=['ARGENTINA', 'BOLIVIA','CHILE','PERU']
colorf = 'blue'
colorc = 'red'
coloro = 'yellow'

filei = open(path,'r')
datai = filei.read()

data = re.split('\n|\t', datai)

foreign = []
foreignn = []
foreignp = []

local = []
localn = []
localp = []

flag = 0

for i in range(3,len(data),3) :

		
	if (flag == len(country)) :

		break

	else :

		if (data[i] in country) :

			local.append(data[i])
			localn.append(data[i+1])
			localp.append(data[i+2])
			
			flag = flag + 1

		else :	

			foreign.append(data[i])
			foreignn.append(data[i+1])
			foreignp.append(data[i+2])

y = foreign[0:5] + local
ynn = foreignn[0:5] + localn
yn = [float(i) for i in ynn]
ypp = foreignp[0:5] + localp
yp = [float(i) for i in ypp]

color = []

for i in range(0,len(foreign[0:5])) :

	color.append(colorf)

for i in range(0,len(local)) :

	if(local[i] == 'CHILE') :

		color.append(colorc)

	else :

		color.append(coloro)

interval = 3
begin = 0
factor = 2

xforeign = [i for i in range(begin,begin + len(foreign[0:5])*interval,interval)]
xlocal = [i for i in range (begin + factor*len(foreign[0:5])*interval,begin + factor*len(foreign[0:5])*interval + len(local) * interval, interval)]

x = xforeign + xlocal

'''
plt.figure(1)
plt.subplot(3,7,(15,21))
plt.bar(x,yp,color=color,edgecolor='black',width=1.5)
plt.xticks(x,y)
plt.grid()
'''

plt.figure(figsize=(150,75))
plt.subplot(3,7,(15,21))
plt.bar(x,yp,color=color,edgecolor='black',width=1.5,linewidth = 10)
plt.xticks(x,y,fontsize = 100)
plt.yticks(fontsize = 80)
plt.grid(linewidth = 10)

#plt.title('Contribution to the natural heritage of the Puna Region\nin terms of publications (4939 articles in total, excluding duplicates), of different countries or group of countries\n(from top to bottom : wordcloud of the main journals used for publication / repartition of field of research / percentage of contribution per country)',y = -0.6)

for i in range(0, len(yp)) :

	plt.text(x[i]-1,yp[i] + 2,str(round(yp[i],1)) + '%',fontsize = 100)

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(35).txt'


filei = open(path,'r')
datai = filei.read()

data = re.split('\n|\t', datai)

field = []
fieldn = []
fieldp = []
limit = 10
count = 1

for i in range(3,len(data),3) :

	
	if (count > limit) :

		break

	else :

		field.append(data[i])
		fieldn.append(float(data[i+1]))
		fieldp.append(float(data[i+2]))
		count = count + 1
'''
total=sum(fieldp)
plt.subplot(3,7,8)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total / 100) + '%',textprops={'fontsize': 7})
plt.axis('equal')
'''

total=sum(fieldp)
plt.subplot(3,7,8)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 5, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total / 100) + '%',textprops={'fontsize': 60})
plt.axis('equal')

path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(37).txt'


filei = open(path,'r')
datai = filei.read()

data = re.split('\n|\t', datai)

field = []
fieldn = []
fieldp = []
limit = 10
count = 1

for i in range(3,len(data),3) :

	
	if (count > limit) :

		break

	else :

		field.append(data[i])
		fieldn.append(float(data[i+1]))
		fieldp.append(float(data[i+2]))
		count = count + 1
'''
total=sum(fieldp)
plt.subplot(3,7,11)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total / 100) + '%',textprops={'fontsize': 7})
plt.axis('equal')
'''

total=sum(fieldp)
plt.subplot(3,7,11)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 5, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total / 100) + '%',textprops={'fontsize': 60})
plt.axis('equal')

path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(39).txt'


filei = open(path,'r')
datai = filei.read()

data = re.split('\n|\t', datai)

field = []
fieldn = []
fieldp = []
limit = 10
count = 1

for i in range(3,len(data),3) :

	
	if (count > limit) :

		break

	else :

		field.append(data[i])
		fieldn.append(float(data[i+1]))
		fieldp.append(float(data[i+2]))
		count = count + 1
'''
total=sum(fieldp)
plt.subplot(3,7,14)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total / 100) + '%',textprops={'fontsize': 7})
plt.axis('equal')
'''

total=sum(fieldp)
plt.subplot(3,7,14)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 5, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total / 100) + '%',textprops={'fontsize': 60})
plt.axis('equal')


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(36).txt'


filei = open(path,'r')
datai = filei.read()

data = re.split('\n|\t', datai)

paper = ''

nlimit = 30
scale = 1
count = 0

for i in range(3,len(data),3) :

	
	if ((count >= 100 **scale) or ((i/3)>nlimit)) :

		break

	else :

		for j in range(0,round(float(data[i+2]))**scale) :

			paper = paper + data[i] + ' '

			count = count + 1	


plt.subplot(3,7,1)

# Create the wordcloud object
#wordcloud = WordCloud(width=480, height=480, colormap='Accent', background_color="yellow").generate(paper)
wordcloud = WordCloud(width=3000, height=3000, colormap='Accent', background_color="skyblue").generate(paper)


# Display the generated image:
'''
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title('External countries')
'''

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title('External countries',fontsize = 120,y=1.1)



path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(38).txt'


filei = open(path,'r')
datai = filei.read()

data = re.split('\n|\t', datai)

paper = ''

nlimit = 30
scale = 1
count = 0

for i in range(3,len(data),3) :

	
	if ((count >= 100 **scale) or ((i/3)>nlimit)) :

		break

	else :

		for j in range(0,round(float(data[i+2]))**scale) :

			paper = paper + data[i] + ' '

			count = count + 1	


plt.subplot(3,7,4)

# Create the wordcloud object
#wordcloud = WordCloud(width=480, height=480, colormap='Accent', background_color="yellow").generate(paper)
wordcloud = WordCloud(width=3000, height=3000, colormap='Accent', background_color="red").generate(paper)


# Display the generated image:
'''
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title('Chile')
'''

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title('Chile',fontsize = 120,y=1.1)


path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(40).txt'


filei = open(path,'r')
datai = filei.read()

data = re.split('\n|\t', datai)

paper = ''

nlimit = 30
scale = 1
count = 0

for i in range(3,len(data),3) :

	
	if ((count >= 100 **scale) or ((i/3)>nlimit)) :

		break

	else :

		for j in range(0,round(float(data[i+2]))**scale) :

			paper = paper + data[i] + ' '

			count = count + 1	


plt.subplot(3,7,7)

# Create the wordcloud object
#wordcloud = WordCloud(width=480, height=480, colormap='Accent', background_color="yellow").generate(paper)
wordcloud = WordCloud(width=3000, height=3000, colormap='Accent', background_color="yellow").generate(paper)


# Display the generated image:
'''
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title("Puna's countries\n(Chile included)") 
'''

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.title("Puna's countries\n(Chile included)",fontsize = 120, y=1.1) 



plt.savefig('/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/Analysis.png')
#plt.show()


