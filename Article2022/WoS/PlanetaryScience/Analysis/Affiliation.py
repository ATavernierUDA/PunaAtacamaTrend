
import re
import matplotlib.pyplot as plt

path = '/home/lica/Downloads/Article2022/WoS/PlanetaryScience/Analysis/analyze(41).txt'


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


total=sum(fieldp)


xx = [i for i in range(0,limit)]

plt.bar(xx,fieldp,edgecolor='black',width=0.5,linewidth = 2)

for i in range(0, len(fieldp)) :

	plt.text(xx[i],fieldp[i] + 0.1,str(round(fieldp[i],1)) + '%')

	plt.text(xx[i],fieldp[i] + 1,field[i])

plt.xticks(xx,field,color='white')


plt.show()



