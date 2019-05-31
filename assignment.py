"""COMP1730/6730 assignment S2 2018.

Coauthors: <u6799959>, <u6797258>, 
Date: <10/21/2018>
"""

from visualise import show_vegetation_type
from visualise import show_vegetation_density
from visualise import show_wind_speed
from visualise import show_bushfire
from visualise import show_fire_risk


# The following functions must return the data in the form of a
# list of lists; the choice of data type to represent the value
# in each cell, for each file type, is up to you.
    

def load_vegetation_type(filename):
    import csv
    '''load vegetation_type.csv into lists of lists, and type of every element(cell) 
           in the lists is string'''
    with open(filename) as vegetype:
       readtype = csv.reader(vegetype)
       datavegtype = [ row for row in readtype ] 
    # if a certain data of a cell is missing, just return '' without any change
    return datavegtype
            
def load_vegetation_density(filename):
    '''load vegetation_density.csv into lists of lists, and type of every element(cell) 
           in the lists is float'''
    import csv
    with open(filename) as vegdensity:
        readdensity = csv.reader(vegdensity)
        datadensity = [ row for row in readdensity ] 
    for rowindex in range (0, len(datadensity)):
        for colindex in range (0, len(datadensity[rowindex])):
            if datadensity[rowindex][colindex] == '' :
                datadensity[rowindex][colindex] = '-1'  
                 # if a certain data of a cell is missing, return '0'      
    for rowindex in range (0, len(datadensity)):
        for colindex in range (0, len(datadensity[rowindex])):
           datadensity[rowindex][colindex] = float(datadensity[rowindex][colindex]) 
           # transfer the type of each element in the lists into float   
    return datadensity

def load_wind_speed(filename):
    '''load wind_speed.csv into lists of lists, and type of every element(cell) 
           in the lists is float'''
    import csv
    with open(filename) as windspeed:
        readspeed = csv.reader(windspeed)
        dataspeed = [ row for row in readspeed ] 
    for rowindex in range (0, len(dataspeed)):
        for colindex in range (0, len(dataspeed[rowindex])):
            if dataspeed[rowindex][colindex] == '' :
                dataspeed[rowindex][colindex] = '-1'  
                # if a certain data of a cell is missing, return '0'         
    for rowindex in range (0, len(dataspeed)):
        for colindex in range (0, len(dataspeed[rowindex])):
           dataspeed[rowindex][colindex] = float(dataspeed[rowindex][colindex])   
           # transfer the type of each element in the lists into float   
    return dataspeed

def load_bushfire(filename):
    ''' load bushfile.csv into lists of lists, and type of every element(cell) 
           in the lists is booleans'''   
    import csv
    with open(filename) as bushfire:
        readfire = csv.reader(bushfire)
        datafire = [ row for row in readfire ]    
    for rowindex in range (0, len(datafire)):
        for colindex in range (0, len(datafire[rowindex])):
           if datafire[rowindex][colindex] == '0':
               # if the area is not infected by bushfire, then return boolean value false
             datafire[rowindex][colindex] = False
           elif datafire[rowindex][colindex] == '1':  
               #otherwise return boolean value true
             datafire[rowindex][colindex] = True                   
    return datafire



# The argument to this function is a wind speed map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_wind_speed
# function.

def highest_wind_speed(wind_speed):
    '''the parameter should be a list of list of numbers
    and it will return the maximum value of it'''
    value_max = [max(row) for row in wind_speed ]
    return max(value_max)




# The argument to this function is a vegetation type map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_vegetation_type
# function.

