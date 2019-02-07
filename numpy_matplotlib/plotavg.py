import numpy as np
import matplotlib.pyplot as plt

files = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
day=[]
min_t=[]
max_t=[]
mean_t=[]
min_p=[]
max_p=[]
mean_p=[]
i=0
for f in files:
    data = np.loadtxt(f+".csv",delimiter=",",skiprows=1)
    print(data.shape)
    day.append(i+1)
    min_t.append(np.min(data[:,1]))
    max_t.append(np.max(data[:,1]))
    mean_t.append(np.mean(data[:,1]))
    min_p.append(np.min(data[:,2]))
    max_p.append(np.max(data[:,2]))
    mean_p.append(np.mean(data[:,2]))
    i+=1

print(min_t)
plt.subplot(1,2,1)
plt.plot(day,min_t,"b")
plt.plot(day,mean_t,"g")
plt.plot(day,max_t,"r")
plt.subplot(1,2,2)
plt.plot(day,min_p,"b")
plt.plot(day,mean_p,"g")
plt.plot(day,max_p,"r")
plt.show()
