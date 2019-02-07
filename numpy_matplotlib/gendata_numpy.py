import numpy as np

files = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
time = np.arange(0,60*60*24)
for fname in files:
    temp = 20.0+5*np.sin(2*np.pi*time/(60*60*24))+ \
        np.random.ranf(np.size(time))-0.5
    p = np.ones(np.size(time))*101300+2000*(np.random.ranf(np.size(time))-0.5)
    data=np.vstack([time,temp,p]).transpose()
    np.savetxt(fname+".csv",data,header="time(s),temperature(deg C),Pressure(Pa)",
        delimiter=",",fmt="%.3f")

# Now write a program using numpy and matplotlib to extract the min, max and mean temp and P
# for each day, and plot from day 1 (monday) to day 7 (sunday)
