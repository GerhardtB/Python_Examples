import random
import math

files=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for day in files:
    f=open(day+".csv","w")
    f.write("Time, Temp (degC),P (bar),Vwind(knots),heading(deg)\n")
    winddir=random.randint(0,360)
    for i in range(1440):
        hours=str(i//60)
        if(len(hours)<2):
            hours="0"+hours
        mins=str(i%60)
        if(len(mins)<2):
            mins="0"+mins
        f.write(hours+":"+mins+","+str(12+random.random()*10+math.sin(i*2*math.pi/1440))+","+str(0.8+random.random()*0.5)+","+str(0+random.random()*20)+","+str(winddir+random.randint(-40,40)*1.0)+"\n")
    f.close()