def count_cells(vegetation_type):
    '''counts the number of cells filled by each kind of vegetation
     and print the result by each kind of vegetation '''
    count_Open_Woodland = 0
    count_Woodland = 0
    count_Grassland = 0
    count_Forest = 0
    count_Open_Forest = 0
    count_Urban_Vegetation = 0
    count_Golf_Course = 0
    count_Pine_Forest = 0
    count_Shrubland = 0
    count_Arboretum = 0
    ### traversal 
    for rowindex in range (0, len(vegetation_type)):
        for colindex in range (0, len(vegetation_type[rowindex])):
            if vegetation_type[rowindex][colindex] == 'Open Woodland':
                count_Open_Woodland = count_Open_Woodland + 1
            elif vegetation_type[rowindex][colindex] == 'Woodland':
                count_Woodland = count_Woodland + 1
            elif vegetation_type[rowindex][colindex] == 'Grassland':
                count_Grassland = count_Grassland  + 1
            elif vegetation_type[rowindex][colindex] == 'Forest':
                count_Forest = count_Forest + 1
            elif vegetation_type[rowindex][colindex] == 'Open Forest':
                count_Open_Forest = count_Open_Forest + 1
            elif vegetation_type[rowindex][colindex] == 'Urban Vegetation':
                count_Urban_Vegetation = count_Urban_Vegetation + 1
            elif vegetation_type[rowindex][colindex] == 'Golf Course':
                count_Golf_Course = count_Golf_Course + 1
            elif vegetation_type[rowindex][colindex] == 'Pine Forest':
                count_Pine_Forest = count_Pine_Forest + 1
            elif vegetation_type[rowindex][colindex] == 'Shrubland':
                count_Shrubland = count_Shrubland  + 1
            elif vegetation_type[rowindex][colindex] == 'Arboretum':
                count_Arboretum = count_Arboretum + 1
    print('Open Woodland : ', count_Open_Woodland)
    print('Woodland : ', count_Woodland)
    print('Grassland : ', count_Grassland)
    print('Forest : ', count_Forest)
    print('Open Forest : ', count_Open_Forest)
    print('Urban Vegetation : ', count_Urban_Vegetation)
    print('Golf Course : ', count_Golf_Course)
    print('Pine Forest : ', count_Pine_Forest)
    print('Shrubland : ', count_Shrubland)
    print('Arboretum : ', count_Arboretum)



# The arguments to this function are a vegetation type map and
# a vegetation density map, both in the form of a list of lists.
# They are the same data structure that is returned by your
# implementations of the load_vegetation_type and load_vegetation_density
# functions, respectively.

def count_area(vegetation_type, vegetation_density):
    '''calculate the area covered by each kind of vegetation
    and print the kind of vegetation with its area'''
    count_area_Open_Woodland = 0
    count_area_Woodland = 0
    count_area_Grassland = 0
    count_area_Forest = 0
    count_area_Open_Forest = 0
    for rowindex in range (0, len(vegetation_type)):
        for colindex in range (0, len(vegetation_type[rowindex])):
            if vegetation_type[rowindex][colindex] == 'Open Woodland':
                if vegetation_density[rowindex][colindex] >= 0:
                  count_area_Open_Woodland = count_area_Open_Woodland + vegetation_density[rowindex][colindex]*10000
            elif vegetation_type[rowindex][colindex] == 'Woodland':
                if vegetation_density[rowindex][colindex] >= 0:
                  count_area_Woodland = count_area_Woodland + vegetation_density[rowindex][colindex]*10000
            elif vegetation_type[rowindex][colindex] == 'Grassland':
                if vegetation_density[rowindex][colindex] >= 0:
                  count_area_Grassland = count_area_Grassland + vegetation_density[rowindex][colindex]*10000
            elif vegetation_type[rowindex][colindex] == 'Forest':
                if vegetation_density[rowindex][colindex] >= 0:
                  count_area_Forest = count_area_Forest + vegetation_density[rowindex][colindex]*10000
            elif vegetation_type[rowindex][colindex] == 'Open Forest':
                if vegetation_density[rowindex][colindex] >= 0:
                  count_area_Open_Forest = count_area_Open_Forest + vegetation_density[rowindex][colindex]*10000
    print('Open Woodland : ', count_area_Open_Woodland, 'sq m')
    print('Woodland : ', count_area_Woodland, 'sq m')
    print('Grassland : ', count_area_Grassland, 'sq m')
    print('Forest : ', count_area_Forest, 'sq m')
    print('Open Forest : ', count_area_Open_Forest, 'sq m')
    print('Urban Vegetation : 0.00 sq m')
    print('Golf Course : 0.00 sq m')
    print('Pine Forest : 0.00 sq m')
    print('Shrubland : 0.00 sq m')
    print('Arboretum : 0.00 sq m')


