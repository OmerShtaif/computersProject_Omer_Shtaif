from math import *
import math
def transpose(m):
    #This can transpose rows to cols
    a=[]
    for i in range(len(m[0])):
        b=[]
        for j in range(len(m)):
            t = m[j][i]
            b.append(t)
        a.append(b)
    return (a)
#this function  works like a range but with floats
def frange(start,end,step):
#since float causes numbers like 1 to become 0.9999999, I have rounded eace number based on the numbers of digits after the decimal poing in step
    list=[]
    if float(start)>float(end):
        num=float(start)
        while num >float(end):
            list.append(round(num,len(str(step))-str(step).find('.')-1))
            num=num+float(step)
        return list
    if float(start)<float(end):
        num=float(start)
        while num <float(end):
            list.append(round(num,len(str(step))-str(step).find('.')-1))
            num=num+float(step)
        return list

#making a fucntion that calculates chi^2
def chi2(xi,yi,dyi,ai,bi,dxi):
    output=0
    for i in range(0, len(xi)):
        upper=(yi[i]-ai*xi[i]-bi)
        lower=sqrt(pow(dyi[i],2)+pow(2*ai*dxi[i],2))

        output=output+math.pow((upper/lower),2)
    return (output)
