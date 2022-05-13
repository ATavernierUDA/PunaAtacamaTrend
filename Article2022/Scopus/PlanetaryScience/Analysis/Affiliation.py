
import re
import matplotlib.pyplot as plt
import numpy as np

path = '/home/lica/Downloads/Article2022/Scopus/PlanetaryScience/Analysis/Scopus-165-Analyze-Affiliation.csv'
total = 165

filei = open(path,'r')
datai = filei.read()

data = re.split('\n|,', datai)

field = []
fieldn = []
limit = 10
count = 1

for i in range(0,len(data),2) :

	
	if (count > limit) :

		break

	else :

		field.append(data[i])
		fieldn.append(float(data[i+1]))
		count = count + 1



xx = [i for i in range(0,limit)]

plt.bar(xx,np.array(fieldn)/total*100,edgecolor='black',width=0.5,linewidth = 2)

for i in range(0, len(fieldn)) :

	plt.text(xx[i],fieldn[i]/total*100 + 0.1,str(round(fieldn[i]/total*100,1)) + '%')

	plt.text(xx[i],fieldn[i]/total*100 + 0.6,field[i],fontsize=8)

plt.xticks(xx,field,color='white')


plt.show()



