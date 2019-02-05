#transfering info from txt to a 2d list in python:
import  math
from moudle_transpose import *
from decimal import *
def fit_linear(filename):
    my_file=open(filename,'r')
    datacols=my_file.readlines()
    my_file.close()
    x=[]
    for col in datacols:
        x.append(col.rstrip('\n'))
    xlabel=datacols[-2]
    ylabel=datacols[-1]

    final=[]
    counter=0
    for y in x:
        counter=counter+1 # that will tell me the place of the exix explanations
        if y == '':
            break
        final.append(y.split())
#cheching if transpoisng is needed
    if final[0][1] !='x' and final[0][1] != 'X' and final[0][1] !='dx' and final[0][1] !='Dx' and final[0][1] !='DX' and final[0][1] !='dX' and final[0][1] !='y' and final[0][1] !='Y' and final[0][1] !='dy' and final[0][1] !='dY' and final[0][1] !='Dy' and final[0][1] !='DY':
        final=transpose(final)
    #@Len eror handling
    for lis in final:
        if len(lis)!=4:
            print('Input file error: Data lists are not the same length.') #When you progress with the code
            exit()
    #Working on list calssification

    countfornames=-1
    xlist=[]
    ylist=[]
    dylist=[]
    dxlist=[]

    countfornames=-1
    for name in final[0]:# here i want to categorize x dx y and dy
        countfornames=countfornames+1
        if name == 'y' or name == 'Y':
            for name1 in final[1:]:
                ylist.append(float(name1[countfornames]))
            break
    countfornames=-1

    for name in final[0]:# here i want to categorize x dx y and dy
        countfornames=countfornames+1
        if name == 'x' or name == 'x':
            for name1 in final[1:]:
                xlist.append(float(name1[countfornames]))
            break
    countfornames=-1

    for name in final[0]:# here i want to categorize x dx y and dy
        countfornames=countfornames+1
        if name == 'dy' or name == 'dY' or name == 'DY' or name == 'Dy':
            for name1 in final[1:]:
                dylist.append(float(name1[countfornames]))
            break
    countfornames=-1
    for name in final[0]:# here i want to categorize x dx y and dy
        countfornames=countfornames+1
        if name == 'Dx' or name == 'DX' or name == 'dx' or name == 'dX':
            for name1 in final[1:]:
                dxlist.append(float(name1[countfornames]))
            break
    countfornames=-1

    #next lines will check that the uncertainties are bigger than zero
    for dy in dylist:
        if float(dy)<0:
            print('Input file error: Not all uncertainties are positive.')
            break

    for dx in dxlist:
        if float(dx)<0:
            print('Input file error: Not all uncertainties are positive.')
            break


    #working on calculating chi^2red
    def weightedmean(z):
        uupersum=0
        downsum=0
        for i in range(0,len(z)):
            uupersum=uupersum+((z[i])/(dylist[i]*dylist[i]))
            downsum=downsum+1/(dylist[i]*dylist[i])
        return (uupersum/downsum)
    dysqared=[]
    for i in range(0,len(ylist)):
        dysqared.append(dylist[i]*dylist[i])

    xylist=[]
    for i in range(0,len(ylist)):
        xylist.append((ylist[i])*(xlist[i]))
    xsquared=[]
    for i in range(0,len(ylist)):
        xsquared.append((xlist[i])*(xlist[i]))

    #calculating desired varibles
    a=(weightedmean(xylist)-weightedmean(xlist)*weightedmean(ylist))/(weightedmean(xsquared)-weightedmean(xlist)*weightedmean(xlist))
    b=weightedmean(ylist)-a*weightedmean(xlist)
    da=math.sqrt((weightedmean(dysqared))/((len(dylist))*(weightedmean(xsquared)-weightedmean(xlist)*weightedmean(xlist))))
    db=math.sqrt((weightedmean(dysqared)*weightedmean(xsquared))/((len(dylist))*(weightedmean(xsquared)-weightedmean(xlist)*weightedmean(xlist))))
    chi=0
    for i in range(0,len(ylist)):
        chi=chi+(math.pow((ylist[i]-(a*xlist[i]+b))/dylist[i],2))
    chired=chi/(len(ylist)-2)
    print("a = {} +- {}".format (a, da))
    print("b = {} +- {}".format (b, db))
    print("chi2 = {}".format (chi))
    print("chi2_reduced = {}".format (chired))
    print(dylist)

    #Graph
    #calculating and show a graph based on two points to make from ax+b
    xpoints=[min(xlist),max(xlist)]
    ypoints=[]
    ypoints.append(xpoints[0]*a+b)
    ypoints.append(xpoints[1]*a+b)
    from matplotlib import pyplot
    import matplotlib.pyplot as plt
    plt.plot(xpoints,ypoints, 'r')

    #adding eror bars:
    plt.errorbar(xlist, ylist, yerr=dylist, xerr=dxlist,color='b',fmt='+',zorder=5)

    # organizing the labels
    xlabel=xlabel.strip('\n',)
    xlabel=xlabel.strip('x axis: ')
    ylabel=ylabel.strip('\n')
    ylabel=ylabel.strip('y axis: ')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('linear_fit.SVG')
    (plt.show())

#bonus!
#bonus!
#bonus!
#bonus!
#bonus!

