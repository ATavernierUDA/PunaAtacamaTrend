
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt

path = '/home/lica/Downloads/Article2022/Scopus/EarthScience/Analysis/Scopus-5305-Analyze-Country.csv'

country=['Argentina', 'Bolivia','Chile','Peru']
colorf = 'blue'
colorc = 'red'
coloro = 'yellow'

filei = open(path,'r')
datai = filei.read()

data = re.split('\n|:|,', datai)

foreign = []
foreignp = []

local = []
localp = []

total = int(data[5])

flag = 0

for i in range(9,len(data),2) :

		
	if (flag == len(country)) :

		break

	else :

		if (data[i] in country) :

			local.append(data[i])
			localp.append(int(data[i+1])/total)
			
			flag = flag + 1

		else :	

			foreign.append(data[i])
			foreignp.append(int(data[i+1])/total)

y = foreign + local
y[0] = 'USA'
y[3] = 'UK'
ypp = foreignp + localp
yp = [float(i)*100 for i in ypp]

color = []

for i in range(0,len(foreign)) :

	color.append(colorf)

for i in range(0,len(local)) :

	if(local[i] == 'Chile') :

		color.append(colorc)

	else :

		color.append(coloro)

interval = 3
begin = 0
factor = 2

xforeign = [i for i in range(begin,begin + len(foreign)*interval,interval)]
xlocal = [i for i in range (begin + factor*len(foreign)*interval,begin + factor*len(foreign)*interval + len(local) * interval, interval)]

x = xforeign + xlocal

plt.figure(1)
plt.subplot(2,7,(8,14))
plt.bar(x,yp,color=color,edgecolor='black',width=1.5)
plt.xticks(x,y)
plt.grid()
#plt.title('Contribution to the natural heritage of the Puna Region\nin terms of publications (4939 articles in total, excluding duplicates), of different countries or group of countries\n(from top to bottom : wordcloud of the main journals used for publication / repartition of field of research / percentage of contribution per country)',y = -0.6)

for i in range(0, len(yp)) :

	plt.text(x[i]-1,yp[i] + 2,str(round(yp[i],1)) + '%')

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

path = '/home/lica/Downloads/Article2022/Scopus/EarthScience/Analysis/Scopus-1999-Analyze-Subject.csv'

filei = open(path,'r')
datai = filei.read()

data = re.split('\n|:|,', datai)

field = []
fieldp = []
limit = 8
count = 1

total = int(data[5])

for i in range(9,len(data),2) :

	
	if (count > limit) :

		break

	else :

		field.append(data[i])
		fieldp.append(int(data[i+1])/total)
		count = count + 1

total=sum(fieldp)
plt.subplot(2,7,1)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total) + '%',textprops={'fontsize': 6})
plt.axis('equal')
plt.title('External Countries')


path = '/home/lica/Downloads/Article2022/Scopus/EarthScience/Analysis/Scopus-3306-Analyze-Subject.csv'

filei = open(path,'r')
datai = filei.read()

data = re.split('\n|:|,', datai)

field = []
fieldp = []
limit = 8
count = 1

total = int(data[5])

for i in range(9,len(data),2) :

	
	if (count > limit) :

		break

	else :

		field.append(data[i])
		fieldp.append(int(data[i+1])/total)
		count = count + 1

total=sum(fieldp)
plt.subplot(2,7,4)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total) + '%',textprops={'fontsize': 6})
plt.axis('equal')
plt.title('Chile')


path = '/home/lica/Downloads/Article2022/Scopus/EarthScience/Analysis/Scopus-1721-Analyze-Subject.csv'

filei = open(path,'r')
datai = filei.read()

data = re.split('\n|:|,', datai)

field = []
fieldp = []
limit = 8
count = 1


total = int(data[5])

for i in range(9,len(data),2) :

	
	if (count > limit) :

		break

	else :

		field.append(data[i])
		fieldp.append(int(data[i+1])/total)
		count = count + 1

total=sum(fieldp)
plt.subplot(2,7,7)
plt.pie(fieldp, labels=field,wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' },autopct=lambda p : '{:.0f}'.format(p * total) + '%',textprops={'fontsize': 6})
plt.axis('equal')
plt.title("Puna's Countries\n(Chile included)")



plt.show()