# The arguments to this function are:
# x and y - integers, representing a position in the grid;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def fire_risk_factor(x, y, vegetation_type, vegetation_density):
    '''return the fir risk factor of the cell itself &&
    this factor is sqrt(a+density) && a is depend by the vagetation type'''
    import math
    if vegetation_type[y][x]=='Shrubland' or vegetation_type[y][x]=='Pine Forest':
        level_a = 0.2
    elif vegetation_type[y][x]=='Arboretum':
        level_a = 0.1
    elif vegetation_type[y][x]=='Urban Vegetation' or vegetation_type[y][x]=='Golf Course':
        level_a = 0.05
    else:
        level_a = 0
    if vegetation_density[y][x] >=0:
        d_number = vegetation_density[y][x]
    elif vegetation_density[y][x] <0:
        d_number = 0
    factor = math.sqrt(level_a+d_number)
    return factor


def near_by_cell(x,y,n,lengthx,lengthy):
    '''this function will return a list, including the position of nearby cells
    and itself. n is the integer part of wind speed, length is the length of map'''
    nb_cells = []
    if n<=0 :   # [wind speed] equal to 0 or blank value
        return [[x,y]]
    elif n>0:
        if x>=n and y>=n: # the cell is not at the left/up edge
            ## if the cell is not at the right/bottom edge 
            if x+n<=lengthx-1 and y+n<=lengthy-1:
                for i in range(x-n,x+n+1):
                    for j in range(y-n,y+n+1):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
            ## if the cell is at the bottom edge 
            elif x+n<=lengthx-1 and y+n> lengthy-1:
                for i in range(x-n,x+n+1):
                    for j in range(y-n,lengthy):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
            ## if the cell is at the right edge
            elif x+n> lengthx-1 and y+n<=lengthy-1:
                for i in range(x-n,lengthx):
                    for j in range(y-n,y+n+1):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
            else: ## if the cell is at bottom right corner
                for i in range(x-n,lengthx):
                    for j in range(y-n,lengthy):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
        ## if the cell is at the left edge         
        elif x>=n and y<n:
            if x+n<=lengthx-1:
                for i in range(x-n,x+n+1):
                    for j in range(0,y+n+1):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
            else:
                for i in range(x-n,lengthx):
                    for j in range(0,y+n+1):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
        # if the cell is at the up edge  
        elif x<n and y>=n:
            if y+n<=lengthy-1:
                for i in range(0,x+n+1):
                    for j in range(y-n,y+n+1):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
            else:
                for i in range(0,x+n+1):
                    for j in range(y-n,lengthy):
                        dsq=(i-x)**2+(j-y)**2
                        if dsq <= n**2:
                            nb_cells.append([i,j])
        # if the cell is at the up left corner
        else:
            for i in range(0,x+n+1):
                for j in range(0,y+n+1):
                    dsq=(i-x)**2+(j-y)**2
                    if dsq <= n**2:
                        nb_cells.append([i,j])
        return nb_cells


def fire_risk(x, y, vegetation_type, vegetation_density, wind_speed):
    '''return the sum of fire-risk-facotrs of itself and its nearby cells '''
    ##the scale of nearby cells depend on the wind spead
    n=int(wind_speed[y][x])
    nearby_position = near_by_cell(x,y,n,len(wind_speed[0]),len(wind_speed))
    nearby_factors = []   # to store the fire risk factors of all nearby cells
    for row in nearby_position:
        f = fire_risk_factor(row[0],row[1],vegetation_type,vegetation_density)
        nearby_factors.append(f)
    total = sum(nearby_factors)
    return total