#transfering info from txt to a 2d list in python:
from moudle_transpose import *
def search_best_parameter(filename):
    my_file = open(filename, 'r')
    datacols = my_file.readlines()
    my_file.close()
    x = []
    for col in datacols:
        x.append(col.rstrip('\n'))

    final = []
    counter = 0
    for y in x:
        counter = counter + 1  # that will tell me the place of the exix explanations
        if y == '':
            break
        final.append(y.split())
    # cheching if transpoisning is needed
    if final[0][1] != 'x' and final[0][1] != 'X' and final[0][1] != 'dx' and final[0][1] != 'Dx' and final[0][
        1] != 'DX' and final[0][1] != 'dX' and final[0][1] != 'y' and final[0][1] != 'Y' and final[0][1] != 'dy' and \
            final[0][1] != 'dY' and final[0][1] != 'Dy' and final[0][1] != 'DY':
        final = transpose(final)
    # len eror handling
    for lis in final:
        if len(lis) != 4:
            print('Input file error: Data lists are not the same length.')  # When you progress with the code
            exit()

    #List calssiication
    countfornames = -1
    xlist = []
    ylist = []
    dylist = []
    dxlist = []

    countfornames = -1
    for name in final[0]:  # here i want to categorize x dx y and dy
        countfornames = countfornames + 1
        if name == 'y' or name == 'Y':
            for name1 in final[1:]:
                ylist.append(float(name1[countfornames]))
            break
    countfornames = -1

    for name in final[0]:  # here i want to categorize x dx y and dy
        countfornames = countfornames + 1
        if name == 'x' or name == 'x':
            for name1 in final[1:]:
                xlist.append(float(name1[countfornames]))
            break
    countfornames = -1

    for name in final[0]:  # here i want to categorize x dx y and dy
        countfornames = countfornames + 1
        if name == 'dy' or name == 'dY' or name == 'DY' or name == 'Dy':
            for name1 in final[1:]:
                dylist.append(float(name1[countfornames]))
            break
    countfornames = -1
    for name in final[0]:  # here i want to categorize x dx y and dy
        countfornames = countfornames + 1
        if name == 'Dx' or name == 'DX' or name == 'dx' or name == 'dX':
            for name1 in final[1:]:
                dxlist.append(float(name1[countfornames]))
            break
    countfornames = -1

    # next lines will check that the uncertainties are bigger than zero
    for dy in dylist:
        if float(dy) < 0:
            print('Input file error: Not all uncertainties are positive.')
            break

    for dx in dxlist:
        if float(dx) < 0:
            print('Input file error: Not all uncertainties are positive.')
            break
#extracting the lines of a and b from the data
    aline=datacols[-2][1:].split()
    bline=datacols[-1][1:].split()

#frange is located in the secondry moudle
    alist=frange(aline[0],aline[1],aline[2])
    blist=frange(bline[0],bline[1],bline[2])

#Searching for the best a and b
    bestaindex = 0
    bestbindex = 0

#chi2 function is located in the secondry moudle
    lowestchi = chi2(xlist, ylist, dylist, alist[0], blist[0],dxlist)
    for a in range(0, len(alist)):
        for b in range(0,len(blist)):
            chi = chi2(xlist, ylist, dylist, alist[a], blist[b],dxlist)
            if chi < lowestchi:
                lowestchi = chi
                bestaindex = a
                bestbindex = b

    # organizing the labels that were extracted from the data
    xlabel = datacols[-5]
    ylabel = datacols[-4]
    xlabel = xlabel.strip('\n', )
    xlabel = xlabel.strip('x axis: ')
    ylabel = ylabel.strip('\n')
    ylabel = ylabel.strip('y axis: ')

#first Graph
    print("a = {} +- {}".format (alist[bestaindex], aline[2].strip('-')))
    print("b = {} +- {}".format (blist[bestbindex], bline[2]))
    print("chi2 = {}".format (lowestchi))

#calculating and show a graph based on two points to make from ax+b
    xpoints=[min(xlist),max(xlist)]
    ypoints=[]
    ypoints.append(xpoints[0]*alist[bestaindex]+blist[bestbindex])
    ypoints.append(xpoints[1]*alist[bestaindex]+blist[bestbindex])
    from matplotlib import pyplot
    import matplotlib.pyplot as plt
    plt.plot(xpoints,ypoints, 'r')
    #adding eror bars:
    plt.errorbar(xlist, ylist, yerr=dylist, xerr=dxlist,color='b',fmt='+',zorder=5)

    # organizing the labels
    xlabel=xlabel.strip('\n',)
    xlabel=xlabel.strip('x axis: ')
    ylabel=ylabel.strip('\n')
    ylabel=ylabel.strip('y axis: ')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('linear_fit.SVG')
    (plt.show())

    #Second Graph
    chilist=[]
    for a in range(0, len(alist)):
        chi = chi2(xlist, ylist, dylist, alist[a], blist[bestbindex],dxlist)
        chilist.append(chi)

    from matplotlib import pyplot
    import matplotlib.pyplot as plt
    plt.xlabel('a')
    plt.ylabel("chi2(b = {}{}".format(blist[bestbindex], ')'))
    plt.savefig('numeric_sampling.SVG')
    plt.plot(alist, chilist, 'b')
    (plt.show())


