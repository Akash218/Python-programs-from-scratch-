import numpy as np,scipy,matplotlib.pyplot as plt
from scipy import special
'''Array=np.array([(1,2,3),(4,5,6)])
print(Array)
print(Array.reshape(3,2))
print(Array.max())
print(Array.sum(axis=0))
print(Array.sum(axis=1))
print(np.sqrt(Array))
print(np.std(Array))
print(Array.ravel())
print(np.vstack(Array))
print(np.hstack(Array))
print(np.exp(Array))'''

#scipy
'''x=scipy.special.exp10(2)
print(x)
y=scipy.special.sindg(90)
print(c)
i=scipy.integrate.quard(lambda x:special.exp10(x),0,1)
print(i)'''
#matplotlib
'''slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0))
plt.title('Pie Plot')
plt.show()'''

plt.bar([1,2,3,4,5],[6,7,8,9,5])
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('bar graph')
plt.show()


