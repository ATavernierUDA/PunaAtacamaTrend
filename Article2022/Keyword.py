
import matplotlib.pyplot as plt
import numpy as np

x = ['Asteroid','Astrobiology','Cosmochemistry','Deimos','Early solar system','Icy Body','Jovian','Kuiper Belt','Mars','Martian','Meteorite','Moon','Neptunian','Outer Planet','Phobos','Plutonian','Presolar Nebula','Regolith','Saturnian','Transneptunian','Uranian','Venus']

y= [2,12,1,0,1,0,1,0,120,40,17,4,0,0,0,0,0,18,0,0,0,1]
total = 161

#y= [2,19,1,0,1,0,1,0,119,44,22,8,0,0,0,0,0,19,0,0,0,1]
#total = 165

y=np.array(y)
y=y/total*100
y=list(y)
x = list(reversed(x))
y= list(reversed(y))
xpos = np.arange(len(x))
plt.figure(1)
plt.barh(xpos,y,edgecolor='black',label='Obvious focus in Planetary Science and/or Astrobiology')

y= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,0,0,0,0]
total = 161

#y= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,0,0,0,0]
#total = 165

y=np.array(y)
y=y/total*100
y=list(y)
y= list(reversed(y))
xpos = np.arange(len(x))
plt.figure(1)
plt.barh(xpos,y,color = 'orange',edgecolor='black',label='Indirect focus in Planetary Science and/or Astrobiology')

y= [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]
total = 161

#y= [0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1]
#total = 165

y=np.array(y)
y=y/total*100
y=list(y)
y= list(reversed(y))
xpos = np.arange(len(x))
plt.figure(1)
plt.barh(xpos,y,color = 'red',edgecolor='black',label = 'Selection error (no link to Planetary Science and/or Astrobiology)')

plt.xlabel('Percentage [%] according to the number of articles (' + str(int(total)) + ')')
plt.yticks(xpos,x,fontsize=8)
plt.legend()
plt.grid()
plt.show()