# The arguments to this function are an initial bushfile map (a list
# of lists, as returned by your implementation of the load_bushfire
# function), a vegetation type map (as returned by your implementation
# of the load_vegetation_type function), a vegetation density map (as
# returned by your implementation of load_vegetation_density) and a
# positive integer, representing the number of steps to simulate.
def position(initial_bushfire):
    '''this function will return a list of the position of the bushfire
    each position is represent by list [x,y]'''
    initial_position = []
    length = len(initial_bushfire)
    for i in range(0,len(initial_bushfire[1])):
        for j in range(0,length):
            if initial_bushfire[j][i]==True:
                initial_position.append([i,j])
    return initial_position


def near_8(x,y,lengthx,lengthy):
    '''this function return a list of the itself and nearby cells' position, 
    if the pixel is not at the edge of the map, it will return 9 cell's position'''
    near = []  # to store the index of nearby cells
    if x>0 and y>0: # the cell is not at the left/up edge
         ## if the cell is not at the right/bottom edge
        if x<lengthx-1 and y<lengthy-1:
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    near.append([i,j])
        ## if the cell is at the bottom edge
        elif x<lengthx-1 and y==lengthy-1:
            for i in range(x-1,x+2):
                for j in range(y-1,y+1):
                    near.append([i,j])
        ## if the cell is at the right edge            
        elif x==lengthx-1 and y< lengthy-1:
            for i in range(x-1,x+1):
                for j in range(y-1,y+2):
                    near.append([i,j])
        ## if the cell is at bottom right corner            
        else:
            for i in range(x-1,x+1):
                for j in range(y-1,y+1):
                    near.append([i,j])
     ## if the cell is at the up edge   
    elif x>0 and y==0:
        if x< lengthx-1:
            for i in range(x-1,x+2):
                for j in range(0,y+2):
                    near.append([i,j])
        else:
            for i in range(x-1,x+1):
                for j in range(0,y+2):
                    near.append([i,j])
    ## if the cell is at the left edge                
    elif x==0 and y>0:
        if y< lengthy-1:
            for i in range(0,x+2):
                for j in range(y-1,y+2):
                    near.append([i,j])
        else:
            for i in range(0,x+1):
                for j in range(y-1,y+2):
                    near.append([i,j])
    else: ## if the cell is at the up left corner
        for i in range(0,x+2):
            for j in range(0,y+2):
                near.append([i,j])                  
    return near

    

def simulate_bushfire_onestep(initial_bushfire, vegetation_density):
    '''this function return the new map after one simulation step'''
    fire_now = position(initial_bushfire)
    nearby = []
    for row in fire_now: 
        nearby.extend(near_8(row[0],row[1],len(initial_bushfire[0]),len(initial_bushfire))) # need modeify
    for row in nearby:
        # the density must not 0(little plants) or -1(blank value)
        if vegetation_density[row[1]][row[0]] > 0: 
            # add the False position into the list of fire_now 
            if initial_bushfire[row[1]][row[0]] == False :
                fire_now.append([row[0],row[1]])  
    ## deep copy of the initial map 
    copy_map = [[i] for i in range(0,len(initial_bushfire))]
    for j in range(0,len(initial_bushfire)):
        copy_map[j]=initial_bushfire[j][:]
    for row in fire_now:
        copy_map[row[1]][row[0]]= True
    return copy_map

def simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, steps):
    '''this function will return a simulate bushfire map after given step numbers, 
    the initial condition is in argument(initial_bushfire)'''
    s = steps
    map_now = [[i] for i in range(0,len(initial_bushfire))]
    # ensure the consistency of initial map 
    for j in range(0,len(initial_bushfire)):
        map_now[j]=initial_bushfire[j][:]  ### to store the current map
    while s > 0:
        map_now = simulate_bushfire_onestep(map_now,vegetation_density)
        s = s-1
    return map_now


# The arguments to this function are two bushfile maps (each a list
# of lists, i.e., same format as returned by your implementation of
# the load_bushfire function).

def compare_bushfires(bushfire_a, bushfire_b):
    '''ignore the blank value in both maps, and compare two bushfire maps,
    then return the similarity ratio of two maps'''
    count = 0 # create place to store the number of cells with same value
    countcell = 0 # create place to store the number of cells with valid value
    for rowindex in range (0, len(bushfire_a)):
        for colindex in range (0, len(bushfire_a[rowindex])):
          if bushfire_a[rowindex][colindex] == bushfire_b[rowindex][colindex] and bushfire_a[rowindex][colindex] != '' and bushfire_b[rowindex][colindex] != '' :
              count = count + 1
    for rowindex in range (0, len(bushfire_a)):
        for colindex in range (0, len(bushfire_a[rowindex])):
            if bushfire_a[rowindex][colindex] != '' and bushfire_b[rowindex][colindex] != '' :
               countcell = countcell + 1
    rate = count/countcell
    return rate


# The arguments to this function are:
# initial_bushfire - an initial bushfile map (a list of lists, same
#   as returned by your implementation of the load_bushfire function);
# steps - a positive integer, the number of steps to simulate;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).
def max_risk(table):
    '''the parameter should be a list of list of numbers
    and it will return the maximum value of it'''
    value_max = [max(row) for row in table ]
    return max(value_max)


def get_prob_table(initial_bushfire, vegetation_type, vegetation_density,
        wind_speed):
    '''a list of lists, the element is the bushfire spreading probability for each cell
    it comes from (cell's fire-risk-value)/max(fire-risk-value in this map)'''
    ## get a possible table
    ### 1) get a fire risk table
    lengthy=len(initial_bushfire)
    lengthx=len(initial_bushfire[0])
    prob_of_spread = [[] for r in range(0,lengthy)]
    for r in range(0,lengthy):
        prob_of_spread[r] = [0 for c in range(0,lengthx)] 
    for j in range(0,lengthy):
        for i in range(0,lengthx):
            prob_of_spread[j][i]=fire_risk(i, j, vegetation_type, vegetation_density, wind_speed)
    ### 2) get the max risk value
    maxrisk = max_risk(prob_of_spread)
    ### 3) prob = risk of this pixel / max risk value of the map 
    for i in range(0,lengthx):
        for j in range(0,lengthy):
            prob_of_spread[j][i]=(prob_of_spread[j][i]/maxrisk)
    return prob_of_spread

def simu_stochastic_onestep(initial_bushfire, prob_of_spread,
        vegetation_type, vegetation_density,
        wind_speed):
    import random
    fire_now = position(initial_bushfire)
    nearby = []
    for row in fire_now: 
        nearby.extend(near_8(row[0],row[1],len(initial_bushfire[0]),len(initial_bushfire)))
    for row in nearby:
        # add the False position into the list of fire_now 
        if initial_bushfire[row[1]][row[0]] == False:
            if vegetation_density[row[1]][row[0]] >0:
                fire_now.append([row[0],row[1]])
    ## deep copy of the initial map 
    copy_map = [[i] for i in range(0,len(initial_bushfire))]
    for j in range(0,len(initial_bushfire)):
        copy_map[j]=initial_bushfire[j][:]
    ### change False to Ture with the probability we calculated
    for row in fire_now:
        copy_map[row[1]][row[0]]= (random.uniform(0,1) <= prob_of_spread[row[1]][row[0]])
    fire_ori = position(initial_bushfire)
    ## ensure the cell already be True won't turn False again
    for row in fire_ori:
        copy_map[row[1]][row[0]]=True
    return copy_map

def simulate_bushfire_stochastic(
        initial_bushfire, steps,
        vegetation_type, vegetation_density,
        wind_speed):
    '''this function will return a list of lists after given steps' simulation
    and every step will involve a probability of spreading'''
    prob_of_spread = get_prob_table(initial_bushfire, vegetation_type, vegetation_density,
        wind_speed)
    s = steps
    map_now = [[i] for i in range(0,len(initial_bushfire))]
    for j in range(0,len(initial_bushfire)):
        map_now[j]=initial_bushfire[j][:]
    while s > 0:
        map_now = simu_stochastic_onestep(map_now, prob_of_spread,
        vegetation_type, vegetation_density,
        wind_speed)
        s = s-1
    return map_now


if __name__ == '__main__':
    # If you want something to happen when you run this file,
    # put the code in this `if` block.
    pass
